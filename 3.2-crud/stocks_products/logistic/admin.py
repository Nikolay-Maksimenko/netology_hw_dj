from django.contrib import admin

from logistic.models import Stock, StockProduct


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    pass
# Register your models here.

@admin.register(StockProduct)
class StockProductAdmin(admin.ModelAdmin):
    pass
