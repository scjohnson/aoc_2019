# /usr/bin/env python


def good_password(num):
    if len(str(num)) != 6:
        return False
    repeat = False
    for i in range(len(str(num))-1):
        pair = str(num)[i:i+2]
        if int(pair[0]) > int(pair[1]):
            return False
        elif int(pair[0]) == int(pair[1]):
            repeat = True
    return repeat


def good_password2(num):
    if len(str(num)) != 6:
        return False
    repeat = False
    for i in range(len(str(num))-1):
        pair = str(num)[i:i+2]
        if int(pair[0]) > int(pair[1]):
            return False
        elif int(pair[0]) == int(pair[1]):
            check = True
            if i > 0 and str(num)[i-1] == pair[0]:
                check = False
            if i < 4 and str(num)[i+2] == pair[0]:
                check = False
            if check:
                repeat = True
    return repeat


def count_passwords(low, high):
    c = 0
    c2 = 0
    for password in range(low, high+1):
        if good_password(password):
            c += 1
        if good_password2(password):
            c2 += 1
    return c, c2


if __name__ == "__main__":
    print(good_password2(111111))
    print(good_password2(123789))
    print(good_password2(223450))
    print(good_password2(123444))
    print(count_passwords(134792, 675810))
    # 915 too low
