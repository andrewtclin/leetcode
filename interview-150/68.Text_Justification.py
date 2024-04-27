from typing import List

def fullJustify(words: List[str], maxWidth: int) -> List[str]:
    output = []
    line, length = [], 0
    i = 0

    while i < len(words):
        if length + len(line) + len(words[i]) > maxWidth:
            # line complete
            extra_spaces = maxWidth - length
            spaces = extra_spaces // max(1, len(line) - 1)
            remainder = extra_spaces % max(1, len(line) - 1)

            for j in range(max(1, len(line)-1)):
                line[j] += ' ' * spaces
                if remainder:
                    line[j] += ' '
                    remainder -= 1
            output.append(''.join(line))
            line, length = [], 0

        line.append(words[i])
        length += len(words[i])
        i += 1

    last_line = ' '.join(line)
    trail_space = maxWidth - len(last_line)
    output.append(last_line + ' ' * trail_space)
    return output
# ["This", "is", "an", "example", "of", "text", "justification."], maxWidth=16
# i=0, line=['This'], length=4; i=1, line=['This', 'is'], length=6; i=2, line=['This', 'is', 'an'], length=8; i=3
# extra_spaces = 16 - 8 = 8, spaces = 8 // 2 = 4, remainder = 8 % 2 = 0
# line=['This    ', 'is    ', 'an'], length=8