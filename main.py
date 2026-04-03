import random

number = random.randint(1, 100)
attempts = 0

print("🎯 1 dan 100 gacha son o‘yladim!")

while True:
    guess = int(input("Taxminingizni kiriting: "))
    attempts += 1

    if guess < number:
        print("🔼 Kattaroq son kiriting")
    elif guess > number:
        print("🔽 Kichikroq son kiriting")
    else:
        print(f"🎉 To‘g‘ri topdingiz! Urinishlar soni: {attempts}")
        break
