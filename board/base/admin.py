from django.contrib import admin
from .models import Meeting, Genre,Game, Message, User
# Register your models here.

admin.site.register(User)
admin.site.register(Meeting)
admin.site.register(Genre)
admin.site.register(Game)
admin.site.register(Message)