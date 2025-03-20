from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # 🏠 Home & Main Sections
    path('', views.home, name='home'),  # Home Page
    path('kids/', views.kids_section, name='kids_section'),  # Kids' Corner
    path('scholars/', views.scholars_section, name='scholars_section'),  # Scholars' Hub
    path('category/<slug:slug>/', views.kids_category, name='kids_category'),

    # 📂 Section Navigation (Fix for NoReverseMatch error)
    path('section/<str:section>/', views.section_view, name='section'),

    # 📂 Kids' Corner Categories
    path('kids/land/', views.kids_land, name='kids_land'),
    path('kids/water/', views.kids_water, name='kids_water'),
    path('kids/flying/', views.kids_flying, name='kids_flying'),

    # 📂 Scholars' Hub Categories
    path('scholars/aerial/', views.scholars_aerial, name='scholars_aerial'),
    path('scholars/aquatic/', views.scholars_aquatic, name='scholars_aquatic'),
    path('scholars/terrestrial/', views.scholars_terrestrial, name='scholars_terrestrial'),

    # 🦁 Animal Encyclopedia Pages (Without API)
    path('animal/<int:pk>/', views.animal_detail, name='animal_detail'),

    # 📂 Miscellaneous Pages
    path('categories/', views.categories_view, name='categories'),
    path('search/', views.search_animals, name='search'),
    path('comment/<int:animal_id>/', views.add_comment, name='add_comment'),
    path('toggle_dark_mode/', views.toggle_dark_mode, name='toggle_dark_mode'),

    # 🔑 Authentication URLs
    path('login/', views.custom_login, name='login'),  # Custom login view
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),  # Logout with redirection
    path('register/', views.register, name='register'),
]

# 🖼️ Serve Static & Media Files (Only in Development)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
