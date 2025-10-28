from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


from .models import Category, News


admin.site.site_header = "Админ-панель сайта Prolab Academy"
admin.site.site_title = "Prolab Academy Admin"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class NewsAdminForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            'content': CKEditorUploadingWidget(),
        }


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subtitle', 'created_at', 'category')
    search_fields = ('title', 'subtitle', 'content')
    list_filter = ('created_at', 'category')
    form = NewsAdminForm


# admin.site.register(Category, CategoryAdmin)
# admin.site.register(News, NewsAdmin)
