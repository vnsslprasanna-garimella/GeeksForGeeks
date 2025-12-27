def pair_sum(arr, sum):
    # code here
    for i in arr:
        for j in arr:
            if i ==j :
                continue
            elif (i+j) == sum:
                return True
    return False

