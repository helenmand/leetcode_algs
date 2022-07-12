class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        
        for jewel in jewels:
            if jewel in stones:
                res += stones.count(jewel)
        return res