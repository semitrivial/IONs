TEMPLATE='''
output("""
X1
""")
'''

X1=""

while True:
    output(X1)
    X1 = TEMPLATE.replace("X1", escape(X1))