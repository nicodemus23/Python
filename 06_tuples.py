# Tuple
# are used to store multiple items in a single variable
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
# is a collection which is ordered, unchangeable, and allows duplicates
# use parenthesis() or NOTHING to define a tuple

tuple1 = ("Jay-Z," "50 Cent", "Eminem", "Drake")
print(tuple1)

tuple2 = 1, 2, True, "Bob"
print(tuple2)

#tuple constructor
tuple3 = tuple(("apple", "banana", "cherry"))   # note the double round-brackets
print(tuple3)

# NOT A TUPLE - this is a string
pseudo_tuple = ('tuple')
print(pseudo_tuple)

# this IS a tuple
tuple4 = ('tuple',)
print(tuple4)

#length of a tuple
print(len(tuple1))

tuple5 = tuple(('real_tuple?'))
print(tuple5)

tuple5 = tuple(('real_tuple?',))
print(tuple5)

a = 5
b = 6
c = 7
tuple6 = tuple(('real_tuple?', a, b, c))
print(tuple6)