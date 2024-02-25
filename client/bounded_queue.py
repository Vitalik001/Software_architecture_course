import hazelcast
import threading

client = hazelcast.HazelcastClient(cluster_name="hazel_cluster")
queue = client.get_queue("bounded_queue").blocking()

def consume(consumer_id):
    while True:
        try:
            item = queue.poll()
            if item is None:
                print(f"Consumer {consumer_id} found the queue empty.")
            else:
                print(f"Consumer {consumer_id} consumed: {item}")
        except Exception as e:
            print(f"Consumer {consumer_id} encountered an error: {e}")
            break

def produce():
    for i in range(1, 101):
        queue.put(f"value-{i}")
        print(f"Produced value-{i}")

# consumer_thread_1 = threading.Thread(target=consume, args=(1,))
# consumer_thread_2 = threading.Thread(target=consume, args=(2,))
# consumer_thread_1.start()
# consumer_thread_2.start()

producer_thread = threading.Thread(target=produce)
producer_thread.start()

producer_thread.join()

client.shutdown()
