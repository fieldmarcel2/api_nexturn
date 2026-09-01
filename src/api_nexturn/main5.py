# from flask import Flask,request

# app= Flask(__name__)



# @app.get( "/handle_get")

# def handle_request():
#     print(request.json)

#     return "hiii"

# @app.post("/handle-post")

# def check_request():
#  print(request.json)
#  return "POST request received"



# if __name__== "__main__":
#  app.run(debug= True)


class Student():

    def __init__(self, student_id , name, age, course, marks):
        self.student_id= student_id
        self.age= age
        self.name= name
        self.course= course
        self.marks= marks



    def calculate_grade(self):


        if ( self.marks >80):
            return "A"
        elif ( self.marks >80):
                    return "B"
        elif  ( self.marks >=60 and self.marks <80):
                    return "B"  

        elif  60 >self.marks >=40: return "C"
        else :return "fail"

    def get_details(self):
       return (f"id is {self.student_id},name is {self.name} , age is {self.age} course is {self.course} , marks is {self.marks} ")

    def update_marks(self,marks):
     self.marks = marks

class StudentManager:

    def __init__(self):
        self.students = []

    # Add student
    def add_student(self, student):

        # Check duplicate ID
        if self.find_student(student.student_id):
            return False

        self.students.append(student)
        return True

    # Find student
    def find_student(self, student_id):

        for student in self.students:

            if student.student_id == student_id:
                return student

        return None

    # Update student
    def update_student(self, student_id, data):

        student = self.find_student(student_id)

        if student is None:
            return None

        if "name" in data:
            student.name = data["name"]

        if "age" in data:
            student.age = data["age"]

        if "course" in data:
            student.course = data["course"]

        if "marks" in data:
            student.update_marks(data["marks"])

        return student

    # Delete student
    def delete_student(self, student_id):

        student = self.find_student(student_id)

        if student is None:
            return False

        self.students.remove(student)
        return True

    # Get all students
    def get_all_students(self):

        return self.students

    # Get passed students
    def get_passed_students(self):

        passed_students = []

        for student in self.students:

            if student.marks >= 40:
                passed_students.append(student)

        return passed_students

    # Statistics
    def get_stats(self):

        if len(self.students) == 0:
            return {
                "total_students": 0,
                "average_marks": 0,
                "highest_marks": 0,
                "lowest_marks": 0
            }

        marks = []

        for student in self.students:
            marks.append(student.marks)

        return {
            "total_students": len(self.students),
            "average_marks": round(sum(marks) / len(marks), 2),
            "highest_marks": max(marks),
            "lowest_marks": min(marks)
        }



manager= StudentManager()


from flask import Flask,request,jsonify


app= Flask(__name__)
@app.post("/students")

def add_student():

    data = request.json

    student = Student(
        data["student_id"],
        data["name"],
        data["age"],
        data["course"],
        data["marks"]
    )

    manager.add_student(student)

    return jsonify(student.get_details()), 201


@app.get("/students")
def get_students():

    students = manager.get_all_students()

    return jsonify([
        student.get_details()
        for student in students
    ])


# -------------------------
# GET /students/<id>
# -------------------------

@app.get("/students/<student_id>")
def get_student(student_id):

    student = manager.find_student(student_id)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    return jsonify(student.get_details())

@app.patch("/students/<student_id>")
def update_student(student_id):

    data = request.json

    student = manager.update_student(student_id, data)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    return jsonify(student.get_details())


# -------------------------
# DELETE /students/<id>
# -------------------------

@app.delete("/students/<student_id>")
def delete_student(student_id):

    if not manager.delete_student(student_id):
        return jsonify({"error": "Student not found"}), 404

    return jsonify({"message": "Student deleted"})

@app.get("/students/passed")
def passed_students():

    students = manager.get_passed_students()

    return jsonify([
        student.get_details()
        for student in students
    ])


# -------------------------
# GET /students/stats
# -------------------------

@app.get("/students/stats")
def stats():

    return jsonify(manager.get_stats())




if __name__ == "__main__":
    app.run(debug=True)