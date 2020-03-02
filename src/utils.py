def _unicode(data):
    try:
        return unicode(data.decode('utf8'))
    except NameError:
        return str(data)
