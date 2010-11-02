# lots of little imports done before anything else so that
# we don't get weird stray module errors

# importing this before we do our import hooks circumvents the weird
# backtraces that end in TypeError: iterable argument required
# FIXME: we really have to sit down and work through this one some day
from twisted.internet import reactor

# make sure we can import from distributed flumotion namespace
import setup
setup.setup()
