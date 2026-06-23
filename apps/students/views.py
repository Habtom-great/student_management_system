from django.shortcuts import render

# Create your views here.
class student_dashboard:
    def __init__(self, request):
        self.request = request

    def get(self):
        return render(self.request, "students/student_dashboard.html")
class student_list:
    def __init__(self, request):
        self.request = request

    def get(self):
        return render(self.request, "students/student_list.html")
class add_student:
    def __init__(self, request):
        self.request = request

    def get(self):
        return render(self.request, "students/add_student.html")
class edit_student:
    def __init__(self, request, student_id):
        self.request = request
        self.student_id = student_id

    def get(self):
        return render(self.request, "students/edit_student.html", {"student_id": self.student_id})
class delete_student:
    def __init__(self, request, student_id):
        self.request = request
        self.student_id = student_id

    def get(self):
        return render(self.request, "students/delete_student.html", {"student_id": self.student_id})