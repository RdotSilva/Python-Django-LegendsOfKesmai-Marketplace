from django_seed import Seed
from models import Potion
from common.utils.mock_data.potion_data import potion_list

seeder = Seed.seeder()


def seed_potion_data():
    for potion in potion_list:
        seeder.add_entity(Potion, 1, potion)

    # Execute the seeding
    inserted_pks = seeder.execute()
    print(f"{inserted_pks} has been seeded")


seed_potion_data()
