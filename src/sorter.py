def sort_json(data, key):
    if isinstance(data, list):
        return sorted(data, key=lambda x: x.get(key, None))
    raise ValueError("Data must be a list of dictionaries.")

def sort_xml(root, tag):
    return sorted(root.findall(tag), key=lambda x: x.text or "")

