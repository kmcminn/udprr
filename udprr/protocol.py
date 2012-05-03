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

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
import socket


class UdpBalance(DatagramProtocol):

    def __init__(self, cfg):
        self.counter = 0
        self.pos = 0
        self.members = []
        self.configure(cfg)

    def startProtocol(self):
        self.SanitizeHosts()
        self.log.info("Balancer Started Successfully")
        """twisted calls when were connected"""
             
    def datagramReceived(self, datagram, address):
        self.log.debug(str(len(datagram)) + " bytes datagram Received")
        
        if self.pos is self.num:
            self.pos = 0

        host, port = self.hosts[self.pos].split(':')
        if self.transport.write(datagram, (host, int(port))):
            lengthd = len(datagram)
            self.pos += 1
            self.log.debug("wrote " + str(lengthd) + " bytes to " + str(host))

    def GetHostAndPort(self, noodle):
        h, p = noodle.split(':')
        host, port = socket.getaddrinfo(h, p)[0][-1]
        return host, port

    def SanitizeHosts(self):
        values = []
        for mem in self.hosts:
            host, port = self.GetHostAndPort(mem)
            values.append(host + ":" + str(port))
        self.hosts = values

    def configure(self, cfg):
        self.cfg = cfg
        DatagramProtocol.log = cfg['log']
        self.hosts = cfg['srvlist']
        self.members = cfg['general']['members']
        self.log = DatagramProtocol.log
        self.log.debug("Logging configured in protocol")
        self.port = int(cfg['general']['listen'])
        self.num = len(cfg['srvlist'])
        assert int(self.members), int(self.port)

    def start(self):
        server = UdpBalance(self.cfg)
        reactor.listenUDP(self.port, server)
        reactor.run()
