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


@app2.route("/metrics")
def metrics():
    metrics = linuxConsumer_s2.get_sensor_reading()
    current_co2_s2.labels("study2").set(metrics["co2"])
    current_temperature_s2.labels("study2").set(metrics["tmp"])
    current_humidity_s2.labels("study2").set(metrics["hum"])
    return Response(generate_latest(), mimetype=content_type)


if __name__ == "__main__":
    app2.run(host="0.0.0.0", port=5003)
