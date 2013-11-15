__author__ = 'hansihe'

from . import clientbound, serverbound

play_packets = {
    "cb": clientbound.packets,
    "sb": serverbound.packets
}