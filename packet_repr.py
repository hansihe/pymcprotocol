__author__ = 'hansihe'

from packets import packets
from encoder import DataEncoder
from decoder import DataDecoder
import field_types

encoder = DataEncoder()
decoder = DataDecoder()


class PacketTypeException(Exception): pass
class NotEnoughDataException(Exception): pass


class PacketDescriptor(object):
    def __init__(self, protocol_status, direction, packet_id):
        self.protocol_status = protocol_status
        self.direction = direction
        self.packet_id = packet_id

        try:
            self.recipe = packets[self.protocol_status][self.direction][self.packet_id]
        except KeyError:
            raise PacketTypeException("Recipe for %s is not defined." % self.__repr__())

        self.name = self.recipe["name"]

    def get_recipe(self):
        return self.recipe

    def __repr__(self):
        return "[PacketDescriptor %s/%s/%#04x]" % (self.protocol_status, self.direction, self.packet_id)


class Packet(object):
    def __init__(self, packet_type):
        """
        :param packet_type: A PacketDescriptor object defining the packet type
        """
        self.__dict__['packet_type'] = packet_type
        self.__dict__['packet_recipe'] = self.packet_type.get_recipe()

        self.__dict__['data'] = dict()

    def __getattr__(self, item):
        return self.data.get(item)

    def __setattr__(self, key, value):
        self.data[key] = value

    def encode(self):
        return encoder.encode(self)

    def encode_full(self):
        data = ""
        data += field_types.types["varint"].encode({}, self.packet_type.packet_id)
        data += self.encode()
        data = field_types.types["varint"].encode({}, len(data)) + data
        return data

    def decode(self, data):
        buf, data = decoder.decode(self, data)
        self.__dict__['data'] = data
        return buf

    @classmethod
    def decode_full(cls, protocol_status, direction, data):
        buf = data

        if len(buf) is 0:
            raise NotEnoughDataException()

        buf, length = field_types.types["varint"].decode({}, buf)
        if length > len(buf) or len(buf) < 1:
            raise NotEnoughDataException()

        rest = buf[length:]
        buf = buf[:length]

        buf, packet_id = field_types.types["varint"].decode({}, buf)

        packet = Packet(PacketDescriptor(protocol_status, direction, packet_id))
        packet.decode(buf)

        return rest, packet


class PacketSub(object):
    pass