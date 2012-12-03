END_VIEW_NAME = "View"
INDEX_VIEW_PREFIX = "Index"

def _get_module(view):

    return view.__module__.split(".")[-1]

def _get_name(view):

    if END_VIEW_NAME in view.__name__:
        return view.__name__[:-len(END_VIEW_NAME)].lower()
    return view.__name__.lower()

def get_template_name(view):

    module = _get_module(view)
    name = _get_name(view)
    return "%s/%s.html" % (module, name)

def get_url(view):

    module = _get_module(view)
    name = _get_name(view)

    if name == INDEX_VIEW_PREFIX.lower():
        return r"^%s/$" % module

    return r"^%s/%s/$" % (module, name)

def get_resource(view):

    return _get_name(view)