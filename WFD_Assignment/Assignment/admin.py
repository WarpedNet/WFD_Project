from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(UserModel)
admin.site.register(Customer)
admin.site.register(Insurance_Provider)
admin.site.register(Law_Firm)
admin.site.register(Government)
admin.site.register(Insurance)
admin.site.register(Claims)
admin.site.register(Purchase_Order)