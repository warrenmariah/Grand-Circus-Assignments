from confluent_kafka import Consumer, KafkaError, KafkaException
import sys

KAFKA_TOPIC = 'jokes'
KAFKA_BOOTSTRAP_SERVERS = ':35987'


def main():
    conf = {'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
            'group.id': 'joke_word_count'}

    consumer = Consumer(conf)
    running_total_word_count = 0
    number_of_jokes = 0

    try:
        consumer.subscribe([KAFKA_TOPIC])

        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None: continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                words = msg.value().split()
                word_count = len(words)
                running_total_word_count += word_count
                number_of_jokes += 1
                print(f"running total: {running_total_word_count}")
                print(f"joke #: {number_of_jokes}")
                print(f"word count: {word_count}")
                if number_of_jokes % 5 == 0:
                    print(f"average word count so far: {running_total_word_count/number_of_jokes}")
                print()
                print([msg.value().decode('utf-8'), word_count])

    except KeyboardInterrupt:
        sys.stderr.write('%% Aborted by user\n')

    finally:
        consumer.close()


if __name__ == '__main__':
    main()