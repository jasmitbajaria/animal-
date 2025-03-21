from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.custom_login, name='login'),
    path('register/', views.register, name='register'),
    path('toggle-dark-mode/', views.toggle_dark_mode, name='toggle_dark_mode'),
    path('logout/', views.custom_logout, name='logout'),
    
    # Animal detail view - MOVE THIS BEFORE THE DYNAMIC SECTION PATTERNS
    path('animal/<int:pk>/', views.animal_detail, name='animal_detail'),
    path('animal/<int:animal_id>/comment/', views.add_comment, name='add_comment'),
    
    # Dynamic section and category views
    path('<str:section_name>/', views.section_view, name='section_view'),
    path('<str:section_name>/<slug:slug>/', views.category_view, name='category_view'),
    
    # Search functionality
    path('search/', views.search_animals, name='search_animals'),
    path('categories/', views.categories_view, name='categories_view'),
    
    # Legacy routes for backward compatibility
    path('kids/', views.kids_section, name='kids_section'),
    path('scholars/', views.scholars_section, name='scholars_section'),
    path('kids/<slug:slug>/', views.kids_category, name='kids_category'),
]