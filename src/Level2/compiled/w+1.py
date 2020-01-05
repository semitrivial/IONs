# w+1.py
output("""
X=\"\"

while True:
    output(X)
    X = \"output(\'\" + escape(X) + \"\')\"
""")