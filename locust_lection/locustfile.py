import io
import random

from faker import Faker
from PIL import Image
from locust import HttpUser, task, SequentialTaskSet, TaskSet, constant_throughput

fake = Faker("ru_RU")

# print(fake.first_name_male())
# print(fake.middle_name_male())
# print(fake.last_name_male())

# image_bytes = fake.image()

# image = Image.open(io.BytesIO(image_bytes))

# image.show()


class StudentTests(TaskSet):
    def on_start(self):
        self.client.post("/login", data={
            "username": "admin",
            "password": "Qwerty_123"
        })

    @task  # помечаем функцию, которая отправляет запрос
    def add_student(self):
        student_date = {
            "first_name": fake.first_name_male(),
            "name": fake.middle_name_male(),
            "lastName": fake.last_name_male(),
            "corpEmail": fake.email(domain="mpt.ru"),
            "university": random.choice(["2388328238",
                                         "3424323243",
                                         "3231321323"]),
            "passport.series": str(fake.random_int(min=1000, max=9999)),
            "passport.number": str(fake.random_int(min=100000, max=999999))
        }

        self.client.post("/students/add", data=student_date) # post
        # self.client.get("/students/add", data=student_date) # get допустим еще


class WebsiteUser(HttpUser):
    wait_time = constant_throughput(2)  # сколько запросов секунду

    tasks = [
        StudentTests
    ]

