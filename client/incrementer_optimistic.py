import hazelcast

if __name__ == "__main__":
    client = hazelcast.HazelcastClient(
        cluster_name="hazel_cluster",
    )
    my_map = client.get_map("distributed_map").blocking()

    my_map.put_if_absent("key_optimistic", 0)
    for k in range(10000):
        while True:

            var_value = my_map.get("key_optimistic")
            new_value = var_value + 1

            if my_map.replace_if_same("key_optimistic", var_value, new_value):
                break
