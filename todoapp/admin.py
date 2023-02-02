from django.contrib import admin
from .models import Todo

# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "created_at")
    list_filter = ("status", )
    search_fields = ("name", )


admin.site.register(Todo, TodoAdmin)