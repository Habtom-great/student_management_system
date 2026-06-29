from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Count, Q

from .models import Instructor


# LIST + SEARCH + PAGINATION
def instructor_list(request):

    query = request.GET.get("q", "")

    instructors = Instructor.objects.annotate(
        course_count=Count("courses")
    ).order_by("-id")

    if query:
        instructors = instructors.filter(
            Q(full_name__icontains=query) |
            Q(title__icontains=query)
        )

    paginator = Paginator(instructors, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "instructors/instructor_list.html", {
        "page_obj": page_obj,
        "query": query
    })

# Add Page

def add_instructor(request):

    if request.method == "POST":
        Instructor.objects.create(
            full_name=request.POST.get("full_name"),
            title=request.POST.get("title"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            bio=request.POST.get("bio"),
            photo=request.FILES.get("photo")
        )

        return redirect("instructors:list")

    return render(request, "instructors/instructor_form.html")
# DETAIL PAGE
def instructor_detail(request, pk):
    instructor = get_object_or_404(Instructor, pk=pk)

    courses = instructor.courses.all()

    return render(request, "instructors/instructor_detail.html", {
        "instructor": instructor,
        "courses": courses
    })


# EDIT
def edit_instructor(request, pk):
    instructor = get_object_or_404(Instructor, pk=pk)

    if request.method == "POST":
        instructor.full_name = request.POST.get("full_name")
        instructor.title = request.POST.get("title")
        instructor.phone = request.POST.get("phone")
        instructor.email = request.POST.get("email")
        instructor.bio = request.POST.get("bio")

        if request.FILES.get("photo"):
            instructor.photo = request.FILES.get("photo")

        instructor.save()
        return redirect("instructors:detail", pk=instructor.pk)

    return render(request, "instructors/edit_instructor.html", {
        "instructor": instructor
    })


# DELETE
def delete_instructor(request, pk):
    instructor = get_object_or_404(Instructor, pk=pk)

    if request.method == "POST":
        instructor.delete()
        return redirect("instructors:list")

    return render(request, "instructors/delete_instructor.html", {
        "instructor": instructor
    })