from kafka import KafkaConsumer, TopicPartition, OffsetAndMetadata
import json
import time

"""kafka variables"""
topic_name = "sensirion_1"  # topic to subscribe
# Broker list creation
# first_broker = "192.168.1.128:9092"
# second_broker = "192.168.1.128:9093"
# third_broker = "192.168.1.128:9094"
# first_broker = "10.2.2.77:9092"
# second_broker = "10.2.2.77:9093"
# third_broker = "10.2.2.77:9094"
first_broker = "10.1.6.83:9092"
second_broker = "10.1.6.83:9093"
third_broker = "10.1.6.83:9094"
kafka_server_ports = [first_broker, second_broker, third_broker]  # broker list

"""Topic Subscription"""
consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=kafka_server_ports,
    auto_offset_reset="latest",
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
)


def get_sensor_reading():
    for msg in consumer:
        fetched_data = msg.value
        print("S1: ", fetched_data)
        return fetched_data


# get_sensor_reading()
