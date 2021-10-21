print("Test string, here is number {}, and here a number {}".format(2, 42))
print("Test, monetary value is U$ {:f}".format(43.20))
print("Test, monetary value is U$ {:.2f}".format(43.20))
print("Test, monetary value is U$ {:7.2f}".format(43.20))
print("Test, monetary value is U$ {:07.1f}".format(43.20))
print("Test, int value is U$ {:07d}".format(43))
print("Test, date format {:2d}/{:2d}".format(9,4))
print("Test, date format {:02d}/{:02d}".format(9,4))
print("Test, date format {:02d}/{:02d}".format(11,11))

list = []
list.append("pessoa 1")
list.append("pessoa 2")

print(type(list))

tuple_converted = tuple(list)
print(type(tuple_converted))
