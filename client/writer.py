import hazelcast

if __name__ == "__main__":
    client = hazelcast.HazelcastClient(
        cluster_name="hazel_cluster",
    )

    distributed_map = client.get_map("distributed_map").blocking()

    for i in range(1000):
        distributed_map.set(i, f"value_{i}")
