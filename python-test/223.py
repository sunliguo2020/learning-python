r1 = {"name": "高效益", "age": 18}
r2 = {"name": "高er", "age": 19}
print(f'r1:{type(r1)}')


tb = (r1, r2)
print(f'tb:{type(tb)}')
print(f"tb[1]:{type(tb[1])}")
print(tb[1].get('age'))
