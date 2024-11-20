import random

from davaleba_16.common import process_user_input
from davaleba_16.db import sessions

def list_admin_menu_items():
    print("1. List all sessions")
    print("2. Remove session")
    print("3. Add session")
    print("4. Edit session")
    print("Type 'exit' to return to the main menu") # მთავარ მენიუში გამოსვლა
    return process_user_input()

def greetings():
    print("Welcome to the admin panel")
    print("Please sign in to continue")

# სანამ ახალ სესიას დავამატებთ, შევამოწმოთ არის თუ არა უკვე ასეთი სესია
def session_exists(session_id):
    for session in sessions:
        if session["session_id"] == session_id:
            return True
    return False

def add_session():
    print("Adding a new session")
    print("Enter the session details:")
    film_name = input("Film name: ")
    start_time = input("Start time (e.g., 14:00): ")
    room_number = input("Room number: ")
    room_length = int(input("Room length (number of rows): "))
    room_width = int(input("Room width (number of seats per row): "))
    capacity = room_length * room_width

    session_id = random.randint(1, 1000)
    while session_exists(session_id):
        session_id = random.randint(1, 1000)

    session = {
        "session_id": session_id,
        "film_name": film_name,
        "start_time": start_time,
        "room_number": room_number,
        "room_length": room_length,
        "room_width": room_width,
        "capacity": capacity,
    }
    sessions.append(session)
    print(f"Session added successfully! Session ID: {session_id}")

# სესიის წაშლა
def remove_session():
    print("Current sessions:")
    list_sessions()
    if not sessions:
        print("No sessions available to remove.")
        return
    session_id = int(input("Enter the session ID to remove: "))
    for session in sessions:
        if session["session_id"] == session_id:
            sessions.remove(session)
            print(f"Session ID {session_id} removed successfully.")
            return
    print(f"Session ID {session_id} not found. Please try again.")

# დაედითება
def edit_session():
    print("Current sessions:")
    list_sessions()
    if not sessions:
        print("No sessions available to edit.")
        return
    session_id = int(input("Enter the session ID to edit: "))
    for session in sessions:
        if session["session_id"] == session_id:
            print("Enter new details (press Enter to keep current value):")
            session["film_name"] = input(f"Film name [{session['film_name']}]: ") or session["film_name"]
            session["start_time"] = input(f"Start time [{session['start_time']}]: ") or session["start_time"]
            session["room_number"] = input(f"Room number [{session['room_number']}]: ") or session["room_number"]
            room_length = input(f"Room length [{session['room_length']}]: ")
            session["room_length"] = int(room_length) if room_length else session["room_length"]
            room_width = input(f"Room width [{session['room_width']}]: ")
            session["room_width"] = int(room_width) if room_width else session["room_width"]
            session["capacity"] = session["room_length"] * session["room_width"]
            print(f"Session ID {session_id} updated successfully.")
            return
    print(f"Session ID {session_id} not found. Please try again.")

def list_sessions():
    print("Available sessions:")
    if not sessions:
        print("No sessions found.")
        return
    for session in sessions:
        print(f"\nSession ID: {session['session_id']}")
        print(f"Film name: {session['film_name']}")
        print(f"Start time: {session['start_time']}")
        print(f"Room number: {session['room_number']}")
        print(f"Room length: {session['room_length']}")
        print(f"Room width: {session['room_width']}")
        print(f"Capacity: {session['capacity']}")

def admin_loop():
    greetings()
    while True:
        user_input = list_admin_menu_items()
        if user_input == "1":
            list_sessions()
        elif user_input == "2":
            remove_session()
        elif user_input == "3":
            add_session()
        elif user_input == "4":
            edit_session()
        elif user_input == "exit":
            print("Returning to the main menu...")
            break
        else:
            print("Invalid input. Please try again.")