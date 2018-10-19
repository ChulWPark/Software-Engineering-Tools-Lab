#! /user/local/bin/python3.4

class Vector:
    # Initializer
    def __init__(self, twovals):
        sp = twovals.split()
        self.x = float(sp[0])
        self.y = float(sp[1])

if __name__ == "__main__":
    v1 = Vector("0.12 3.14")
    print(v1.x)
    print(v1.y)
