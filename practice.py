# class NewNode:
#     def __init__(self,val = 0,next = None):
#         self.val = val
#         self.next = next
# l1 = NewNode(2)
# node = l1
# # node.next= NewNode(4)
# while node.next != None:
#     node = node.next
# node.next = NewNode(3)
# print(l1.next.val)


class CreditCard:
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._acnt

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        self._balance -= amount


#
# cc = CreditCard('John doe', '1st Bank','5391 0375 9387 5309',1000)
#
# cc.charge(200)
#
# print([x for x in cc.__dir__() if '_' != x[0]])


class Vector:
    def __init__(self, d):
        self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, item):
        return self._coords[item]

    def __setitem__(self, key, value):
        self._coords[key] = value

    def __add__(self, other):
        if len(other) != len(self):
            raise ValueError("dimensions must agree!!")
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] + other[i]
        return result

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return "{" + str(self._coords)[1:-1] + "}"


# v = Vector(5)
#
# v[2] = 23
#
# v[1] = 23 # <0, 23, 0, 0, 0> (based on use of setitem )
# v[-1] = 45 # <0, 23, 0, 0, 45> (also via setitem )
# print(v[4]) # print 45 (via getitem )
# u = v + v # <0, 46, 0, 0, 90> (via add )
# print(u) # print <0, 46, 0, 0, 90>
# total = 0
# for entry in v: # implicit iteration via len and getitem
#     total += entry


class SequenceIter:
    def __init__(self, sequence):
        self._seq = sequence
        self._k = -1

    def __next__(self):
        self._k += 1
        if self._k < len(self._seq):
            return self._seq[self._k]
        raise StopIteration()

    def __iter__(self):
        return self


itr = SequenceIter([1, 2, 3, 5, 6, 4])
print(itr)
for i in itr:
    try:
        print(i)
    except StopIteration:
        print("Index overflow: Can't iterate further")
    except ZeroDivisionError:
        print("LOL Why?!!")


class Range:
    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError("step cannot be 0")

        if stop is None:
            start, stop = 0, start

        self._length = max(0, (stop - start + step - 1) // step)

        self._start = start
        self._step = step

    def __len__(self):
        return self._length

    def __getitem__(self, item):
        if item < 0:
            item += len(self)
        if not 0 <= item < self._length:
            raise IndexError("index out of range")

        return self._start + item * self._step


# r = Range(8, 140, 5)
#
# print(r, r[15], len(r))
#
# for i in Range(3, 7):
#     print(i)

# print(Range(2)[-3])


class PredatoryCreditClass(CreditCard):
    def __init__(self, customer, bank, acnt, limit, apr):

        super().__init__(customer, bank, acnt, limit)
        self._apr = apr

    def charge(self, price):
        success = super().charge(price)
        if not success:
            self._balance += 5
        return success

    def process_monthly(self):
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1 / 12)
            self._balance *= monthly_factor


# ppc = PredatoryCreditClass('John doe', '1st Bank',
#                            '5391 0375 9387 5309', 1000, 21)

# print(ppc.charge(299))
