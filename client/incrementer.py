import hazelcast

if __name__ == "__main__":
    client = hazelcast.HazelcastClient(
        cluster_name="hazel_cluster",
    )

    my_map = client.get_map("distributed_map").blocking()
    my_map.put_if_absent("key", 0)
    for k in range(10000):
        var_value = my_map.get("key")
        var_value+=1
        my_map.put("key", var_value)
