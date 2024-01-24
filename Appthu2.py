from flask import request,Flask,jsonify
from flask_basicauth import BasicAuth
app = Flask(__name__) 

app.config['BASIC_AUTH_USERNAME']='username'
app.config['BASIC_AUTH_PASSWORD']='password'
basic_auth = BasicAuth(app)

student=[
    {"id":6530300252,"Name":"Student 1","Major":"Author 1","GPA":"ur grade"},
    {"id":6530300259,"Name":"Student 2","Major":"Author 2","GPA":"ur grade"},
    {"id":6530300257,"Name":"Student 3","Major":"Author 3","GPA":"ur grade"}
]
@app.route("/")
def Greet():
    return "<p>Welcome to Student Management Systems</p>"

@app.route("/student",methods=["GET"])
@basic_auth.required
def get_all_student():
    return jsonify({"Student":student})

@app.route("/student/<int:student_id>",methods=["GET"])
@basic_auth.required
def get_student(student_id):
    stu =  next(( b for b in student if b["id"]==student_id),None)
    if stu:
        return jsonify(stu)
    else:
        return jsonify({"error":"Student not found"}),404

@app.route("/student",methods=["POST"])
@basic_auth.required
def create_student():
    data = request.get_json()
    new_student={
        "id":data["id"],
        "Name":data["Name"],
        "Major":data["Major"],
        "GPA":data["GPA"]
    }
    if any(student["id"] == new_student["id"] for student in student):
          return jsonify({"error": "Cannot create new student"}),500
    else:
          student.append(new_student)
          return jsonify(new_student),200

@app.route("/student/<int:student_id>",methods=["PUT"])
@basic_auth.required
def update_student(student_id):
    stu = next((b for b in student if b["id"]==student_id),None)
    if stu:
        data = request.get_json()
        stu.update(data)
        return jsonify(stu)
    else:
        return jsonify({"error":"Student not found"}),404

@app.route("/student/<int:student_id>",methods=["DELETE"])
@basic_auth.required
def delete_student(student_id):
    stu = next((b for b in student if b["id"]==student_id),None)
    if stu:
        student.remove(stu)
        return jsonify({"message":"student deleted successfully"}),200
    else:
        return jsonify({"error":"student not found"}),404
    




if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)