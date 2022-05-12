from django.contrib import admin

from .models import OrderProduct, Product, Category, SubCategory


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'sub_category',
                    'price', 'quantity', 'vendor', 'price', 'modified', 'create']

# Register your models here.


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(OrderProduct)
