from ipaddress import ip_address

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate(*args):
    first_sum = 0
    for item in args:
        if isinstance(item,(int, float)):
            first_sum += item
        elif isinstance(item, str):
            first_sum += len(item)
        elif isinstance(item, ( list, dict, set, tuple)):
            if isinstance(item, dict):
                first_sum += calculate((*item.keys(), *item.values()))
            else:
                first_sum += calculate(*item)
    return first_sum


result = calculate(data_structure)
print(result)
