def group_students(students: list[dict[str, str]]) -> dict[str, list[str]]:
    group = dict()
    for student in students:
        group_name = student['group']
        if group_name not in group.keys():
            group[group_name] = []

            group[group_name].append(student['name'])

            return group
        
students = [
    {'name':'Laziz',
     'group':'A'
    },
    {'name':'Ahmad',
     'group':'B'
     },
     {'name':'Bobur',
      'group':'A'
     },]
result = group_students(students)
print(result)
