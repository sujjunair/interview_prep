def reverse_string_recursive(input_str):
    if len(input_str) == 1:
        return input_str
    else:
        return input_str[-1] + reverse_string_recursive(input_str[:-1])


if __name__=="__main__":
    input_str = "abcdef"
    print reverse_string_recursive(input_str)
