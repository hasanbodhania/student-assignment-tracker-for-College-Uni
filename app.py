from database import create_table, add_assignment, get_all_assignments, mark_completed
from datetime import datetime


def show_menu():
    print("\n📚 Student Assignment Tracker")
    print("1. Add Assignment")
    print("2. View All Assignments")
    print("3. Mark Assignment as Complete")
    print("4. Exit")


def add_assignment_menu():
    subject = input("Subject: ")
    title = input("Assignment Title: ")
    due_date = input("Due Date (YYYY-MM-DD): ")
    priority = input("Priority (Low / Medium / High): ")

    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("❌ Invalid date format.")
        return

    add_assignment(subject, title, due_date, priority)
    print("✅ Assignment added successfully!")


def view_assignments():
    assignments = get_all_assignments()

    if not assignments:
        print("📭 No assignments found.")
        return

    print("\nID | Subject | Title | Due Date | Priority | Status")
    print("-" * 60)

    for a in assignments:
        print(f"{a[0]} | {a[1]} | {a[2]} | {a[3]} | {a[4]} | {a[5]}")


def complete_assignment():
    try:
        assignment_id = int(input("Enter assignment ID to mark complete: "))
        mark_completed(assignment_id)
        print("✅ Assignment marked as completed!")
    except ValueError:
        print("❌ Please enter a valid number.")


def main():
    create_table()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_assignment_menu()
        elif choice == "2":
            view_assignments()
        elif choice == "3":
            complete_assignment()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option.")


if __name__ == "__main__":
    main()
