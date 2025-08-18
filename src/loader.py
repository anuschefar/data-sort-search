import json
import xml.etree.ElementTree as ET
from pathlib import Path

def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return root

def load_file(file_path):
    ext = Path(file_path).suffix.lower()
    if ext == ".json":
        return load_json(file_path)
    elif ext == ".xml":
        return load_xml(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")

