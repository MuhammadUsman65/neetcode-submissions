class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans =[0]*len(temperatures)
        stack =[]
        for i, t in enumerate(temperatures):
            #stack[-1][0] means top of the the stack ka temperatue (temperature 0, index 1)
            while stack and stack[-1][0] < t:
                stack_t, stack_i =stack.pop()
                ans[stack_i] = i - stack_i
            stack.append((t,i))
        return ans

# time: O(n) n nikal ke n daal rahe
#space: O(n)
        