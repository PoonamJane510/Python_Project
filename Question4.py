import re

def to_camel_case(name):
    parts = name.split('_')
    return parts[0] + ''.join(x.title() for x in parts[1:])

def function_renamer(code):
    d = {}

    # Regular expression pattern to find function definitions
    pattern = r'def\s+([_a-zA-Z][_a-zA-Z0-9]*)\s*\('

    # Function to process each match found by the pattern
    def process_match(match):
        original_name = match.group(1)
        camel_case_name = to_camel_case(original_name)

        # If the name is already in camel case, return unchanged
        if original_name == camel_case_name:
            return match.group(0)

        # Replace all occurrences of the original name with camel case name in the code
        nonlocal code
        code = code.replace(original_name, camel_case_name)

        # Update nested dictionary with function details
        d[original_name] = {
            'hash': hash(original_name),
            'camelcase': camel_case_name,
            'allcaps': original_name.upper()
        }

        # Return the modified function definition
        return match.group(0).replace(original_name, camel_case_name)

    # Apply the pattern to find function definitions and process each match
    newcode = re.sub(pattern, process_match, code)

    return d, newcode

# Test cases
test_code_1 = """
def add_two_numbers(a, b):
  return a + b
print(add_two_numbers(10, 20))
"""

test_code_2 = """
def _major_split(*args):
  return (args[:2], args[2:])


def CheckTruth(t = True):
  print('t is', t)
  return _major_split([t]*10)

x, y = _major_split((10, 20, 30, 40, 50))


CheckTruth(len(x) == 10)
"""

d1, newcode1 = function_renamer(test_code_1)
print("Nested Dictionary 1:", d1)
print("Modified Code 1:", newcode1)

print()

d2, newcode2 = function_renamer(test_code_2)
print("Nested Dictionary 2:", d2)
print("Modified Code 2:", newcode2)
