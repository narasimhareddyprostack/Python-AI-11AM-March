#coin flip simulation
import random
coin=["head","tail"]
no_heads=0
no_tails=0
for num in range(100):
    if random.choice(coin) =="head":
        no_heads=no_heads+1
    else: 
        no_tails=no_tails+1


print("No of Heads", no_heads)
print("No of Tails", no_tails)