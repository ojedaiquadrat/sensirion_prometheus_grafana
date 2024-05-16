from flask import Flask, Response
from prometheus_client import Counter, Gauge, start_http_server, generate_latest
import linuxConsumer_s2


# Flask App name
app2 = Flask(__name__)
content_type = str("text/plain; version=0.0.4; charset=utf-8")

# prometheus client to expose the environmental metrics
current_co2_s2 = Gauge(
    "current_co2_s2_label",
    "the current co2 in ppm, this is a gauge as the value can increase or decrease",
    ["room2"],
)

current_temperature_s2 = Gauge(
    "current_temperature_s2_label",
    "the current temperature in celsius, this is a gauge as the value can increase or decrease",
    ["room2"],
)

current_humidity_s2 = Gauge(
    "current_humidity_s2_label",
    "the current humidity percentage, this is a gauge as the value can increase or decrease",
    ["room2"],
)

sensor_status_2 = Gauge(
    "sensor_status_2",
    "the current sensor status, this is a gauge as the value can be 1 for activated or 0 deactivated",
    ["room2"],
)


temperature_validation_s2 = Gauge(
    "temperature_validation_s2",
    "the current temperature validation with ML, this is a gauge as the value can get 1 or -1",
    ["room2"],
)

humidity_validation_s2 = Gauge(
    "humidity_validation_S2",
    "the current humidity validation with ML, this is a gauge as the value can get 1 or -1",
    ["room2"],
)


@app2.route("/metrics")
def metrics():
    metrics = linuxConsumer_s2.get_sensor_reading()
    current_co2_s2.labels("study2").set(metrics["co2"])
    current_temperature_s2.labels("study2").set(metrics["tmp"])
    current_humidity_s2.labels("study2").set(metrics["hum"])
    sensor_status_2.labels("study2").set(metrics["stat"])
    # data validation
    temperature_validation_s2.labels("study2").set(metrics["tmpValid"])
    humidity_validation_s2.labels("study2").set(metrics["humValid"])
    return Response(generate_latest(), mimetype=content_type)


if __name__ == "__main__":
    app2.run(host="0.0.0.0", port=5004)
