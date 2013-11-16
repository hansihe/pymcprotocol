__author__ = 'HansiHE'

from .basetype import BaseType
import struct


class SignedShortType(BaseType):
    def encode(self, field, val):
        return struct.pack("!h", val)

    def decode(self, field, buf):
        return buf[2:], struct.unpack("!h", buf[:2])[0]


class UnsignedShortType(BaseType):
    def encode(self, field, val):
        return struct.pack("!H", val)

    def decode(self, field, buf):
        return buf[2:], struct.unpack("!H", buf[:2])[0]