X = get_file('w^2+w.py')

while True:
    output(X)
    X = "output('''" + escape(X) + "''')"