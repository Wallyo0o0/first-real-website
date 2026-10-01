
age = int(input("How old are you "))
if age > 85:
    print("You are not that old liar")
elif age > 18:
    print("You are an adult you are able to join")
elif age <= 0 :
    print("you are not born yet go trick someone else")
elif 0 < age < 17:
    print("You are a child")