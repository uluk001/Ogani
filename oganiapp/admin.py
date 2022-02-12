from django.contrib import admin
from oganiapp.models import Contact, Category, FoodCard



# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ("email", "sent_at")


admin.site.register(Contact,  ContactAdmin)
admin.site.register(Category)
admin.site.register(FoodCard)
