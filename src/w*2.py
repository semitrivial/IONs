X=get_file('w.py')

while True:
    output(X)
    X = "output('''" + escape(X) + "''')"