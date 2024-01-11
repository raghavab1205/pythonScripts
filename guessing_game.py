secret_fi = 0
crack_no = int(input("Enter a random no(0 - 5): "))
while secret_fi < 9:
    secret_no = secret_fi + crack_no
    while secret_no < 9:
        guess_count = 0
        while guess_count < 3:
            guess = int(input("Your guess: "))
            guess_count += 1
            if guess == secret_no:
                print("You have won!!!!")
                break
        else:
            print("Sorry you have failed...")
            break
    secret_fi += 1
    crack_no += 1