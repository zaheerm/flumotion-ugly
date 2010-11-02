include $(top_srcdir)/common/python.mk

component_PYTHON = __init__.py x264.py wizard_gtk.py
componentdir = $(libdir)/flumotion/python/flumotion/component/encoders/x264
component_DATA = x264.xml wizard.glade

clean-local:
	rm -rf *.pyc *.pyo

EXTRA_DIST = $(component_DATA)
