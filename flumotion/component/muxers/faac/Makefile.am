include $(top_srcdir)/common/python.mk

component_PYTHON = __init__.py faac.py
componentdir = $(libdir)/flumotion/python/flumotion/component/muxers/faac
component_DATA = \
	faac.xml

clean-local:
	rm -rf *.pyc *.pyo

EXTRA_DIST = $(component_DATA)
