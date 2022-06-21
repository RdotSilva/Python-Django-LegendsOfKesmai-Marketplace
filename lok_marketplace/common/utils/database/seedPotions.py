from django_seed import Seed
from potions.models import Potion

seeder = Seed.seeder()


def seed_potion_data():
    # TODO: Seed potion data to DB
    # Loop through potion seed data and add each entity
    seeder.add_entity(Potion, potionData)

    # Execute the seeding
    inserted_pks = seeder.execute()
