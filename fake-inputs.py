from faker import Faker
from faker.providers import internet

fake = Faker(['en_US', 'el_GR'])

for _ in range(10):
    print(fake.name())