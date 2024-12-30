from confluent_kafka import Consumer, KafkaError, KafkaException
import sys

KAFKA_TOPIC = 'jokes'
KAFKA_BOOTSTRAP_SERVERS = ':35987'


def main():
    conf = {'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
            'group.id': 'demo_logger'}

    consumer = Consumer(conf)

    try:
        consumer.subscribe([KAFKA_TOPIC])

        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                sys.stderr.write(msg.error())
                continue
            
            print(msg.value().decode('utf-8'))

    except KeyboardInterrupt:
        sys.stderr.write('%% Aborted by user\n')

    finally:
        consumer.close()


if __name__ == '__main__':
    main()