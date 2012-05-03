# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
#
# Copyright 2012 Electronic Arts

from ConfigParser import ConfigParser


class Configure():

    def __init__(self, config):
        self.file = config
        self.cp = ConfigParser()
        self.parsed = {}

    def read(self):
        self.cp.read(self.file)

    def parse(self):
        self.read()
        parseret = 0
        for se in self.cp._sections:
            if "general" in se:
                parseret += 1
            if "servers" in se:
                parseret += 1
        if parseret >= 2:
            assert len(self.cp._sections) >= 2
            return self.cp._sections
        else:
            return
