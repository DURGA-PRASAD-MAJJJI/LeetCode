class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        li=[]
        for i in range(len(nums1)):
            for k in range(len(nums2)):
                if nums2[k]==nums1[i]:
                    for j in range(k + 1,len(nums2)):
                        if nums2[j]>nums1[i]:
                            li.append(nums2[j])
                            break
                    else:
                        li.append(-1)
                    break
        return li

        