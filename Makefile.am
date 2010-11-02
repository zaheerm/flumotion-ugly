AUTOMAKE_OPTIONS = dist-bzip2 no-dist-gzip 1.8

ACLOCAL_AMFLAGS = -I m4 -I common

include $(srcdir)/common/common.mk
include $(srcdir)/common/pychecker.mk

SUBDIRS = flumotion common misc po

all-local: locale-uninstalled
clean-local: locale-uninstalled-clean

EXTRA_DIST = flumotion-ugly.spec \
	env \
	LICENSE.GPL

PYCHECKER_WHITELIST = flumotion/component/*/*.py
PYCHECKER_BLACKLIST =

COVERAGE_MODULES = flumotion.component
