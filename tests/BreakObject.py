import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)

from pySQLBuilder.QueryObject import QueryObject
from pySQLBuilder.Builder import SelectBuilder, InsertBuilder, UpdateBuilder, DeleteBuilder
from pySQLBuilder.Structure import Table, Column, Value, Clause, Order, Limit, Expression, Join

def table(table: Table) -> tuple :
    return (table.name(), table.alias())

def column(column) -> tuple :
    col = ()
    if isinstance(column, Column) :
        col = (column.table(), column.name(), column.function(), column.alias())
    elif isinstance(column, Expression) :
        col = expression(column)
    return col

def value(value: Value) -> tuple :
    pairs = ()
    for i in range(len(value.columns())) :
        pairs = pairs + (value.columns()[i], value.values()[i])
    return pairs

def clause(clause: Clause) -> tuple :
    col = ()
    clauseCol = clause.column()
    if isinstance(clauseCol, Column) :
        col = column(clauseCol)
    elif isinstance(clauseCol, Expression) :
        col = expression(clauseCol)
    return (col, clause.operator(), clause.value(), clause.conjunctive(), clause.level())

def order(order: Order) -> tuple :
    col = column(order.column())
    return (col, order.orderType())

def limit(limit: Limit) -> tuple :
    return (limit.limit(), limit.offset())

def expression(exps: Expression) -> tuple :
    return (exps.expression(), exps.alias(), exps.params())

def join(join: Join) -> tuple :
    baseColumns = ()
    joinColumns = ()
    usingColumns = ()
    for baseCol in join.baseColumns() :
        baseColumns += (column(baseCol),)
    for joinCol in join.joinColumns() :
        joinColumns += (column(joinCol),)
    for usingCol in join.usingColumns() :
        usingColumns += (column(usingCol),)
    return (join.joinType(), join.baseTable(), join.joinTable(), join.joinAlias(), baseColumns, joinColumns, usingColumns)

def printTable(tableObject: Table) :
    tableBreak = table(tableObject)
    print("Table{}".format(tableBreak))

def printColumn(columnObject, label = "Column") :
    columnBreak = column(columnObject)
    print("{0}{1}".format(label, columnBreak))

def printValue(valueObject: Value) :
    valueBreak = value(valueObject)
    print("Value{}".format(valueBreak))

def printClause(clauseObject: Clause, label = "Where") :
    clauseBreak = clause(clauseObject)
    print("{0}{1}".format(label, clauseBreak))

def printOrder(orderObject: Order) :
    orderBreak = order(orderObject)
    print("Order{}".format(orderBreak))

def printLimit(limitObject: Limit) :
    limitBreak = limit(limitObject)
    print("Limit{}".format(limitBreak))

def printJoin(joinObject: Join) :
    joinBreak = join(joinObject)
    print("Join{}".format(joinBreak))

def printSelectBuilder(selectBuilder: SelectBuilder) :
    print("Type: {}".format(selectBuilder.builderType()))
    printTable(selectBuilder.getTable())
    for col in selectBuilder.getColumns() :
        printColumn(col)
    for where in selectBuilder.getWhere() :
        printClause(where, "Where")
    for group in selectBuilder.getGroup() :
        printColumn(group, "Group")
    for having in selectBuilder.getHaving() :
        printClause(having, "Having")
    for order in selectBuilder.getOrder() :
        printOrder(order)
    if selectBuilder.hasLimit() :
        printLimit(selectBuilder.getLimit())
    for join in selectBuilder.getJoin() :
        printJoin(join)

def printInsertBuilder(insertBuilder: InsertBuilder) :
    print("Type: {}".format(insertBuilder.builderType()))
    printTable(insertBuilder.getTable())
    for val in insertBuilder.getValues() :
        printValue(val)
    if insertBuilder.hasLimit() :
        printLimit(insertBuilder.getLimit())

def printUpdateBuilder(updateBuilder: UpdateBuilder) :
    print("Type: {}".format(updateBuilder.builderType()))
    printTable(updateBuilder.getTable())
    for val in updateBuilder.getValues() :
        printValue(val)
    for where in updateBuilder.getWhere() :
        printClause(where, "Where")
    if updateBuilder.hasLimit() :
        printLimit(updateBuilder.getLimit())
    for join in updateBuilder.getJoin() :
        printJoin(join)

def printDeleteBuilder(deleteBuilder: DeleteBuilder) :
    print("Type: {}".format(deleteBuilder.builderType()))
    printTable(deleteBuilder.getTable())
    for where in deleteBuilder.getWhere() :
        printClause(where, "Where")
    if deleteBuilder.hasLimit() :
        printLimit(deleteBuilder.getLimit())

def query(query: QueryObject) -> tuple :
    queryParts = query.parts()
    queryParams = query.params()
    queryPair = ()
    for i in range(len(queryParts)) :
        param = None
        if len(queryParams) > i : param = queryParams[i]
        queryPair += ((queryParts[i], param),)
    return queryPair

def printQuery(queryObject: QueryObject) :
    pairs = query(queryObject)
    for pair in pairs :
        print("{}<-|->{}".format(pair[0], pair[1]))
