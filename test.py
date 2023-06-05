import random
import bf2
import matplotlib.pyplot as plt


def generate_random_data(num_elements):
    """Genera una lista di stringhe casuali di lunghezza 128"""
    return [str(random.getrandbits(128)) for _ in range(num_elements)]


def test_bloom_filter(bf_size, num_hashes, input_data, num_test_elements):
    """Crea un bloom filter, aggiunge i dati di input, e testa con un insieme di test"""
    bf = bf2.BloomFilter(bf_size, num_hashes)
    for element in input_data:
        bf.add(element)
    false_positives = 0
    num_present_element = 0;
    for _ in range(num_test_elements):
        element = str(random.getrandbits(128))
        if bf.contains(element):
            num_present_element +=1
        if bf.contains(element) and element not in input_data:
            false_positives += 1
    false_positive_rate = (false_positives / num_test_elements) * 100
    print(f"k={num_hashes}, fp_rate={false_positive_rate}, num_pres = {num_present_element}, num_falsi = {false_positives}")
    return false_positive_rate


def plot_bloom_filter(num_hashes_list, input_data_size, num_test_elements):
    """Genera un grafico della probabilità di falsi positivi al variare del numero di funzioni hash"""
    bf_size = 10000
    false_positive_rates = []
    for num_hashes in num_hashes_list:
        input_data = generate_random_data(input_data_size)
        false_positive_rate = test_bloom_filter(
            bf_size, num_hashes, input_data, num_test_elements)
        false_positive_rates.append(false_positive_rate)
    plt.plot(num_hashes_list, false_positive_rates)
    plt.title('Probabilità di falsi positivi al variare del numero di funzioni hash')
    plt.xlabel('Numero di funzioni hash')
    plt.ylabel('Probabilità di falsi positivi')
    plt.show()


# Test con una lista di 10 valori del numero di funzioni hash, 1000000 elementi di input e 50000 elementi di test
num_hashes_list = list(range(1, 11))
input_data_size = 1000
num_test_elements = 50000
plot_bloom_filter(num_hashes_list, input_data_size, num_test_elements)