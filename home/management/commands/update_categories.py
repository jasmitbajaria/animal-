from django.core.management.base import BaseCommand
from home.models import AnimalCategory, Animal

class Command(BaseCommand):
    help = 'Updates AnimalCategory section values based on related Animal records'

    def handle(self, *args, **options):
        count = 0
        for category in AnimalCategory.objects.all():
            # Find animals with this category type
            animal = Animal.objects.filter(category=category.type).first()
            if animal:
                # Set section from the animal's section
                category.section = animal.section.lower()
            else:
                # Default to scholars if no animals found
                category.section = 'scholars'
            category.save()
            count += 1
        
        self.stdout.write(self.style.SUCCESS(f'Successfully updated {count} categories'))