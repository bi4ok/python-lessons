def next_numb(number):
    start = number

    list_of_numbers = list(str(number))
    while len(list_of_numbers):
        if list_of_numbers[0] == max(list_of_numbers):
            list_of_numbers.pop(0)
        else:
            break
    else:
        return -1

    while len(str(start)) == len(str(number)):
        start += 1
        for number_in in str(start):
            if str(start).count(number_in) != str(number).count(number_in):
                break
        else:
            return start
    return -1


print(next_numb(144))
