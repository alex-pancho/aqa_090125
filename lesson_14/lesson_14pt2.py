class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other_point:object) -> bool:
        return self.x == other_point.x and self.y == other_point.y
    
    def __add__(self, arg):
        self.y = self.y + arg

if __name__ == "__main__":
    point_1 = Point(1, 1)
    point_2 = Point(1, 2)
    print(point_1 == point_2)
    point_1 + 1
    print(point_1 == point_2)


class Money():

    def __init__(self, amount: float) -> None:
        self.amount = amount
    
    def __str__(self):
        return f"{self.amount:.2f}"
    
    def __add__(self, other):
        if isinstance(other, Money) and type(self) == type(other):
            return type(self)(self.amount + other.amount)
        elif isinstance(other, (int, float)):
            return type(self)(self.amount + other)
        else:
            raise ValueError("Неправильний тип вхідного значення для операції додавання")
    
    def __sub__(self, other):
        if isinstance(other, Money) and type(self) == type(other):
            return type(self)(self.amount - other.amount)
        elif isinstance(other, (int, float)):
            return type(self)(self.amount - other)
        else:
            raise ValueError("Неправильний тип вхідного значення для операції додавання")
    
    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return type(self)(self.amount * scalar)
        else:
            raise ValueError("Неправильний тип для операції множення")
    
    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)) and scalar != 0:
            return type(self)(self.amount / scalar)
        else:
            raise ValueError("Неправильний тип або ділення на нуль")



class UAH(Money):
    def __init__(self, amount: float) -> None:
        super().__init__(amount)
 
    def __str__(self):
        return f"{self.amount:.2f} грн"
 
 
class USD(Money):
    def __init__(self, amount: float) -> None:
        super().__init__(amount)
 
    def __str__(self):
        return f"${self.amount:.2f}"

class ForEx():

    def __init__(self, exchange_rate_by, exchange_rate_sell):
        self.exchange_rate_by = exchange_rate_by
        self.exchange_rate_sell = exchange_rate_sell
    
    def convert_to_usd(self, uah_amount):
        if isinstance(uah_amount, UAH):
            usd_amount = uah_amount.amount / self.exchange_rate_sell
            return USD(usd_amount)
        else:
            raise ValueError("Неправильний тип для конвертації")

    def convert_to_uah(self, usd_amount):
        if isinstance(usd_amount, USD):
            uah_amount = usd_amount.amount * self.exchange_rate_by
            return UAH(uah_amount)
        else:
            raise ValueError("Неправильний тип для конвертації")

if __name__ == "__main__":
 
    my_uah_cash = UAH(3000)
    my_wife_uah_cash = UAH(30500)
    my_usd_cash = USD(100)
    wife_usd = USD(100)
    my_total_cash = my_uah_cash + my_wife_uah_cash 
    print(my_total_cash)
    
    privatbank = ForEx(37.05, 37.57)
    akord_bank = ForEx(37.37, 38.00)

    pb_to_uah = privatbank.convert_to_uah(my_usd_cash)
    pb_to_usd = privatbank.convert_to_usd(my_uah_cash)
    ak_to_uah = akord_bank.convert_to_uah(my_usd_cash)
    ak_to_usd = akord_bank.convert_to_usd(my_uah_cash)

    print(f"Продати {my_usd_cash}:", pb_to_uah, "|", ak_to_uah)
    print(f"Купити на {my_uah_cash}:", pb_to_usd, "|", ak_to_usd)


    """
    object.__add__(self, other)
    object.__sub__(self, other)
    object.__mul__(self, other)
    object.__matmul__(self, other)
    object.__truediv__(self, other)
    object.__floordiv__(self, other)
    object.__mod__(self, other)
    object.__divmod__(self, other)
    object.__pow__(self, other[, modulo])
    object.__lshift__(self, other)
    object.__rshift__(self, other)
    object.__and__(self, other)
    object.__xor__(self, other)
    object.__or__(self, other)
    """