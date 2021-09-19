# CORRECT 100%

"""
DESCRIPTION: Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.
You need to help them find out their common interest with the least list index sum. 
If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.


TEST CASES: 
Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
Output: ["KFC","Burger King","Tapioca Express","Shogun"]

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KNN","KFC","Burger King","Tapioca Express","Shogun"]
Output: ["KFC","Burger King","Tapioca Express","Shogun"]

Input: list1 = ["KFC"], list2 = ["KFC"]
Output: ["KFC"]
"""
class Solution:
    
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = [] # list that contains the returning restaurants.

        sum = 2001 # worst case len(list) = 1000, worst case sum = len(list)*2 + 1.
        sums = [] # list that stores included restaurant sums.

        # finding common restaurants between the two lists and checkign their index sums.
        for restaurant1 in list1:
            for restaurant2 in list2:
                if ((restaurant1 == restaurant2) and 
                (list1.index(restaurant1) + list2.index(restaurant2) <= sum)):
                    res.append(restaurant1)
                    sum = list1.index(restaurant1) + list2.index(restaurant2)
                    sums.append(sum)
        
        # tie checking, in case of multiple restaurants in result list
        # if not tie, returing the last added restaurant (minimum index sum possible)
        if len(res) > 1:
            if sums[1:] == sums[:-1]: 
                return res
            else:
                res[-1] = []
        return res

