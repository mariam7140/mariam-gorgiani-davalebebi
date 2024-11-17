friendships = {}

while True:
    user_input = input("Enter friendship (e.g., 'Giorgi - Nini') or 'FINISH' to stop: ").strip()
    
    if user_input == "FINISH":
        break
    
    if " - " in user_input:
        person_1, person_2 = user_input.split(" - ")

        if person_1 not in friendships:
            friendships[person_1] = set()
        if person_2 not in friendships:
            friendships[person_2] = set()
        
        friendships[person_1].add(person_2)
        friendships[person_2].add(person_1)
    else:
        print("Incorrect input format. Please use 'Name_1 - Name_2' or 'FINISH'.")

print("Friendship List:", end="\n")
for person, friends in friendships.items():
    print(f"{person}: {', '.join(friends)}")