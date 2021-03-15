import json
from time import sleep

from kafka import KafkaConsumer

if __name__ == '__main__':
    parsed_topic_name = 'raw_recipes'
    # Notify if a recipe has more than 200 calories
    calories_threshold = 200

    consumer = KafkaConsumer(parsed_topic_name, auto_offset_reset='earliest',
                             bootstrap_servers=['kafkaserver:9092'], api_version=(0,9,0,1), consumer_timeout_ms=1000)
    while True:
       msg = consumer.poll(10)
       if msg != {}:
            print("messages are ",msg)

    #if consumer is not None:
        #consumer.close()