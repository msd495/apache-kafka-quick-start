from kafka import KafkaConsumer, KafkaProducer
from fetchData import fetch_raw,get_recipes
from json import dumps
from time import sleep

def connect_kafka_producer():
    _producer = None
    try:
        _producer = KafkaProducer(bootstrap_servers=['kafkaserver:9092'], api_version=(0,9,0,1),
                                  value_serializer=lambda x:dumps(x).encode('utf-8'))
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _producer

def publish_message(producer_instance, topic_name, key, value):
    try:
        for e in range(10):
            data = {'number' : e}
            producer_instance.send('raw_recipes', value=data)
            sleep(5)
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Pragma': 'no-cache'
    }
all_recipes = get_recipes(headers)
if len(all_recipes) > 0:
    kafka_producer = connect_kafka_producer()
    for recipe in all_recipes:
        publish_message(kafka_producer, 'raw_recipes', 'raw', recipe)
    if kafka_producer is not None:
        kafka_producer.close()