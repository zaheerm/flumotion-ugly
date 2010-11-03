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


class FaacAudioEncoder(AudioEncoder):
    componentType = 'faac-encoder'

    def __init__(self):
        super(FaacAudioEncoder, self).__init__()

        self.properties.bitrate = 128

    def getProperties(self):
        properties = super(FaacAudioEncoder, self).getProperties()
        properties.bitrate *= 1000
        return properties


class FaacStep(AudioEncoderStep):
    name = 'Faac AAC encoder'
    title = _('Faac AAC Encoder')
    sidebarName = _('Faac AAC')
    componentType = 'faac'
    docSection = 'help-configuration-assistant-encoder-faac'
    docAnchor = ''
    docVersion = 'local'

    # WizardStep

    def setup(self):
        self.bitrate.set_range(16, 256)
        self.bitrate.set_value(128)

        self.bitrate.data_type = int

        self.add_proxy(self.model.properties, ['bitrate'])

        if self.wizard.getStep('Encoding').getMuxerFormat() == 'aac':
            self.model.properties.adts = True

    def workerChanged(self, worker):
        self.model.worker = worker
        self.wizard.requireElements(worker, 'faac')


class FaacWizardPlugin(object):
    implements(IEncoderPlugin)

    def __init__(self, wizard):
        self.wizard = wizard
        self.model = FaacAudioEncoder()

    def getConversionStep(self):
        return FaacStep(self.wizard, self.model)
