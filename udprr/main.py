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
import optparse
import setproctitle
import logging as l
from udprr.config import Configure
from udprr.protocol import UdpBalance




LOGGING_LEVELS = {'critical': l.CRITICAL,
                  'error': l.ERROR,
                  'warning': l.WARNING,
                  'info': l.INFO,
                  'debug': l.DEBUG}


def main():

    # set unix process name
    setproctitle.setproctitle('udprr')

    parser = optparse.OptionParser()
    parser.add_option('-l', '--logging-level',
        help='debug level default is warning')
    parser.add_option('-o', '--log-file',
        help='log to file instead of stdout')
    parser.add_option('-c', '--config-file',
        help='path to config file')

    (options, args) = parser.parse_args()

    # set default logging level
    logging_level = LOGGING_LEVELS.get(options.logging_level, l.WARNING)


    if not options.log_file:
        l.basicConfig(level=logging_level,
            format='%(asctime)s %(levelname)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S')
    else:
        l.basicConfig(level=logging_level, filename=options.logging_file,
            format='%(asctime)s %(levelname)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S')

    # load config
    if not options.config_file:
        l.error('no config specified, exiting')
        sys.exit(1)
    else:
        c = Configure(options.config_file)
        l.debug('Loading config at ' + str(options.config_file))
        cfg = c.parse()
        cfg['log'] = l
        l.info('Listening on ' + str(cfg['general']['listen']))
        cfg['srvlist'] = eval(cfg['servers']['hosts'])
        l.info('Starting udp round robin for ' + str(len(cfg['srvlist'])) + ' hosts')

    """start the server """
    UdpBalance(cfg).start()
    


if __name__ == '__main__':
    main()
