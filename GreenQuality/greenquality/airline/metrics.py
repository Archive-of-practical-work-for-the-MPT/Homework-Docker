import os
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
from django.db.models import Count, Sum


class InfluxMetricsWriter:
    """
    Класс для записи метрик в InfluxDB.
    """

    def __init__(self):
        """
        Инициализация клиента InfluxDB.
        """
        self.token = os.environ.get(
            "INFLUXDB_TOKEN", "Ny9WfF77-bxdyWn4zzjFv9GP-_sCaftbFGQv2dhUB46Ovk0GJRHjRuSdA_paTgf81_9OZYoJIkEKwcMFrOVQjg==")
        self.org = "MPT"
        self.url = "http://host.docker.internal:8086"
        self.bucket = "metrics"

        self.client = influxdb_client.InfluxDBClient(
            url=self.url,
            token=self.token,
            org=self.org
        )
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)

    def write_flights_by_status(self):
        """
        Запись метрик по количеству рейсов по статусам.
        """
        from .models import Flight

        # Получаем количество рейсов для каждого статуса
        flight_objects = Flight.objects.all()
        flight_counts = flight_objects.values(
            'status').annotate(count=Count('id_flight'))

        # Записываем данные в InfluxDB
        for row in flight_counts:
            status = row['status'] if row['status'] else 'Не определен'
            count = float(row['count'])

            point = (
                influxdb_client.Point("flights_by_status")
                .tag("status", status)
                .field("count", count)
            )
            self.write_api.write(bucket=self.bucket,
                                 org=self.org, record=point)

        # Добавляем нулевые значения для статусов, которых нет в базе
        existing_statuses = {row['status']
                             for row in flight_objects.values('status')}
        all_possible_statuses = ['Запланирован',
                                 'В пути', 'Прибыл', 'Отменен', 'Задержан']

        for status in all_possible_statuses:
            if status not in existing_statuses:
                point = (
                    influxdb_client.Point("flights_by_status")
                    .tag("status", status)
                    .field("count", 0.0)
                )
                self.write_api.write(bucket=self.bucket,
                                     org=self.org, record=point)

    def write_tickets_by_class(self):
        """
        Запись метрик по количеству проданных билетов по классам обслуживания.
        """
        from .models import Ticket, Class

        # Получаем количество билетов для каждого класса обслуживания
        ticket_objects = Ticket.objects.all()
        ticket_counts = (ticket_objects
                         .select_related('class_id')
                         .values('class_id__class_name')
                         .annotate(count=Count('id_ticket')))

        # Записываем данные в InfluxDB
        for row in ticket_counts:
            class_name = row['class_id__class_name'] if row['class_id__class_name'] else 'Не определен'
            count = float(row['count'])

            point = (
                influxdb_client.Point("tickets_by_class")
                .tag("class_name", class_name)
                .field("count", count)
            )
            self.write_api.write(bucket=self.bucket,
                                 org=self.org, record=point)

        # Добавляем нулевые значения для классов, по которым нет билетов
        existing_classes = {row['class_id__class_name']
                            for row in ticket_counts}
        class_objects = Class.objects.all()

        for cls in class_objects:
            if cls.class_name not in existing_classes:
                point = (
                    influxdb_client.Point("tickets_by_class")
                    .tag("class_name", cls.class_name)
                    .field("count", 0.0)
                )
                self.write_api.write(bucket=self.bucket,
                                     org=self.org, record=point)

    def write_profit_by_flight(self):
        """
        Запись метрик по доходу по каждому рейсу.
        """
        from .models import Ticket

        # Вычисляем общий доход для каждого рейса
        ticket_objects = Ticket.objects.all()
        profit_by_flight = (ticket_objects
                            .select_related('flight_id', 'flight_id__departure_airport_id', 'flight_id__arrival_airport_id')
                            .values(
                                'flight_id__id_flight',
                                'flight_id__departure_airport_id__id_airport',
                                'flight_id__arrival_airport_id__id_airport'
                            )
                            .annotate(total_revenue=Sum('price')))

        # Записываем данные в InfluxDB
        for row in profit_by_flight:
            flight_id = str(row['flight_id__id_flight']
                            ) if row['flight_id__id_flight'] else 'Не определен'
            departure = row['flight_id__departure_airport_id__id_airport'] if row[
                'flight_id__departure_airport_id__id_airport'] else 'Не определен'
            arrival = row['flight_id__arrival_airport_id__id_airport'] if row[
                'flight_id__arrival_airport_id__id_airport'] else 'Не определен'
            revenue = float(row['total_revenue']
                            ) if row['total_revenue'] else 0.0

            point = (
                influxdb_client.Point("profit_by_flight")
                .tag("flight_id", flight_id)
                .tag("departure_airport", departure)
                .tag("arrival_airport", arrival)
                .field("revenue", revenue)
            )
            self.write_api.write(bucket=self.bucket,
                                 org=self.org, record=point)

    def write_all_metrics(self):
        """
        Запись всех метрик в InfluxDB.
        """
        self.write_flights_by_status()
        self.write_tickets_by_class()
        self.write_profit_by_flight()

    def close(self):
        """
        Закрытие соединения с InfluxDB.
        """
        self.write_api.close()
        self.client.close()
