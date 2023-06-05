import random
import string


def generate_random_string(length):
    """Genera una stringa casuale di lunghezza 'length'"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


num_strings = 50000
string_length = 4
output_file = "strings1.txt"

with open(output_file, "w") as file:
    for _ in range(num_strings):
        random_string = generate_random_string(string_length)
        file.write(random_string + "\n")

print(
    f"Generazione completata. Le stringhe sono state salvate su {output_file}.")
