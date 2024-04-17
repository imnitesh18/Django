from django.contrib import admin

from .models import Cookie, Customers, Emp,Blogpost, Faculty, Section
# Register your models here.
admin.site.register(Emp)
admin.site.register(Blogpost)
admin.site.register(Faculty)
admin.site.register(Customers)
admin.site.register(Section)
admin.site.register(Cookie)



