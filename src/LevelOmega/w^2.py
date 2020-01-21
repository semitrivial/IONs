## w^2.py
# We notate ω^2 by starting with the notation for ω, replacing
# the initial value of X1 by a wildcard X2, and then repeatedly
# plugging the resulting template into itself. Convince yourself
# the first few outputs of this program notate 0, ω, ω*2, ω*3, ...
TEMPLATE = <INSERT_FILE w.py>.replace('=\""', '=\"""X2"""')

X2=""

while True:
    output(X2)
    X2 = TEMPLATE.replace("X2", escape(X2))