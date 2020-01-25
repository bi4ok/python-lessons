import time


def next_numb(number):
    if int("".join(sorted(str(number), reverse=True))) == number:
        return -1

    start = number
    while len(str(start)) == len(str(number)):
        start += 1
        for number_in in str(start):
            if str(start).count(number_in) != str(number).count(number_in):
                break
        else:
            return start
    return -1


def next_numb2(number):
    rev_numb = number[::-1]
    for index_s, start in enumerate(rev_numb):
        for index_e, end in enumerate(rev_numb):
            if index_e <= index_s:
                continue
            if start > end:
                rev_numb = list(rev_numb)
                rev_numb[index_e], rev_numb[index_s] = rev_numb[index_s], rev_numb[index_e]
                rev_numb = sorted(rev_numb[:index_e], reverse=True) + rev_numb[index_e:]
                return ''.join(rev_numb[::-1])
        else:
            return -1
1