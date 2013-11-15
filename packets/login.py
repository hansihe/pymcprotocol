__author__ = 'hansihe'

login_packets = {
    "cb": {
        0x00: {
            "name": "disconnect",
            "fields": [
                {"n": "data", "t": "str", "processor": "json"}
            ]
        },
        0x01: {
            "name": "encryption_request",
            "fields": [
                {"n": "server_id", "t": "str"},
                {"n": "pubkey_length", "t": "short", "output_source": { #output source replaces the value of the field on emission
                    "op": "length",
                    "field": "pubkey"
                }},
                {"n": "pubkey", "t": "bytes", "bytes_def": {
                    "length_source": "field",
                    "length_field": "pubkey_length"
                }},
                {"n": "verify_token_length", "t": "short", "output_source": {
                    "op": "length",
                    "field": "verify_token"
                }},
                {"n": "verify_token", "t": "bytes", "bytes_def": {
                    "length_source": "field",
                    "length_field": "verify_token_length"
                }}
            ]
        },
        0x02: {
            "name": "login_success",
            "fields": [
                {"n": "uuid", "t": "str"},
                {"n": "username", "t": "str"}
            ]
        }
    },
    "sb": {
        0x00: {
            "name": "login_start",
            "fields": [
                {"n": "name", "t": "str"}
            ]
        },
        0x01: {
            "name": "encryption_response",
            "fields": [
                {"n": "shared_secret_length", "t": "short", "output_source": {
                    "op": "length",
                    "field": "shared_secret"
                }},
                {"n": "shared_secret", "t": "bytes", "bytes_def": {
                    "length_source": "field",
                    "length_field": "shared_secret_length"
                }},
                {"n": "verify_token_length", "t": "short", "output_source": {
                    "op": "length",
                    "field": "verify_token"
                }},
                {"n": "verify_token", "t": "bytes", "bytes_def": {
                    "length_source": "field",
                    "length_field": "verify_token_length"
                }}
            ]
        }
    }
}