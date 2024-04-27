def strStr(haystack: str, needle: str) -> int:
    # Solution 1
    for i in range(len(haystack)+1 - len(needle)):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

    # Solution 2
    # for i in range(len(haystack) + 1 - len(needle)):
    #     for j in range(len(needle)):
    #         if haystack[i + j] != needle[j]:
    #             break
    #         if j == len(needle) - 1:
    #             return i
    # return -1          