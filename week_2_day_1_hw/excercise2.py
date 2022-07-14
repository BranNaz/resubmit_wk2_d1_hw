for num in range(2, 100):
    for factor in range(2, num):
        if num % factor == 0:
            break
    else:
        print(num)