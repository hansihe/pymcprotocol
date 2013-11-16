__author__ = 'hansihe'

from .basetype import BaseType
from util import varint as varint_util

class StrType(BaseType):
    def encode(self, field, val):
        buf = varint_util.encode_varint(len(val))
        buf += val.encode("utf-8")
        return buf

    def decode(self, field, buf):
        byte_count, str_length = varint_util.decode_varint(buf)
        buf = buf[byte_count:]
        val = buf[:str_length].decode("utf-8")
        buf = buf[str_length:]
        return buf, val