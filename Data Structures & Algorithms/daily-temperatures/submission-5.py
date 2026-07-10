class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans =[0]*len(temperatures)
        for i in range(len(temperatures)):
            days=1
            for j in range(i+1,len(temperatures)): 
                if temperatures[j]>temperatures[i]:
                    ans[i] =days
                    break
                days+=1
        return ans
        