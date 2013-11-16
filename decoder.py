__author__ = 'hansihe'

import field_types


class DataDecoder(object):

    def decode(self, packet, data):
        result = dict()
        return self._decode(packet.packet_recipe["fields"], data, result)

    def _decode(self, fields, data, result):
        buf = data
        for field in fields:
            type_handler = field_types.types[field["t"]]
            try:
                buf, result[field["n"]] = type_handler.decode(field, buf)
            except KeyError:
                raise BufferError(field)

        return buf, result