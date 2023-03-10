# list 

list = ["I'll be back", "With great power comes great responsibility", "I am Iron Man", "Why so serious?", "Loki, I thought the world of you."]

question = input ("Choose your hero and i will pick a phrase for you : Terminator, Spider-Man, IronMan, Joker or Thor ")

if question == "Terminator":
    print(list[0])
elif question == "Spider-Man":
    print(list[1])
elif question == "IronMan":
    print(list[2])
elif question == "Joker":
    print(list[3])
elif question == "Thor":
    print(list[4])
else:
    print("Please choose the correct Hero from the list")