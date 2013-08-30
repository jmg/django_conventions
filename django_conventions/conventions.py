END_VIEW_NAME = "View"
INDEX_VIEW_PREFIX = "index"

def _get_module(view):

    module = view.__module__.split(".")[-1]
    return r"%s/" % module

def _get_name(view):

    if END_VIEW_NAME in view.__name__:
        return view.__name__[:-len(END_VIEW_NAME)].lower()
    return view.__name__.lower()

def _get_namespace(view):

    if hasattr(view, "namespace") and view.namespace is not None:
        return r"%s/" % view.namespace
    return ""

def get_template_name(view):
    
    namespace = _get_namespace(view)
    module = _get_module(view)
    name = _get_name(view)
    return "%s%s%s.html" % (namespace, module, name)

def get_url(view):

    url = r"^"
    url += _get_namespace(view)
    url += _get_module(view)

    name = _get_name(view)
    if name != INDEX_VIEW_PREFIX:
        url += r"%s/$" % name
    else:
        url += r"$"

    return url

def get_resource(view):

    return _get_name(view)