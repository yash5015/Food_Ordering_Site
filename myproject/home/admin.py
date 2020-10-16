from django.contrib import admin

# Register your models here.
from.models import FoodItem,Contact,Order
admin.site.register(FoodItem)
admin.site.register(Contact)
admin.site.register(Order)

class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('Item_name','category','quantity','price')
    list_filter=('category')
    search_fields = ('Item_name','category')
    # prepopulated_fields = ('category')

