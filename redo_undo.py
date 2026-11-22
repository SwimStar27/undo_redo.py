undo_stack = []
redo_stack = []
text = ""

while True:
    print("------- Text Editor -------")
    print("Current Text: This is the code", text)
    print("1. Type Text")
    print("2. Undo")
    print("3. Redo")
    print("4. View Undo History")
    print("5. View Redo History")
    print("6. Exit App")

    choice = input("Enter Your Choice Number: ")

    if choice == "1":
        undo_stack.append(text)
        new_text = input("Enter Text to Add: ")
        text += new_text
        redo_stack.clear()
        print("Text Added Successfully")

    elif choice == "2":
        if len(undo_stack) > 0:
            redo_stack.append(text)
            text = undo_stack.pop()
            print("Undo Successful")
        else:
            print("No Actions to Do")

    elif choice == "3":
        if len(redo_stack) > 0:
            undo_stack.append(text)
            text = redo_stack.pop()
            print("Redo Successful")

        else:
            print("No Actions to Redo")

    elif choice == "4":
        print("Undo Stack:", undo_stack)

    elif choice == "5":
        print("Redo Stack:", redo_stack)

    elif choice == "6":
        print("Closing Text Editor...")
        break

    else:
        print("Invalid Choice. Enter a New Number")