from roboparse.schemas import Filter


class FilterMetaClass(type):
    def __call__(cls, *args, **kwargs):
        _obj = type.__call__(cls, *args, **kwargs)
        filters = [func for func in dir(_obj) if callable(getattr(_obj, func))]

        for _filter in filters:
            if _filter[:3] != "_fb":
                continue

            _obj.filters.register_filter(getattr(_obj, _filter))
        return _obj


class FilterFactory:
    def __init__(self):
        self._filters = []

    def get(self):
        return self._filters

    def register_filter(self, method):
        _filter = Filter(method=method)
        self._filters.append(_filter)
