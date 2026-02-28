import random
import string

from faker import Faker

faker = Faker()


def random_job_title() -> str:
    return faker.job()


def generate_random_job_title(prefix: str = "Consultant") -> str:
    random_part = "".join(random.choices(string.ascii_letters, k=10))
    return f"{prefix}_{random_part}"
