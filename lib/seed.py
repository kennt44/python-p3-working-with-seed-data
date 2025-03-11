from app import session
from app.models import Game
from faker import Faker
import random

# Initialize Faker and generate random data
fake = Faker()

print("Seeding games...")

# Clear out any existing data
session.query(Game).delete()
session.commit()

# Create 50 random Game entries
games = [
    Game(
        title=fake.name(),
        genre=fake.word(),
        platform=fake.word(),
        price=random.randint(0, 60)
    )
    for _ in range(50)
]

# Save the generated objects to the database
session.bulk_save_objects(games)
session.commit()

print("Seeding complete.")
