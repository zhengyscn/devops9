from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):

    list_display=('username', 'name', 'phone',)



# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)