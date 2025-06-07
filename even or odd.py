"""def isEven(num):
  return num&1

#if __name__=="__main__":
  #num = 14
  print(__name__)
  if isEven(14):
    print('Even')
  else:
    print('Odd')"""

def iseven(a):
    return not a&1
print(__name__)
print("even" if iseven(90) else "odd")
