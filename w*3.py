X=get_file('w*2.py')

while True:
    output(X)
    X = "output(\"\"\"\n" + escape(X) + "\n\"\"\")"