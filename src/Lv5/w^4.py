## w^4.py
# We notate ω^4 by starting with the notation for ω^3, replacing
# the initial value of X3 by a wildcard X4, and then repeatedly
# plugging the resulting template into itself. Convince yourself
# the first few outputs of this program notate 0, ω^3, ω^3*2, ω^3*3, ...
TEMPLATE = get_file('w^3.py').replace('=\""', '=\"""X4"""')

X4=""

while True:
    output(X4)
    X4 = TEMPLATE.replace("X4", escape(X4))