from textwrap import dedent

def generate_git_script(id):
    script = f"""
    if [ ! -d {id} ]; then
        git clone https://github.com/{id}/project {id}
    else
        (cd {id}; git pull)
    fi
    """
    return dedent(script).strip()

print(generate_git_script(233))

def foo():
    string = """
    a
    b
    c
    """
    return dedent(string).strip()
print(foo())