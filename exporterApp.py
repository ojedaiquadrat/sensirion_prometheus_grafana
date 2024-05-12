from flask import Flask, Response
from prometheus_client import Counter, Gauge, start_http_server, generate_latest
import linuxConsumer


# Flask App name
app = Flask(__name__)
content_type = str("text/plain; version=0.0.4; charset=utf-8")

# prometheus client to expose the environmental metrics
current_co2 = Gauge(
    "current_co2",
    "the current co2 in ppm, this is a gauge as the value can increase or decrease",
    ["room"],
)

current_temperature = Gauge(
    "current_temperature",
    "the current temperature in celsius, this is a gauge as the value can increase or decrease",
    ["room"],
)

current_humidity = Gauge(
    "current_humidity",
    "the current humidity percentage, this is a gauge as the value can increase or decrease",
    ["room"],
)


@app.route("/metrics")
def metrics():
    metrics = linuxConsumer.get_sensor_reading()
    current_co2.labels("study").set(metrics["co2"])
    current_temperature.labels("study").set(metrics["tmp"])
    current_humidity.labels("study").set(metrics["hum"])
    return Response(generate_latest(), mimetype=content_type)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
