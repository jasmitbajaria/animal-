import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'animal_encyclopedia.settings')
django.setup()

from home.models import Animal
from django.core.files import File

# Sample animal data
ANIMALS = [
    # Air Animals
    {
        'name': 'Eagle',
        'category': 'air',
        'section': 'Kids',
        'description_kids': 'Eagles are amazing birds that can fly very high in the sky! They have super-sharp eyes that help them spot tiny animals from far away. Eagles build big nests called eyries at the top of tall trees or cliffs.',
        'description_adults': 'Eagles are large, powerfully built birds of prey with heavy heads and beaks. They possess exceptionally keen eyesight which enables them to spot potential prey from a very long distance. Their wingspan can reach up to 7.5 feet, making them one of the largest birds of prey.',
        'image1': 'media/animals/New folder/eagle.jpg',
    },
    {
        'name': 'Penguin',
        'category': 'air',
        'section': 'Kids',
        'description_kids': 'Penguins are funny birds that waddle when they walk! They can\'t fly in the air, but they\'re amazing swimmers. They love to slide on their bellies in the snow!',
        'description_adults': 'Penguins are aquatic flightless birds that live almost exclusively in the Southern Hemisphere. They are highly adapted for life in the water, with countershaded dark and white plumage and flippers for swimming. They spend roughly half of their lives on land and half in the oceans.',
        'image1': 'media/animals/New folder/10 Adorable Photos of Baby Penguins.jpg',
    },

    # Water Animals
    {
        'name': 'Dolphin',
        'category': 'water',
        'section': 'Kids',
        'description_kids': 'Dolphins are super smart and friendly sea animals! They love to play and jump out of the water. They make special clicking sounds to talk to each other.',
        'description_adults': 'Dolphins are highly intelligent marine mammals known for their complex social structures and sophisticated echolocation abilities. They can produce high-pitched sounds that allow them to determine the location, size, and shape of nearby objects.',
        'image1': 'media/animals/New folder/dolphin.jpg',
    },

    # Land Animals
    {
        'name': 'Elephant',
        'category': 'land',
        'section': 'Kids',
        'description_kids': 'Elephants are the biggest animals that live on land! They have long noses called trunks that they use like hands. Elephants love to play in the water and mud!',
        'description_adults': 'Elephants are the largest existing land animals and are known for their intelligence, memory, and complex social behavior. They are highly adaptable and can be found in different habitats ranging from savannas to forests. Their trunks contain over 40,000 muscles and are used for breathing, grasping objects, trumpeting, drinking, and smelling.',
        'image1': 'media/animals/New folder/25 Fun And Amazing Facts About Elephants For Kids.jpg',
    },
    {
        'name': 'Wolf',
        'category': 'land',
        'section': 'Adults',
        'description_kids': 'Wolves are wild dogs that live in families called packs. They work together to hunt and take care of their puppies. They can howl very loudly!',
        'description_adults': 'Wolves are apex predators crucial to maintaining ecosystem balance. They exhibit complex social hierarchies within their packs, sophisticated hunting strategies, and remarkable endurance. Their howling serves multiple purposes including territory marking, pack assembly, and social bonding.',
        'image1': 'media/animals/New folder/25 Interesting And Informative Wolf Facts For Kids.jpg',
    },
]

def add_sample_animals():
    for animal_data in ANIMALS:
        try:
            # Check if animal already exists
            if not Animal.objects.filter(name=animal_data['name']).exists():
                animal = Animal(
                    name=animal_data['name'],
                    category=animal_data['category'],
                    section=animal_data['section'],
                    description_kids=animal_data['description_kids'],
                    description_adults=animal_data['description_adults']
                )
                
                # Handle image file
                image_path = animal_data['image1']
                if os.path.exists(image_path):
                    with open(image_path, 'rb') as img_file:
                        animal.image1.save(
                            os.path.basename(image_path),
                            File(img_file),
                            save=True
                        )
                animal.save()
                print(f"Added {animal.name}")
            else:
                print(f"Animal {animal_data['name']} already exists")
        except Exception as e:
            print(f"Error adding {animal_data['name']}: {str(e)}")

if __name__ == '__main__':
    print("Adding sample animals...")
    add_sample_animals()
    print("Done!")
