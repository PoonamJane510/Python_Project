def do_arithmetic(x, y, op='add'):
    # Check the operation and perform it
    if op in ('add', '+'):
        return float(x + y)
    elif op in ('subtract', '-'):
        return float(x - y)
    elif op in ('multiply', '*'):
        return float(x * y)
    elif op in ('divide', '/'):
        # Avoid division by zero
        if y == 0:
            print('Division by 0!')
            return None
        else:
            return float(x / y)
    else:
        print('Unknown operation')
        return None

# Test cases
print(do_arithmetic(24, -7, 'add'))  # Expected result: 17.0
print(do_arithmetic(6, 6, 'multiply'))  # Expected result: 36.0
print(do_arithmetic(4, 0, '/'))  # Expected result: "Division by 0!"
print(do_arithmetic(3, 9, '-'))  # Expected result: -6.0
print(do_arithmetic(10, -43, 'subtract'))  # Expected result: 53.0
print(do_arithmetic(3, 9))  # Expected result: 12.0
