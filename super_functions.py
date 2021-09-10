def min_of_string_list(list_of_strings):
    string_list = []
    for string_ in list_of_strings:
        string_list.append(string_.replace(' ',''))
    min_string = min(string_list)
    
    return min_string