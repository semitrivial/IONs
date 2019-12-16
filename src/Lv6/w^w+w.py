TEMPLATE = get_file('1.py').replace('=\""', '=\"""X1"""')

X1=get_file('w^w.py')

while True:
    output(X1)
    X1 = TEMPLATE.replace("X1", escape(X1))