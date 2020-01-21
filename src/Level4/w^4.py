## w^4.py
# The below program is obtained by meditating upon
# w^3.py, w^3*2.py, w^3*3.py, figuring out the pattern,
# and generalizing the pattern. Note that TEMPLATE
# already contains wildcards '___' and '***'. We take
# the X="" from w^3.py and replace it with a new
# wildcard, X='''!!!'''. This is to ensure we can
# replace the outermost wildcard without accidentally
# replacing the deeper two wildcards.
# Verify that the first few outputs of this program
# notate 0, ω^3, ω^3*2, ω^3*3. By induction, this
# program notates ω^3*ω, i.e., ω^4.
TEMPLATE=<INSERT_FILE w^3.py>
TEMPLATE=TEMPLATE.replace('X=""', "X='''!!!'''")
X=""
while True:
    output(X)
    X = TEMPLATE.replace("!!!", escape(X))