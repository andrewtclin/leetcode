def isSubsequence(s: str, t: str) -> bool:
    if s == '': return True
    if len(s) > len(t): return False
    
    i, j = 0, 0
    while i < len(t):
        if t[i] == s[j]:
            if j == len(s) - 1:
                return True
            j += 1
        i += 1
    return False