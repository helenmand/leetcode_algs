# CORRECT 100% 
# Runtime: 40 ms, faster than 85.06% of Python3 online submissions for Fizz Buzz.
# Memory Usage: 15 MB, less than 67.34% of Python3 online submissions for Fizz Buzz.

"""
DESCRIPTION:Given an integer n, return a string array answer (1-indexed) where:
answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i if non of the above conditions are true.


TEST CASES:
Input: n = 3
Output: ["1","2","Fizz"]

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
"""
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        
        for num in range(1, n + 1):

            divisibleBy3 = (num%3 == 0)
            divisibleBy5 = (num%5 == 0)
            
            if divisibleBy3 and divisibleBy5:
                answer.append("FizzBuzz")
            elif divisibleBy3:
                answer.append("Fizz")
            elif divisibleBy5:
                answer.append("Buzz")
            else:
                answer.append(str(num))
        
        return answer