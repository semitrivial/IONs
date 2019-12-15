TEMPLATE = get_file('w^3.py').replace('=\""', '=\"""X4"""')

X4=""

while True:
    output(X4)
    X4 = TEMPLATE.replace("X4", escape(X4))