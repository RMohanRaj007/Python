def odd(a):
 return a&1
if __name__=="__main__":
    a=int(input("enter the value"))
    print("odd") if odd(a) else print("even")
