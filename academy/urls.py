from django.urls import path

from .views import StudentCreateView, StudentDetailView, StudentListView, MainTemplateView, AboutTemplateView, StudentListFilter


urlpatterns = [
    path('', StudentListFilter.as_view(), name="main"),
    path('about/', AboutTemplateView.as_view(), name="about"),
    path('students/create/', StudentCreateView.as_view(), name="create_student"),
    path('students/<int:id>', StudentListView.as_view(), name="student_detail"),
    # path('', StudentListView.as_view(), name="main")
]