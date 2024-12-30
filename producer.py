from confluent_kafka import Producer
import socket
import time
import requests

KAFKA_TOPIC = 'jokes'
KAFKA_BOOTSTRAP_SERVERS = ':35987'



def delivery_callback(err, msg):
    if err:
        print('%% Message failed delivery: %s' % err)
    else:
        print('%% Message delivered to %s [%d]' % (msg.topic(), msg.partition()))


def main():
    conf = {'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
            'client.id': socket.gethostname()}

    
    producer = Producer(conf)

    while True:
        r=requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
        r=r.json()
        joke=r['joke']
        producer.produce(KAFKA_TOPIC, joke,
                         callback=delivery_callback)

        
        producer.flush()           
        time.sleep(5)


    producer.close()


if __name__ == '__main__':
    main()