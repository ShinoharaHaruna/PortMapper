import argparse
import hashlib


class ConsistentHash:
    def __init__(self, threshold, num_buckets):
        self.threshold = threshold
        self.num_buckets = num_buckets
        self.buckets = []
        for i in range(num_buckets):
            self.buckets.append(i)

    def add_bucket(self, bucket):
        self.buckets.append(bucket)

    def remove_bucket(self, bucket):
        self.buckets.remove(bucket)

    def get_mapped_value(self, key):
        hash_value = self._hash_key(key)
        bucket_index = self._find_bucket_index(hash_value)
        mapped_value = self._map_to_range(bucket_index)
        return mapped_value

    def _hash_key(self, key):
        hash_object = hashlib.sha1(key.encode())
        hash_value = int(hash_object.hexdigest(), 16)
        return hash_value

    def _find_bucket_index(self, hash_value):
        bucket_index = hash_value % len(self.buckets)
        return bucket_index

    def _map_to_range(self, bucket_index):
        range_size = 65535 - self.threshold
        bucket_size = range_size // self.num_buckets
        mapped_value = self.threshold + bucket_index * bucket_size
        return mapped_value


def map_to_port(s, threshold):
    assert 0 <= threshold < 65536, "Threshold must be in range [0, 65536)"
    assert 10 <= args.num_buckets, "The num_buckets must be greater than 10."
    hasher = ConsistentHash(threshold, args.num_buckets)
    return hasher.get_mapped_value(s)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Map a string to a port number.")
    parser.add_argument(
        "-n", "--string", type=str, required=True, help="The input string."
    )
    parser.add_argument(
        "-t",
        "--threshold",
        type=int,
        default=4096,
        help="The threshold value that port must be greater than.",
    )
    parser.add_argument(
        "-c", "--num-buckets", type=int, default=127, help="The number of buckets."
    )

    args = parser.parse_args()

    port = map_to_port(args.string, args.threshold)
    print('The string "%s" is mapped to port %d.' % (args.string, port))
