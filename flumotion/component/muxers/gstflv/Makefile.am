include $(top_srcdir)/common/python.mk

component_PYTHON = __init__.py gstflv.py wizard_gtk.py
componentdir = $(libdir)/flumotion/python/flumotion/component/muxers/gstflv
component_DATA = \
	gstflvmuxer.xml

clean-local:
	rm -rf *.pyc *.pyo

EXTRA_DIST = $(component_DATA)
