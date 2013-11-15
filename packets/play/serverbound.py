__author__ = 'hansihe'


packets = {
    0x00: {
        "name": "keep_alive",
        "fields": [
            {"n": "keep_alive_id", "t": "int"}
        ]
    },
    0x01: {
        "name": "chat_message",
        "fields": [
            {"n": "message", "t": "str"}
        ]
    },
    0x02: {
        "name": "entity_use",
        "fields": [
            {"n": "target_entity", "t": "int"},
            {"n": "mouse_action", "t": "byte"}
        ]
    },
    0x03: {
        "name": "player_base",
        "fields": [
            {"n": "on_ground", "t": "bool"}
        ]
    },
    0x04: {
        "name": "player_position",
        "fields": [
            {"n": "x", "t": "double"},
            {"n": "y", "t": "double"},
            {"n": "stance", "t": "double"},
            {"n": "z", "t": "double"},
            {"n": "on_ground", "t": "bool"}
        ]
    },
    0x05: {
        "name": "player_look",
        "fields": [
            {"n": "yaw", "t": "float"},
            {"n": "pitch", "t": "float"},
            {"n": "on_ground", "t": "bool"}
        ]
    },
    0x06: {
        "name": "player_position_look",
        "fields": [
            {"n": "x", "t": "double"},
            {"n": "y", "t": "double"},
            {"n": "stance", "t": "double"},
            {"n": "z", "t": "double"},
            {"n": "yaw", "t": "float"},
            {"n": "pitch", "t": "float"},
            {"n": "on_ground", "t": "bool"}
        ]
    },
    0x07: {
        "name": "player_block_dig",
        "fields": [
            {"n": "status", "t": "byte"},
            {"n": "x", "t": "int"},
            {"n": "y", "t": "u_byte"},
            {"n": "z", "t": "int"},
            {"n": "face", "t": "byte"}
        ]
    },
    0x08: {
        "name": "player_block_place",
        "fields": [
            {"n": "x", "t": "int"},
            {"n": "y", "t": "u_byte"},
            {"n": "z", "t": "int"},
            {"n": "direction", "t": "byte"},
            {"n": "held_item", "t": "slot"},
            {"n": "cursor_x", "t": "byte"},
            {"n": "cursor_y", "t": "byte"},
            {"n": "cursor_z", "t": "byte"}
        ]
    },
    0x09: {
        "name": "player_held_item_change",
        "fields": [
            {"n": "slot_num", "t": "short"}
        ]
    },
    0x0a: {
        "name": "animation",
        "fields": [
            {"n": "entity_id", "t": "int"}, #player id
            {"n": "animation", "t": "byte"}
        ]
    },
    0x0b: {
        "name": "entity_action",
        "fields": [
            {"n": "entity_id", "t": "int"}, #player id
            {"n": "action_id", "t": "byte"},
            {"n": "jump_boost", "t": "int"}
        ]
    },
    0x0c: {
        "name": "vehicle_steer",
        "fields": [
            {"n": "sideways", "t": "float"},
            {"n": "forward", "t": "float"},
            {"n": "jump", "t": "bool"},
            {"n": "unmount", "t": "bool"}
        ]
    },
    0x0d: {
        "name": "window_close",
        "fields": [
            {"n": "window_id", "t": "byte"}
        ]
    },
    0x0e: {
        "name": "window_click",
        "fields": [
            {"n": "window_id", "t": "byte"},
            {"n": "slot_num", "t": "short"},
            {"n": "button", "t": "byte"},
            {"n": "action_number", "t": "short"},
            {"n": "inventory_mode", "t": "byte"},
            {"n": "item", "t": "slot"}
        ]
    },
    0x0f: {
        "name": "confirm_transaction",
        "fields": [
            {"n": "window_id", "t": "byte"},
            {"n": "action_number", "t": "short"},
            {"n": "accepted", "t": "bool"}
        ]
    },
    0x10: {
        "name": "inventory_action_creative",
        "fields": [
            {"n": "slot_num", "t": "short"},
            {"n": "item", "t": "slot"}
        ]
    },
    0x11: {
        "name": "item_enchant",
        "fields": [
            {"n": "window_id", "t": "byte"},
            {"n": "enchantment", "t": "byte"}
        ]
    },
    0x12: {
        "name": "sign_update",
        "fields": [
            {"n": "x", "t": "int"},
            {"n": "y", "t": "short"},
            {"n": "z", "t": "int"},
            {"n": "line_1", "t": "str"},
            {"n": "line_2", "t": "str"},
            {"n": "line_3", "t": "str"},
            {"n": "line_4", "t": "str"}
        ]
    },
    0x13: {
        "name": "player_abilities",
        "fields": [
            {"n": "flags", "t": "byte"},
            {"n": "flying_speed", "t": "float"},
            {"n": "walking_speed", "t": "float"}
        ]
    },
    0x14: {
        "name": "tab_complete",
        "fields": [
            {"n": "text", "t": "str"}
        ]
    },
    0x15: {
        "name": "client_settings",
        "fields": [
            {"n": "locale", "t": "str"},
            {"n": "view_distance", "t": "byte"},
            {"n": "chat_flags", "t": "byte"},
            {"n": "unused", "t": "bool"},
            {"n": "difficulty", "t": "byte"},
            {"n": "show_cape", "t": "boolean"}
        ]
    },
    0x16: {
        "name": "client_status",
        "fields": [
            {"n": "action_id", "t": "byte"}
        ]
    },
    0x17: {
        "name": "plugin_message",
        "fields": [
            {"n": "channel", "t": "str"},
            {"n": "length", "t": "short", "output_source": {
                "op": "length",
                "field": "data"
            }},
            {"n": "data", "t": "bytes", "bytes_def": {
                "length_source": "field",
                "length_field": "length"
            }}
        ]
    }
}