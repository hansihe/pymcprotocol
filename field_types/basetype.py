__author__ = 'hansihe'


class EncodeError(Exception): pass
class DecodeError(Exception): pass


class BaseType(object):

    def encode(self, field, val):
        raise NotImplementedError()

    def decode(self, field, buffer):
        raise NotImplementedError()