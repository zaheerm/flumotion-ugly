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

from zope.interface import implements

from flumotion.admin.assistant.interfaces import IEncoderPlugin
from flumotion.admin.assistant.models import AudioEncoder
from flumotion.admin.gtk.basesteps import AudioEncoderStep

__version__ = "$Rev: 7268 $"
_ = gettext.gettext


class LameMp3AudioEncoder(AudioEncoder):
    componentType = 'lamemp3-encoder'

    def __init__(self):
        super(LameMp3AudioEncoder, self).__init__()

        self.properties.bitrate = 128

    def getProperties(self):
        properties = super(LameMp3AudioEncoder, self).getProperties()
        properties.bitrate *= 1000
        return properties


class LameMp3Step(AudioEncoderStep):
    name = 'Lame Mp3 encoder'
    title = _('Lame Mp3 Encoder')
    sidebarName = _('Lame mp3')
    componentType = 'lamemp3'
    docSection = 'help-configuration-assistant-encoder-lamemp3'
    docAnchor = ''
    docVersion = 'local'

    # WizardStep

    def setup(self):
        self.bitrate.set_range(16, 256)
        self.bitrate.set_value(128)

        self.bitrate.data_type = int

        self.add_proxy(self.model.properties, ['bitrate'])

    def workerChanged(self, worker):
        self.model.worker = worker
        self.wizard.requireElements(worker, 'lamemp3enc')


class LameMp3WizardPlugin(object):
    implements(IEncoderPlugin)

    def __init__(self, wizard):
        self.wizard = wizard
        self.model = LameMp3AudioEncoder()

    def getConversionStep(self):
        return LameMp3Step(self.wizard, self.model)
