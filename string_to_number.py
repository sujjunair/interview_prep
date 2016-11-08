def string_to_number(input_list):
    if len(input_list) == 1:
        return [input_list[0]]
    else:
        return [input_list[0]] + string_to_number(input_list[1:])


def number_to_string(input_num):
    quot = input_num / 10
    rem  = input_num % 10
    if quot == 0:
        return [str(input_num)]
    else:
        return number_to_string(quot) + [str(rem)]


if __name__=="__main__":
    input_num = 1234
    print "".join(number_to_string(input_num))

