def f(a):
  if a==1 or a==0:
    return 1
  else:
    return a*f(a-1)
a=int(input())
print(f(a))