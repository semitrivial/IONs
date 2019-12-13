TEMPLATE='''
output("""
X0
""")
'''

X1=""

while True:
    output(X1)
    X1 = TEMPLATE.replace("X0", escape(X1))