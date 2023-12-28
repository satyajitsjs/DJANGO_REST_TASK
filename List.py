def list_io(list_item):
    new_list = []
    for item in list_item:
        if isinstance(item, list):
            new_list.extend(list_io(item))
        else:
            new_list.append(item)
    return new_list

input_list = [1, 2, [3, 4], 5, [6], 7, [8, [9, 10]]]
output_list = list_io(input_list)

print("Input List:", input_list)
print("Output List:", output_list)
