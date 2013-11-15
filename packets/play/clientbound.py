__author__ = 'HansiHE'

packets = {
    0x00: {
        "name": "keep_alive",
        "fields": [
            {"n": "keep_alive_id", "t": "int"}
        ]
    },
    0x01: {
        "name": "join_game",
        "fields": [
            {"n": "entity_id", "t": "int"},
            {"n": "gamemode", "t": "u_byte"},
            {"n": "dimension", "t": "byte"},
            {"n": "difficulty", "t": "u_byte"},
            {"n": "max_players", "t": "u_byte"},
            {"n": "level_type", "t": "str"}
        ]
    },
    0x02: {
        "name": "chat_message",
        "fields": [
            {"n": "chat_data", "t": "json"}
        ]
    },
    0x03: {
        "name": "time_update",
        "fields": [
            {"n": "age_of_world", "t": "long"},
            {"n": "time_of_day", "t": "long"}
        ]
    },
    0x04: {
        "name": "entity_equipment",
        "fields": [
            {"n": "entity_id", "t": "int"},
            {"n": "slot", "t": "short"},
            {"n": "item", "t": "slot"}
        ]
    },
    0x05: {
        "name": "spawn_position",
        "fields": [
            {"n": "x", "t": "int"},
            {"n": "y", "t": "int"},
            {"n": "z", "t": "int"}
        ]
    },
    0x06: {
        "name": "update_health",
        "fields": [
            {"n": "health", "t": "float"},
            {"n": "food", "t": "short"},
            {"n": "food_saturation", "t": "float"}
        ]
    },
    0x07: {
        "name": "respawn",
        "fields": [
            {"n": "dimension", "t": "int"},
            {"n": "difficulty", "t": "u_byte"},
            {"n": "gamemode", "t": "u_byte"},
            {"n": "level_type", "t": "string"}
        ]
    },
    0x08: {
        "name": "player_position",
        "fields": [
            {"n": "x", "t": "double"},
            {"n": "y", "t": "double"},
            {"n": "z", "t": "double"},
            {"n": "yaw", "t": "float"},
            {"n": "pitch", "t": "float"},
            {"n": "on_ground", "t": "bool"}
        ]
    },
    0x09: {
        "name": "held_item_change",
        "fields": [
            {"n": "slot", "t": "byte"}
        ]
    },
    0x0a: {
        "name": "use_bed",
        "fields": [
            {"n": "entity_id", "t": "int"},
            {"n": "x", "t": "int"},
            {"n": "y", "t": "u_byte"},
            {"n": "z", "t": "int"}
        ]
    },
    0x0b: {
        "name": "animation",
        "fields": [
            {"n": "entity_id", "t": "varint"}, #https://developers.google.com/protocol-buffers/docs/encoding#varints
            {"n": "animation", "t": "u_byte"}
        ]
    },
    0x0c: {
        "name": "spawn_player",
        "fields": [
            {"n": "entity_id", "t": "varint"},
            {"n": "player_uuid", "t": "str"},
            {"n": "player_name", "t": "str"},
            {"n": "x", "t": "int"}, #fixed point
            {"n": "y", "t": "int"}, #fixed point
            {"n": "z", "t": "int"}, #fixed point
            {"n": "yaw", "t": "byte"}, #Player rotation as a packed byte
            {"n": "pitch", "t": "byte"}, #Player rotation as a packet byte
            {"n": "current_item", "t": "short"},
            {"n": "metadata", "t": "entity_metadata"} #http://wiki.vg/Entities#Entity_Metadata_Format
        ]
    },
    0x0d: {
        "name": "collect_item",
        "fields": [
            {"n": "collected_entity_id", "t": "int"},
            {"n": "collector_entity_id", "t": "int"}
        ]
    },
    0x0e: {
        "name": "spawn_object",
        "fields": [
            {"n": "entity_id", "t": "varint"},
            {"n": "type", "t": "byte"},
            {"n": "x", "t": "int"}, #fixed point
            {"n": "y", "t": "int"}, #fixed point
            {"n": "z", "t": "int"}, #fixed point
            {"n": "pitch", "t": "byte"}, #in steps of 2p/256
            {"n": "yaw", "t": "byte"}, #in steps of 2p/256
            {"n": "data", "t": "object_data"} #http://wiki.vg/Object_Data
        ]
    },
    0x0f: {
        "name": "spawn_mob",
        "fields": [
            {"n": "entity_id", "t": "varint"},
            {"n": "type", "t": "u_byte"},
            {"n": "x", "t": "int"}, #fixed point
            {"n": "y", "t": "int"}, #fixed point
            {"n": "z", "t": "int"}, #fixed point
            {"n": "pitch", "t": "byte"}, #in steps of 2p/256
            {"n": "head_pitch", "t": "byte"}, #in steps of 2p/256
            {"n": "yaw", "t": "byte"}, #in steps of 2p/256
            {"n": "velocity_x", "t": "short"},
            {"n": "velocity_y", "t": "short"},
            {"n": "velocity_z", "t": "short"},
            {"n": "metadata", "t": "entity_metadata"}
        ]
    },
    0x10: {
        "name": "spawn_painting",
        "fields": [
            {"n": "entity_id", "t": "varint"},
            {"n": "title", "t": "str"},
            {"n": "x", "t": "int"},
            {"n": "y", "t": "int"},
            {"n": "z", "t": "int"},
            {"n": "direction", "t": "int"}
        ]
    },
    0x11: {
        "name": "spawn_experience_orb",
        "fields": [
            {"n": "entity_id", "t": "varint"},
            {"n": "x", "t": "int"}, #fixed point
            {"n": "y", "t": "int"}, #fixed point
            {"n": "z", "t": "int"}, #fixed point
            {"n": "count", "t": "int"}
        ]
    },
    0x12: {
        "name": "entity_velocity", #http://wiki.vg/Protocol#Entity_Velocity
        "fields": [
            {"n": "entity_id", "t": "int"},
            {"n": "velocity_x", "t": "short"},
            {"n": "velocity_y", "t": "short"},
            {"n": "velocity_z", "t": "short"}
        ]
    },
    0x13: {
        "name": "destroy_entities",
        "fields": [
            {"n": "count", "t": "byte", "output_source": {
                "op": "length",
                "field": "ids"
            }},
            {"n": "ids", "t": "array", "array_def": {
                "fields": [
                    {"n": "id", "t": "int"}
                ]
            }}
        ]
    },
    0x14: {
        "name": "entity_base",
        "fields": [
            {"n": "entity_id", "t": "int"}
        ]
    },
    0x15: {
        "name": "entity_relative_move",
        "fields": [
            {"n": "entity_id", "t": "int"},
            {"n": "delta_x", "t": "byte"}, #fixed point
            {"n": "delta_y", "t": "byte"}, #fixed point
            {"n": "delta_z", "t": "byte"} #fixed point
        ]
    },
    0x16: {
        "name": "entity_look",
        "fields": [
            {"n": "entity_id", "t": "int"},
            {"n": "yaw", "t": "byte"}, #fraction of 360
            {"n": "pitch", "t": "byte"} #fraction of 360
        ]
    },
    0x17: {
        "name": "entity_look_relative_move",
        "fields": [
            {"n": "entity_id", "t": "int"},
            {"n": "delta_x", "t": "byte"}, #fixed point
            {"n": "delta_y", "t": "byte"}, #fixed point
            {"n": "delta_z", "t": "byte"}, #fixed point
            {"n": "yaw", "t": "byte"}, #fraction of 360
            {"n": "pitch", "t": "byte"} #fraction of 360
        ]
    },
    0x18: {
        "name": "entity_teleport",
        "fields": [
            {"n": "entity_id", "t": "int"},
            {"n": "x", "t": "int"}, #fixed point
            {"n": "y", "t": "int"}, #fixed point
            {"n": "z", "t": "int"}, #fixed point
            {"n": "yaw", "t": "byte"}, #fraction of 360
            {"n": "pitch", "t": "byte"} #fraction of 360
        ]
    },
    0x19: {
        "name": "entity_head_look",
        "fields": [
            {"n": "entity_id", "t": "int"},
            {"n": "head_yaw", "t": "byte"} #in steps of 2p/256
        ]
    },
    0x1a: {
        "name": "entity_status",
        "fields": [
            {"n": "entity_id", "t": "int"},
            {"n": "entity_status", "t": "byte"} #http://wiki.vg/Protocol#Entity_Status
        ]
    },
    0x1b: {
        "name": "attach_entity",
        "fields": [
            {"n": "entity_id", "t": "int"},
            {"n": "vehicle_id", "t": "int"},
            {"n": "leash", "t": "bool"}
        ]
    },
    0x1c: {
        "name": "entity_metadata",
        "fields": [
            {"n": "entity_id", "t": "int"},
            {"n": "entity_metadata", "t": "entity_metadata"}
        ]
    },
    0x1d: {
        "name": "entity_effect",
        "fields": [
            {"n": "entity_id", "t": "int"},
            {"n": "effect_id", "t": "byte"},
            {"n": "amplifier", "t": "byte"},
            {"n": "duration", "t": "short"}
        ]
    },
    0x1e: {
        "name": "entitiy_remove_effect",
        "fields": [
            {"n": "entity_id", "t": "int"},
            {"n": "effect_id", "t": "byte"}
        ]
    },
    0x1f: {
        "name": "set_experience",
        "fields": [
            {"n": "experience_bar", "t": "float"},
            {"n": "level", "t": "short"},
            {"n": "total_experience", "t": "short"}
        ]
    },
    0x20: {
        "name": "entity_properties",
        "fields": [
            {"n": "entity_id", "t": "int"},
            {"n": "count", "t": "int", "output_source": {
                "op": "length",
                "field": "properties"
            }},
            {"n": "properties", "t": "array", "array_def": {
                "length_source": "field",
                "length_type": "count",
                "length_field": "count",
                "fields": [
                    {"n": "key", "t": "str"},
                    {"n": "value", "t": "double"},
                    {"n": "modifier_count", "t": "short", "output_source": {
                        "op": "length",
                        "field": "modifiers"
                    }},
                    {"n": "modifiers", "t": "array", "array_def": {
                        "length_source": "field",
                        "length_type": "count",
                        "length_field": "modifier_count",
                        "fields": [
                            {"n": "uuid", "t": "str"},
                            {"n": "amount", "t": "double"},
                            {"n": "operation", "t": "byte"}
                        ]
                    }}
                ]
            }}
        ]
    },
    0x21: {
        "name": "chunk_data" #Fuck that, saving this for last
    },
    0x22: {
        "name": "block_change_multi",
        "fields": [
            {"n": "chunk_x", "t": "int"},
            {"n": "chunk_y", "t": "int"},
            {"n": "block_change_count", "t": "short", "output_source": {
                "op": "length",
                "field": "changes"
            }},
            {"n": "block_change_data_size", "t": "int", "output_source": { #(wat)
                "op": "length",
                "field": "changes" #TODO: Multiply by 4
            }},
            {"n": "changes", "t": "array", "array_def": { #http://wiki.vg/Protocol#Multi_Block_Change
                "length_source": "field",
                "length_type": "count",
                "length_field": "block_change_count",
                "field": {"t": "int"}
            }}
        ]
    },
    0x23: {
        "name": "block_change",
        "fields": [
            {"n": "x", "t": "int"},
            {"n": "y", "t": "u_byte"},
            {"n": "z", "t": "int"},
            {"n": "block_type", "t": "varint"},
            {"n": "block_data", "t": "u_byte"}
        ]
    },
    0x24: {
        "name": "block_action",
        "fields": [
            {"n": "x", "t": "int"},
            {"n": "y", "t": "short"},
            {"n": "z", "t": "int"},
            {"n": "byte_1", "t": "byte"},
            {"n": "byte_2", "t": "byte"},
            {"n": "block_type", "t": "varint"}
        ]
    },
    0x25: {
        "name": "block_animation_break",
        "fields": [
            {"n": "entity_id", "t": "varint"},
            {"n": "x", "t": "int"},
            {"n": "y", "t": "int"},
            {"n": "z", "t": "int"},
            {"n": "destroy_stage", "t": "byte"}
        ]
    },
    0x26: {
        "name": "chunk_data_bulk" #See 0x21
    },
    0x27: {
        "name": "explosion",
        "fields": [
            {"n": "x", "t": "float"},
            {"n": "y", "t": "float"},
            {"n": "z", "t": "float"},
            {"n": "radius", "t": "float"},
            {"n": "record_count", "t": "int", "output_source": {
                    "op": "length",
                    "field": "records"
            }},
            {"n": "records", "t": "array", "array_def": { #http://wiki.vg/Protocol#Explosion
                "length_source": "field",
                "length_type": "count",
                "length_field": "record_count",
                "fields": [
                    {"n": "offset_x", "t": "byte"},
                    {"n": "offset_y", "t": "byte"},
                    {"n": "offset_z", "t": "byte"}
                ]
            }},
            {"n": "player_motion_x", "t": "float"},
            {"n": "player_motion_y", "t": "float"},
            {"n": "player_motion_z", "t": "float"}
        ]
    },
    0x28: {
        "name": "effect",
        "fields": [
            {"n": "effect_id", "t": "int"},
            {"n": "position_x", "t": "int"},
            {"n": "position_y", "t": "byte"},
            {"n": "position_z", "t": "int"},
            {"n": "data", "t": "int"},
            {"n": "disable_relative_volume", "t": "bool"}
        ]
    },
    0x29: {
        "name": "sound_effect", #http://wiki.vg/Protocol#Sound_Effect
        "fields": [
            {"n": "sound_name", "t": "str"},
            {"n": "position_x", "t": "int"},
            {"n": "position_y", "t": "int"},
            {"n": "position_z", "t": "int"},
            {"n": "volume", "t": "float"}, #1 is 100%
            {"n": "pitch", "t": "u_byte"} #63 is 100%
        ]
    },
    0x2b: {
        "name": "change_game_state",
        "fields": [
            {"n": "reason", "t": "u_byte"},
            {"n": "value", "t": "float"}
        ]
    },
    0x2c: {
        "name": "spawn_global_entity",
        "fields": [
            {"n": "entity_id", "t": "varint"},
            {"n": "type", "t": "byte"},
            {"n": "x", "t": "int"},
            {"n": "y", "t": "int"},
            {"n": "z", "t": "int"}
        ]
    },
    0x2d: {
        "name": "window_open",
        "fields": [
            {"n": "window_id", "t": "u_byte"},
            {"n": "inventory_type", "t": "u_byte"},
            {"n": "window_title", "t": "str"},
            {"n": "slot_count", "t": "u_byte"},
            {"n": "use_title_directly", "t": "bool"},
            {"n": "entity_id", "t": "int", "if": [{ #Horse entity id. Only sent when inventory_type==11(animalchest)
                "field": "inventory_type", "op": "eq", "value": "11"}
            ]}
        ]
    },
    0x2e: {
        "name": "window_close",
        "fields": [
            {"n": "window_id", "t": "u_byte"}
        ]
    },
    0x2f: {
        "name": "window_set_slot",
        "fields": [
            {"n": "window_id", "t": "u_byte"},
            {"n": "slot_num", "t": "short"},
            {"n": "slot_data", "t": "slot"}
        ]
    },
    0x30: {
        "name": "window_items",
        "fields": [
            {"n": "window_id", "t": "u_byte"},
            {"n": "count", "t": "short"},
            {"n": "slots", "t": "array", "array_def": {
                "length_source": "field",
                "length_type": "count",
                "length_field": "count",
                "field": {"t": "slot"}
            }}
        ]
    },
    0x31: {
        "name": "window_property",
        "fields": [
            {"n": "window_id", "t": "u_byte"},
            {"n": "property", "t": "short"},
            {"n": "value", "t": "short"}
        ]
    },
    0x32: {
        "name": "window_confirm_transaction",
        "fields": [
            {"n": "window_id", "t": "u_byte"},
            {"n": "action_number", "t": "short"},
            {"n": "accepted", "t": "bool"}
        ]
    },
    0x33: {
        "name": "sign_update",
        "fields": [
            {"n": "x", "t": "int"},
            {"n": "y", "t": "short"},
            {"n": "z", "t": "int"},
            {"n": "line_1", "t": "str"}, #Change these to array?
            {"n": "line_2", "t": "str"},
            {"n": "line_3", "t": "str"},
            {"n": "line_4", "t": "str"}
        ]
    },
    0x34: {
        "name": "map",
        "fields": [
            {"n": "item_damage", "t": "varint"},
            {"n": "length", "t": "short", "output_source": {
                    "op": "length",
                    "field": "data"
            }},
            {"n": "data", "t": "bytes", "bytes_def": {
                    "length_source": "field",
                    "length_field": "length"
            }}
        ]
    },
    0x35: {
        "name": "block_entity_update",
        "fields": [
            {"n": "x", "t": "int"},
            {"n": "y", "t": "short"},
            {"n": "z", "t": "int"},
            {"n": "action", "t": "u_byte"},
            {"n": "data_length", "t": "short"},
            {"n": "data", "t": "bytes", "processor": "nbt", "nbt_def": {
                "length_source": "field",
                "length_field": "data_length"
            }}
        ]
    },
    0x36: {
        "name": "sign_open_editor",
        "fields": [
            {"n": "x", "t": "int"},
            {"n": "y", "t": "int"},
            {"n": "z", "t": "int"}
        ]
    },
    0x37: {
        "name": "statistics",
        "fields": [
            {"n": "entry_count", "t": "varint", "output_source": {
                "op": "length",
                "source": "entries"
            }},
            {"n": "entries", "t": "array", "array_def": {
                "length_source": "field",
                "length_type": "count",
                "length_field": "entry_count",
                "fields": [
                    {"n": "name", "t": "string"},
                    {"n": "value", "t": "varint"}
                ]
            }}
        ]
    },
    0x38: {
        "name": "player_list_item",
        "fields": [
            {"n": "player_name", "t": "str"},
            {"n": "player_online", "t": "bool"},
            {"n": "player_ping", "t": "short"}
        ]
    },
    0x39: {
        "name": "player_abilities",
        "fields": [
            {"n": "flags", "t": "byte"},
            {"n": "flying_speed", "t": "float"},
            {"n": "walking_speed", "t": "float"}
        ]
    },
    0x3a: {
        "name": "tab_complete",
        "fields": [
            {"n": "match_count", "t": "varint"},
            {"n": "matches", "t": "array", "array_def": {
                "length_source": "field",
                "length_type": "count",
                "length_field": "match_count",
                "field": {"t": "str"}
            }}
        ]
    },
    0x3b: {
        "name": "scoreboard",
        "fields": [
            {"n": "scoreboard_name", "t": "str"},
            {"n": "scoreboard_text", "t": "str"},
            {"n": "action", "t": "byte"}
        ]
    },
    0x3c: {
        "name": "scoreboard_update_score",
        "fields": [
            {"n": "item_name", "t": "str"},
            {"n": "action", "t": "byte"},
            {"n": "scoreboard_name", "t": "str"},
            {"n": "value", "t": "int"}
        ]
    },
    0x3d: {
        "name": "scoreboard_display",
        "fields": [
            {"n": "position", "t": "byte"},
            {"n": "scoreboard_name", "t": "byte"}
        ]
    },
    0x3e: {
        "name": "teams",
        "fields": [
            {"n": "team_name", "t": "str"},
            {"n": "action", "t": "byte"},
            {"n": "team_name", "t": "str", "if": [
                {"op": "or", "conditions": [
                    {"field": "action", "op": "eq", "value": "0"},
                    {"field": "action", "op": "eq", "value": "2"}
                ]}
            ]},
            {"n": "team_prefix", "t": "str", "if": [
                {"op": "or", "conditions": [
                    {"field": "action", "op": "eq", "value": "0"},
                    {"field": "action", "op": "eq", "value": "2"}
                ]}
            ]},
            {"n": "team_suffix", "t": "str", "if": [
                {"op": "or", "conditions": [
                    {"field": "action", "op": "eq", "value": "0"},
                    {"field": "action", "op": "eq", "value": "2"}
                ]}
            ]},
            {"n": "friendly_fire", "t": "byte", "if": [
                {"op": "or", "conditions": [
                    {"field": "action", "op": "eq", "value": "0"},
                    {"field": "action", "op": "eq", "value": "2"}
                ]}
            ]},
            {"n": "players_count", "t": "short", "if": [
                {"op": "or", "conditions": [
                    {"field": "action", "op": "eq", "value": "0"},
                    {"field": "action", "op": "eq", "value": "3"},
                    {"field": "action", "op": "eq", "value": "4"}
                ]}], "output_source": {
                    "op": "length",
                    "field": "players"
                }
            },
            {"n": "players", "t": "array", "if": [
                {"op": "or", "conditions": [
                    {"field": "action", "op": "eq", "value": "0"},
                    {"field": "action", "op": "eq", "value": "3"},
                    {"field": "action", "op": "eq", "value": "4"}
                ]}], "array_def": {
                    "length_source": "field",
                    "length_type": "count",
                    "length_field": "players_count",
                    "field": {"t": "str"}
                }
            }
        ]
    },
    0x3f: {
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
    },
    0x40: {
        "name": "disconnect",
        "fields": [
            {"n": "reason", "t": "str", "processor": "json"}
        ]
    }
}