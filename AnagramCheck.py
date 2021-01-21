str1 = (input("Enter First string: "))
str2 = (input("Enter second string: "))
str1_lower = str1.lower()
str2_lower = str2.lower()
def CheckAnagram(str1_lower,str2_lower):
    if(sorted(str1_lower)== sorted(str2_lower)):
        print("The Given input strings are anagrams")
    else:
        print("The Given input strings are not anagrams") 
CheckAnagram(str1_lower,str2_lower)
