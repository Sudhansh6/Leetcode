class Solution:
    def checkInclusion(self, S1: str, S2: str) -> bool:
        # Do it with counts
        freq1 = [0 for _ in range(26)]
        freq2 = [0 for _ in range(26)]
        a = ord('a')

        for i in range(len(S1)):
            freq1[ord(S1[i]) - a] += 1

        for i in range(len(S2) - len(S1)):
            for j in range(26):
                freq2[j] = 0

            # print(S1, S2[i + 1:i + len(S1) + 1])
            for j in range(i + 1, i + len(S1) + 1):
                freq2[ord(S2[j]) - a] += 1

            flag = False
            for j in range(26):
                if freq1[j] != freq2[j]:
                    flag = True
                    break
            
            if not flag:
                return True
            
        return False