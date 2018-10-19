#! /user/local/bin/python3.4

class TimeSpan:
    # Initializer
    def __init__(self, weeks, days, hours):
        if weeks < 0 or days < 0 or hours < 0:
            raise ValueError("The arguments cannot be negative")
        self.hours = hours % 24
        if hours >= 24:
            days_temp = days + hours // 24
            self.days = days_temp % 7
        else:
            days_temp = days
            self.days = days % 7
        if days_temp >= 7:
            self.weeks = weeks + days_temp // 7
        else:
            self.weeks = weeks
    
    # String Representation
    def __str__(self):
        rep = str(self.weeks).zfill(2) + "W " + str(self.days) + "D " + str(self.hours).zfill(2) + "H"
        return rep

    # getTotalHours
    def getTotalHours(self):
        total = self.weeks * (7 * 24) + self.days * 24 + self.hours
        return total
    
    # TimeSpan + TimeSpan
    def __add__(self, other):
        if not isinstance(other, TimeSpan):
            raise TypeError("TimeSpan instance is expected")
        weeks = self.weeks + other.weeks
        days = self.days + other.days
        hours = self.hours + other.hours
        return TimeSpan(weeks, days, hours)
    def __radd__(self, other):
        return self.__add__(other)
    
    # TimeSpan * int / int * TimeSpan
    def __mul__(self, other):
        if not isinstance(other, int):
            raise TypeError("Integer is expected")
        if other <= 0:
            raise ValueError("Integer passed must be greater than 0")
        weeks = self.weeks * other
        days = self.days * other
        hours = self.hours * other
        return TimeSpan(weeks, days, hours)
    def __rmul__(self, other):
        return self.__mul__(other)

# Conditional Main Block
if __name__ == "__main__":
    print("__init__ testing...")
    ts1 = TimeSpan(weeks=2, days=15, hours=49)
    print(ts1)
    print("getTotalHours() testing...")
    print(ts1.getTotalHours())
    print("__init__ testing...")
    ts2 = TimeSpan(weeks=100, days=21, hours=24)
    print(ts2)
    print("getTotalHours() testing...")
    print(ts2.getTotalHours())
    print("__add__ testing...")
    ts3 = ts1 + ts2
    print(ts3)
    print("__add__ testing...")
    ts3 = ts2 + ts1
    print(ts3)
    print("__mul__ testing...")
    ts4 = ts1 * 3
    print(ts4)
    print("__mul__ testing...")
    ts4 = 3 * ts1
    print(ts4)
