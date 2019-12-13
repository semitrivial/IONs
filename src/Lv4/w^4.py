TEMPLATE=get_file('w^3.py')
TEMPLATE=TEMPLATE.replace('X=""', "X='''{}'''")
X=""
while True:
    output(X)
    X = TEMPLATE.format("{}", "{}", escape(X))