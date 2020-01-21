## w^3.py
# We notate ω^3 by starting with the notation for ω^2, replacing
# the initial value of X2 by a wildcard X3, and then repeatedly
# plugging the resulting template into itself. Convince yourself
# the first few outputs of this program notate 0, ω^2, ω^2*2, ω^2*3, ...
TEMPLATE = <INSERT_FILE w^2.py>.replace('=\""', '=\"""X3"""')

X3=""

while True:
    output(X3)
    X3 = TEMPLATE.replace("X3", escape(X3))