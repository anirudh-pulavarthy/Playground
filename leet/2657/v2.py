from typing import List
from collections import defaultdict

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = []
        setA, setB = {A[0]}, {B[0]}

        ans.append(1 if A[0] == B[0] else 0)
        for i in range(1, len(A)):
            ans.append(ans[-1])
            if A[i] == B[i]: ans[i] += 1
            else:
                if A[i] in setB: ans[i] += 1
                if B[i] in setA: ans[i] += 1
            setA.add(A[i])
            setB.add(B[i])
            
        print(ans)
        return ans