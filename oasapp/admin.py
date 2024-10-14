from django.contrib import admin
from .models import Enquiry , AdminLogin,tbl_session,tbl_course,Student
# Register your models here.

admin.site.register(Enquiry)
admin.site.register(AdminLogin)
admin.site.register(tbl_session)
admin.site.register(tbl_course)
admin.site.register(Student)
