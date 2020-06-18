"""
using stack we can get binary representation of a number

"""

def dec_bin(num):
    s=[]
    while num > 0:
      r=num%2
      num=num // 2
      s.append(r)

    ans=""
    for i in range(len(s)):
      ans+=str(s.pop())
    return ans


if __name__ =='__main__':
    num=input()
    a=dec_bin(num)
    print(a)



