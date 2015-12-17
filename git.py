# -*- coding: utf-8 -*-
#
# Copyright 2014 Microstrategy Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Git utils."""
__author__ = 'ryu@microstrategy.com'

import subprocess
from subprocess import check_output, CalledProcessError


class Git(object):
    def __init__(self, url):
        self.url = url

    def extra_params(self):
        """Generate extra params for git.

        Args:
            return: list, extra params.
        """
        return []

    def exec_git_command(self, params):
        final_params = params + self.extra_params()
        print final_params
        try:
            output = check_output(final_params, stderr=subprocess.STDOUT)
            print "Result:", output
            return output.rstrip('\n') or True
        except CalledProcessError as e:
            print "Error:", e.output
            return False

    def clone(self, url):
        self.exec_git_command(['git', 'clone', url])

    def pull(self):
        self.exec_git_command(['git', 'pull'])

    def fetch(self, origin_name):
        self.exec_git_command(['git', 'fetch', origin_name])

    def checkout(self, git_version):
        return self.exec_git_command(['git', 'checkout', git_version])

    def copy_remote_branch_to_local(self, origin_name, branch_name):
        self.exec_git_command(['git', 'checkout', '-b', branch_name, origin_name + '/' + branch_name])

    def reset(self, version):
        return self.exec_git_command(['git', 'reset', '--hard', version])

    def ls_branches(self, remote=False):
        #params = ['git', 'ls-remote', '--heads', url] + self.extraParams()
        params = ['git', 'branch']
        if remote:
            params.append('-r')
        return self.exec_git_command(params)

    def diff(self, base, target, file_path=None):
        """Generate diff
        Args:
            base: str, base revision
            target: str, target revision
            file_path: str, file/directory path
            return: str, standard git diff output
        """
        # git diff --name-only SHA1 SHA2
        params = ['git', 'diff', base, target]
        if file_path is not None:
            params.append(file_path)
        return self.exec_git_command(params)

    def export(self):
        """
        In fact, not used, but can be recorded as an example for future usage. The command is like this:
        mkdir path2
        git archive dev -o {path2}/latest.tar.gz
        tar -zvxf latest.tar.gz -C {path2}
        rm {path2}/latest.tar.gz
        """
        pass

    def get_local_latest_version(self):
        """ Get respository max revision info for git dir """
        # git rev-parse "refs/remotes/origin/master^{commit}"
        params = ['git', 'rev-parse', "HEAD"]
        return self.exec_git_command(params)

    def get_last_tag(self):
        # git describe --abbrev=0 --tags
        params = ['git', "describe", "--abbrev=0", "--tags"]
        return self.exec_git_command(params)

    def get_commit_id_from_tag(self, tag_name):
        params = ['git', 'rev-list', '-n', '1', tag_name]
        return self.exec_git_command(params)

    def reset_remote_url(self, remote_name, remote_url):
        # git remote set-url origin git://new.url.here
        params = ['git', 'remote', 'set-url', remote_name, remote_url]
        return self.exec_git_command(params)

    def get_remotes(self):
        # git remote -v
        params = ['git', 'remote', '-v']
        return self.exec_git_command(params)

    def add_remote(self, remote_name, url):
        # git remote add origin https://github.microstrategy.com/ryu/test2.git
        params = ['git', 'remote', 'add', remote_name, url]
        return self.exec_git_command(params)


