#!/usr/bin/env python

from sys import exit
from config.config import config
import lib.bot as bot

# Twitch Plays
# Inpsired by http://twitch.tv/twitchplayspokemon
# Written by Aidan Thomson - <aidraj0 at gmail dot com>
# Button modifications for SNES/DS use by JackNet
# *nix implementation by ynohtna92

try:
    bot.Bot().run()
except KeyboardInterrupt:
    exit()
