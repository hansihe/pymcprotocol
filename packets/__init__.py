__author__ = 'hansihe'

from . import play, handshake, login, status

packets = {
    "play": play.play_packets,
    "login": login.login_packets,
    "handshake": handshake.handshake_packets,
    "status": status.status_packets
}