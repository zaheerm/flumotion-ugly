include $(top_srcdir)/common/python.mk

component_PYTHON = __init__.py lamemp3.py wizard_gtk.py
componentdir = $(libdir)/flumotion/python/flumotion/component/encoders/lamemp3
component_DATA = lamemp3.xml

clean-local:
	rm -rf *.pyc *.pyo

EXTRA_DIST = $(component_DATA)
