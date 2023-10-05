import os
import sys
import time

msg = """

|1|-----> text to base64

|2|-----> base64 to text

"""

os.system('clear')  
print(msg)

sh = input("select one \n")

if (sh == 1 ) :
   os.chdir('hash.sh')

elif (sh == 2) :
   os.chdir('hash2.0.sh')

else : 
   print("pls chose '1' or '2' ")