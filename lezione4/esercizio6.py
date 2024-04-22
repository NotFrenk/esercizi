def intersection(nums1: list[int],nums2:list[int]) ->list[int]:
    nums_comune:list=[]
    for i in nums1:
        if i in nums2:
            nums_comune.append(i)
    print(set(nums_comune))




out=intersection([2,3,2,1,2,3,],[7,8,4,2,3,1,5])