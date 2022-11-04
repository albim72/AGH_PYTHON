class PositiveNumberTuple(tuple):

    def __new__(cls, *numbers):
        skipped = 0
        positive_numbers = []

        for x in numbers:
            if x>=0:
                positive_numbers.append(x)
            else:
                skipped += 1

        instance = super().__new__(cls, tuple(positive_numbers))
        instance.skipped = skipped
        return instance

mojakrotka = PositiveNumberTuple(9,0,-3,4,-6,15,8,19,0,18,-33,45,678,-1323)
print(mojakrotka)
print(type(mojakrotka))
print(mojakrotka.skipped)
