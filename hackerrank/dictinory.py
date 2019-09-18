# n = int(input())
# dict = {}
# for i in range((n)):
#     a = input()
#     b = a.split(" ")
#     dict[b[0]] = b[1]
#     d = input()
#
# c = dict.keys()
# for row in d:
#     for row1 in c:
#         if row == row1:
#             print(row+"="+dict[row])
#         else:
#             print("Not found")

n = int(input())
dict = {}
for i in range((n)):
    a = input()
    b = list(a.split(" "))
    dict[b[0]] = b[1]
c = []
c = list(dict.keys())

for i in range(n):
    d = input()
    if d in c:
        print(d+"="+dict[d])

    else:
        print("Not found")
