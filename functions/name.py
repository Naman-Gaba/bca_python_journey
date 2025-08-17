students = []  # global list

def add_student(name, age=18):
    global students  # tell Python we are using the global list
    student_info = {"name": name, "age": age}
    students.append(student_info)
    print(students)

add_student("naman")