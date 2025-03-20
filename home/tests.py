from django.test import TestCase
from django.contrib.auth.models import User
from .models import Animal, Comment

class AnimalModelTest(TestCase):
    
    def setUp(self):
        # Setup initial data for tests
        self.animal = Animal.objects.create(
            name="Lion",
            category="Land",
            section="Adults",
            description_kids="Lions are big cats that live in the wild.",
            description_adults="Lions are apex predators found primarily in sub-Saharan Africa.",
            image1="path/to/image1.jpg",
            image2="path/to/image2.jpg",
            image3="path/to/image3.jpg",
            audio="path/to/audio.mp3"
        )

    def test_animal_creation(self):
        # Check if the animal object is created correctly
        self.assertEqual(self.animal.name, "Lion")
        self.assertEqual(self.animal.category, "Land")
        self.assertEqual(self.animal.section, "Adults")
        self.assertEqual(self.animal.description_kids, "Lions are big cats that live in the wild.")
        self.assertEqual(self.animal.description_adults, "Lions are apex predators found primarily in sub-Saharan Africa.")

    def test_slug_generation(self):
        # Check if the slug is auto-generated
        self.assertEqual(self.animal.slug, "lion")

    def test_get_absolute_url(self):
        # Check if the get_absolute_url method returns the correct URL
        self.assertEqual(self.animal.get_absolute_url(), f"/animals/{self.animal.pk}/")

class CommentModelTest(TestCase):
    
    def setUp(self):
        # Setup initial data for tests
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.animal = Animal.objects.create(
            name="Tiger",
            category="Land",
            section="Adults",
            description_kids="Tigers are large cats with beautiful orange fur.",
            description_adults="Tigers are solitary apex predators found in Asia."
        )
        self.comment = Comment.objects.create(
            animal=self.animal,
            user=self.user,
            content="This is a great animal!",
        )

    def test_comment_creation(self):
        # Check if the comment object is created correctly
        self.assertEqual(self.comment.animal, self.animal)
        self.assertEqual(self.comment.user, self.user)
        self.assertEqual(self.comment.content, "This is a great animal!")

    def test_comment_timestamp(self):
        # Check if the comment's timestamp is generated correctly (it's automatically set to current time)
        self.assertIsNotNone(self.comment.created_at)

    def test_comment_str(self):
        # Check the string representation of the comment
        self.assertEqual(str(self.comment), f"{self.user.username} on {self.animal.name} ({self.comment.created_at.strftime('%Y-%m-%d')})")
