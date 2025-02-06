class Solution:
    def combinationSum(self, candidates: List[int], Mtarget: int) -> List[List[int]]:
        sum_dict = {}
        def helper(candidates, idx, target):
            if idx == len(candidates) and target > 0:
                return []
                
            res = []
            curr = target
            step = 0
            while curr > 0:
                if sum_dict.get((idx + 1, curr), None):
                    intermediary = sum_dict[(idx + 1, curr)]
                else:
                    intermediary = helper(candidates, idx + 1, curr)
                    sum_dict[(idx + 1, curr)] = intermediary
                # print(candidates[idx], step, curr, intermediary)
                for arr in intermediary:
                    if step > 0:
                        res.append(arr + [candidates[idx]]*step)
                    else:
                        res.append(arr)
                curr -= candidates[idx]
                step += 1
            
            if curr == 0 and step > 0:
                res.append([candidates[idx]]*step)
            return res
        candidates.sort(key=lambda a: -a)
        return helper(candidates, 0, Mtarget)
        