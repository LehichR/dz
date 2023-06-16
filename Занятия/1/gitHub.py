def numbs():
    for long in range(1001):
        integerr = int(input("Введите число (Если последовательность завершена - нажмите enter) >>>"))
        if integerr:
            a = [integerr]
            b = []
            for i in a:
                elem = a[i]
                if elem // 5: b.append(elem)
                return max(b)


five = [numbs()]
print(five)
