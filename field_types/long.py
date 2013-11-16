__author__ = 'HansiHE'

from .basetype import BaseType
import struct


class SignedLongType(BaseType):
    def encode(self, field, val):
        return struct.pack("!q", val)

    def decode(self, field, buf):
        return buf[8:], struct.unpack("!q", buf[:8])[0]


class UnsignedLongType(BaseType):
    def encode(self, field, val):
        return struct.pack("!Q", val)

    def decode(self, field, buf):
        return buf[8:], struct.unpack("!Q", buf[:8])[0]