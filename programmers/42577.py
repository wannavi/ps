def solution(phone_book):
    mp = {}

    for pn in phone_book:
        mp[pn] = 1

    for pn in phone_book:
        tmp = ""
        for n in pn:
            tmp += n
            if tmp in mp and tmp != pn:
                return False

    return True
