# having a function with return variables

def my_func():
    result = 3 * 2
    return result

output = my_func()
print(output)

def format_name(fname, lname):
    """User triple quotation marks to include docstrings
    Mainly used to describe what the function does"""
    result = fname + " " + lname
    return result.title()

formatted_name = format_name("my", "name")
print(f"Formatted name: {formatted_name}")

def outer_func(a, b):
    def inner_func(c, d):
        return c + d

    return inner_func(a, b)

result = outer_func(5, 10)
print(result)