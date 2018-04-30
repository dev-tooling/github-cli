'''
Copyright 2018 Riverstone Software, LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
from __future__ import print_function
import os

from git import Repo
from git.exc import InvalidGitRepositoryError
from github.GithubException import UnknownObjectException

from riverstone_cli.commands.base import Command
from riverstone_cli.common.constants import GITHUB


def _get_repo():
    repo_path = os.getcwd()
    try:
        return Repo(repo_path)
    except InvalidGitRepositoryError:
        return None


def _get_remote(git_repo):
    for remote in git_repo.remotes:
        if remote.name == "origin":
            return remote
    return None


def _github_path_from_remote(remote):
    for url in remote.urls:
        return url.split(':')[1].split('.git')[0]


def _get_github_repo():
    repo = _get_repo()
    if not repo:
        return None
    remote = _get_remote(repo)
    github_path = _github_path_from_remote(remote)
    try:
        return GITHUB.get_repo(github_path)
    except UnknownObjectException:
        return None


def _get_issue(github_repo, issue):
    try:
        return github_repo.get_issue(issue)
    except UnknownObjectException:
        return None


def _parse_issue_body(issue):
    body = issue.body.splitlines()
    metadata = {}

    for line in body:
        key, value = line.split(':')
        key = key.strip()
        value = value.strip()
        key = key.replace(' ', '_')

        metadata[key.lower()] = value

    return metadata


def _generate_branch_name(issue_number, issue_metadata):
    short_desc = issue_metadata.get('short_description')

    if not short_desc:
        raise ValueError('Incorrect metadata')
    else:
        short_desc = short_desc.replace(' ', '-').lower()

    return "issue-%s/%s" % (issue_number, short_desc)


def _checkout_branch(name):
    repo = _get_repo()
    git = repo.git

    branch_exists = False
    for branch in repo.branches:
        if name == branch.name:
            branch_exists = True

    if branch_exists:
        git.checkout(name)
    else:
        git.checkout('HEAD', b=name)


def _set_issue_labels(issue, labels):
    issue.set_labels(labels)


def _start(args):
    issue_number = args.get('issue_number')
    github_repo = _get_github_repo()
    if not github_repo:
        print("Repo not found")
        return
    issue = _get_issue(github_repo, issue_number)
    if not issue:
        print("Issue not found")
        return
    issue_metadata = _parse_issue_body(issue)
    if not issue_metadata:
        print("Issue metadata incomplete or non-existent")
        return
    branch_name = _generate_branch_name(issue_number, issue_metadata)
    if not branch_name:
        print("Error generating branch name")
        return
    print('Checking out %s' % branch_name)
    _checkout_branch(branch_name)
    print('Adding WIP label to issue')
    _set_issue_labels(issue, 'WIP')


def _stop(_):
    pass


class IssueCommand(Command):
    """ IssueCommand class defines the subcommands and logic for issue related
    tasks.
    """
    def __init__(self):
        """Setup subparser and other attributes
        """
        self.name = "issue"
        self.sub_commands = {
            'start': _start,
            'stop': _stop
        }

    def handler(self, args):
        """Handle issue commands.
        """
        sub_command = args['sub_command'].pop(0)
        self.sub_commands.get(sub_command)(args)

    def _register_opts(self):
        self._register_start_opts()

    def _register_start_opts(self):
        self.subparser.add_argument(
            'issue_number',
            metavar='issue_number',
            type=int,
            help='Issue number to start work on.'
        )
