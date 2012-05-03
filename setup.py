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

import os
import sys
from setuptools import setup
from udprr import __version__

setup(
    name = 'udprr',
    version = __version__,

    description = 'Udp Round Robin load balancer',
    long_description = file(
        os.path.join(
            os.path.dirname(__file__),
            'README.rst'
        )
    ).read(),
    author = 'Karsten McMinn',
    author_email = 'kmcminn@ea.com',
    license = 'GPLv2',
    url = 'http://github.com/kmcminn/udprr.git',

    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Topic :: Internet :: Proxy Servers',
        'Topic :: System :: Networking'
    ],
    zip_safe = False,
    packages = ['udprr'],
    include_package_data = True,

    entry_points="""\
    [console_scripts]
    udprr=udprr.main:main
    """
)
