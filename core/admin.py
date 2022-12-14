from django.contrib import admin
from .models import User, Task, Profile


admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Task)

