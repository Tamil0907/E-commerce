from django.contrib import admin

from .models import *

# class catagory_admin(admin.ModelAdmin):
#     list_display=["name,image,discription"]
#     admin.site.register(catagory,catagory_admin)

admin.site.register(Catagory)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Favourite)