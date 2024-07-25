#!/bin/python3

f = open('top-100.txt', 'rt')
print(f)

print(f.readlines())


print(f.readlines())
f.seek(0)
print(f.readlines())
f.seek(0)

for line in f:
	print(line.strip())
f.close()

f = open("test2.txt", "a")
f.write("readlines2")
f.close()

print(f.name)
print(f.closed)
print(f.mode)

with open('rockyou.txt', encoding="latin1") as f:
	for line in f:
		pass
