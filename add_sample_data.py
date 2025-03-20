import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'animal_encyclopedia.settings')
django.setup()

from django.core.management.base import BaseCommand
from home.models import Animal
from django.utils.text import slugify
import random

def create_unique_slug(name, model_class):
    base_slug = slugify(name)
    slug = base_slug
    counter = 1
    while model_class.objects.filter(slug=slug).exists():
        slug = f"{base_slug}-{counter}"
        counter += 1
    return slug

# Sample data for both kids and scholars sections
ANIMALS = [
    {
        'name': 'Golden Eagle',
        'scientific_name': 'Aquila chrysaetos',
        'category': 'air',
        'description_kids': """
        Meet the amazing Golden Eagle! 🦅 
        
        I'm one of the biggest and strongest birds in the world! My wings are so wide, they could stretch across your bedroom - that's about 7-8 feet wide! I have super sharp eyes that can spot tiny animals from very far away, like a rabbit from a mile up in the sky.

        My beautiful golden-brown feathers help me blend in with the mountains where I live. I can fly super fast - faster than a car on the highway! And guess what? I build my nest way up high in tall trees or on cliffs, and I use the same nest for many years, making it bigger and cozier each time.

        Fun fact: I can carry things that are almost as heavy as a small dog! But don't worry, I mostly catch rabbits, squirrels, and other small animals.
        """,
        'description_scholars': """
        The Golden Eagle (Aquila chrysaetos) is one of the most formidable aerial predators in the Northern Hemisphere. This magnificent raptor exhibits remarkable adaptations for hunting and survival across diverse terrain.

        Morphology:
        - Wingspan: 1.8-2.3 meters (5.9-7.5 feet)
        - Body length: 66-102 cm (26-40 inches)
        - Sexual dimorphism: Females notably larger than males
        - Distinctive dark brown plumage with golden-buff crown and nape

        Visual Capabilities:
        - Exceptional visual acuity, estimated at 8x human vision
        - Binocular vision field of 30°
        - Specialized foveal regions for precise depth perception
        
        Hunting Behavior:
        The species employs various hunting strategies, including:
        1. High-altitude soaring and scanning
        2. Contour hunting along hillsides
        3. Direct pursuit of prey
        4. Tandem hunting by paired adults

        Population dynamics studies indicate territorial fidelity spanning multiple generations, with pairs maintaining several alternate nest sites within their territory.
        """,
        'fun_facts_kids': """
        🦅 Did you know?
        - My eyesight is so good, I can see a rabbit from a mile away!
        - I can fly as fast as a car on the highway - up to 200 miles per hour when diving!
        - My nest is HUGE - it can be as big as a car!
        - I can use tools to hunt - I've been seen dropping rocks on eggs to break them!
        - I'm so strong, I can lift things that weigh as much as a small dog!
        """,
        'habitat_info': """
        Habitat Distribution and Preferences:
        
        The Golden Eagle occupies diverse habitats across the Holarctic region, demonstrating remarkable adaptability to various environmental conditions. Primary habitat requirements include:

        1. Nesting Territory:
        - Cliff faces or large trees in open or semi-open areas
        - Elevation range: sea level to 3,000+ meters
        - Preference for areas with minimal human disturbance

        2. Hunting Grounds:
        - Open terrain for effective hunting
        - Mixed vegetation providing cover for prey species
        - Adequate prey density to support territorial pairs

        3. Geographical Distribution:
        - North America: From Alaska to Mexico
        - Eurasia: Scotland to Japan
        - Limited presence in North Africa

        Habitat selection is strongly influenced by:
        - Prey availability
        - Suitable nesting sites
        - Thermal updrafts for efficient soaring
        - Human activity levels
        """,
        'behavior_info': """
        Behavioral Ecology:

        1. Hunting Strategies:
        - Primary hunting periods: Early morning and late afternoon
        - Utilizes both solo and cooperative hunting techniques
        - Employs various attack strategies based on prey and terrain

        2. Social Structure:
        - Maintains strong monogamous pair bonds
        - Territorial defense throughout the year
        - Complex aerial displays during courtship

        3. Nesting Behavior:
        - Constructs multiple nests within territory
        - Annual nest maintenance and expansion
        - Both parents participate in:
          * Nest construction
          * Incubation (43-45 days)
          * Chick rearing (70-80 days)

        4. Migration Patterns:
        - Varies by population and latitude
        - Partial migration in some regions
        - Year-round residents in others
        """,
        'conservation_status': """
        Conservation Status and Threats:

        IUCN Red List Status: Least Concern
        Population Trend: Stable globally, with regional variations

        Current Threats:
        1. Habitat Loss:
        - Urban expansion
        - Agricultural intensification
        - Energy infrastructure development

        2. Human Persecution:
        - Historical shooting and trapping
        - Continued illegal poisoning in some regions
        - Collisions with wind turbines and power lines

        3. Environmental Factors:
        - Climate change impacts on prey availability
        - Habitat fragmentation
        - Reduced nesting site availability

        Conservation Measures:
        1. Legal Protection:
        - Protected under various international agreements
        - Strict regulations on possession and trade
        - Designated protected areas

        2. Recovery Programs:
        - Habitat restoration projects
        - Artificial nest site creation
        - Public education initiatives

        3. Research and Monitoring:
        - Population surveys
        - Tracking studies
        - Breeding success monitoring
        """,
        'image1': 'images/golden-eagle-soaring.jpg',
        'image2': 'images/golden-eagle-nest.jpg',
        'image3': 'images/golden-eagle-hunting.jpg',
        'image1_caption': 'Adult Golden Eagle soaring, displaying characteristic wing posture and plumage patterns',
        'image2_caption': 'Nest site on a cliff face, showing typical placement and structure',
        'image3_caption': 'Hunting sequence demonstrating aerial pursuit capabilities',
        'audio': 'audio/golden-eagle-call.mp3',
        'audio_description': 'Territorial call of an adult Golden Eagle, recorded during breeding season'
    },
    # Add more animals here...
]

def add_sample_data():
    for animal_data in ANIMALS:
        try:
            # Create unique slug
            slug = create_unique_slug(animal_data['name'], Animal)
            
            # Create or update the animal
            animal, created = Animal.objects.update_or_create(
                name=animal_data['name'],
                defaults={
                    'slug': slug,
                    'scientific_name': animal_data.get('scientific_name', ''),
                    'category': animal_data['category'],
                    'description_kids': animal_data['description_kids'],
                    'description_scholars': animal_data['description_scholars'],
                    'fun_facts_kids': animal_data['fun_facts_kids'],
                    'habitat_info': animal_data['habitat_info'],
                    'behavior_info': animal_data['behavior_info'],
                    'conservation_status': animal_data['conservation_status'],
                    'image1': animal_data.get('image1', ''),
                    'image2': animal_data.get('image2', ''),
                    'image3': animal_data.get('image3', ''),
                    'image1_caption': animal_data.get('image1_caption', ''),
                    'image2_caption': animal_data.get('image2_caption', ''),
                    'image3_caption': animal_data.get('image3_caption', ''),
                    'audio': animal_data.get('audio', ''),
                    'audio_description': animal_data.get('audio_description', '')
                }
            )
            print(f"{'Created' if created else 'Updated'} {animal.name}")
        except Exception as e:
            print(f"Error adding {animal_data['name']}: {str(e)}")

if __name__ == '__main__':
    add_sample_data()
