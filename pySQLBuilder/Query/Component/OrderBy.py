from ...Structure import Order
from ...Builder import OrderByBuilder
from typing import Iterable, Mapping

class OrderBy :

    def oderBy(self, columns, orderType) :
        if (isinstance(columns, Mapping) and len(columns) == 1) or isinstance(columns, str) :
            orderObject = Order.create(columns, orderType)
            self.builder.addOrder(orderObject)
        elif isinstance(columns, Iterable) :
            for column in columns :
                orderObject = Order.create(column, orderType)
                if isinstance(self.builder, OrderByBuilder) :
                    self.builder.addOrder(orderObject)
                else :
                    raise Exception('Builder object does not support ORDER BY query')
        return self

    def orderByAsc(self, column) -> Order :
        return self.oderBy(column, Order.ORDER_ASC)

    def orderByDesc(self, column) -> Order :
        return self.oderBy(column, Order.ORDER_DESC)
