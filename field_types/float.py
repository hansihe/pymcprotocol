__author__ = 'HansiHE'

from .basetype import BaseType
import struct


class FloatType(BaseType):
    def encode(self, field, val):
        return struct.pack("!f", val)

    def decode(self, field, buf):
        return buf[4:], struct.unpack("!f", buf[:4])[0]