originalstring= input ("please input a string")

reverse = originalstring[-1::-1]
if reverse == originalstring:
   print("It's a palindrome")
else:
   print("It's not a palindrome")
