class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'

    @staticmethod
    def from_sum(value1, value2):
        return FixedFloat(value1+value2)

    @classmethod
    def from_sum2(cls, value1, value2):
        return cls(value1 + value2)


new_number = FixedFloat.from_sum(19.575, 0.789)
print(new_number)


class Dollar(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '$'

    def __repr__(self):
        return f'<Dollar {self.symbol}{self.amount:.2f}>'


money = Dollar(18.786)
money2 = Dollar.from_sum2(16.758, 9.999)
print(money)
print(money2)
