from django.http import HttpResponseForbidden

def admin_only(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.role != "admin":
            return HttpResponseForbidden("Admins only")
        return view_func(request, *args, **kwargs)
    return wrapper


def instructor_only(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.role != "instructor":
            return HttpResponseForbidden("Instructors only")
        return view_func(request, *args, **kwargs)
    return wrapper


def student_only(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.role != "student":
            return HttpResponseForbidden("Students only")
        return view_func(request, *args, **kwargs)