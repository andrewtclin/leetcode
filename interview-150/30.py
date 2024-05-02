from typing import List

def findSubstring(self, s: str, words: List[str]) -> List[int]:
    # edge cases
    if len(s) == 0 or s is None or words is None:
        return []
    
    count = {}
    word_len = len(words[0])
    words_len = len(words) * word_len
    res = []
    
    for word in words:
        count[word] = count.get(word, 0) + 1

    for l in range(len(s) - words_len + 1):
        words_seen = {}

        for r in range(len(words)):
            curr_word_idx = l + r * word_len
            curr_word = s[curr_word_idx : curr_word_idx + word_len]

            if curr_word not in count:
                break
            
            words_seen[curr_word] = words_seen.get(curr_word, 0) + 1

            if words_seen[curr_word] > count[curr_word]:
                break

        if words_seen == count:
            res.append(l)

    return res