def anagrams(s1, s2):
    a1_list = list(s1)
    a2_list = list(s2)
    a1_list.sort()
    a2_list.sort()
    matches = True
    pos = 0
    while pos < len(s1) and matches:
        if a1_list[pos] == a2_list[pos]:
            pos += 1
        else:
            matches = False
    return matches

print anagrams("bcde", "cdba")