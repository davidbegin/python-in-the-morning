try:
 f = open('missing')
except OSError, FileNotFoundError as e:
    if isinstance(e, OSError):


