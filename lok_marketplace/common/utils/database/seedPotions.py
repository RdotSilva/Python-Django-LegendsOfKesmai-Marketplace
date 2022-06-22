from django_seed import Seed
from potions.models import Potion
from potion_data import potion_list

seeder = Seed.seeder()


def seed_potion_data():
    for potion in potion_list:
        seeder.add_entity(Potion, potion)

    # Execute the seeding
    inserted_pks = seeder.execute()
    print(f"{inserted_pks} has been seeded")


# TODO: Call seed_potion_data and test seeding
