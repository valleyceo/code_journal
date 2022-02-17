# Online Random Sampling

'''
- Take input size k and packets
- Continuously maintain uniform random subset S of size k of the read packets

Assumption: there are at least k elements in the stream.
'''
# Time: O(1)/element, Space: O(k)
def online_random_sample(stream: Iterator[int], k: int) -> List[int]:

    # Stores the first k elements.
    running_sample = list(itertools.islice(stream, k))

    # Have read the first k elements.
    num_seen_so_far = k
    for x in stream:
        num_seen_so_far += 1
        # Generate a random number in [0, num_seen_so_far - 1], and if this
        # number is in [0, k - 1], we replace that element from the sample with
        # x.
        idx_to_replace = random.randrange(num_seen_so_far)
        if idx_to_replace < k:
            running_sample[idx_to_replace] = x
    return running_sample

'''
Note:
1. For every new packet, find random number between 0 - new_stream_size
2. If new_stream_size < k, replace S[new_stream_size] to the new packet - P(k/stream_size)
'''
