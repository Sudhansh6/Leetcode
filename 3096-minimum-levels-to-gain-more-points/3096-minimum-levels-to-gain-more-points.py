class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        # Assume Alice doesn't play any levels and keep adding?
        for i in range(len(possible)):
            if not possible[i]:
                possible[i] = -1
        total, rem = sum(possible) - possible[0], possible[0]
        i = 0
        while total >= rem:
            i += 1
            if i == len(possible) - 1:
                break
            if possible[i] > 0:
                total -= 1
                rem += 1
            else:
                total += 1
                rem -= 1
        if total >= rem:
            return -1
        return i + 1