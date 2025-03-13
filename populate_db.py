import os
import django
from faker import Faker
import random
from events.models import Event, Participant, Category

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_management.settings')
django.setup()

# Initialize Faker
fake = Faker()

def populate_db():
    # Create Categories
    categories = [Category.objects.create(
        name=fake.word().capitalize(),
        description=fake.sentence()
    ) for _ in range(5)]
    print(f"Created {len(categories)} categories.")

    # Create Participants
    participants = [Participant.objects.create(
        name=fake.name(),
        email=fake.unique.email()
    ) for _ in range(10)]
    print(f"Created {len(participants)} participants.")

    # Create Events
    events = []
    for _ in range(10):
        event = Event.objects.create(
            name=fake.sentence(nb_words=3).strip('.'),
            description=fake.paragraph(),
            date=fake.date_this_year(),
            time=fake.time(),
            location=fake.city(),
            category=random.choice(categories)
        )
        event.participants.set(random.sample(participants, random.randint(1, 5)))  # Assign random participants
        events.append(event)

    print(f"Created {len(events)} events.")

    print("Database populated successfully!")

# Run the function
if __name__ == "__main__":
    populate_db()
