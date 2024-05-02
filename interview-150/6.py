def convert(s: str, numRows: int) -> str:
    if numRows == 1: return s

    output = ''
    for row in range(numRows):
        jump = 2 * (numRows - 1)
        for i in range(row, len(s), jump):
            output += s[i]
            if row > 0 and row < numRows - 1 and i + jump - 2 * row < len(s):
                output += s[i + jump - 2 * row]
    return output