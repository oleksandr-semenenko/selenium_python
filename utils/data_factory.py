from faker import Faker

faker = Faker()

def random_job_title() -> str:
    return faker.job()