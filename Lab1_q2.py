integer = 10
floating_point = 50.0
string = "Hello"
boolean = True

addition = integer + floating_point
subtraction = integer - floating_point
multiplication = integer * floating_point
division = integer / floating_point if floating_point != 0 else "Undefined (division by zero)"
modulus = integer % floating_point if floating_point != 0 else "Undefined (modulus by zero)"

print("Arithmetic Operations:")
print(f"Addition: {integer} + {floating_point} = {addition}")
print(f"Subtraction: {integer} - {floating_point} = {subtraction}")
print(f"Multiplication: {integer} * {floating_point} = {multiplication}")
print(f"Division: {integer} / {floating_point} = {division}")
print(f"Modulus: {integer} % {floating_point} = {modulus}\n")

concatenated_string = string + " World !!"
print("String Concatenation:")
print(concatenated_string, "\n")

and_op = boolean and False
or_op = boolean or False
not_op = not boolean

print("Logical Operations:")
print(f"Boolean AND False: {and_op}")
print(f"Boolean OR False: {or_op}")
print(f"NOT Boolean: {not_op}")
