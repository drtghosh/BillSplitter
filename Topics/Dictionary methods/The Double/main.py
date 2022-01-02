# put your python code here
str_start, str_end = 97, 123
double_alphabet = dict.fromkeys([chr(code) for code in range(str_start, str_end)])
for key, _ in double_alphabet.items():
    double_alphabet[key] = 2 * key