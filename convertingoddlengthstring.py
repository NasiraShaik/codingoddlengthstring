def transform_string(input_string):
    length = len(input_string)
    mid_point = length // 2

    if length % 2 == 1:
        first_half = input_string[:mid_point].upper()
        second_half = input_string[mid_point:].lower()
        transformed_string = first_half + second_half
    else:
        transformed_string = input_string.lower()

    return transformed_string

# Example usage:
input_str1 = input()
output_str1 = transform_string(input_str1)
print(output_str1)
