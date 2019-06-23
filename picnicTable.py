def print_picnic(items_dict,left_width,right_width):
    print('PCINIC ITEMS'.center(left_width + right_width, '-'))
    for k, v in items_dict.items():
        print(k.ljust(left_width, '-') + str(v).rjust(right_width))

pcinic_items = {'sandwiches': 4,'apples': 12,'cups': 4,'coolies': 8000}
print_picnic(pcinic_items, 12, 5)
print_picnic(pcinic_items, 20, 6)