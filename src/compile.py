import os
from util import escape

top_level = 5

STANDALONE_PREAMBLE = """
def escape(s):
    return s.replace('\\\\', '\\\\\\\\').replace('"', '\\\\"').replace("'", "\\\\'")
def output(x):
    print('PREAMBLE=\\\"\\\"\\\"')
    print(escape(PREAMBLE).strip())
    print('\\\"\\\"\\\"')
    print('exec(PREAMBLE)')
    print(x)
    try:
        input("---- (Press enter to continue) ----")
    except Exception:
        pass
"""

def compile_level(n):
    level = "Level" + (str(n) if n<5 else "Omega")
    compiled_files = {}

    for fname in os.listdir(level):
        if not(fname.endswith(".py")):
            continue
        if fname == 'test.py' or fname == '__init__.py':
            continue
        compile_file(level, fname, compiled_files)

    try:
        os.mkdir(level + "/compiled")
    except Exception:
        pass

    for fname in compiled_files.keys():
        with open(level + "/compiled/" + fname, "w") as fp:
            fp.write("# " + fname + "\n")
            fp.write(compiled_files[fname])
        with open(level + "/standalone/" + fname, "w") as fp:
            fp.write("# " + fname + "\n")
            fp.write("# This version of the file is completely standalone.\n")
            fp.write("# You can actually run it in python, completely on its own,\n")
            fp.write("# and you can run its outputs, and their outputs, etc.\n")
            fp.write("PREAMBLE = \"\"\"\n")
            fp.write(escape(STANDALONE_PREAMBLE).strip() + "\n")
            fp.write("\"\"\"\n")
            fp.write("exec(PREAMBLE)\n\n")
            fp.write(compiled_files[fname])

def compile_file(level, fname, compiled_files):
    if fname in compiled_files:
        return

    start_token, end_token = "<INSERT_FILE ", ">"

    with open(level + "/" + fname) as fp:
        raw = fp.read()

    raw = strip_comments(raw)

    while True:
        try:
            get_file_index = raw.index(start_token)
        except Exception:
            compiled_files[fname] = raw
            return

        end = raw[get_file_index+len(start_token):].index(end_token)
        sub_file = raw[get_file_index+len(start_token):][:end]
        compile_file(level, sub_file, compiled_files)

        sub_contents = compiled_files[sub_file]

        left = raw[:get_file_index]
        right = raw[get_file_index+end+len(start_token)+len(end_token):]
        raw = left + '"""\n' + escape(sub_contents) + '\n"""' + right

def compile_files():
    for i in range(top_level):
        compile_level(i+1)

def strip_comments(txt):
    lines = txt.splitlines()
    lines = [line for line in lines if not(line.startswith('#'))]
    return "\n".join(lines)


