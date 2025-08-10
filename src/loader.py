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
Optimize am 2025-02-01
Update am 2025-02-11
Change am 2025-02-13
Update am 2025-02-21
Update am 2025-02-25
Optimize am 2025-02-28
Update am 2025-03-05
Optimize am 2025-03-07
Change am 2025-03-10
Update am 2025-03-11
Improve am 2025-03-12
Update am 2025-03-21
Fix am 2025-03-28
Add am 2025-03-29
Refactor am 2025-04-03
Add am 2025-04-05
Update am 2025-04-10
Fix am 2025-04-11
Change am 2025-04-19
Add am 2025-04-20
Add am 2025-04-21
Update am 2025-05-01
Update am 2025-05-02
Add am 2025-05-04
Cleanup am 2025-05-07
Optimize am 2025-05-12
Cleanup am 2025-05-13
Improve am 2025-05-17
Refactor am 2025-05-19
Refactor am 2025-05-30
Fix am 2025-06-04
Optimize am 2025-06-08
Add am 2025-06-10
Update am 2025-06-11
Change am 2025-06-12
Refactor am 2025-06-18
Improve am 2025-06-19
Update am 2025-06-24
Cleanup am 2025-06-28
Cleanup am 2025-07-05
Refactor am 2025-07-08
Cleanup am 2025-07-13
Update am 2025-07-15
Cleanup am 2025-07-16
Update am 2025-07-18
Fix am 2025-07-20
Fix am 2025-07-25
Update am 2025-08-06
Optimize am 2025-08-07
Refactor Änderung 1 am 2025-02-01
Refactor Änderung 2 am 2025-02-01
Refactor Änderung 3 am 2025-02-01
Refactor Änderung 4 am 2025-02-01
Improve Änderung 1 am 2025-02-01
Update Änderung 1 am 2025-02-02
Update Änderung 2 am 2025-02-02
Update Änderung 3 am 2025-02-02
Update Änderung 4 am 2025-02-02
Fix Änderung 1 am 2025-02-05
Fix Änderung 2 am 2025-02-05
Fix Änderung 3 am 2025-02-05
Fix Änderung 4 am 2025-02-05
Fix Änderung 5 am 2025-02-05
Fix Änderung 6 am 2025-02-05
Add Änderung 1 am 2025-02-06
Add Änderung 2 am 2025-02-06
Add Änderung 3 am 2025-02-06
Add Änderung 4 am 2025-02-06
Add Änderung 5 am 2025-02-06
Update Änderung 1 am 2025-02-08
Update Änderung 2 am 2025-02-08
Optimize Änderung 1 am 2025-02-11
Optimize Änderung 2 am 2025-02-11
Optimize Änderung 3 am 2025-02-11
Optimize Änderung 4 am 2025-02-11
Optimize Änderung 5 am 2025-02-11
Refactor Änderung 1 am 2025-02-11
Refactor Änderung 2 am 2025-02-11
Refactor Änderung 3 am 2025-02-11
Refactor Änderung 4 am 2025-02-11
Refactor Änderung 5 am 2025-02-11
Update Änderung 1 am 2025-02-11
Update Änderung 2 am 2025-02-11
Improve Änderung 1 am 2025-02-11
Improve Änderung 2 am 2025-02-11
Improve Änderung 3 am 2025-02-11
Improve Änderung 4 am 2025-02-11
Improve Änderung 5 am 2025-02-11
Fix Änderung 1 am 2025-02-12
Fix Änderung 2 am 2025-02-12
Fix Änderung 3 am 2025-02-12
Cleanup Änderung 1 am 2025-02-14
Cleanup Änderung 2 am 2025-02-14
Cleanup Änderung 3 am 2025-02-14
Change Änderung 1 am 2025-02-14
Change Änderung 2 am 2025-02-14
Change Änderung 3 am 2025-02-14
Change Änderung 4 am 2025-02-14
Improve Änderung 1 am 2025-02-16
Improve Änderung 2 am 2025-02-16
Improve Änderung 3 am 2025-02-16
Improve Änderung 4 am 2025-02-16
Improve Änderung 5 am 2025-02-16
Update Änderung 1 am 2025-02-18
Update Änderung 2 am 2025-02-18
Update Änderung 3 am 2025-02-18
Refactor Änderung 1 am 2025-02-22
Refactor Änderung 2 am 2025-02-22
Refactor Änderung 3 am 2025-02-22
Optimize Änderung 1 am 2025-02-22
Optimize Änderung 2 am 2025-02-22
Add Änderung 1 am 2025-02-25
Add Änderung 2 am 2025-02-25
Add Änderung 3 am 2025-02-25
Add Änderung 4 am 2025-02-25
Add Änderung 5 am 2025-02-25
Update Änderung 1 am 2025-02-25
Update Änderung 2 am 2025-02-25
Optimize Änderung 1 am 2025-02-28
Optimize Änderung 2 am 2025-02-28
Optimize Änderung 3 am 2025-02-28
Improve Änderung 1 am 2025-03-01
Improve Änderung 2 am 2025-03-01
Improve Änderung 3 am 2025-03-01
Improve Änderung 1 am 2025-03-03
Improve Änderung 2 am 2025-03-03
Improve Änderung 3 am 2025-03-03
Improve Änderung 4 am 2025-03-03
Add Änderung 1 am 2025-03-04
Add Änderung 2 am 2025-03-04
Add Änderung 3 am 2025-03-04
Refactor Änderung 1 am 2025-03-06
Refactor Änderung 2 am 2025-03-06
Refactor Änderung 3 am 2025-03-06
Refactor Änderung 4 am 2025-03-06
Refactor Änderung 5 am 2025-03-06
Refactor Änderung 6 am 2025-03-06
Refactor Änderung 7 am 2025-03-06
Optimize Änderung 1 am 2025-03-10
Optimize Änderung 1 am 2025-03-11
Optimize Änderung 2 am 2025-03-11
Improve Änderung 1 am 2025-03-12
Improve Änderung 2 am 2025-03-12
Improve Änderung 3 am 2025-03-12
Improve Änderung 4 am 2025-03-12
Refactor Änderung 1 am 2025-03-13
Refactor Änderung 1 am 2025-03-16
Refactor Änderung 2 am 2025-03-16
Refactor Änderung 3 am 2025-03-16
Fix Änderung 1 am 2025-03-17
Fix Änderung 2 am 2025-03-17
Fix Änderung 3 am 2025-03-17
Fix Änderung 4 am 2025-03-17
Optimize Änderung 1 am 2025-03-20
Optimize Änderung 2 am 2025-03-20
Optimize Änderung 3 am 2025-03-20
Add Änderung 1 am 2025-03-24
Add Änderung 2 am 2025-03-24
Add Änderung 1 am 2025-03-24
Add Änderung 2 am 2025-03-24
Add Änderung 3 am 2025-03-24
Add Änderung 4 am 2025-03-24
Add Änderung 5 am 2025-03-24
Optimize Änderung 1 am 2025-03-28
Optimize Änderung 2 am 2025-03-28
Optimize Änderung 3 am 2025-03-28
Refactor Änderung 1 am 2025-03-28
Change Änderung 1 am 2025-03-30
Change Änderung 2 am 2025-03-30
Change Änderung 3 am 2025-03-30
Optimize Änderung 1 am 2025-04-03
Optimize Änderung 2 am 2025-04-03
Optimize Änderung 3 am 2025-04-03
Optimize Änderung 4 am 2025-04-03
Optimize Änderung 5 am 2025-04-03
Optimize Änderung 6 am 2025-04-03
Optimize Änderung 1 am 2025-04-04
Optimize Änderung 2 am 2025-04-04
Improve Änderung 1 am 2025-04-08
Improve Änderung 2 am 2025-04-08
Improve Änderung 3 am 2025-04-08
Improve Änderung 4 am 2025-04-08
Improve Änderung 5 am 2025-04-08
Improve Änderung 6 am 2025-04-08
Improve Änderung 7 am 2025-04-08
Update Änderung 1 am 2025-04-11
Update Änderung 2 am 2025-04-11
Update Änderung 3 am 2025-04-11
Update Änderung 4 am 2025-04-11
Update Änderung 5 am 2025-04-11
Update Änderung 6 am 2025-04-11
Add Änderung 1 am 2025-04-19
Add Änderung 2 am 2025-04-19
Refactor Änderung 1 am 2025-04-21
Refactor Änderung 2 am 2025-04-21
Add Änderung 1 am 2025-04-23
Add Änderung 2 am 2025-04-23
Add Änderung 3 am 2025-04-23
Add Änderung 4 am 2025-04-23
Add Änderung 5 am 2025-04-23
Optimize Änderung 1 am 2025-04-26
Optimize Änderung 2 am 2025-04-26
Add Änderung 1 am 2025-04-28
Add Änderung 2 am 2025-04-28
Fix Änderung 1 am 2025-04-29
Fix Änderung 2 am 2025-04-29
Fix Änderung 3 am 2025-04-29
Cleanup Änderung 1 am 2025-04-29
Cleanup Änderung 2 am 2025-04-29
Cleanup Änderung 3 am 2025-04-29
Cleanup Änderung 4 am 2025-04-29
Cleanup Änderung 5 am 2025-04-29
Optimize Änderung 1 am 2025-04-30
Optimize Änderung 2 am 2025-04-30
Improve Änderung 1 am 2025-05-02
Improve Änderung 2 am 2025-05-02
Improve Änderung 3 am 2025-05-02
Refactor Änderung 1 am 2025-05-08
Refactor Änderung 2 am 2025-05-08
Refactor Änderung 3 am 2025-05-08
Optimize Änderung 1 am 2025-05-09
Optimize Änderung 2 am 2025-05-09
Optimize Änderung 3 am 2025-05-09
Optimize Änderung 4 am 2025-05-09
Optimize Änderung 5 am 2025-05-09
Optimize Änderung 6 am 2025-05-09
Optimize Änderung 7 am 2025-05-09
Optimize Änderung 8 am 2025-05-09
Refactor Änderung 1 am 2025-05-15
Refactor Änderung 2 am 2025-05-15
Refactor Änderung 1 am 2025-05-23
Refactor Änderung 2 am 2025-05-23
Refactor Änderung 3 am 2025-05-23
Refactor Änderung 4 am 2025-05-23
Refactor Änderung 5 am 2025-05-23
Change Änderung 1 am 2025-05-24
Change Änderung 2 am 2025-05-24
Cleanup Änderung 1 am 2025-05-27
Optimize Änderung 1 am 2025-05-28
Optimize Änderung 2 am 2025-05-28
Optimize Änderung 3 am 2025-05-28
Optimize Änderung 4 am 2025-05-28
Optimize Änderung 5 am 2025-05-28
Improve Änderung 1 am 2025-05-30
Improve Änderung 2 am 2025-05-30
Improve Änderung 3 am 2025-05-30
Refactor Änderung 1 am 2025-06-05
Refactor Änderung 2 am 2025-06-05
Refactor Änderung 3 am 2025-06-05
Refactor Änderung 4 am 2025-06-05
Fix Änderung 1 am 2025-06-05
Fix Änderung 2 am 2025-06-05
Fix Änderung 3 am 2025-06-05
Fix Änderung 4 am 2025-06-05
Add Änderung 1 am 2025-06-07
Add Änderung 2 am 2025-06-07
Refactor Änderung 1 am 2025-06-10
Refactor Änderung 2 am 2025-06-10
Refactor Änderung 3 am 2025-06-10
Refactor Änderung 4 am 2025-06-10
Improve Änderung 1 am 2025-06-17
Improve Änderung 2 am 2025-06-17
Improve Änderung 3 am 2025-06-17
Improve Änderung 4 am 2025-06-17
Cleanup Änderung 1 am 2025-06-22
Cleanup Änderung 2 am 2025-06-22
Cleanup Änderung 3 am 2025-06-22
Cleanup Änderung 4 am 2025-06-22
Cleanup Änderung 5 am 2025-06-22
Cleanup Änderung 6 am 2025-06-22
Update Änderung 1 am 2025-06-26
Add Änderung 1 am 2025-06-28
Add Änderung 2 am 2025-06-28
Add Änderung 3 am 2025-06-28
Add Änderung 4 am 2025-06-28
Update Änderung 1 am 2025-06-28
Update Änderung 2 am 2025-06-28
Change Änderung 1 am 2025-07-02
Change Änderung 2 am 2025-07-02
Change Änderung 3 am 2025-07-02
Change Änderung 4 am 2025-07-02
Change Änderung 5 am 2025-07-02
Refactor Änderung 1 am 2025-07-03
Cleanup Änderung 1 am 2025-07-03
Cleanup Änderung 2 am 2025-07-03
Update Änderung 1 am 2025-07-12
Update Änderung 2 am 2025-07-12
Update Änderung 3 am 2025-07-12
Update Änderung 4 am 2025-07-12
Update Änderung 5 am 2025-07-12
Update Änderung 6 am 2025-07-12
Update Änderung 7 am 2025-07-12
Add Änderung 1 am 2025-07-14
Add Änderung 2 am 2025-07-14
Add Änderung 3 am 2025-07-14
Add Änderung 4 am 2025-07-14
Add Änderung 5 am 2025-07-14
Add Änderung 6 am 2025-07-14
Add Änderung 7 am 2025-07-14
Add Änderung 8 am 2025-07-14
Change Änderung 1 am 2025-07-14
Change Änderung 2 am 2025-07-14
Change Änderung 3 am 2025-07-14
Change Änderung 4 am 2025-07-14
Fix Änderung 1 am 2025-07-15
Fix Änderung 2 am 2025-07-15
Fix Änderung 3 am 2025-07-15
Fix Änderung 4 am 2025-07-15
Fix Änderung 5 am 2025-07-15
Fix Änderung 6 am 2025-07-15
Add Änderung 1 am 2025-07-18
Add Änderung 2 am 2025-07-18
Improve Änderung 1 am 2025-07-23
Update Änderung 1 am 2025-07-26
Update Änderung 2 am 2025-07-26
Update Änderung 3 am 2025-07-26
Update Änderung 4 am 2025-07-26
Update Änderung 5 am 2025-07-26
Update Änderung 6 am 2025-07-26
Update Änderung 7 am 2025-07-26
Add Änderung 1 am 2025-07-29
Add Änderung 2 am 2025-07-29
Add Änderung 3 am 2025-07-29
Add Änderung 4 am 2025-07-29
Add Änderung 1 am 2025-08-05
Add Änderung 2 am 2025-08-05
Add Änderung 3 am 2025-08-05
Add Änderung 4 am 2025-08-05
Cleanup Änderung 1 am 2025-08-05
Cleanup Änderung 2 am 2025-08-05
Cleanup Änderung 3 am 2025-08-05
Update Änderung 1 am 2025-08-07
Update Änderung 2 am 2025-08-07
Update Änderung 3 am 2025-08-07
Update Änderung 4 am 2025-08-07
Refactor Änderung 1 am 2025-02-01
Refactor Änderung 2 am 2025-02-01
Refactor Änderung 3 am 2025-02-01
Refactor Änderung 4 am 2025-02-01
Improve Änderung 1 am 2025-02-16
Improve Änderung 2 am 2025-02-16
Change Änderung 1 am 2025-02-17
Change Änderung 2 am 2025-02-17
Change Änderung 3 am 2025-02-17
Change Änderung 1 am 2025-02-23
Add Änderung 1 am 2025-03-02
Add Änderung 2 am 2025-03-02
Add Änderung 3 am 2025-03-02
Cleanup Änderung 1 am 2025-03-05
Cleanup Änderung 2 am 2025-03-05
Cleanup Änderung 3 am 2025-03-05
Cleanup Änderung 4 am 2025-03-05
Cleanup Änderung 5 am 2025-03-05
Cleanup Änderung 6 am 2025-03-05
Change Änderung 1 am 2025-03-05
Change Änderung 2 am 2025-03-05
Change Änderung 3 am 2025-03-05
Change Änderung 1 am 2025-03-06
Change Änderung 2 am 2025-03-06
Change Änderung 3 am 2025-03-06
Fix Änderung 1 am 2025-03-06
Fix Änderung 2 am 2025-03-06
Fix Änderung 3 am 2025-03-06
Fix Änderung 4 am 2025-03-06
Cleanup Änderung 1 am 2025-03-07
Cleanup Änderung 2 am 2025-03-07
Cleanup Änderung 3 am 2025-03-07
Cleanup Änderung 1 am 2025-03-09
Cleanup Änderung 2 am 2025-03-09
Cleanup Änderung 3 am 2025-03-09
Add Änderung 1 am 2025-03-12
Add Änderung 2 am 2025-03-12
Add Änderung 3 am 2025-03-12
Optimize Änderung 1 am 2025-03-14
Optimize Änderung 2 am 2025-03-14
Optimize Änderung 3 am 2025-03-14
Optimize Änderung 4 am 2025-03-14
Optimize Änderung 5 am 2025-03-14
Change Änderung 1 am 2025-03-16
Change Änderung 2 am 2025-03-16
Change Änderung 3 am 2025-03-16
Change Änderung 4 am 2025-03-16
Add Änderung 1 am 2025-03-17
Add Änderung 2 am 2025-03-17
Add Änderung 3 am 2025-03-17
Add Änderung 4 am 2025-03-17
Add Änderung 5 am 2025-03-17
Cleanup Änderung 1 am 2025-03-21
Cleanup Änderung 2 am 2025-03-21
Cleanup Änderung 3 am 2025-03-21
Cleanup Änderung 4 am 2025-03-21
Improve Änderung 1 am 2025-03-22
Change Änderung 1 am 2025-03-23
Change Änderung 2 am 2025-03-23
Change Änderung 3 am 2025-03-23
Change Änderung 4 am 2025-03-23
Fix Änderung 1 am 2025-03-24
Fix Änderung 2 am 2025-03-24
Fix Änderung 3 am 2025-03-24
Fix Änderung 4 am 2025-03-24
Fix Änderung 5 am 2025-03-24
Improve Änderung 1 am 2025-03-24
Improve Änderung 2 am 2025-03-24
Improve Änderung 3 am 2025-03-24
Improve Änderung 4 am 2025-03-24
Improve Änderung 5 am 2025-03-24
Improve Änderung 6 am 2025-03-24
Add Änderung 1 am 2025-03-26
Add Änderung 2 am 2025-03-26
Add Änderung 3 am 2025-03-26
Add Änderung 4 am 2025-03-26
Add Änderung 5 am 2025-03-26
Optimize Änderung 1 am 2025-03-26
Optimize Änderung 2 am 2025-03-26
Optimize Änderung 3 am 2025-03-26
Update Änderung 1 am 2025-03-31
Update Änderung 2 am 2025-03-31
Add Änderung 1 am 2025-04-02
Add Änderung 2 am 2025-04-02
Add Änderung 3 am 2025-04-02
Update Änderung 1 am 2025-04-03
Update Änderung 2 am 2025-04-03
Update Änderung 3 am 2025-04-03
Update Änderung 4 am 2025-04-03
Add Änderung 1 am 2025-04-04
Add Änderung 2 am 2025-04-04
Add Änderung 3 am 2025-04-04
Add Änderung 4 am 2025-04-04
Add Änderung 1 am 2025-04-07
Add Änderung 2 am 2025-04-07
Add Änderung 3 am 2025-04-07
Add Änderung 4 am 2025-04-07
Add Änderung 5 am 2025-04-07
Add Änderung 6 am 2025-04-07
Change Änderung 1 am 2025-04-09
Change Änderung 2 am 2025-04-09
Change Änderung 3 am 2025-04-09
Change Änderung 4 am 2025-04-09
Change Änderung 5 am 2025-04-09
Refactor Änderung 1 am 2025-04-17
Refactor Änderung 2 am 2025-04-17
Update Änderung 1 am 2025-04-18
Update Änderung 2 am 2025-04-18
Update Änderung 3 am 2025-04-18
Update Änderung 4 am 2025-04-18
Optimize Änderung 1 am 2025-04-18
Optimize Änderung 2 am 2025-04-18
Optimize Änderung 3 am 2025-04-18
Optimize Änderung 4 am 2025-04-18
Optimize Änderung 5 am 2025-04-18
Update Änderung 1 am 2025-04-24
Update Änderung 2 am 2025-04-24
Update Änderung 3 am 2025-04-24
Update Änderung 4 am 2025-04-24
Update Änderung 5 am 2025-04-24
Update Änderung 6 am 2025-04-24
Refactor Änderung 1 am 2025-04-26
Refactor Änderung 2 am 2025-04-26
Refactor Änderung 3 am 2025-04-26
Refactor Änderung 4 am 2025-04-26
Cleanup Änderung 1 am 2025-04-27
Cleanup Änderung 2 am 2025-04-27
Cleanup Änderung 3 am 2025-04-27
Cleanup Änderung 4 am 2025-04-27
Cleanup Änderung 5 am 2025-04-27
Cleanup Änderung 6 am 2025-04-27
Cleanup Änderung 7 am 2025-04-27
Update Änderung 1 am 2025-04-27
Update Änderung 2 am 2025-04-27
Update Änderung 3 am 2025-04-27
Update Änderung 4 am 2025-04-27
Update Änderung 5 am 2025-04-27
Update Änderung 6 am 2025-04-27
Optimize Änderung 1 am 2025-04-28
Optimize Änderung 2 am 2025-04-28
Optimize Änderung 3 am 2025-04-28
Cleanup Änderung 1 am 2025-04-29
Cleanup Änderung 2 am 2025-04-29
Cleanup Änderung 3 am 2025-04-29
Cleanup Änderung 4 am 2025-04-29
Cleanup Änderung 5 am 2025-04-29
Cleanup Änderung 6 am 2025-04-29
Cleanup Änderung 1 am 2025-05-04
Cleanup Änderung 2 am 2025-05-04
Cleanup Änderung 3 am 2025-05-04
Optimize Änderung 1 am 2025-05-04
Optimize Änderung 2 am 2025-05-04
Optimize Änderung 3 am 2025-05-04
Optimize Änderung 1 am 2025-05-08
Optimize Änderung 2 am 2025-05-08
Optimize Änderung 3 am 2025-05-08
Cleanup Änderung 1 am 2025-05-09
Cleanup Änderung 2 am 2025-05-09
Cleanup Änderung 3 am 2025-05-09
Cleanup Änderung 4 am 2025-05-09
Cleanup Änderung 5 am 2025-05-09
Cleanup Änderung 6 am 2025-05-09
Optimize Änderung 1 am 2025-05-17
Optimize Änderung 2 am 2025-05-17
Optimize Änderung 3 am 2025-05-17
Cleanup Änderung 1 am 2025-05-20
Cleanup Änderung 2 am 2025-05-20
Cleanup Änderung 3 am 2025-05-20
Cleanup Änderung 4 am 2025-05-20
Cleanup Änderung 5 am 2025-05-20
Optimize Änderung 1 am 2025-05-21
Optimize Änderung 2 am 2025-05-21
Optimize Änderung 3 am 2025-05-21
Optimize Änderung 4 am 2025-05-21
Optimize Änderung 5 am 2025-05-21
Fix Änderung 1 am 2025-05-25
Fix Änderung 2 am 2025-05-25
Fix Änderung 3 am 2025-05-25
Fix Änderung 4 am 2025-05-25
Fix Änderung 5 am 2025-05-25
Fix Änderung 6 am 2025-05-25
Fix Änderung 1 am 2025-05-26
Fix Änderung 2 am 2025-05-26
Fix Änderung 3 am 2025-05-26
Improve Änderung 1 am 2025-05-28
Improve Änderung 2 am 2025-05-28
Improve Änderung 3 am 2025-05-28
Improve Änderung 4 am 2025-05-28
Improve Änderung 5 am 2025-05-28
Improve Änderung 6 am 2025-05-28
Improve Änderung 7 am 2025-05-28
Optimize Änderung 1 am 2025-05-31
Optimize Änderung 2 am 2025-05-31
Optimize Änderung 3 am 2025-05-31
Optimize Änderung 4 am 2025-05-31
Change Änderung 1 am 2025-06-01
Change Änderung 2 am 2025-06-01
Change Änderung 3 am 2025-06-01
Update Änderung 1 am 2025-06-03
Update Änderung 2 am 2025-06-03
Update Änderung 3 am 2025-06-03
Update Änderung 4 am 2025-06-03
Refactor Änderung 1 am 2025-06-03
Refactor Änderung 2 am 2025-06-03
Refactor Änderung 3 am 2025-06-03
Refactor Änderung 4 am 2025-06-03
Refactor Änderung 5 am 2025-06-03
Refactor Änderung 6 am 2025-06-03
Refactor Änderung 7 am 2025-06-03
Refactor Änderung 8 am 2025-06-03
Refactor Änderung 9 am 2025-06-03
Refactor Änderung 10 am 2025-06-03
Improve Änderung 1 am 2025-06-06
Improve Änderung 2 am 2025-06-06
Cleanup Änderung 1 am 2025-06-07
Cleanup Änderung 2 am 2025-06-07
Cleanup Änderung 3 am 2025-06-07
Cleanup Änderung 4 am 2025-06-07
Cleanup Änderung 5 am 2025-06-07
Cleanup Änderung 6 am 2025-06-07
Cleanup Änderung 7 am 2025-06-07
Refactor Änderung 1 am 2025-06-13
Refactor Änderung 2 am 2025-06-13
Refactor Änderung 3 am 2025-06-13
Refactor Änderung 4 am 2025-06-13
Cleanup Änderung 1 am 2025-06-14
Cleanup Änderung 2 am 2025-06-14
Cleanup Änderung 3 am 2025-06-14
Cleanup Änderung 4 am 2025-06-14
Cleanup Änderung 5 am 2025-06-14
Cleanup Änderung 6 am 2025-06-14
Cleanup Änderung 7 am 2025-06-14
Cleanup Änderung 8 am 2025-06-14
Improve Änderung 1 am 2025-06-17
Improve Änderung 2 am 2025-06-17
Change Änderung 1 am 2025-06-18
Change Änderung 2 am 2025-06-18
Refactor Änderung 1 am 2025-06-21
Refactor Änderung 2 am 2025-06-21
Refactor Änderung 3 am 2025-06-21
Refactor Änderung 4 am 2025-06-21
Refactor Änderung 5 am 2025-06-21
Refactor Änderung 6 am 2025-06-21
Refactor Änderung 7 am 2025-06-21
Optimize Änderung 1 am 2025-06-25
Optimize Änderung 2 am 2025-06-25
Optimize Änderung 3 am 2025-06-25
Optimize Änderung 4 am 2025-06-25
Optimize Änderung 5 am 2025-06-25
Update Änderung 1 am 2025-06-28
Update Änderung 2 am 2025-06-28
Update Änderung 3 am 2025-06-28
Update Änderung 4 am 2025-06-28
Update Änderung 5 am 2025-06-28
Update Änderung 6 am 2025-06-28
Update Änderung 7 am 2025-06-28
Cleanup Änderung 1 am 2025-07-01
Improve Änderung 1 am 2025-07-03
Improve Änderung 2 am 2025-07-03
Update Änderung 1 am 2025-07-06
Update Änderung 2 am 2025-07-06
Update Änderung 3 am 2025-07-06
Update Änderung 4 am 2025-07-06
Change Änderung 1 am 2025-07-07
Update Änderung 1 am 2025-07-10
Update Änderung 2 am 2025-07-10
Improve Änderung 1 am 2025-07-13
Improve Änderung 2 am 2025-07-13
Improve Änderung 3 am 2025-07-13
Improve Änderung 4 am 2025-07-13
Refactor Änderung 1 am 2025-07-13
Refactor Änderung 2 am 2025-07-13
Refactor Änderung 3 am 2025-07-13
Optimize Änderung 1 am 2025-07-16
Optimize Änderung 2 am 2025-07-16
Optimize Änderung 3 am 2025-07-16
Refactor Änderung 1 am 2025-07-16
Refactor Änderung 2 am 2025-07-16
Refactor Änderung 3 am 2025-07-16
Refactor Änderung 4 am 2025-07-16
Optimize Änderung 1 am 2025-07-27
Optimize Änderung 2 am 2025-07-27
Optimize Änderung 3 am 2025-07-27
Optimize Änderung 4 am 2025-07-27
Cleanup Änderung 1 am 2025-08-01
Cleanup Änderung 2 am 2025-08-01
Cleanup Änderung 3 am 2025-08-01
Cleanup Änderung 4 am 2025-08-01
Cleanup Änderung 5 am 2025-08-01
Cleanup Änderung 6 am 2025-08-01
Change Änderung 1 am 2025-08-06
Change Änderung 2 am 2025-08-06
Add Änderung 1 am 2025-08-10
Add Änderung 2 am 2025-08-10
Add Änderung 3 am 2025-08-10
Add Änderung 4 am 2025-08-10
Add Änderung 5 am 2025-08-10
Add Änderung 6 am 2025-08-10
