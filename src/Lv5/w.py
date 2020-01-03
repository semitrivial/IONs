## w.py
# We notate ω by starting with the notation for 1, replacing
# the initial value of X0 by a wildcard X1, and then repeatedly
# plugging the resulting template into itself. Convince yourself
# the first few outputs of this program notate 0, 1, 2, ...
TEMPLATE = get_file('1.py').replace('=\""', '=\"""X1"""')

X1=""

while True:
    output(X1)
    X1 = TEMPLATE.replace("X1", escape(X1))