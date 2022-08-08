# import random
import matplotlib.pyplot as plt
# user = int(input("원하는 개수 : "))
Number_set = {
    '1':0,
    '2':0,
    '3':0,
    '4':0,
    '5':0,
    '6':0,
    '7':0,
    '8':0,
    '9':0
}

# for _ in range(user):
#     Number_set.append(random.randint([1,2,3,4,5,]))

for _ in range(1, 100000):
    Number_set[str(_)[0]] += 1
print(Number_set)