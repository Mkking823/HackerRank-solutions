given an array arr of n integers,and two integers l and r find the number of pairs(i,j)
where (1<=i<j<=n)such that the value arr[i] +arr[j] lies between l and r both inclusive ,arry indices start at 1.
solution:
  def getNumPairs(arr,l,r):
    count=0
    sum_counts={}
    for num in arr:
        for target_sum in range(l,r+1):
          complement =target_sum-num
          if complement in sum_counts:
            count += sum_counts[complement]
       if num in sum_counts:
         sum_count[num]+=1
       else:
         sum_counts[num]=1
    return count
      
