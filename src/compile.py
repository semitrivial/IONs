import os
from util import escape

top_level = 5

def compile_level(n):
    level = "Lv" + str(n)
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
            fp.write(compiled_files[fname])

def compile_file(level, fname, compiled_files):
    if fname in compiled_files:
        return

    start_token, end_token = "get_file('", "')"

    with open(level + "/" + fname) as fp:
        raw = fp.read()

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



