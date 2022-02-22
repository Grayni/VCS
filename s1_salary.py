from sys import argv

hours, rate, award = map(int, argv[1:])

print((lambda h, r, a: (h * r) + a)(hours, rate, award))
