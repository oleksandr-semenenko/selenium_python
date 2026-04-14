import random
import string

# import fake
# from faker import Faker
#
# faker = Faker()

from faker import Faker

fake = Faker()


def random_job_title() -> str:
    return fake.job()


def generate_random_job_title(prefix: str = "Consultant") -> str:
    random_part = "".join(random.choices(string.ascii_letters, k=10))
    return f"{prefix}_{random_part}"

def generate_random_name():
    first_name = fake.first_name()
    last_name = fake.last_name()
    return f"{first_name} {last_name}"

# 1
def generate_random_department_name() -> str:
    return f"{fake.company()} Dept {fake.random_int(1000, 9999)}"

# 2
# def generate_random_department_name() -> str:
#     prefixes = ["Global", "Advanced", "Corporate", "Dynamic", "International"]
#     areas = ["Sales", "Marketing", "Development", "Research", "Support", "Finance"]
#
#     return f"{random.choice(prefixes)} {random.choice(areas)}"
