import random
n=random.randint(1,100)
a = -1
gesses=0
while (n != a):
    gesses += 1
    a = int(input("Guess the Number :"))
    if a > n:
        print("Lower Number")
    else:
        print("Higher Number")
print()
print(f"You Gusees the number in {gesses} Attempts")