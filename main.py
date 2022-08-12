print("Welcome to Random PW Generator")
print("By NoobzSquad")
import random
import string
ans = string.printable
length = 9
password = "".join(random.sample(ans,length))
print("Your Generated Password is: " + password.replace(" ",""))
