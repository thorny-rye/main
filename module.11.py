import inspect
from pprint import pprint


def introspection_info(obj):
    attr_obj = [i for i in dir(obj)]
    meth_obj = [i for i in dir(obj) if callable(getattr(inspect.ismethod(obj), i))]
    dict = {'type': type(obj).__name__, "attributes": attr_obj, "methods": meth_obj, 'module': obj.__class__.__module__}

    return dict



number_info = introspection_info(42)
pprint(number_info)
