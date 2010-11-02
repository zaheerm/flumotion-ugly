include $(top_srcdir)/common/python.mk

component_PYTHON = __init__.py faac.py wizard_gtk.py
componentdir = $(libdir)/flumotion/python/flumotion/component/encoders/faac
component_DATA = faac.xml

clean-local:
	rm -rf *.pyc *.pyo

EXTRA_DIST = $(component_DATA)
