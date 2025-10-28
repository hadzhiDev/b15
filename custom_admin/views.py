from django.shortcuts import render, HttpResponse

from django.views.generic import DetailView, CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from academy.models import Student
from custom_admin.forms import StudentModelForm


# def only_admins(view_func):
#     def wrapper(request, *args, **kwargs):
#         if not request.user.is_authenticated or not request.user.is_staff:
#             return HttpResponse("Access denied", status=403)
#         return view_func(request, *args, **kwargs)
#     return wrapper


@login_required
def admin_main(request):
    return render(request, 'custom_admin/main.html')


class MainAdminView(TemplateView):
    template_name = 'custom_admin/main.html'


class StudentDetailView(DetailView):
    model = Student
    template_name = 'custom_admin/student_detail.html'
    context_object_name = 'student'  


class StudentCreateView(CreateView):
    model = Student
    template_name = 'custom_admin/student_create.html'
    form_class = StudentModelForm
