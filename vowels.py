string=input("enter a string:  ")
vowels="aeiouAEIOU"
count=sum(string.count(vowel)  for vowel in vowels)
print(count)