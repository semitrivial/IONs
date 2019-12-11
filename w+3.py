output("""
output('''
output(\"""
X=""

while True:
    output(X)
    X = "output('" + escape(X) + "')"
\""")
''')
""")