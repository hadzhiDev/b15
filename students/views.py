from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.core.paginator import Paginator

from students.models import Student, Group
from students.forms import StudentForm, StudentModelForm
from students.filters import StudentFilter


def main(request):
    students = Student.objects.all()
    
    search = request.GET.get('search')
    
    if search:
        students = Student.objects.filter(name__icontains=search)

    filter_set = StudentFilter(request.GET, queryset=students)

    page = request.GET.get('page', 1)
    limit = request.GET.get('limit', 2)

    paginator = Paginator(filter_set.qs, limit)
    students = paginator.get_page(page)

    return render(request, 'index.html', {
        'students': students,         
        'is_paginated': students.has_other_pages(),
        'search': search,
        'filter': filter_set
    })


def student_detail(request, id):
    student = Student.objects.get(id=id)
    print(student)
    return render(request, 'student_detail.html', {'student': student})


def student_update(request, id: int):
    student = get_object_or_404(Student, id=id)
    groups = Group.objects.all()

    if request.method == "POST":
        print(request.POST)
        print(request.FILES)

        form = StudentModelForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
    
    form = StudentModelForm(instance=student)

    return render(request, 'student_update.html', {'student': student, 'groups': groups, "form": form})


# def student_update(request, id: int):
#     groups = Group.objects.all()
#     # student = Student.objects.get(id=id)
#     student = get_object_or_404(Student, id=id)
#     # print(student)

#     if request.method == "POST":
#         student.name = request.POST.get("name")
#         student.last_name = request.POST.get("last_name")
#         student.age = request.POST.get("age")
#         student.phone_number = request.POST.get("phone_number")
#         student.email = request.POST.get("email")

#         group = Group.objects.get(id=int(request.POST.get("group")))
#         print(group)
#         student.group = group

#         student.save()

#         # print(new_name, new_last_name)
#         return redirect("/")


#     return render(request, 'student_update.html', {'student': student, "groups": groups},)


def create_student(request):
    # print(request.method)
    groups = Group.objects.all()
    form = StudentForm()
 
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            print("Post request")
            form_data = form.cleaned_data
            print(form_data)
            Student.objects.create(
                name=form_data.get("name"),
                last_name=form_data.get("last_name"),
                age=form_data.get("age"),           
                email=form_data.get("email"),
                phone_number=form_data.get("phone_number"),
                group=form_data.get("group"),
                avatar=form_data.get("avatar"),
                is_active=form_data.get("is_active"),
            )
            # form.save()
            print("worked")
            return redirect("/")
        # print("Post method!")
        # print(request.POST, type(request.POST))
        # name = request.POST.get("name")
        # last_name = request.POST.get("last_name")
        # age = request.POST.get("age", 21)
        # phone_number = request.POST.get("phone_number", "+996553999290")
        # email = request.POST.get("email", "hadzhi@gmail.com")
        # group = int(request.POST.get("group", 1))
        # avatar = request.FILES.get("avatar", None)
        # print(avatar)
        # print(group, type(group))

        # if avatar:
        #     newsImageSystem = FileSystemStorage('media/studentsAvatars/')
        #     newsImageSystem.save(avatar.name, avatar)

        # Student.objects.create(
        #     name=name,
        #     last_name=last_name,
        #     age=age,
        #     phone_number=phone_number,
        #     email=email,
        #     group_id=group,
        #     avatar=avatar
        # )

        # return redirect("/")

    return render(request, 'student_create.html', {"groups": groups, "form": form})


def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("/")


# CSRF / CSRF Token, 
# Template tags: extends; include; block, 
# Methods: get_object_or_404; redirect,
# Student delete view