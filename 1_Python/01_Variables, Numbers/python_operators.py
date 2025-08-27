'''
🧮 1. Arithmetic Operators
Used to perform basic math operations.
| Operator | Description         | Example  | Result |
| -------- | ------------------- | -------- | ------ |
| `+`      | Addition            | `5 + 2`  | `7`    |
| `-`      | Subtraction         | `5 - 2`  | `3`    |
| `*`      | Multiplication      | `5 * 2`  | `10`   |
| `/`      | Division            | `5 / 2`  | `2.5`  |
| `//`     | Floor division      | `5 // 2` | `2`    |
| `%`      | Modulus (remainder) | `5 % 2`  | `1`    |
| `**`     | Exponentiation      | `5 ** 2` | `25`   |


📝 2. Assignment Operators
Used to assign values to variables.
| Operator | Example   | Same As      |
| -------- | --------- | ------------ |
| `=`      | `x = 5`   | `x = 5`      |
| `+=`     | `x += 3`  | `x = x + 3`  |
| `-=`     | `x -= 3`  | `x = x - 3`  |
| `*=`     | `x *= 3`  | `x = x * 3`  |
| `/=`     | `x /= 3`  | `x = x / 3`  |
| `//=`    | `x //= 3` | `x = x // 3` |
| `%=`     | `x %= 3`  | `x = x % 3`  |
| `**=`    | `x **= 3` | `x = x ** 3` |


⚖️ 3. Comparison Operators
Used to compare values, return True or False.
| Operator | Description      | Example           |
| -------- | ---------------- | ----------------- |
| `==`     | Equal to         | `5 == 5` → `True` |
| `!=`     | Not equal        | `5 != 3` → `True` |
| `>`      | Greater than     | `5 > 3` → `True`  |
| `<`      | Less than        | `5 < 3` → `False` |
| `>=`     | Greater or equal | `5 >= 5` → `True` |
| `<=`     | Less or equal    | `5 <= 6` → `True` |


🧠 4. Logical Operators
Used to combine conditional statements.
| Operator | Description                            | Example                  |
| -------- | -------------------------------------- | ------------------------ |
| `and`    | Returns `True` if both are true        | `True and True` → `True` |
| `or`     | Returns `True` if at least one is true | `True or False` → `True` |
| `not`    | Reverses the result                    | `not True` → `False`     |


🧍 5. Identity Operators
Used to compare memory locations of two objects.
| Operator | Description                             | Example      |
| -------- | --------------------------------------- | ------------ |
| `is`     | True if both point to same object       | `a is b`     |
| `is not` | True if they point to different objects | `a is not b` |
'''

a = [1,2,3]
b = a
c = [1,2,3]
print(a is b)  # True
print(c is a)  # False (same content, different memory)