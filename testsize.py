import random
import bf2
import matplotlib.pyplot as plt


def generate_random_data_input(num_elements):
    return read_strings_from_file("strings.txt")[:num_elements]


def generate_random_data_insert():
    strings = read_strings_from_file("dati.txt")
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
        element_contains = generate_random_data_insert()
        if bf.contains(element_contains):
            num_present_element += 1
        if bf.contains(element_contains) and element_contains not in input_data:
            false_positives += 1
    return false_positives


def find_bloom_filter_size(num_hashes, input_data_size, num_test_elements):
    bf_size = 1000000
    false_positives_list = []
    bf_size_list = []
    while True:
        input_data = generate_random_data_input(input_data_size)
        false_positives = test_bloom_filter(bf_size, num_hashes, input_data, num_test_elements)
        print(f"Dimensione corrente del Bloom Filter: {bf_size}")
        print(f"Numero di falsi positivi: {false_positives}")
        false_positives_list.append(false_positives)
        bf_size_list.append(bf_size)
        if false_positives == 0:
            break
        bf_size *= 2
    return false_positives_list, bf_size_list


num_hashes = 3
input_data_size = 1000000
num_test_elements = 50000

false_positives_list, bloom_filter_size_list = find_bloom_filter_size(num_hashes, input_data_size, num_test_elements)

plt.plot(bloom_filter_size_list, false_positives_list)
plt.title('Dimensione del Bloom Filter in funzione dei falsi positivi')
plt.xlabel('Dimensione del Bloom Filter')
plt.ylabel('Numero di falsi positivi')
plt.show()
