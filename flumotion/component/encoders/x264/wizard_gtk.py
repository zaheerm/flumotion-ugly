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

import gettext
import os

from zope.interface import implements

from flumotion.admin.assistant.interfaces import IEncoderPlugin
from flumotion.admin.assistant.models import VideoEncoder
from flumotion.common.fraction import fractionAsFloat
from flumotion.admin.gtk.basesteps import VideoEncoderStep

__version__ = "$Rev$"
_ = gettext.gettext


class X264VideoEncoder(VideoEncoder):
    """
    @ivar framerate: number of frames per second; to be set by view
    @type framerate: float
    """
    componentType = 'x264-encoder'

    def __init__(self):
        super(X264VideoEncoder, self).__init__()
        self.framerate = 25.0

        self.properties.keyframe_delta = 2.0
        self.properties.bitrate = 400
        self.properties.quality = 6

    def getProperties(self):
        properties = super(X264VideoEncoder, self).getProperties()
        properties.bitrate *= 1000

        # convert the human-friendly delta to maxdistance
        properties.keyframe_maxdistance = int(properties.keyframe_delta *
            self.framerate)
        del properties.keyframe_delta

        return properties


class X264Step(VideoEncoderStep):
    name = 'X264Encoder'
    title = _('X264 H.264 Encoder')
    sidebarName = _('X264 H.264 Encoder')
    gladeFile = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              'wizard.glade')
    componentType = 'x264'
    docSection = 'help-configuration-assistant-encoder-x264'
    docAnchor = ''
    docVersion = 'local'

    # WizardStep

    def setup(self):
        self.bitrate.data_type = int
        self.quality.data_type = int
        self.keyframe_delta.data_type = float
        self.option_string.data_type = str

        self.add_proxy(self.model.properties,
                       ['bitrate', 'quality', 'keyframe_delta',
                        'option_string'])

        # we specify keyframe_delta in seconds, but x264 expects
        # a number of frames, so we need the framerate and calculate
        # we need to go through the Step (which is the view) because models
        # don't have references to other models
        producer = self.wizard.getScenario().getVideoProducer(self.wizard)
        self.model.framerate = fractionAsFloat(producer.getFramerate())
        self.debug('Framerate of video producer: %r' % self.model.framerate)
        step = 1 / self.model.framerate
        page = 1.0
        self.keyframe_delta.set_increments(step, page)

    def workerChanged(self, worker):
        self.model.worker = worker
        self.wizard.requireElements(worker, 'x264enc')


class X264WizardPlugin(object):
    implements(IEncoderPlugin)

    def __init__(self, wizard):
        self.wizard = wizard
        self.model = X264VideoEncoder()

    def getConversionStep(self):
        return X264Step(self.wizard, self.model)
