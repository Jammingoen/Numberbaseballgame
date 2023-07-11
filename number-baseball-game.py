import random
numbers = []
for i in range(5):
    while True:
        num = random.randint(0, 9)
        if num not in numbers:
            numbers.append(num)
            break
while True:
    guess = input("5자리 숫자를 맞춰보세요!: ")
    if len(guess) != 5 or not guess.isdigit():
        print("잘못 입력하셨습니다. 5자리숫자를 입력해주세요.")
        continue
    guess = [int(x) for x in guess]
    if guess == numbers:
        print("정답!")
        break
    else:
        strikes = 0
        balls = 0
        for i in range(5):
            if guess[i] == numbers[i]:
                strikes += 1
            elif guess[i] in numbers:
                balls += 1
        print(f"{strikes} strikes, {balls} balls")

