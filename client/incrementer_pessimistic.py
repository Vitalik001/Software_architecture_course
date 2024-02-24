import hazelcast

if __name__ == "__main__":
    client = hazelcast.HazelcastClient(
        cluster_name="hazel_cluster",
    )
    my_map = client.get_map("distributed_map").blocking()
    my_map.put_if_absent("key_pessimistic", 0)
    for k in range(10000):
        my_map.lock("key_pessimistic")
        try:
            var_value = my_map.get("key_pessimistic")
            var_value+=1
            my_map.put("key_pessimistic", var_value)
        finally:
            my_map.unlock("key_pessimistic")
