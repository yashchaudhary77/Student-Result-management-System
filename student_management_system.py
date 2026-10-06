student = {}  # Dictionary to store student information

while True:
    print("\n-----STUDENT MANAGEMENT SYSTEM APP-----")
    print("1. ADD STUDENT")
    print("2. View Students")
    print("3. Check Results")
    print("4. Exit")

    choice = input("Enter your Choice: ")

    # logic for adding student 

    if choice == "1":
        name = input("Enter Student Name:")
        roll_number = input("Enter Student Roll Number: ")
        marks = float(input("Enter Student Marks: "))
        student[roll_number]= {"name": name , "marks": marks}
        print(f"{name} successfully Added!")

    # logic for viewing student    

    elif choice == "2":
        if not student:
            print("No students found.")
        else:
            for roll_number, data in student.items():
                print(roll_number, data["name"], ":", data["marks"])

    # logic for checking results            

    elif choice == "3":
        roll_number = input("Enter Student Roll Number: ")

        if roll_number in student :
            marks = student[roll_number]["marks"]
            if marks >= 40:
                print("Pass")
            else:
                print("Fail")

        else:
            print("Student not found")

    # logic for exiting the program                     

    elif choice == "4":
        print("Exiting the program...")
        break

    else:
        print("Invalid choice. Please try again.")
