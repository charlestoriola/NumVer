from Function.functions import *
print("#"*30)
print("Welcome to the Number Verifier")
print("#"*30)
next()


number = input("Enter the phone number: ")
if verify(number):
	print("Issa Number")
else:
	print("Nah G. Not a phone number")