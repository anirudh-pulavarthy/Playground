from typing import List

class Solution:
    
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0

        start = 0
        index = 0
        st = []
        for num in arr:
            # If stack is empty and current number is index => it can be its own chunk
            if not st and num == index:
                start = index + 1
                chunks += 1
            else:
                st.append(num)
                test = set(range(start, index + 1))
                test2 = set(st)
                if test2 == test:
                    chunks += 1
                    st.clear()
                    start = index + 1
            
            index += 1

        return chunks

if __name__ == "__main__":
    arr = [0,2,1,4,3]

    s = Solution()
    res = s.maxChunksToSorted(arr)
    print("Max chunks = ", res)
