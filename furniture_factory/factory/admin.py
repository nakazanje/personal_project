from django.contrib import admin
from .models import Workshop, Worker, Order

@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('name', 'manager', 'worker_count')
    search_fields = ('name',)

    def worker_count(self, obj):
        return obj.workers.count()
    worker_count.short_description = "Количество рабочих"

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position', 'workshop')
    list_filter = ('workshop',)
    search_fields = ('first_name', 'last_name')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at')
    list_filter = ('status', 'workshops')
    search_fields = ('title',)
