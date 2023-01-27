# THIS IS A PRANK BITCOIN MINER
import random, string

def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

print(''' _       _             _        _______ _                   
(_)     (_)  _     _  | |      (_______|_)                  
 _       _ _| |_ _| |_| | _____ _  _  _ _ ____  _____  ____ 
| |     | (_   _|_   _) || ___ | ||_|| | |  _ \| ___ |/ ___)
| |_____| | | |_  | |_| || ____| |   | | | | | | ____| |    
|_______)_|  \__)  \__)\_)_____)_|   |_|_|_| |_|_____)_|    
''')

password = ""

while password != "root":
    password = input("This is a paid service, please enter the password: ")

print("Loading",end="")

for i in range(5):
    print(".",end="")

print("")

for i in range(147):
    print(randomword(random.randint(26,35))+" | Status: Failed")

print(randomword(random.randint(26,35))+" | Status: Successful")
print("+0.2 BTC added to Bitcoin Wallet")
exit()
