def search_json(data, key, value):
    if isinstance(data, list):
        return [item for item in data if item.get(key) == value]
    raise ValueError("Data must be a list of dictionaries.")

def search_xml(root, tag, value):
    return [elem for elem in root.findall(tag) if elem.text == value]
Add am 2025-02-06
Change am 2025-02-10
Refactor am 2025-02-15
Fix am 2025-02-17
Refactor am 2025-03-03
Cleanup am 2025-03-04
Improve am 2025-03-06
Refactor am 2025-03-13
Improve am 2025-03-15
Improve am 2025-03-17
Change am 2025-03-20
Cleanup am 2025-03-26
Fix am 2025-03-27
Update am 2025-04-01
Improve am 2025-04-06
Optimize am 2025-04-08
Fix am 2025-04-12
Optimize am 2025-04-16
Cleanup am 2025-04-23
Cleanup am 2025-04-26
Fix am 2025-04-30
Improve am 2025-05-03
Refactor am 2025-05-09
Optimize am 2025-05-25
Improve am 2025-05-26
Cleanup am 2025-05-28
Fix am 2025-05-31
Refactor am 2025-06-01
Change am 2025-06-05
Update am 2025-06-06
Update am 2025-06-07
Cleanup am 2025-06-09
Cleanup am 2025-06-20
Change am 2025-06-25
Change am 2025-06-26
Optimize am 2025-06-27
Add am 2025-07-02
Optimize am 2025-07-06
Optimize am 2025-07-17
Optimize am 2025-07-23
Update am 2025-07-26
Add am 2025-07-28
Update am 2025-07-29
Fix am 2025-07-31
Fix am 2025-08-03
Update Änderung 1 am 2025-02-08
Update Änderung 2 am 2025-02-08
Update Änderung 3 am 2025-02-08
Add Änderung 1 am 2025-02-12
Add Änderung 2 am 2025-02-12
Add Änderung 3 am 2025-02-12
Add Änderung 1 am 2025-02-14
Add Änderung 2 am 2025-02-14
Add Änderung 3 am 2025-02-14
Add Änderung 4 am 2025-02-14
Add Änderung 5 am 2025-02-14
Add Änderung 6 am 2025-02-14
Refactor Änderung 1 am 2025-02-16
Refactor Änderung 2 am 2025-02-16
Cleanup Änderung 1 am 2025-02-18
Cleanup Änderung 2 am 2025-02-18
Cleanup Änderung 3 am 2025-02-18
Fix Änderung 1 am 2025-02-19
Fix Änderung 2 am 2025-02-19
Fix Änderung 3 am 2025-02-19
Fix Änderung 4 am 2025-02-19
Fix Änderung 5 am 2025-02-19
Update Änderung 1 am 2025-02-26
Update Änderung 2 am 2025-02-26
Cleanup Änderung 1 am 2025-02-28
Improve Änderung 1 am 2025-02-28
Add Änderung 1 am 2025-03-09
Add Änderung 2 am 2025-03-09
Add Änderung 3 am 2025-03-09
Add Änderung 4 am 2025-03-09
Add Änderung 5 am 2025-03-09
Add Änderung 6 am 2025-03-09
Add Änderung 7 am 2025-03-09
Add Änderung 8 am 2025-03-09
Add Änderung 9 am 2025-03-09
Update Änderung 1 am 2025-03-12
Update Änderung 1 am 2025-03-16
Update Änderung 2 am 2025-03-16
Update Änderung 1 am 2025-03-19
Update Änderung 2 am 2025-03-19
Update Änderung 3 am 2025-03-19
Optimize Änderung 1 am 2025-03-20
Optimize Änderung 2 am 2025-03-20
Optimize Änderung 3 am 2025-03-20
Optimize Änderung 4 am 2025-03-20
Optimize Änderung 5 am 2025-03-20
Optimize Änderung 6 am 2025-03-20
Improve Änderung 1 am 2025-03-20
Improve Änderung 2 am 2025-03-20
Fix Änderung 1 am 2025-03-22
Improve Änderung 1 am 2025-03-25
Improve Änderung 2 am 2025-03-25
Change Änderung 1 am 2025-03-28
Change Änderung 2 am 2025-03-28
Change Änderung 3 am 2025-03-28
Change Änderung 4 am 2025-03-28
Change Änderung 5 am 2025-03-28
Change Änderung 6 am 2025-03-28
Change Änderung 7 am 2025-03-28
Optimize Änderung 1 am 2025-04-01
Optimize Änderung 2 am 2025-04-01
Cleanup Änderung 1 am 2025-04-05
Cleanup Änderung 2 am 2025-04-05
Cleanup Änderung 3 am 2025-04-05
Cleanup Änderung 4 am 2025-04-05
Cleanup Änderung 5 am 2025-04-05
Refactor Änderung 1 am 2025-04-06
Refactor Änderung 2 am 2025-04-06
Refactor Änderung 3 am 2025-04-06
Cleanup Änderung 1 am 2025-04-09
Cleanup Änderung 1 am 2025-04-10
Cleanup Änderung 2 am 2025-04-10
Cleanup Änderung 3 am 2025-04-10
Cleanup Änderung 4 am 2025-04-10
Cleanup Änderung 5 am 2025-04-10
Cleanup Änderung 6 am 2025-04-10
Change Änderung 1 am 2025-04-17
Change Änderung 2 am 2025-04-17
Optimize Änderung 1 am 2025-04-19
Optimize Änderung 2 am 2025-04-19
Optimize Änderung 3 am 2025-04-19
Optimize Änderung 4 am 2025-04-19
Optimize Änderung 5 am 2025-04-19
Change Änderung 1 am 2025-04-20
Change Änderung 2 am 2025-04-20
Change Änderung 3 am 2025-04-20
Change Änderung 4 am 2025-04-20
Improve Änderung 1 am 2025-04-23
Improve Änderung 2 am 2025-04-23
Refactor Änderung 1 am 2025-04-23
Refactor Änderung 2 am 2025-04-23
Refactor Änderung 3 am 2025-04-23
Update Änderung 1 am 2025-04-24
Update Änderung 2 am 2025-04-24
Update Änderung 3 am 2025-04-24
Update Änderung 4 am 2025-04-24
Update Änderung 5 am 2025-04-24
Update Änderung 6 am 2025-04-24
Fix Änderung 1 am 2025-04-26
Fix Änderung 1 am 2025-04-27
Optimize Änderung 1 am 2025-04-30
Optimize Änderung 2 am 2025-04-30
Optimize Änderung 3 am 2025-04-30
Improve Änderung 1 am 2025-05-01
Improve Änderung 2 am 2025-05-01
Improve Änderung 3 am 2025-05-01
Improve Änderung 4 am 2025-05-01
Improve Änderung 5 am 2025-05-01
Add Änderung 1 am 2025-05-03
Add Änderung 2 am 2025-05-03
Add Änderung 3 am 2025-05-03
Add Änderung 4 am 2025-05-03
Add Änderung 5 am 2025-05-03
Add Änderung 1 am 2025-05-07
Add Änderung 2 am 2025-05-07
Add Änderung 3 am 2025-05-07
Add Änderung 4 am 2025-05-07
Add Änderung 5 am 2025-05-07
Add Änderung 6 am 2025-05-07
Change Änderung 1 am 2025-05-08
Change Änderung 2 am 2025-05-08
Change Änderung 3 am 2025-05-08
Change Änderung 1 am 2025-05-13
Change Änderung 2 am 2025-05-13
Change Änderung 3 am 2025-05-13
Change Änderung 4 am 2025-05-13
Change Änderung 5 am 2025-05-13
Change Änderung 1 am 2025-05-13
Change Änderung 2 am 2025-05-13
Cleanup Änderung 1 am 2025-05-14
Cleanup Änderung 2 am 2025-05-14
Cleanup Änderung 3 am 2025-05-14
Cleanup Änderung 4 am 2025-05-14
Refactor Änderung 1 am 2025-05-14
Refactor Änderung 2 am 2025-05-14
Add Änderung 1 am 2025-05-20
Add Änderung 2 am 2025-05-20
Add Änderung 3 am 2025-05-20
Add Änderung 4 am 2025-05-20
Add Änderung 5 am 2025-05-20
Add Änderung 1 am 2025-05-28
Add Änderung 2 am 2025-05-28
Add Änderung 3 am 2025-05-28
Add Änderung 4 am 2025-05-28
Add Änderung 5 am 2025-05-28
Add Änderung 6 am 2025-05-28
Refactor Änderung 1 am 2025-05-28
Refactor Änderung 2 am 2025-05-28
Refactor Änderung 3 am 2025-05-28
Refactor Änderung 4 am 2025-05-28
Add Änderung 1 am 2025-05-29
Add Änderung 2 am 2025-05-29
Add Änderung 3 am 2025-05-29
Add Änderung 4 am 2025-05-29
Add Änderung 1 am 2025-05-29
Add Änderung 2 am 2025-05-29
Fix Änderung 1 am 2025-05-31
Update Änderung 1 am 2025-05-31
Update Änderung 2 am 2025-05-31
Update Änderung 3 am 2025-05-31
Update Änderung 4 am 2025-05-31
Update Änderung 5 am 2025-05-31
Refactor Änderung 1 am 2025-05-31
Refactor Änderung 2 am 2025-05-31
Refactor Änderung 3 am 2025-05-31
Refactor Änderung 1 am 2025-06-03
Refactor Änderung 1 am 2025-06-10
Update Änderung 1 am 2025-06-15
Update Änderung 2 am 2025-06-15
Update Änderung 3 am 2025-06-15
Update Änderung 4 am 2025-06-15
Update Änderung 5 am 2025-06-15
Improve Änderung 1 am 2025-06-17
Improve Änderung 1 am 2025-06-19
Improve Änderung 1 am 2025-06-20
Improve Änderung 2 am 2025-06-20
Improve Änderung 3 am 2025-06-20
Improve Änderung 4 am 2025-06-20
Improve Änderung 5 am 2025-06-20
Improve Änderung 6 am 2025-06-20
Optimize Änderung 1 am 2025-06-20
Optimize Änderung 2 am 2025-06-20
Optimize Änderung 3 am 2025-06-20
Optimize Änderung 4 am 2025-06-20
Update Änderung 1 am 2025-06-26
Update Änderung 2 am 2025-06-26
Update Änderung 3 am 2025-06-26
Add Änderung 1 am 2025-06-28
Add Änderung 2 am 2025-06-28
Add Änderung 3 am 2025-06-28
Add Änderung 4 am 2025-06-28
Optimize Änderung 1 am 2025-06-30
Optimize Änderung 2 am 2025-06-30
Change Änderung 1 am 2025-07-01
Change Änderung 2 am 2025-07-01
Change Änderung 3 am 2025-07-01
Change Änderung 4 am 2025-07-01
Change Änderung 5 am 2025-07-01
Cleanup Änderung 1 am 2025-07-10
Cleanup Änderung 2 am 2025-07-10
Refactor Änderung 1 am 2025-07-13
Refactor Änderung 2 am 2025-07-13
Refactor Änderung 3 am 2025-07-13
Refactor Änderung 4 am 2025-07-13
Refactor Änderung 5 am 2025-07-13
Cleanup Änderung 1 am 2025-07-14
Cleanup Änderung 2 am 2025-07-14
Cleanup Änderung 3 am 2025-07-14
Cleanup Änderung 4 am 2025-07-14
Cleanup Änderung 5 am 2025-07-14
Cleanup Änderung 6 am 2025-07-14
Change Änderung 1 am 2025-07-24
Change Änderung 2 am 2025-07-24
Change Änderung 3 am 2025-07-24
Change Änderung 4 am 2025-07-24
Change Änderung 5 am 2025-07-24
Change Änderung 6 am 2025-07-24
Change Änderung 7 am 2025-07-24
Change Änderung 8 am 2025-07-24
Update Änderung 1 am 2025-07-24
Update Änderung 2 am 2025-07-24
Update Änderung 3 am 2025-07-24
Update Änderung 4 am 2025-07-24
Update Änderung 5 am 2025-07-24
Change Änderung 1 am 2025-07-29
Change Änderung 2 am 2025-07-29
Update Änderung 1 am 2025-07-30
Update Änderung 2 am 2025-07-30
Update Änderung 3 am 2025-07-30
Update Änderung 4 am 2025-07-30
Update Änderung 5 am 2025-07-30
Optimize Änderung 1 am 2025-07-31
Optimize Änderung 2 am 2025-07-31
Optimize Änderung 3 am 2025-07-31
Optimize Änderung 4 am 2025-07-31
Optimize Änderung 5 am 2025-07-31
Optimize Änderung 6 am 2025-07-31
Add Änderung 1 am 2025-08-06
Improve Änderung 1 am 2025-08-07
Improve Änderung 2 am 2025-08-07
Improve Änderung 3 am 2025-08-07
Improve Änderung 4 am 2025-08-07
Cleanup Änderung 1 am 2025-08-08
Cleanup Änderung 2 am 2025-08-08
Cleanup Änderung 3 am 2025-08-08
Cleanup Änderung 4 am 2025-08-08
Cleanup Änderung 5 am 2025-08-08
Cleanup Änderung 6 am 2025-08-08
Fix Änderung 1 am 2025-08-09
Fix Änderung 2 am 2025-08-09
Refactor Änderung 1 am 2025-02-02
Refactor Änderung 2 am 2025-02-02
Refactor Änderung 3 am 2025-02-02
Refactor Änderung 4 am 2025-02-02
Refactor Änderung 5 am 2025-02-02
Add Änderung 1 am 2025-02-05
Add Änderung 2 am 2025-02-05
Add Änderung 3 am 2025-02-05
Add Änderung 1 am 2025-02-06
Update Änderung 1 am 2025-02-07
Update Änderung 2 am 2025-02-07
Update Änderung 3 am 2025-02-07
Improve Änderung 1 am 2025-02-04
Improve Änderung 2 am 2025-02-04
Improve Änderung 3 am 2025-02-04
Improve Änderung 4 am 2025-02-04
Improve Änderung 5 am 2025-02-04
Cleanup Änderung 1 am 2025-02-05
Cleanup Änderung 2 am 2025-02-05
Cleanup Änderung 3 am 2025-02-05
Optimize Änderung 1 am 2025-02-07
Optimize Änderung 2 am 2025-02-07
Optimize Änderung 3 am 2025-02-07
Update Änderung 1 am 2025-02-08
Update Änderung 2 am 2025-02-08
Update Änderung 3 am 2025-02-08
Refactor Änderung 1 am 2025-02-09
Optimize Änderung 1 am 2025-02-17
Optimize Änderung 2 am 2025-02-17
Optimize Änderung 3 am 2025-02-17
Optimize Änderung 1 am 2025-02-19
Optimize Änderung 2 am 2025-02-19
Optimize Änderung 3 am 2025-02-19
Optimize Änderung 4 am 2025-02-19
Cleanup Änderung 1 am 2025-02-21
Cleanup Änderung 2 am 2025-02-21
Cleanup Änderung 3 am 2025-02-21
Cleanup Änderung 4 am 2025-02-21
Refactor Änderung 1 am 2025-02-22
Refactor Änderung 2 am 2025-02-22
Fix Änderung 1 am 2025-02-23
Fix Änderung 2 am 2025-02-23
Fix Änderung 3 am 2025-02-23
Improve Änderung 1 am 2025-02-25
Improve Änderung 2 am 2025-02-25
Improve Änderung 3 am 2025-02-25
Improve Änderung 4 am 2025-02-25
Improve Änderung 5 am 2025-02-25
Improve Änderung 6 am 2025-02-25
Refactor Änderung 1 am 2025-02-26
Cleanup Änderung 1 am 2025-03-10
Cleanup Änderung 2 am 2025-03-10
Cleanup Änderung 3 am 2025-03-10
Cleanup Änderung 4 am 2025-03-10
Update Änderung 1 am 2025-03-11
Update Änderung 2 am 2025-03-11
Update Änderung 3 am 2025-03-11
Update Änderung 4 am 2025-03-11
Update Änderung 5 am 2025-03-11
Update Änderung 6 am 2025-03-11
Fix Änderung 1 am 2025-03-13
Fix Änderung 2 am 2025-03-13
Fix Änderung 3 am 2025-03-13
Fix Änderung 4 am 2025-03-13
Fix Änderung 5 am 2025-03-13
Fix Änderung 1 am 2025-03-17
Fix Änderung 2 am 2025-03-17
Fix Änderung 3 am 2025-03-17
Fix Änderung 4 am 2025-03-17
Fix Änderung 5 am 2025-03-17
Refactor Änderung 1 am 2025-03-22
Refactor Änderung 2 am 2025-03-22
Refactor Änderung 3 am 2025-03-22
Refactor Änderung 4 am 2025-03-22
Optimize Änderung 1 am 2025-03-23
Optimize Änderung 2 am 2025-03-23
Improve Änderung 1 am 2025-03-24
Improve Änderung 2 am 2025-03-24
Optimize Änderung 1 am 2025-03-25
Optimize Änderung 2 am 2025-03-25
Optimize Änderung 3 am 2025-03-25
Optimize Änderung 4 am 2025-03-25
Optimize Änderung 5 am 2025-03-25
Optimize Änderung 6 am 2025-03-25
Optimize Änderung 1 am 2025-04-02
Optimize Änderung 2 am 2025-04-02
Optimize Änderung 3 am 2025-04-02
Optimize Änderung 4 am 2025-04-02
Update Änderung 1 am 2025-04-03
Update Änderung 2 am 2025-04-03
Update Änderung 3 am 2025-04-03
Update Änderung 4 am 2025-04-03
Update Änderung 1 am 2025-04-06
Update Änderung 2 am 2025-04-06
Update Änderung 3 am 2025-04-06
Update Änderung 4 am 2025-04-06
Update Änderung 5 am 2025-04-06
Add Änderung 1 am 2025-04-06
Add Änderung 2 am 2025-04-06
Add Änderung 3 am 2025-04-06
Add Änderung 4 am 2025-04-06
Add Änderung 5 am 2025-04-06
Add Änderung 6 am 2025-04-06
Add Änderung 7 am 2025-04-06
Cleanup Änderung 1 am 2025-04-10
Cleanup Änderung 2 am 2025-04-10
Cleanup Änderung 3 am 2025-04-10
Cleanup Änderung 4 am 2025-04-10
Change Änderung 1 am 2025-04-12
Change Änderung 2 am 2025-04-12
Improve Änderung 1 am 2025-04-21
Improve Änderung 2 am 2025-04-21
Improve Änderung 1 am 2025-04-22
Improve Änderung 2 am 2025-04-22
Optimize Änderung 1 am 2025-04-22
Optimize Änderung 2 am 2025-04-22
Optimize Änderung 3 am 2025-04-22
Optimize Änderung 4 am 2025-04-22
Add Änderung 1 am 2025-04-23
Add Änderung 2 am 2025-04-23
Add Änderung 3 am 2025-04-23
Add Änderung 4 am 2025-04-23
Add Änderung 5 am 2025-04-23
Add Änderung 6 am 2025-04-23
Refactor Änderung 1 am 2025-04-26
Refactor Änderung 2 am 2025-04-26
Refactor Änderung 3 am 2025-04-26
Refactor Änderung 4 am 2025-04-26
Refactor Änderung 5 am 2025-04-26
Refactor Änderung 1 am 2025-04-29
Refactor Änderung 2 am 2025-04-29
Improve Änderung 1 am 2025-04-29
Improve Änderung 2 am 2025-04-29
Improve Änderung 3 am 2025-04-29
Add Änderung 1 am 2025-04-30
Add Änderung 2 am 2025-04-30
Optimize Änderung 1 am 2025-05-03
Optimize Änderung 2 am 2025-05-03
Cleanup Änderung 1 am 2025-05-03
Cleanup Änderung 2 am 2025-05-03
Cleanup Änderung 3 am 2025-05-03
Fix Änderung 1 am 2025-05-04
Fix Änderung 2 am 2025-05-04
Fix Änderung 3 am 2025-05-04
Fix Änderung 4 am 2025-05-04
Fix Änderung 5 am 2025-05-04
Fix Änderung 6 am 2025-05-04
Add Änderung 1 am 2025-05-05
Add Änderung 2 am 2025-05-05
Optimize Änderung 1 am 2025-05-08
Optimize Änderung 2 am 2025-05-08
Optimize Änderung 3 am 2025-05-08
Optimize Änderung 4 am 2025-05-08
Optimize Änderung 5 am 2025-05-08
Optimize Änderung 6 am 2025-05-08
Update Änderung 1 am 2025-05-13
Update Änderung 2 am 2025-05-13
Update Änderung 3 am 2025-05-13
Update Änderung 4 am 2025-05-13
Update Änderung 5 am 2025-05-13
Cleanup Änderung 1 am 2025-05-14
Cleanup Änderung 2 am 2025-05-14
Improve Änderung 1 am 2025-05-20
Improve Änderung 1 am 2025-05-26
Improve Änderung 2 am 2025-05-26
Improve Änderung 3 am 2025-05-26
Improve Änderung 4 am 2025-05-26
Improve Änderung 5 am 2025-05-26
Cleanup Änderung 1 am 2025-05-27
Cleanup Änderung 2 am 2025-05-27
Cleanup Änderung 3 am 2025-05-27
Cleanup Änderung 4 am 2025-05-27
Refactor Änderung 1 am 2025-05-29
Refactor Änderung 2 am 2025-05-29
Refactor Änderung 3 am 2025-05-29
Refactor Änderung 4 am 2025-05-29
Improve Änderung 1 am 2025-06-06
Fix Änderung 1 am 2025-06-08
Fix Änderung 2 am 2025-06-08
Fix Änderung 3 am 2025-06-08
Fix Änderung 4 am 2025-06-08
Fix Änderung 5 am 2025-06-08
Fix Änderung 6 am 2025-06-08
Fix Änderung 7 am 2025-06-08
Optimize Änderung 1 am 2025-06-08
Optimize Änderung 2 am 2025-06-08
Optimize Änderung 3 am 2025-06-08
Optimize Änderung 4 am 2025-06-08
Optimize Änderung 5 am 2025-06-08
Update Änderung 1 am 2025-06-09
Update Änderung 2 am 2025-06-09
Update Änderung 3 am 2025-06-09
Update Änderung 4 am 2025-06-09
Fix Änderung 1 am 2025-06-12
Fix Änderung 2 am 2025-06-12
Cleanup Änderung 1 am 2025-06-17
Cleanup Änderung 2 am 2025-06-17
Cleanup Änderung 3 am 2025-06-17
Cleanup Änderung 4 am 2025-06-17
