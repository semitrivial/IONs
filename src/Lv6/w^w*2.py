# x[0] = w^w
# x[1][0] = 0
# x[1][1] = w^w
# x[1][2][0] = 1
# x[1][2][1] = w
# x[1][2][2] = w^2
# x[1][2][3] = w^3
# x[1][2] = w^w
# x[1][3] = w^w ....?
# x[2][0] = 0
# x[2][1][0] = 0
# x[2][1][1] = w^w
# x[2][2][0][0] = 0
# x[2][2][0][1] = w^w
# x[2][2][0][2] = w^w

X=get_file('w^w.py')

i = 0
while True:
    output(X)
    Xa = "X" + str(i)
    Xb = "X" + str(i+1)
    X = """
TEMPLATE = '''"""+escape(X)+"""'''
TEMPLATE = TEMPLATE.replace('"""+Xa+"""=""', '"""+Xa+"""=\"\"\""""+Xb+"""\"\"\"')

"""+Xb+"""=""

while True:
    output("""+Xb+""")
    """+Xb+""" = TEMPLATE.replace(\""""+Xb+"""\", escape("""+Xb+"""))
"""
    i += 1