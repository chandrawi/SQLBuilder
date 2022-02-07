from .QueryObject import QueryObject
from .Builder import SelectBuilder, InsertBuilder, UpdateBuilder, DeleteBuilder
from .Translator import BaseTranslator, GenericTranslator, MySQLTranslator

class QueryTranslator :

    TRANSLATOR_GENERIC = 1
    TRANSLATOR_BEAUTIFY = 2
    TRANSLATOR_MYSQL = 3
    TRANSLATOR_SQLITE = 4

    NO_PARAM = 1
    PARAM_NUM = 2
    PARAM_ASSOC = 3

    query = QueryObject()
    translator = 0
    bindingOption = 0

    def __init__(self, translator: int = TRANSLATOR_GENERIC, bindingOption: int = PARAM_NUM) :
        self.query = QueryObject()
        self.translator = translator
        self.bindingOption = bindingOption

    def getQueryObject(self) :
        return self.query

    @staticmethod
    def translateBuilder(query: QueryObject, builder, translator: int) :
        translatorClass = QueryTranslator.getTranslator(query, translator)
        if isinstance(builder, SelectBuilder) :
            translatorClass.translateSelect(query, builder)
        elif isinstance(builder, InsertBuilder) :
            translatorClass.translateInsert(query, builder)
        elif isinstance(builder, UpdateBuilder) :
            translatorClass.translateUpdate(query, builder)
        elif isinstance(builder, DeleteBuilder) :
            translatorClass.translateDelete(query, builder)
        else :
            raise Exception('Tried to translate unregistered builder object')

    @staticmethod
    def getTranslator(query: QueryObject, translator: int) :
        if translator == QueryTranslator.TRANSLATOR_GENERIC :
            return GenericTranslator(query)
        elif translator == QueryTranslator.TRANSLATOR_MYSQL :
            return MySQLTranslator(query)
        else :
            raise Exception('Translator selected is not registered')

    @staticmethod
    def getBindingOption(bindingOption: int) :
        bindingFlag = False
        bindingMode = False
        if bindingOption == QueryTranslator.PARAM_ASSOC :
            bindingFlag = True
            bindingMode = True
        elif bindingOption == QueryTranslator.PARAM_NUM :
            bindingFlag = True
            bindingMode = False
        return (bindingFlag, bindingMode)

    @staticmethod
    def getQuery(query: QueryObject, bindingOption: int) :
        (bindingFlag, bindingMode) = QueryTranslator.getBindingOption(bindingOption)
        queryString = ''
        for part in query.parts :
            queryString += part
        return queryString
