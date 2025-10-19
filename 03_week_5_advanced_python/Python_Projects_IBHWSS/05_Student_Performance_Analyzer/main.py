# main.py
from UserManagement import UserManager
from MarksManagement import MarksManager
from ReportsManagement import ReportsManager

def main():
    user_manager = UserManager()
    marks_manager = MarksManager()
    report_manager = ReportsManager()

    print(f"{'-' * 60}")
    print("🎓 Welcome to Student Result & Performance Analyzer")
    print(f"{'-' * 60}")

    while True:
        print("\nMain Menu:")
        print("1) Login (Teacher)")
        print("2) Create Teacher Account")
        print("3) Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            teacher_username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()

            # ✅ Use the function from UserManagement
            login_success = user_manager.login_teacher(teacher_username, password)

            # Modify login_teacher() to return True/False instead of just print
            if not login_success:
                continue  # back to main menu

            # Teacher dashboard
            while True:
                print(f"\n{'-' * 60}")
                print(f"📘 Teacher Dashboard ({teacher_username})")
                print(f"{'-' * 60}")
                print("1) Add Student Result")
                print("2) View All Students Results")
                print("3) View Top 3 Performers")
                print("4) View Subject Average Marks")
                print("5) View Class Average Marks")
                print("6) Search Student by Name & Roll No")
                print("7) Visualize Average Marks of Each Subject")
                print("8) Logout")

                option = input("Enter your option: ").strip()

                if option == '1':
                    std_name = input("Enter student name: ")
                    roll_no = input("Enter roll no: ")
                    class_ = input("Enter class (e.g., 10-A): ")

                    marks = {}
                    print("Enter marks for subjects (type 'done' to finish):")
                    while True:
                        subject = input("Subject name: ").strip()
                        if subject.lower() == 'done':
                            break
                        try:
                            score = int(input(f"Marks for {subject}: "))
                            marks[subject] = score
                        except ValueError:
                            print("❌ Please enter a valid integer value for marks.")

                    marks_manager.add_student_result(teacher_username, std_name, roll_no, class_, **marks)

                elif option == '2':
                    report_manager.view_all_students_result(teacher_username)

                elif option == '3':
                    report_manager.view_top_3_performer(teacher_username)

                elif option == '4':
                    class_name = input("Enter class name (e.g., 10-A): ")
                    subject = input("Enter subject name: ")
                    avg = report_manager.view_subject_avg(teacher_username, class_name, subject)
                    if avg:
                        print(f"\n📊 Average marks in {subject}: {round(avg,2)}")

                elif option == '5':
                    class_name = input("Enter class name (e.g., 10-A): ")
                    avg = report_manager.avg_class_marks(teacher_username, class_name)
                    print(f"\n🏫 Average marks of class {class_name}: {round(avg,2)}")

                elif option == '6':
                    std_name = input("Enter student name: ")
                    roll_no = int(input("Enter roll no: "))
                    report_manager.filter_std(std_name, roll_no)

                elif option == '7':
                    class_name = input("Enter class name (e.g., 10-A): ")
                    report_manager.visualize_avgMarks_allSub(teacher_username, class_name)

                elif option == '8':
                    print(f"👋 Logged out successfully, {teacher_username}.")
                    break

                else:
                    print("❌ Invalid option. Please select from 1 to 8.")

        elif choice == '2':
            teacher_username = input("Enter new username: ")
            password = input("Enter password: ")
            phone = input("Enter phone number: ")
            user_manager.create_teacher_acc(teacher_username, password, phone)

        elif choice == '3':
            print("👋 Thank you for using Student Result & Performance Analyzer!")
            break

        else:
            print("❌ Invalid choice! Please select 1, 2, or 3.")


if __name__ == '__main__':
    main()
