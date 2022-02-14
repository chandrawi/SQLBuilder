from .BaseBuilder import BaseBuilder
from .Component import WhereBuilder, LimitBuilder, JoinBuilder

class UpdateBuilder(BaseBuilder, WhereBuilder, LimitBuilder, JoinBuilder) :

    def __init__(self) :
        BaseBuilder.__init__(self)
        WhereBuilder.__init__(self)
        LimitBuilder.__init__(self)
        JoinBuilder.__init__(self)
