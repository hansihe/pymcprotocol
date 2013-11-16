__author__ = 'hansihe'

import basetype
from util import varint as varint_util


class VarintType(basetype.BaseType):

    def encode(self, field, val):
        return varint_util.encode_varint(val)

    def decode(self, field, buf):
        byte_count, var = varint_util.decode_varint(buf)
        buf = buf[byte_count:]
        return buf, var