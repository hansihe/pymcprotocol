__author__ = 'HansiHE'

from .basetype import BaseType
import struct


class SignedByteType(BaseType):
    def encode(self, field, val):
        return struct.pack("!b", val)

    def decode(self, field, buf):
        return buf[1:], struct.unpack("!b", buf[:1])[0]


class UnsignedByteType(BaseType):
    def encode(self, field, val):
        return struct.pack("!B", val)

    def decode(self, field, buf):
        return buf[1:], struct.unpack("!B", buf[:1])[0]