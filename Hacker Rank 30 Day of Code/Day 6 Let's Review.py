t = int(input())
for i in range(t):

    n = input()

    even = ""
    old = ""

    for i in range(len(n)):
        if i % 2 == 0:
            even += n[i]

        else:
            old += n[i]

    print(even, old)