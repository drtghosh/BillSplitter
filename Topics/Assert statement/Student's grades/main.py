def grades(x):
    possible_grades = 'ABCDF'
    assert x in possible_grades
    return f"You have got {x}"