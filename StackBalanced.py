# create a ist of all open and close parentheses
open_list=["[","{","("]
close_list=["]","}",")"]

#validation function
def balanced_parentheses(s):

   #parse through the string and push and pop values in stack
   stack=[]
   for i in s:
       if i in open_list:
           stack.append(i)
       if i in close_list:
           pos=close_list.index(i)
           if ((len(stack)>0) and open_list[pos]==stack[len(stack)-1]):
               stack.pop()
           else:
               return "UnBalanced Parentheses"
   if len(stack) == 0:
       return "Balanced Parentheses"
   else:
       return "UnBalanced Parentheses"

if __name__ == '__main__':
    s=input()
    print(balanced_parentheses(s))



