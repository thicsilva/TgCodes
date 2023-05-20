def bitcount(n):
  count=0
  while n:
    n ^= n - 1
    count += 1
    return count
    

def gcd(a,b):
  if b==0:
    return a
  else:
    return gcd(a % b, b)