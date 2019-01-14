
def order_dict(_dict: dict, reverse: bool=True) -> dict:
    temp_dict = {}

    unordered_list = [(k, v) for k, v in _dict.items()]
    ordered_list = sorted(unordered_list, key=lambda x: x[1], reverse=reverse)

    for item in ordered_list:
        temp_dict[item[0]] = item[1]

    return temp_dict
