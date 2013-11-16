__author__ = 'HansiHE'

from twisted.internet import reactor, protocol
import field_types
import packets
import packet_repr
import time

class MinecraftClient(protocol.Protocol):

    def __init__(self):
        self.buf = ""

    def connectionMade(self):
        print "made"

        packet = packet_repr.Packet(packet_repr.PacketDescriptor("handshake", "sb", 0x00))
        packet.protocol_version = 4
        packet.server_address = "junction.at"
        packet.server_port = 25565
        packet.next_state = 1
        self.transport.write(packet.encode_full())

        packet = packet_repr.Packet(packet_repr.PacketDescriptor("status", "sb", 0x00))
        self.transport.write(packet.encode_full())


    def dataReceived(self, data):
        self.buf += data
        while True:
            try:
                self.buf, packet = packet_repr.Packet.decode_full("status", "cb", self.buf)
            except packet_repr.NotEnoughDataException:
                break
            print(packet.data)

            if packet.packet_type.name == "status_response":
                out_packet = packet_repr.Packet(packet_repr.PacketDescriptor("status", "sb", 0x01))
                out_packet.time = int(time.time()*100)
                self.transport.write(out_packet.encode_full())

            elif packet.packet_type.name == "status_ping":
                print(int(time.time()*100) - packet.time)


    def connectionLost(self, reason="connectionDone"):
        print reason


class MinecraftClientFactory(protocol.ClientFactory):
    protocol = MinecraftClient

    def clientConnectionFailed(self, connector, reason):
        print reason

    def clientConnectionLost(self, connector, reason):
        print reason


def main():
    f = MinecraftClientFactory()
    reactor.connectTCP("junction.at", 25565, f)
    reactor.run()

main()

#import packet_repr
#print packet_repr.PacketDescriptor("play", "cb", 0x3b).__repr__()

#packet = "\x11\x00\x04\x0b\x6a\x75\x6e\x63\x74\x69\x6f\x6e\x2e\x61\x74\x63\xdd\x01"
#
#buf, length = field_types.types["varint"].decode({}, packet)
#buf, packet_id = field_types.types["varint"].decode({}, buf)
#
##print(length)
##print(packet_id)
#import packet_repr
#packet_r = packet_repr.Packet(packet_repr.PacketDescriptor("handshake", "sb", packet_id))
#print packet_r.decode(buf)
#
#print(packet_r.data)