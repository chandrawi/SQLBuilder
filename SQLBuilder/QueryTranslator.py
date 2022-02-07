from .QueryObject import QueryObject
from .Builder import SelectBuilder, InsertBuilder, UpdateBuilder, DeleteBuilder

class QueryTranslator :

    TRANSLATOR_GENERIC = 1
    TRANSLATOR_BEAUTIFY = 2
    TRANSLATOR_MYSQL = 3
    TRANSLATOR_SQLITE = 4

    NO_PARAM = 1
    PARAM_NUM = 2
    PARAM_ASSOC = 3

    _query = None
    _translator = 0
    _bindingOption = 0

    def __init__(self, translator: int = TRANSLATOR_GENERIC, bindingOption: int = PARAM_NUM) :
        self._query = QueryObject()
        self._translator = translator
        self._bindingOption = bindingOption
