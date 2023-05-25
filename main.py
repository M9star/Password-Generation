import string
import random

if __name__ == '__main__':
    p1 = string.ascii_lowercase
    # print(p1)
    p2 = string.ascii_uppercase
    # print(p2)
    p3 = string.digits
    # print(p3)
    p4 = string.punctuation
    # print(p4)
    print("Enter the name you want to generate password for")
    name = input()
    while True:
        pwd_len = input("Enter the length of password to generate: \n")
        if pwd_len.isdigit():
            pwd_len = int(pwd_len)
            break
        else:
            print("Invalid input! Please enter a positive integer")

    s =[]
    # s.extend(list(p1))
    # s.extend(list(p2))
    # s.extend(list(p3))
    # s.extend(list(p4))
    s += list(p1) +list(p2) + list(p3) +list(p4)
    # print(s)
    random.shuffle(s)
    # print(s)
    print("YOur password is")
    password = "".join(s[0:pwd_len])
    print(password)
    with open("Store_pwd.txt", "a") as file:
        store = f"{name}:{password}\n"
        file.write(store)

    # print("".join(random.sample(s,4)))
