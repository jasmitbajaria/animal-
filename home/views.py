from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Animal

# 🏠 Home page view
def home(request):
    return render(request, 'home/home.html')

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

def kids_category(request, slug):
    category = get_object_or_404(AnimalCategory, slug=slug)
    animals = Animal.objects.filter(section='kids', category=category.type)
    context = {
        'category': category,
        'animals': animals
    }
    return render(request, 'home/kids_category.html', context)

from .models import AnimalCategory

def kids_section(request):
    categories = AnimalCategory.objects.all()
    context = {'categories': categories}
    return render(request, 'home/kids_section.html', context)

# 📚 Scholars section view
def scholars_section(request):
    return render(request, 'home/scholars_section.html')

# 📂 Section navigation view
def section_view(request, section):
    if section.lower() == 'kids':
        return redirect('kids_section')
    elif section.lower() == 'scholars':
        return redirect('scholars_section')
    else:
        return redirect('home')

# 📂 Direct category views for Kids' Corner
def kids_land(request):
    animals = Animal.objects.filter(category='land', section='Kids')
    return render(request, 'home/kids_land.html', {'animals': animals})

def kids_water(request):
    animals = Animal.objects.filter(category='water', section='Kids')
    return render(request, 'home/kids_water.html', {'animals': animals})

def kids_flying(request):
    animals = Animal.objects.filter(category='air', section='Kids')
    return render(request, 'home/kids_flying.html', {'animals': animals})

# 📂 Direct category views for Scholars' Hub
def scholars_aerial(request):
    animals = Animal.objects.filter(category='aerial', section='Scholars')
    return render(request, 'home/scholars_aerial.html', {'animals': animals})

def scholars_aquatic(request):
    animals = Animal.objects.filter(category='aquatic', section='Scholars')
    return render(request, 'home/scholars_aquatic.html', {'animals': animals})

def scholars_terrestrial(request):
    animals = Animal.objects.filter(category='terrestrial', section='Scholars')
    return render(request, 'home/scholars_terrestrial.html', {'animals': animals})

# 🦁 Animal detail view (No API, all data rendered in template)
def animal_detail(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    return render(request, 'home/animal_detail.html', {'animal': animal})

# 🔍 Search functionality with pagination
def search_animals(request):
    query = request.GET.get('q', '').strip()
    animals = Animal.objects.filter(name__icontains=query) if query else []

    if query and not animals.exists():
        messages.info(request, f"No animals found matching '{query}'.")

    paginator = Paginator(animals, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home/search_results.html', {'page_obj': page_obj, 'query': query})

# 💬 Add comment for an animal
@login_required
def add_comment(request, animal_id):
    if request.method == "POST":
        content = request.POST.get("content", "").strip()
        if content:
            animal = get_object_or_404(Animal, pk=animal_id)
            animal.comments.create(user=request.user, content=content)
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
            form.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login')
        messages.error(request, "Error in registration. Please check your inputs.")
    else:
        form = UserCreationForm()
    return render(request, 'home/register.html', {'form': form})

# 📂 View for animal categories (Shows all categories at once)
def categories_view(request):
    sections = {
        'kids': {
            'Flying': Animal.objects.filter(category='air', section='Kids'),
            'Water': Animal.objects.filter(category='water', section='Kids'),
            'Land': Animal.objects.filter(category='land', section='Kids'),
        },
        'scholars': {
            'Aerial': Animal.objects.filter(category='aerial', section='Scholars'),
            'Aquatic': Animal.objects.filter(category='aquatic', section='Scholars'),
            'Terrestrial': Animal.objects.filter(category='terrestrial', section='Scholars'),
        }
    }
    return render(request, 'home/categories.html', {'sections': sections})
