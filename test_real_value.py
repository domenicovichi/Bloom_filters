import random
import bf2
import matplotlib.pyplot as plt


def generate_random_data_input(num_elements):
    return read_strings_from_file("strings.txt")[:num_elements]


def generate_random_data_contains():
    strings = read_strings_from_file("dati1.txt")
    return random.choice(strings)

def read_strings_from_file(file_name):
    with open(file_name, 'r') as file:
        return file.read().splitlines()


def test_bloom_filter(bf_size, num_hashes, input_data, num_test_elements):
    bf = bf2.BloomFilter(bf_size, num_hashes)
    for element in input_data:
        bf.add(element)
    false_positives = 0
    num_present_element = 0
    for _ in range(num_test_elements):
        element_contains = generate_random_data_contains()
        if bf.contains(element_contains):
            num_present_element += 1
        if bf.contains(element_contains) and element_contains not in input_data:
            false_positives += 1
    false_positive_rate = (false_positives / num_test_elements) * 100
    print(f"k={num_hashes}, fp_rate={false_positive_rate}, fp = {false_positives}, npe = {num_present_element} ")
    return false_positive_rate


def plot_bloom_filter(num_hashes_list, input_data_size, num_test_elements):
    """Genera un grafico della probabilità di falsi positivi al variare del numero di funzioni hash"""
    bf_size = 1000000
    false_positive_rates = []
    for num_hashes in num_hashes_list:
        input_data = generate_random_data_input(input_data_size)
        false_positive_rate = test_bloom_filter(
            bf_size, num_hashes, input_data, num_test_elements)
        false_positive_rates.append(false_positive_rate)
    plt.plot(num_hashes_list, false_positive_rates)
    plt.title('Probabilità di falsi positivi al variare del numero di funzioni hash')
    plt.xlabel('Numero di funzioni hash')
    plt.ylabel('Probabilità di falsi positivi')
    plt.show()


num_hashes_list = list(range(1, 11))
input_data_size = 100000
num_test_elements = 10000
plot_bloom_filter(num_hashes_list, input_data_size, num_test_elements)
