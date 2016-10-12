def anagrams(s1, s2):
    char_list = list(s2)
    pos1 = 0
    still_ok = True
    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False
        while pos2 < len(s2) and not found:
            if s1[pos1] == char_list[pos2]:
                found = True
            else:
                pos2 += 1
        if found:
            char_list[pos2] = None
        else:
            still_ok = False
        pos1 += 1
    return still_ok

print anagrams("abcd", "dbce")
