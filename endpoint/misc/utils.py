def omit(dictionary, *keys):
    return {i: dictionary[i] for i in dictionary if i not in keys}


def send(func, **args):
    try:
        return func(**args)
    except Exception as e:
        return str(e), 500