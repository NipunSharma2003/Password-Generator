import random
import string 
charValues=string.ascii_letters+string.digits+string.punctuation
password=""
for i in range(1,13):
    password=password+random.choice(charValues)

print("Suggested password is :",password)    