def fractionalknapsack(W,arr,n):
  n = len(arr)
  arr.sort(reverse = True, key = lambda x: x[0]/x[1])

  rem_wt = W
  value= 0

  for i in range(n):
    if rem_wt == 0:
      break

    weight = min(rem_wt, arr[i][1])
    rem_wt -= weight
    value += (arr[i][0]/arr[i][1]) * weight

  return value
