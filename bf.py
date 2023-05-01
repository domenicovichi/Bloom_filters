import math
import mmh3


class BloomFilter:
    def __init__(self, n, p):
        self.n = n
        self.p = p
        self.m = int(-(n * math.log(p)) / (math.log(2) ** 2)) #dimensione ottimale array di bit
        self.k = int((self.m / n) * math.log(2)) #numero ottimale di funzioni hash
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


# Esempio di utilizzo
bf = BloomFilter(10000, 0.1)

# Aggiunge alcuni elementi al Bloom filter
bf.add("ciao")
bf.add("mondo")
bf.add("come")
bf.add("stai")

# Verifica se alcuni elementi sono presenti nel Bloom filter
print(bf.contains("ciao"))   # True
print(bf.contains("mondo"))  # True
print(bf.contains("hello"))  # False
print(bf.contains("world"))  # False
