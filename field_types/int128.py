__author__ = 'HansiHE'

from .basetype import BaseType
import struct

max_int64 = 0xFFFFFFFFFFFFFFFF


class Integer128Type(BaseType):
    def encode(self, field, val):
        return struct.pack("!QQ", (val >> 64) & max_int64, val & max_int64)

    def decode(self, field, buf):
        a, b = struct.unpack("!QQ", buf[:16])
        return buf[16:], (a << 64) | b