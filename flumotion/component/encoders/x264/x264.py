# -*- Mode: Python -*-
# vi:si:et:sw=4:sts=4:ts=4
#
# flumotion-ugly - components for the Flumotion streaming media server
# Copyright (C) 2010 Zaheer Abbas Merali
# Some portions may be Copyright (C) 2004-2010 Fluendo, S.L. (www.fluendo.com).
# All rights reserved.

# This file may be distributed and/or modified under the terms of
# the GNU General Public License version 2 as published by
# the Free Software Foundation.
# This file is distributed without any warranty; without even the implied
# warranty of merchantability or fitness for a particular purpose.
# See "LICENSE.GPL" in the source distribution for more information.

# Headers in this file shall remain intact.

from flumotion.common import messages, errors
from flumotion.common.i18n import N_, gettexter
from flumotion.component import feedcomponent


__version__ = "$Rev$"
T_ = gettexter()

PROFILES={'iphone': 'profile=baseline vbv-buf-capacity=10000 ',
          'ipod': 'profile=baseline cabac=false vbv-buf-capacity=768 ',
          'default': 'profile=baseline'
         }

class X264(feedcomponent.EncoderComponent):
    checkTimestamp = True
    checkOffset = True

    def check_properties(self, props, addMessage):
        profile = props.get('profile', 'default')
        if profile not in PROFILES.keys():
            raise errors.ConfigError("The profile '%s' do not exists.")

    def get_pipeline_string(self, properties):
        profile_str = PROFILES[properties.get('profile', 'default')]
        return "ffmpegcolorspace ! x264enc name=encoder %s" % profile_str

    def configure_pipeline(self, pipeline, properties):
        element = pipeline.get_by_name('encoder')
        if 'bitrate' in properties:
            element.set_property('bitrate', properties['bitrate'] / 1000)
        if 'keyframe-maxdistance' in properties:
            element.set_property('key-int-max',
               properties['keyframe-maxdistance'])
        if 'option-string' in properties:
            element.set_property('option-string', properties['option-string'])
        if 'byte-stream' in properties:
            element.set_property('byte-stream', properties['byte-stream'])
