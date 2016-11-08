def recursive_list_sum(input_list):
    if len(input_list) > 1:
        return input_list[0] + recursive_list_sum(input_list[1:])
    else:
        return input_list[0]

if __name__=="__main__":
    input_list = [1,2,3,4]
    print recursive_list_sum(input_list)
