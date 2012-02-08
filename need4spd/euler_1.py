#!/usr/bin/python

numbers=range(1, 1000)

multiple3=set()
multiple5=set()

for n in numbers:
    t=divmod(n, 3)[1]
    if t == 0:
        multiple3.add(n)

    t=divmod(n, 5)[1]
    if t == 0:
        multiple5.add(n)

result=0

for n in multiple3:
    result = result + n

for n in multiple5:
    result = result + n

intersectionNumbers=multiple3.intersection(multiple5)

for n in intersectionNumbers:
    result = result - n


print result


