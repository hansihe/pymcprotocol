__author__ = 'hansihe'

handshake_packets = {
    "cb": {},
    "sb": {
        0x00: {
            "name": "handshake",
            "fields": [
                {"n": "protocol_version", "t": "varint"},
                {"n": "server_address", "t": "str"},
                {"n": "server_port", "t": "u_short"},
                {"n": "next_state", "t": "varint"}
            ]
        }
    }
}