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

sensor_status = Gauge(
    "sensor_status",
    "the current sensor status, this is a gauge as the value can be 1 for activated or 0 deactivated",
    ["room"],
)

# adding result from data validation


co2_validation_s1 = Gauge(
    "co2_validation_s1",
    "the current temperature validation with ML, this is a gauge as the value can get 1 or -1",
    ["room"],
)

temperature_validation_s1 = Gauge(
    "temperature_validation_s1",
    "the current temperature validation with ML, this is a gauge as the value can get 1 or -1",
    ["room"],
)

humidity_validation_s1 = Gauge(
    "humidity_validation_S1",
    "the current humidity validation with ML, this is a gauge as the value can get 1 or -1",
    ["room"],
)


@app.route("/metrics")
def metrics():
    metrics = linuxConsumer.get_sensor_reading()
    current_co2.labels("study").set(metrics["co2"])
    current_temperature.labels("study").set(metrics["tmp"])
    current_humidity.labels("study").set(metrics["hum"])
    sensor_status.labels("study").set(metrics["stat"])
    # data validation
    co2_validation_s1.labels("study").set(metrics["co2Valid"])
    temperature_validation_s1.labels("study").set(metrics["tmpValid"])
    humidity_validation_s1.labels("study").set(metrics["humValid"])
    return Response(generate_latest(), mimetype=content_type)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
