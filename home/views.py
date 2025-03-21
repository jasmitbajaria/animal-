from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import Paginator
# Import your models here:
from .models import Animal, AnimalCategory, UserContribution, Rating, Favorite

@login_required
def add_comment(request, animal_id):
    if request.method == "POST":
        content = request.POST.get("content", "").strip()
        if content:
            animal = get_object_or_404(Animal, pk=animal_id)
            UserContribution.objects.create(
                user=request.user,
                animal=animal,
                fact=content  # We use 'fact' field from UserContribution model
            )
            messages.success(request, "Comment added successfully!")
        else:
            messages.error(request, "Comment cannot be empty.")
    return redirect("animal_detail", pk=animal_id)


# 🏠 Home page view
def home(request):
    categories = AnimalCategory.objects.all()
    # Using rating for featured animals
    featured_animals = Animal.objects.order_by('-id')[:6]  # Using id instead of rating as a fallback
    
    context = {
        'categories': categories,
        'featured_animals': featured_animals,
        'is_home': True,
        'section': 'scholars'  # Default section
    }
    return render(request, 'home/home.html', context)

# 🔑 Custom login view with age-based redirection
def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        age = request.POST.get('age')

        if not age or not age.isdigit() or int(age) < 0:
            messages.error(request, "Invalid age entered. Please enter a valid number.")
            return redirect('login')

        age = int(age)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['age'] = age  # Store age in session
            return redirect('kids_section' if age < 8 else 'home')  # Redirect based on age
        else:
            messages.error(request, "Invalid credentials. Please check your username and password.")
    
    return render(request, 'home/login.html')

# Custom logout view
def custom_logout(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('home')

# 📚 Generic section view for both kids and scholars
def section_view(request, section_name):
    section_name = section_name.lower()
    if section_name not in ['kids', 'scholars']:
        return redirect('home')
        
    categories = AnimalCategory.objects.filter(section=section_name)
    # Using top rated animals instead of featured
    featured_animals = Animal.objects.filter(section=section_name.capitalize()).order_by('-rating')[:4]
    
    context = {
        'section': section_name,
        'categories': categories,
        'featured_animals': featured_animals
    }
    return render(request, f'home/{section_name}_section.html', context)

# For backward compatibility
def kids_section(request):
    return section_view(request, 'kids')

def scholars_section(request):
    return section_view(request, 'scholars')

# 📂 Dynamic category view for any section
def category_view(request, section_name, slug):
    section_name = section_name.lower()
    category = get_object_or_404(AnimalCategory, slug=slug, section=section_name)
    animals = Animal.objects.filter(category=category.type, section=section_name.capitalize())
    
    # Add pagination
    paginator = Paginator(animals, 12)  # Show 12 animals per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'section': section_name,
        'category': category,
        'animals': page_obj,
        'total_count': animals.count()
    }
    return render(request, f'home/category_view.html', context)

# For backward compatibility
def kids_category(request, slug):
    return category_view(request, 'kids', slug)

# 🦁 Animal detail view (No API, all data rendered in template)
def animal_detail(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    section = animal.section.lower()
    
    # Get related animals (same category)
    related_animals = Animal.objects.filter(
        category=animal.category, 
        section=animal.section
    ).exclude(pk=animal.pk)[:4]
    
    context = {
        'animal': animal,
        'related_animals': related_animals,
        'section': section
    }
    return render(request, 'home/animal_detail.html', context)

# 🔍 Search functionality with pagination
def search_animals(request):
    query = request.GET.get('q', '').strip()
    section = request.GET.get('section', '').lower()
    category = request.GET.get('category', '')
    
    # Start with all animals
    animals = Animal.objects.all()
    
    # Apply filters
    if query:
        animals = animals.filter(name__icontains=query)
    if section in ['kids', 'scholars']:
        animals = animals.filter(section=section.capitalize())
    if category:
        animals = animals.filter(category=category)
        
    if query and not animals.exists():
        messages.info(request, f"No animals found matching '{query}'.")

    paginator = Paginator(animals, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get all categories for filter dropdown
    categories = AnimalCategory.objects.all()

    context = {
        'page_obj': page_obj, 
        'query': query,
        'section': section,
        'category': category,
        'categories': categories,
        'total_count': animals.count()
    }
    return render(request, 'home/search_results.html', context)

# 💬 Add comment for an animal
@login_required
def add_comment(request, animal_id):
    if request.method == "POST":
        content = request.POST.get("content", "").strip()
        if content:
            animal = get_object_or_404(Animal, pk=animal_id)
            UserContribution.objects.create(
                user=request.user,
                animal=animal,
                fact=content  # Notice we use 'fact' field, not 'content'
            )
            messages.success(request, "Comment added successfully!")
        else:
            messages.error(request, "Comment cannot be empty.")
    return redirect("animal_detail", pk=animal_id)
# 🌗 Toggle dark mode with session storage
def toggle_dark_mode(request):
    dark_mode = not request.session.get('dark_mode', False)
    request.session['dark_mode'] = dark_mode
    return redirect(request.META.get('HTTP_REFERER', 'home'))

# 🔑 User registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login')
        messages.error(request, "Error in registration. Please check your inputs.")
    else:
        form = UserCreationForm()
    return render(request, 'home/register.html', {'form': form})
# Add this function to your views.py
def toggle_dark_mode(request):
    dark_mode = not request.session.get('dark_mode', False)
    request.session['dark_mode'] = dark_mode
    return redirect(request.META.get('HTTP_REFERER', 'home'))

# 📂 View for all animal categories (Shows all categories at once)
def categories_view(request):
    sections = {}
    
    # Get all distinct sections
    distinct_sections = AnimalCategory.objects.values_list('section', flat=True).distinct()
    
    # For each section, get its categories
    for section in distinct_sections:
        # Skip empty sections
        if not section:
            continue
            
        section_categories = AnimalCategory.objects.filter(section=section)
        section_dict = {}
        
        # For each category, get its animals
        for category in section_categories:
            animals = Animal.objects.filter(category=category.type, section=section.capitalize())
            section_dict[category.name] = animals
        
        if section_dict:  # Only add non-empty sections
            sections[section] = section_dict
    
    # If we have no sections, add default ones
    if not sections:
        sections = {
            'kids': {},
            'scholars': {}
        }
    
    return render(request, 'home/categories.html', {'sections': sections})

# Add these view functions for backward compatibility 

def scholars_aerial(request):
    # Find the slug for the aerial category in scholars section
    category = AnimalCategory.objects.filter(section='scholars', type='aerial').first()
    if category:
        return category_view(request, 'scholars', category.slug)
    else:
        # Fallback to scholars section if category not found
        return redirect('scholars_section')

def scholars_terrestrial(request):
    category = AnimalCategory.objects.filter(section='scholars', type='terrestrial').first()
    if category:
        return category_view(request, 'scholars', category.slug)
    else:
        return redirect('scholars_section')

def scholars_aquatic(request):
    category = AnimalCategory.objects.filter(section='scholars', type='aquatic').first()
    if category:
        return category_view(request, 'scholars', category.slug)
    else:
        return redirect('scholars_section')