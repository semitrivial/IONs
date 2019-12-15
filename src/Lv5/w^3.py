TEMPLATE = get_file('w^2.py').replace('=\""', '=\"""X3"""')

X3=""

while True:
    output(X3)
    X3 = TEMPLATE.replace("X3", escape(X3))