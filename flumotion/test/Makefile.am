include $(top_srcdir)/common/python.mk
include $(top_srcdir)/common/trial.mk
TRIAL_ENV = $(top_srcdir)/env

BUILT_SOURCES = setup.py
CLEANFILES = $(BUILT_SOURCES)

EXTRA_DIST = 				\
	__init__.py			\
	common.py			\
	setup.py

check-local: trial
