# while True:
#   print("This program is running")
#   goAgain = input("Go again?: ")
#   if goAgain == "no":
#     break
# print("Aww, I was having a good time 😭")

# counter = 0
# while True:
#   answer = int(input("Enter a number: "))
#   print("Adding it up!")
#   counter += answer
#   print("Current total is", counter)
#   addAnother = input("Add another? ")
#   if addAnother == "no" or "No":
#     break
# print("Bye!")

# while True:
#   color = input("Enter a color: ")
#   if color == "red":
#     break
#   else:
#     print("Cool color!")
# print("I don't like red")

print("Welcome to Name the Song Lyric")
print()
print("Figure out the missing word as quickly as you can!")
print()


counter = 1
while True:
    lyrics = input("I don't wanna ______ a thing. ")
    if lyrics == "miss" or lyrics == "Miss":
        print("You got it!")
    else:
        print("Nope! Try again!")
        counter += 1
    if lyrics == "miss":
        break
print("Thanks for playing!")

print("You got the correct lyrics in", counter, "attempt(s).")
