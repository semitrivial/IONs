# And to get from ω+2 to ω+3, we write a program which outputs
# the program which we used to notate ω+2.
#
# It sure is fun using character-escape codes to embed quotation
# marks within quotation marks within quotation marks!
output("""
output(\"\"\"
output(\\\"\\\"\\\"
X=\\\\\\\"\\\\\\\"

while True:
    output(X)
    X = \\\\\\\"output(\\\\\\\'\\\\\\\" + escape(X) + \\\\\\\"\\\\\\\')\\\\\\\"
\\\"\\\"\\\")
\"\"\")
""")