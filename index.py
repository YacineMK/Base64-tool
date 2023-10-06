import os
import sys
import time

msg = """

|1|------> text to base64

|2|------> base64 to text

"""

os.system('clear')
print(msg)

sh = input("select one \n")

if sh == '1':
    script_path = os.path.join(os.path.dirname(__file__), 'hash.sh')
    os.system(script_path)

elif sh == '2':
    script_path = os.path.join(os.path.dirname(__file__), 'hash2.0.sh')
    os.system(script_path)

else:
    print("Please choose '1' or '2'")
