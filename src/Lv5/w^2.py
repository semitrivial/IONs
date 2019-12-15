TEMPLATE = get_file('w.py')
TEMPLATE = TEMPLATE.replace('=\""', '=\"""X2"""')

X2=""

while True:
    output(X2)
    X2 = TEMPLATE.replace("X2", escape(X2))