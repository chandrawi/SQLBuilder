from ...Structure import Limit

class LimitOffset :

    def limit(self, limit, offset = Limit.NOT_SET) :
        validLimit = Limit.NOT_SET
        validOffset = Limit.NOT_SET
        if isinstance(limit, int) :
            if limit > 0: validLimit = limit
        if isinstance(offset, int) :
            if offset > 0: validOffset = offset
        limitObject = Limit(validLimit, validOffset)
        self.builder.setLimit(limitObject)
        return self

    def offset(self, offset) :
        return self.limit(Limit.NOT_SET, offset)
