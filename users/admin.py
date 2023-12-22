from django.contrib import admin
from users.models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'is_staff', 'is_active', 'is_superuser')

admin.site.register(User, UserAdmin)
