from django.contrib import admin
from .models import (
    Animal, AnimalCategory, UserProfile, Favorite,
    Rating, Quiz, UserContribution, Achievement
)

# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'created_at')
    search_fields = ('user__username',)

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'section')
    list_filter = ('category', 'section')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

@admin.register(AnimalCategory)
class AnimalCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'section')
    list_filter = ('section',)
    search_fields = ('name', 'type')
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        (None, {
            'fields': ('name', 'type', 'slug', 'description')
        }),
    )

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'animal', 'created_at')  # Added id to show the unique ID for Favorites
    search_fields = ('user__username', 'animal__name')

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'correct_option', 'created_at')  # Added id to show unique ID for Quiz
    search_fields = ('question',)

admin.site.register(Rating)
admin.site.register(UserContribution)
admin.site.register(Achievement)
