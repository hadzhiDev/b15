from django.urls import path

from .views import MainTemplateView, AboutTemplateView, StudentListFilter, set_cookie_view, get_cookie_view, visit_counter


urlpatterns = [
    path('', MainTemplateView.as_view(), name="main"),
    path('about/', AboutTemplateView.as_view(), name="about"),
    path('set-cookie-test/', set_cookie_view),
    path('get-cookie-test/', get_cookie_view),
    path('visit-counter-page/', visit_counter)
    # path('', StudentListView.as_view(), name="main")
]