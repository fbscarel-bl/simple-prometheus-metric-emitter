from prometheus_client import start_http_server, Gauge
import random
import time

start_http_server(8000)
random_gauge = Gauge('random_gauge_value', 'Random gauge value between 0.0 and 100.0')

def generate_random_gauge():
    random_value = random.uniform(0.0, 100.0)
    random_gauge.set(random_value)
    print(f"Updated random gauge to: {random_value}")

if __name__ == "__main__":
    print("Exposing metrics at http://localhost:8000/metrics")
    while True:
        generate_random_gauge()
        time.sleep(10)
