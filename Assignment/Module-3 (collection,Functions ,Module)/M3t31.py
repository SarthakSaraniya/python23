# Write a Python function that checks whether a passed string is palindrome or not 

def palindrome(s) :
      
    if s == s[::-1] :
        print("Passed string is palindrome.")
        
    else :
        print("Passed string is not palindrome.")
        
s = input("Enter the string : ")
palindrome(s)