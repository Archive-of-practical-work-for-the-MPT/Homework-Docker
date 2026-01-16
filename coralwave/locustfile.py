import random
from faker import Faker
from locust import HttpUser, task, SequentialTaskSet, TaskSet, constant_throughput

fake = Faker("ru_RU")  # Указываем локаль нашей России


class CoralWaveAPITests(TaskSet):
    # У нас тут три tasks в сумме дают 11
    # А значит 1-й и 2-й будут выполняться с веростностью 45.5%, а 3-й с 9%
    @task(5)  # Ставим 5, чтобы task выполнялся в 5 раз чаще
    def get_countries(self):
        """Получение списка стран (GET запрос)"""
        self.client.get("/api/countries/")

    @task(5)
    def get_seas(self):
        """Получение списка морей (GET запрос)"""
        self.client.get("/api/seas/")

    @task(1)  # Ставим 1 (базовая частота)
    def create_country(self):
        """Создание новой страны (POST запрос)"""
        country_data = {
            "name": fake.country() + " " + str(random.randint(1000, 9999)),
            "code": fake.country_code()
        }
        self.client.post("/api/countries/", json=country_data)


class ReefCreationFlow(SequentialTaskSet):
    def on_start(self):
        self.sea_id = None
        self.country_id = None

    @task
    def create_sea(self):
        """Шаг 1: Создание моря"""
        sea_data = {
            "name": f"{fake.word().capitalize()} море"
        }

        with self.client.post("/api/seas/", json=sea_data, catch_response=True) as response:
            if response.status_code in [201, 200]:
                try:
                    data = response.json()
                    # Сохраняем ID созданного моря
                    self.sea_id = data.get('id_sea')
                    response.success()
                except:
                    response.failure(
                        "Не получилось вытащить ID созданного моря")
            else:
                response.failure(
                    f"Создание нового моря - неудачно: {response.status_code}")

    @task
    def create_country(self):
        """Шаг 2: Создание страны"""
        country_data = {
            "name": fake.country(),
            "code": fake.country_code()
        }

        with self.client.post("/api/countries/", json=country_data, catch_response=True) as response:
            if response.status_code in [201, 200]:
                try:
                    data = response.json()
                    # Сохраняем ID созданной страны
                    self.country_id = data.get('id_country')
                    response.success()
                except:
                    response.failure(
                        "Не получилось вытащить ID созданной страны")
            else:
                response.failure(
                    f"Создание новой страны - неудачно: {response.status_code}")

    @task
    def create_reef(self):
        """Шаг 3: Создание рифа с использованием ID моря и страны"""
        if not self.sea_id or not self.country_id:
            return  # Пропускаем, если нет необходимых ID

        reef_data = {
            "name": f"{fake.word().capitalize()} риф",
            "description": fake.text(max_nb_chars=200),
            "coordinate": f"{fake.latitude()}, {fake.longitude()}",
            "id_sea": self.sea_id,
            "id_country": self.country_id
        }

        with self.client.post("/api/reefs/", json=reef_data, catch_response=True) as response:
            if response.status_code in [201, 200]:
                response.success()
            else:
                response.failure(
                    f"Создание рифа - неудачно: {response.status_code} - {response.text}")

    @task
    def stop_sequence(self):
        """Завершение последовательности"""
        # Сбрасываем ID для следующей итерации
        self.sea_id = None
        self.country_id = None
        # Останавливаем выполнение этой последовательности
        self.interrupt()


class WebsiteUser(HttpUser):
    """Точка входа"""
    # Частота запросов - 2 запроса в секунду от 1 пользователя
    wait_time = constant_throughput(2)

    tasks = {
        # TaskSet (случайный порядок, имитация реального поведения, веса) [3 - 75% времени]
        CoralWaveAPITests: 3,
        # SequentialTaskSet (строгий порядок, четкие сценарии) [1 - 25% времени]
        ReefCreationFlow: 1
    }
