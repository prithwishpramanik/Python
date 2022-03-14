email=input("email")
password=input("password")

if email=="abc@gmail.com" and password=="123":
    print("welcome")
elif email=="abc@gmail.com" and password!="123":
    print("password is not right")
    password=input("password")
    if password=="123":
        print("chillax")
    else:
        print("🙏")
else:
    print("you")