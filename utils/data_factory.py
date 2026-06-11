import random
import string

# import fake
# from faker import Faker
#
# faker = Faker()

from faker import Faker
from typing import Final

fake: Final[Faker] = Faker()


def random_job_title() -> str:
    return fake.job()


def generate_random_job_title(prefix: str = "Consultant") -> str:
    random_part = "".join(random.choices(string.ascii_letters, k=10))
    return f"{prefix}_{random_part}"

def generate_random_name() -> str:
    first_name: str = fake.first_name()
    last_name: str = fake.last_name()
    return f"{first_name} {last_name}"


def generate_random_department_name() -> str:
    return f"{fake.company()} Dept {fake.random_int(1000, 9999)}"