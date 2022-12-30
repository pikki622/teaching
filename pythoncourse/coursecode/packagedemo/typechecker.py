def print_is_a_float(x):
    if isinstance(x, float):
        print(f'{str(x)} is a float')
    else:
        print(f'{str(x)} is not a float')

def print_is_a_string(x):
    if isinstance(x, str):
        print(f'{str(x)} is a str')
    else:
        print(f'{str(x)} is not a str')