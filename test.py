# Flattening question

nested = {
    "user": {"name": "John", "age": 30, "add": "US"},
    "items": [1, {"id": 42}, 3, {"id": 19}],
}


def flattening(nested, result, key_history):
    if isinstance(nested, dict):
        for key, value in nested.items():
            new_key = key_history + "." + key if key_history else key
            if isinstance(value, int) or isinstance(value, str):
                result.append((new_key, value))
            else:
                flattening(
                    value, result, new_key
                )  # Since value is dict recurssion to extract key_history
    if isinstance(nested, list):
        for index in range(len(nested)):
            nested_elm = nested[index]
            if isinstance(nested_elm, int) or isinstance(nested_elm, str):
                pass
            else:
                new_key = key_history + "." + str(index)
                flattening(nested_elm, result, new_key)
    return result


result = flattening(nested, [], "")
print(result)
