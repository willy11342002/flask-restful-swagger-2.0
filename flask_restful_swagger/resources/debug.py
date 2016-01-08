import logging
import types


def tag_full(self, fname, local_args):
    if not self.debugmode:
        return
    fname = fname + '()'
    self.debug("FUNCTION CALL: %s" % fname)
    for key, value in local_args.iteritems():
        self.debug("    %s=%s:" % (key, value))


def tag(self, fname, kwargs):
    if not self.debugmode:
        return
    fname = fname + '()'
    self.debug("FUNCTION CALL: %s" % fname)
    for key, value in kwargs.iteritems():
        self.debug("    %s=%s:" % (key, value))


# Creates a custom logger object
def setup_logging(filename=None, level=logging.DEBUG):
    """
    Sets up the logging interface.
    :param filename: A string containing the filename to log to.
    :param level:  The minimum log level to log with.
    :return: A logging object
    """
    log = logging.getLogger("swagger")
    log.setLevel(level)
    log_formatter = logging.Formatter("[ swagger ] [ %(asctime)s ] [ %(levelname)-5.5s]  %(message)s")
    if filename is not None:
        handler1 = logging.FileHandler(filename)
        handler1.setFormatter(log_formatter)
        log.addHandler(handler1)
    handler2 = logging.StreamHandler()
    handler2.setFormatter(log_formatter)
    log.addHandler(handler2)
    log.tag = types.MethodType(tag, log)
    log.tag_full = types.MethodType(tag_full, log)
    return log
