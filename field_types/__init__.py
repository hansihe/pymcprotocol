__author__ = 'hansihe'

from . import varint, str, short, int, byte, long, float, int128


types = {
    "varint": varint.VarintType(),
    "int": int.SignedIntegerType(),
    "u_int": int.UnsignedIntegerType(),
    "short": short.SignedShortType(),
    "u_short": short.UnsignedShortType(),
    "byte": byte.SignedByteType(),
    "u_byte": byte.UnsignedByteType(),
    "long": long.SignedLongType(),
    "u_long": long.UnsignedLongType(),
    "float": float.FloatType(),
    "int128": int128.Integer128Type(),
    "bool": None,
    "str": str.StrType(),
    "array": None,
    "bytes": None,

    # Minecraft specific types
    "slot": None,
    "entity_metadata": None
}