#!/usr/bin/env python
# coding: utf-8

# ##
# Linked Lists
# 
# Formation of Linked List,------->     Addition  of Linked List at the begening and ------->     Addition  of Linked List at the ending ------> Addition of Linked list before and after any specific index or data ##

# In[1]:


class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
    
class Linked_List:
    def __init__(self):
        self.head = None
        
    def print_LL(self):
        n=self.head
        while n is not None:
            print(n.data) 
            n = n.ref
            
    def add_begning(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
        
    def add_ending(self,data):
        new_node = Node(data)
        n =self.head
        if n is None:
            n =new_node
        else:
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
            
    def add_before(self,data,x):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref =self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n= n.ref
        if n.ref is None:
            print('No data in any node belongs to x')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
        
    def add_after(self,data,x):
        if self.head is None:
            print("List is empty")
            return
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.ref
            new_node= Node(data)
            new_node.ref= n.ref
            n.ref = new_node        
                
        


# In[2]:


LL = Linked_List()
LL.add_begning(10)
LL.add_begning(40)
LL.add_begning(10.1)
LL.add_begning(100)
LL.add_ending(4.4)
LL.add_begning(1)
LL.add_before(0,10.1)
LL.add_after(0,10.1)


LL.print_LL()

