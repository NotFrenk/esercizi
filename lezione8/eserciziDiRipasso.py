# Given the head of a singly linked list, return true if it is a palindrome. 
# Model the Node and Linked List concepts using classes. 


class Node:
    def __init__(self, value=0, next=None):
        self.value=value
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,value):
        if not self.head:
            self.head=Node(value)
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=Node(value)
        
def is_palindrome(head: Node) -> list[int]:
    if not head or not head.next:
        return True
    
    slow=head
    fast=head
    prev_of_slow=None

    while fast and fast.next:
        prev_of_slow=slow
        slow=slow.next
        fast=fast.next.next

    middle =None
    if fast:
        middle=slow
        slow=slow.next

    



# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
# representing the number of elements in nums1 and nums2 respectively. 
# Write a function to merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""
def merge(nums1, m, nums2, n):
    
    p1= m - 1
    p2= n - 1
    p=  m+n -1

    while p1>=0 and p2>=0:
        if nums1[p1] > nums1[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    while p2>=0:
        nums1[p] = nums2[p2]
        p -=1
        p2 -=1
    
    nums1.sort()
    


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)  
"""





# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# write a function to determine if the input string is valid.

# An input string is valid if: 

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.
"""
def is_valid_parenthesis(s: str) -> bool:
    ogni_elemento=[]
    for carattere in s:
        if carattere =="(":
            ogni_elemento.append(carattere)
        
        elif carattere ==")":
            if not ogni_elemento or ogni_elemento[-1] != '(':
                return False
            ogni_elemento.pop()

        if carattere =="{":
            ogni_elemento.append(carattere)
        
        elif carattere =="}":
            if not ogni_elemento or ogni_elemento[-1] != '{':
                return False
            ogni_elemento.pop()

        if carattere =="[":
            ogni_elemento.append(carattere)
        
        elif carattere =="]":
            if not ogni_elemento or ogni_elemento[-1] != '[':
                return False
            ogni_elemento.pop()

    return len(ogni_elemento) ==0
"""        
        

	

# Given a string s which consists of lowercase or uppercase letters, 
# write a function that returns the length of the longest palindrome that can be built with those letters. 
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
"""
from collections import Counter

def longest_palindrome(s: str) -> int:
    contatore_lettere=Counter(s)
    length=0
    odd_found= False

    for conteggio in contatore_lettere.values():
        if conteggio % 2 == 0:
            length += conteggio
        else:
            length += conteggio-1
            odd_found=True

    if odd_found:
        length += 1

    return length
    

print(longest_palindrome("abccccdd"))
"""







# Implement a last-in-first-out (LIFO) stack using only two queues. 
# The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

# Implement the MyStack class:

# - push(x: int) -> None: Pushes element x to the top of the stack.
# - top() -> None Removes the element on the top of the stack and returns it.
# - pop() -> None Returns the element on the top of the stack.
# - empty() -> None Returns true if the stack is empty, false otherwise.





class MyStack:
    def __init__(self):
        self.queue :list= []
 
    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop(0)

    def top(self):

        self.queue.reverse()
        return self.queue[0]

    def empty(self):
       if len(self.queue)==0:
           return True
       else:
           return False
    





mystack = MyStack()
mystack.push(1)
mystack.push(2)
print(mystack.top())    # Output: 2
print(mystack.pop())    # Output: 2
print(mystack.empty())  # Output: False
print(mystack.pop())    # Output: 1
print(mystack.empty())