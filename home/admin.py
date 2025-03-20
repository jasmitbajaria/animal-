from django.contrib import admin
from .models import AnimalCategory, UserProfile, Animal, Favorite, Quiz

# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'created_at')
    search_fields = ('user__username',)

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'section', 'slug', 'created_at')  # Added id for unique tracking
    list_filter = ('category', 'section')
    search_fields = ('name', 'description_kids', 'description_adults')

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'category', 'section')  # Added slug here
        }),
        ('Images', {
            'fields': ('image1', 'image2', 'image3'),
            'description': 'Upload up to 3 high-quality images of the animal'
        }),
        ('Audio', {
            'fields': ('audio', 'audio_description'),
            'description': 'Upload animal sounds with description'
        }),
        ('Kids Content', {
            'fields': ('description_kids', 'fun_facts_kids'),
            'description': 'Content written for children (3rd-4th grade level)'
        }),
        ('Scholar Content', {
            'fields': ('description_adults', 'habitat_info', 'behavior_info', 'conservation_status'),
            'description': 'Detailed scientific information'
        })
    )

    prepopulated_fields = {"slug": ("name",)}  # Auto-generates slug from name
@admin.register(AnimalCategory)
class AnimalCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'slug')
    list_filter = ('type',)
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        (None, {
            'fields': ('name', 'type', 'slug', 'image', 'description')
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
