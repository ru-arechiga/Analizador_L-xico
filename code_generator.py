import random
import string

def generate_random_comment():
    """Generates a random comment of random length between 5 and 30 characters."""
    length = random.randint(5, 30)
    comment_text = ''.join(random.choices(string.ascii_letters + string.digits + " ", k=length))
    return f"// {comment_text}"

def generate_random_declaration():
    """Generates a random float or integer declaration."""
    declarations = ["f", "i"]  # float or int declaration
    variable = random.choice(["a", "b", "c", "x", "y", "z"])  # Random variable names
    return f"{random.choice(declarations)} {variable}"

def generate_random_assignment():
    """Generates a random assignment with either integer or float values."""
    variable = random.choice(["a", "b", "c", "x", "y", "z"])  # Random variable names
    value_type = random.choice(["integer", "float"])
    
    if value_type == "integer":
        value = random.randint(0, 100)
        return f"{variable} = {value}"
    else:
        value = round(random.uniform(0, 100), 2)  # Floating point value
        return f"{variable} = {value}"

def generate_random_expression():
    """Generates a random expression with variables and arithmetic operations."""
    var1 = random.choice(["a", "b", "c", "x", "y", "z"])
    var2 = random.choice(["a", "b", "c", "x", "y", "z"])
    operator = random.choice(["+", "-", "*", "/"])
    return f"{var1} = {var2} {operator} {random.uniform(1, 100):.2f}"

def generate_random_print():
    """Generates a random print statement."""
    variable = random.choice(["a", "b", "c", "x", "y", "z"])
    return f"p {variable}"

def generate_random_code_line():
    """Randomly generates either a comment, code line, or both."""
    code_types = [
        generate_random_declaration(),
        generate_random_assignment(),
        generate_random_expression(),
        generate_random_print()
    ]
    
    # Randomly choose between code, comment, or both on the same line
    choice = random.choice(["comment", "code", "both"])
    
    if choice == "comment":
        return generate_random_comment()
    elif choice == "code":
        return random.choice(code_types)
    else:  # Both
        return f"{generate_random_comment()} {random.choice(code_types)}"

def generate_ac_code():
    """Generates random AC code with a mix of comments and code."""
    num_lines = random.randint(5, 15)  # Random number of lines
    lines = [generate_random_code_line() for _ in range(num_lines)]
    
    return "\n".join(lines)

if __name__ == "__main__":
    code = generate_ac_code()
    with open("example.ac", "w") as f:
        f.write(code)
