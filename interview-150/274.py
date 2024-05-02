from typing import List

def hIndex(citations: List[int]) -> int:
    paper_nums = len(citations)
    citations.sort()
    for idx, value in enumerate(citations):
        if paper_nums - idx <= value:
            return paper_nums - idx
    return 0