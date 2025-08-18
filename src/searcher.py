def search_json(data, key, value):
    if isinstance(data, list):
        return [item for item in data if item.get(key) == value]
    raise ValueError("Data must be a list of dictionaries.")

def search_xml(root, tag, value):
    return [elem for elem in root.findall(tag) if elem.text == value]

