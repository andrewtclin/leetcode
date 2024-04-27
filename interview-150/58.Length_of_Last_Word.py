def lengthOfLastWord(s: str) -> int:
  return len(str(s.strip().rsplit(' ', maxsplit=1)[-1]))

  # solution 2 
  # pointer = -1
  # count = 0
  # flag = False
  # for _ in range(len(s)):
  #     if s[pointer] == ' ' and flag == False:
  #         pointer -= 1
  #         continue
  #     else:
  #         if s[pointer] == ' ':
  #             return count
  #         flag = True
  #         count += 1
  #         pointer -= 1
  # return count