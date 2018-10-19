#! /user/local/bin/python3.4

class Element:
    # Initializer
    def __init__(self, intKey, strVal):
        # Input Arguments Verification
        if not isinstance(intKey, int):
            raise TypeError("intKey is not an instance of int.")
        if not isinstance(strVal, str):
            raise TypeError("strVal is not an instance of str.")
        self.IntegerKey = intKey
        self.StringValue = strVal

    # String Representation
    def __str__(self):
        rep = '(' + str(self.IntegerKey) + ': "' + self.StringValue + '")'
        return rep
    
    # Hashing Function
    def __hash__(self):
        return hash(self.IntegerKey)

class StrongDictionary:
    # Initializer
    def __init__(self, name):
        # Input Arugument Verification
        if name == "":
            raise ValueError("name is not allowed to be empty.")
        self._backend = {}
        self._name = name

    # String Representation
    def __str__(self):
        rep = '["' + self._name + '": ' + '{:02d}'.format(len(self._backend)) + ' Elements]'
        return rep

    # member function: add()
    def add(self, elem):
        # Input Argument Verification
        if hash(elem) in self._backend:
            raise ValueError("Element already in backend dictionary")
        else:
            self._backend[hash(elem)] = elem

    # member function: remove()
    def remove(self, elem):
        # Input Argument Verification
        if hash(elem) not in self._backend:
            raise KeyError("Element does not exist in backend dictionary")
        else:
            del self._backend[hash(elem)]

    # member function: get()
    def get(self, val):
        for key in self._backend:
            if key == val:
                return self._backend[key]
        # Input Argument Verification
        raise KeyError("No element with the given key exists.")

    # member function: getAll()
    def getAll(self):
        retdict = {}
        for key in self._backend:
            retdict[key] = self._backend[key].StringValue
        return retdict

if __name__ == "__main__":
    print("\ntesting Element class...")
    elem1 = Element(42, 'Answer to Life, the Universe, and Everything')
    print(elem1)
    print(hash(elem1))
    print("\ntesting StrongDictionary class...")
    sd1 = StrongDictionary("Products")
    print(sd1)
    print(sd1._backend)
    elem1 = Element(1, 'one')
    elem2 = Element(2, 'two')
    elem3 = Element(3, 'three')
    elem4 = Element(4, 'four')
    elem5 = Element(5, 'five')
    elem6 = Element(6, 'six')
    elem7 = Element(7, 'seven')
    elem8 = Element(8, 'eight')
    elem9 = Element(9, 'nine')
    elem10 = Element(10, 'ten')
    print("\ntesting add()...")
    sd1.add(elem1)
    sd1.add(elem2)
    sd1.add(elem3)
    sd1.add(elem4)
    sd1.add(elem5)
    sd1.add(elem6)
    sd1.add(elem7)
    sd1.add(elem8)
    sd1.add(elem9)
    print(sd1)
    print(sd1._backend)
    print("\ntesting remove()...")
    sd1.remove(elem1)
    sd1.remove(elem2)
    sd1.remove(elem3)
    print(sd1)
    print(sd1._backend)
    print("\ntesting get()...")
    print(sd1.get(5))
    print("\ntesting getAll()...")
    print(sd1.getAll()[5])
    print("")
