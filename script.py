from prometheus_client import start_http_server, Gauge
import random
import time


temperature_gauge = Gauge('temperature', 'Random temperature readings')
voltage_gauge = Gauge('voltage', 'Random voltage readings')
electricity_gauge = Gauge('electricity', 'Random electricity readings')
power_gauge = Gauge('power', 'Random power readings')

start_http_server(8000)

while True:
    temperature_gauge.set(random.uniform(10.0, 30.0))
    voltage_gauge.set(random.uniform(10.0, 30.0))
    electricity_gauge.set(random.uniform(10.0, 30.0))
    power_gauge.set(random.uniform(10.0, 30.0))
    time.sleep(10)
