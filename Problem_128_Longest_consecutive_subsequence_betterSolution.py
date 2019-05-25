import operator
def longestConsecutive(nums):
    nums = set(nums)
    best = 0
    best_list=[]

    for x in nums:
        current_best = [x]
        # check previous element is there in set or not otherwise continue
        if x-1  not in nums:
            y = x+1
            while y in nums:
                current_best.append(y)
                y+=1
        best=max(best,y-x)
        print("best ",best)
        print("curernt best list",current_best)
        best_list.append((len(current_best),current_best))
    best_list.sort(key = operator.itemgetter(0),reverse=True)

    print(best_list)
    return  best
print(longestConsecutive([1,12,3,4,5,8,7,6,1,2,3,4,5,6,7,8,9,11,12,13,14,16,15,17,18,19,20,21,22]))