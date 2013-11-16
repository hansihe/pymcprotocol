__author__ = 'hansihe'

import field_types


class EncodeDataFieldNotExisting(Exception): pass


class DataEncoder(object):

    def encode(self, packet):
        result = self._encode(packet.packet_recipe["fields"], packet.data, "")
        return result

    def _encode(self, fields, data, result):
        for field in fields:
            type_handler = field_types.types[field["t"]]
            try:
                result += type_handler.encode(field, data[field["n"]])
            except KeyError:
                raise EncodeDataFieldNotExisting(field)
        return result