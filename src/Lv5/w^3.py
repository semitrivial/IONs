TEMPLATE=get_file("w^2.py")
TEMPLATE=TEMPLATE.replace('X2=""', 'X2="""X3"""')

X3=""

while True:
    output(X3)
    X3 = TEMPLATE.replace("X3", escape(X3))