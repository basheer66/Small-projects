def high_and_low(numbers):
    numlist = numbers.rsplit(" ",",")
	print(numlist)
	max = numbers[0]
    min = max
    for i in numlist:
        if max < i:
            max = i
        if min > i:
            min = i
    return "{} {}".format(max, min)
high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")