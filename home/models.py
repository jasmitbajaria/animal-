from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    bio = models.TextField(blank=True, help_text="A short bio about the user")
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # auto_now_add should be fine
    updated_at = models.DateTimeField(auto_now=True)  # auto_now should be fine

    def can_access_scholars_hub(self):
        return self.age >= 8

    def __str__(self):
        return f"{self.user.username} - Age: {self.age}"

class Animal(models.Model):
    CATEGORY_CHOICES = [
        ('air', 'Air'), ('water', 'Water'), ('land', 'Land'), 
        ('aerial', 'Aerial'), ('terrestrial', 'Terrestrial'), ('aquatic', 'Aquatic'),
    ]
    
    SECTION_CHOICES = [('Kids', 'Kids'), ('Scholars', 'Scholars')]
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    section = models.CharField(max_length=10, choices=SECTION_CHOICES)
    
    image1 = models.ImageField(upload_to='animals/', blank=True, null=True)
    image2 = models.ImageField(upload_to='animals/', blank=True, null=True)
    image3 = models.ImageField(upload_to='animals/', blank=True, null=True)
    
    description_kids = models.TextField(blank=True, help_text="Kid-friendly description")
    description_adults = models.TextField(blank=True, help_text="Scholarly description")
    fun_facts_kids = models.TextField(blank=True, help_text="Fun facts for kids")
    habitat_info = models.TextField(blank=True)
    behavior_info = models.TextField(blank=True)
    conservation_status = models.TextField(blank=True)
    
    audio = models.FileField(upload_to='animal_sounds/', blank=True, null=True)
    audio_description = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # auto_now_add should be fine
    updated_at = models.DateTimeField(auto_now=True)  # auto_now should be fine

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            unique_slug = base_slug
            counter = 1
            while Animal.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
        
class AnimalCategory(models.Model):
    CATEGORY_CHOICES = [
        ('flying', 'Flying Animals'),
        ('land', 'Land Animals'),
        ('water', 'Water Animals'),
    ]
    
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='category_images/')
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'animal')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} favorited {self.animal.name}"

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1 to 5 stars
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} rated {self.animal.name} {self.rating} stars"

class Quiz(models.Model):
    question = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.question

class UserContribution(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='contributions')
    fact = models.TextField()
    image = models.ImageField(upload_to='contributions/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} contributed to {self.animal.name}"

class Achievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.title}"
