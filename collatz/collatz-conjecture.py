import matplotlib.pyplot as plt

for collatz in range(2, 40000):
    coll_int_li = [collatz]
    while collatz != 1:
        if collatz % 2 == 1:
            collatz = collatz*3+1
        else:
            collatz //= 2

        coll_int_li.append(collatz)

    print(f'{coll_int_li[0]}의 콜라츠 추측 : 총{len(coll_int_li)}번을 거치며 가장 큰 숫자는{coll_int_li.index(max(coll_int_li))}번째인 {max(coll_int_li)}입니다.')
    plt.plot(coll_int_li)
plt.show()
