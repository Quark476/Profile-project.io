from django.contrib import admin
from .models import Portfolio

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['get_full_name', 'email', 'school', 'education_level', 'created_at']
    list_filter = ['education_level', 'created_at']
    search_fields = ['last_name', 'first_name', 'email', 'school']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = [
        ('Основная информация', {
            'fields': [
                'last_name', 'first_name', 'email', 'phone'
            ]
        }),
        ('Образование', {
            'fields': [
                'school', 'education_level', 'specialization'
            ]
        }),
        ('Опыт и навыки', {
            'fields': [
                'experience', 'hobbies', 'skills', 'achievements', 'goals'
            ]
        }),
        ('Метаданные', {
            'fields': [
                'created_at', 'updated_at'
            ],
            'classes': ['collapse']
        }),
    ]
    
    def get_full_name(self, obj):
        return obj.get_full_name()
    get_full_name.short_description = 'ФИО'