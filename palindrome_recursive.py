def is_palindrome(input_str):
    if len(input_str) == 1:
        return True
    else:
        return input_str[0] == input_str[-1] and is_palindrome(input_str[1:-1])


if __name__=="__main__":
    input_str = "kayask"
    print is_palindrome(input_str)
