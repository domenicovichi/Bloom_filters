import math
import mmh3

# Bloom filter con in input funzioni hash per calcolare in ouptut la probabilità di falsi positivi


class BloomFilter:
    def __init__(self, m, k):
        self.m = m
        self.k = k
        self.bit_array = [0] * self.m

    def add(self, element):
        for i in range(self.k):
            index = mmh3.hash(element, i) % self.m
            self.bit_array[index] = 1

    def contains(self, element):
        for i in range(self.k):
            index = mmh3.hash(element, i) % self.m
            if self.bit_array[index] == 0:
                return False
        return True
