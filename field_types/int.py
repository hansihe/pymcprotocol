__author__ = 'HansiHE'

from .basetype import BaseType
import struct


class SignedIntegerType(BaseType):
    def encode(self, field, val):
        return struct.pack("!i", val)

    def decode(self, field, buf):
        return buf[4:], struct.unpack("!i", buf[:4])[0]


class UnsignedIntegerType(BaseType):
    def encode(self, field, val):
        return struct.pack("!I", val)

    def decode(self, field, buf):
        return buf[4:], struct.unpack("!I", buf[:4])[0]