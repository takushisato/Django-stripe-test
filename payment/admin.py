from django.contrib import admin
from .models import Product, Price, Transaction  # models.pyで作成したマスタを読込

class PriceInlineAdmin(admin.TabularInline):
    model = Price
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    inlines = [PriceInlineAdmin]

# 管理画面に商品マスタと価格マスタを表示
admin.site.register(Product, ProductAdmin)
admin.site.register(Price)
admin.site.register(Transaction)