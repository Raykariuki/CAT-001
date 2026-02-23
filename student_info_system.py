import json

def get_student_details():
    """Get student details from user input"""
    print("\n" + "="*50)
    print("Enter Student Details")
    print("="*50)
    
    name = input("Enter student name: ").strip()
    student_id = input("Enter student ID: ").strip()
    favorite_ai_tool = input("Enter favorite AI tool: ").strip()
    
    student = {
        'name': name,
        'student_id': student_id,
        'favorite_ai_tool': favorite_ai_tool
    }
    
    return student

def display_all_students(students):
    """Display all students in a formatted way"""
    print("\n" + "="*50)
    print(f"STUDENT RECORDS (Total: {len(students)} students)")
    print("="*50)
    
    if not students:
        print("No students in the system yet.")
        return
    
    for i, student in enumerate(students, 1):
        print(f"\nStudent #{i}:")
        print(f"  Name: {student['name']}")
        print(f"  ID: {student['student_id']}")
        print(f"  Favorite AI Tool: {student['favorite_ai_tool']}")
    
    print("\n" + "="*50)

def save_to_file(students, filename="students.txt"):
    """Save students list to a text file"""
    try:
        with open(filename, 'w') as file:

            file.write("="*60 + "\n")
            file.write(f"STUDENT INFORMATION SYSTEM - Total Students: {len(students)}\n")
            file.write("="*60 + "\n\n")
    
            for i, student in enumerate(students, 1):
                file.write(f"Student #{i}:\n")
                file.write(f"  Name: {student['name']}\n")
                file.write(f"  ID: {student['student_id']}\n")
                file.write(f"  Favorite AI Tool: {student['favorite_ai_tool']}\n")
                file.write("-"*40 + "\n")
        
            file.write("\n\n" + "="*60 + "\n")
            file.write("JSON FORMAT:\n")
            file.write("="*60 + "\n")
            json.dump(students, file, indent=4)
            
        print(f"\n✅ Data successfully saved to {filename}")
        return True
    except Exception as e:
        print(f"\n❌ Error saving to file: {e}")
        return False

def main():
    """Main program function"""
    students = []  
    
    print("\n🎓 STUDENT INFORMATION SYSTEM 🎓")
    print("Welcome! This program will help you manage student records.")
    
    while True:
        print("\n" + "-"*50)
        print("Options:")
        print("1. Add a new student")
        print("2. View all students")
        print("3. Save to file and exit")
        print("4. Exit without saving")
        print("-"*50)
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            student = get_student_details()
            students.append(student)
            print(f"\n✅ Student '{student['name']}' added successfully!")
            
        elif choice == '2':
        
            display_all_students(students)
            
        elif choice == '3':
            
            if students:
                if save_to_file(students):
                    print("\n👋 Goodbye! Your data has been saved.")
                else:
                    print("\n⚠️  Exiting without saving due to error.")
            else:
                print("\n⚠️  No student data to save.")
            break
            
        elif choice == '4':
            
            print("\n👋 Goodbye! No data was saved.")
            break
            
        else:
            print("\n❌ Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()