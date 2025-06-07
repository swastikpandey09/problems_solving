def kmp_search(text, pattern):
    lps = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
    i, j, count = 0, 0, 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == len(pattern):
            count += 1
            j = lps[j - 1]
        elif i < len(text) and text[i] != pattern[j]:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1

    return count

a = input()
b = input()
print(kmp_search(a, b))