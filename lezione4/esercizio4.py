"""data una lista nums di n elementi, restituire l'elemento che 
compare piu di n/2 volte

esempio 1
nums= [3,2,3] -> restituisce 3
"""

def majority_element(nums:list[int]) -> int:
    for i in nums:
        if nums.count(i) > len(nums) %2:
            print(i)
            return i
    return print("non ci siamo")
majority_element([3,7,6,2,1])