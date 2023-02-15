import sys

n = int(input())

phonebook = {}
for i in range(n):

    data = input().split()

    phonebook[data[0]] = data[1]

input = sys.stdin.readlines()

for name in input:

    name = name.strip()

    if name in phonebook:
        print(f'{name}={phonebook[name]}')

    else:
        print('Not found')

