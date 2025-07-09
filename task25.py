from typing import Union

def group_by_age(people: list[dict[str, int | str]]) -> dict[int, list[str]]:
    group = {}
    for person in people:
        group.setdefault(person['age'], []).append(person['name'])
        return group
    

people = [{  'name':'Laziz','age':'23'},{'name': 'Ali','age':'25'}]
result = group_by_age(people)
print(result)
