__author__ = 'hansihe'

status_packets = {
    "cb": {
        0x00: {
            "name": "status_response",
            "fields": [
                {"n": "data", "t": "str", "processor": "json"}
            ]
        },
        0x01: {
            "name": "status_ping",
            "fields": [
                {"n": "time", "t": "long"}
            ]
        }
    },
    "sb": {
        0x00: {
            "name": "status_request",
            "fields": []
        },
        0x01: {
            "name": "status_ping",
            "fields": [
                {"n": "time", "t": "long"}
            ]
        }
    }
}