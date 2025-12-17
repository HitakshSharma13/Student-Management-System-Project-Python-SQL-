import sqlite3

# Database setup
def create_table():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            grade TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Add a student
def add_student(name, age, grade):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO students (name, age, grade) VALUES (?, ?, ?)', (name, age, grade))
    conn.commit()
    conn.close()
    print("Student added successfully!")

# View all students
def view_students():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    rows = cursor.fetchall()
    conn.close()
    if rows:
        print("ID | Name | Age | Grade")
        print("-" * 25)
        for row in rows:
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")
    else:
        print("No students found.")

# Update a student
def update_student(student_id, name=None, age=None, grade=None):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    updates = []
    params = []
    if name:
        updates.append("name = ?")
        params.append(name)
    if age:
        updates.append("age = ?")
        params.append(age)
    if grade:
        updates.append("grade = ?")
        params.append(grade)
    params.append(student_id)
    if updates:
        cursor.execute(f'UPDATE students SET {", ".join(updates)} WHERE id = ?', params)
        conn.commit()
        print("Student updated successfully!")
    else:
        print("No updates provided.")
    conn.close()

# Delete a student
def delete_student(student_id):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
    conn.commit()
    conn.close()
    print("Student deleted successfully!")

# Search for a student by ID
def search_student(student_id):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students WHERE id = ?', (student_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Grade: {row[3]}")
    else:
        print("Student not found.")

# Main menu
def main():
    create_table()
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            grade = input("Enter grade: ")
            add_student(name, age, grade)
        elif choice == '2':
            view_students()
        elif choice == '3':
            student_id = int(input("Enter student ID to update: "))
            name = input("Enter new name (leave blank to skip): ") or None
            age = input("Enter new age (leave blank to skip): ")
            age = int(age) if age else None
            grade = input("Enter new grade (leave blank to skip): ") or None
            update_student(student_id, name, age, grade)
        elif choice == '4':
            student_id = int(input("Enter student ID to delete: "))
            delete_student(student_id)
        elif choice == '5':
            student_id = int(input("Enter student ID to search: "))
            search_student(student_id)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()