# Peter Finnerty

# Task 1 from Fundamentals of Data Analysis

# October 5th, 2020: Write a Python function called counts that takes a list as
# input and returns a dictionary of unique items in the list as keys and the number of
# times each item appears as values. So, the input ['A', 'A', 'B', 'C', 'A']
# should have output {'A': 3, 'B': 1, 'C': 1} . Your code should not depend
# on any module from the standard library1 or otherwise. You should research
# the task first and include a description with references of your algorithm in the
# notebook.

# Create input function for user and assign to variable 'U'.
U = input("Enter a list:")

# Reference: Python program to check if two to get unique values from list using traversal.  
# Example found at https://www.geeksforgeeks.org/python-get-unique-values-list/

# function to get unique values 
def unique(list1): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    # print list 
    for x in unique_list: 
        print (x, ) 
# driver code 
list1 = U 
print("the unique values from user input are:") 
unique(list1) 

