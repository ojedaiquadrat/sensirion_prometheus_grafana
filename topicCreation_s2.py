import asyncio

from kafka import *
from kafka.admin import KafkaAdminClient, NewTopic
import json
from time import sleep

""" Kafka brokers and topic parameters """
# Topic name
topic_name = "sensirion_2"
topic_partitions = 3
topic_replication = 3


# Broker list creation
# first_broker = "192.168.1.128:9092"
# second_broker = "192.168.1.128:9093"
# third_broker = "192.168.1.128:9094"
first_broker = "10.2.2.77:9092"
second_broker = "10.2.2.77:9093"
third_broker = "10.2.2.77:9094"
kafka_broker_list = [first_broker, second_broker, third_broker]


""" Admin TOPIC creation and verification """
# Create AdminClient to access Brokers features
admin_client = KafkaAdminClient(bootstrap_servers=kafka_broker_list)


# list topics
print("List topics:", admin_client.list_topics())

# check if topic exists and create it
if topic_name not in admin_client.list_topics():
    new_topic = NewTopic(
        name=topic_name,
        num_partitions=topic_partitions,
        replication_factor=topic_replication,
    )
    admin_client.create_topics(new_topics=[new_topic])
