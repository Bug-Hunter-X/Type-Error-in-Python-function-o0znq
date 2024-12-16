def function(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, str) and isinstance(b, str):
        return a + b
    else:
        return "Type Error: Cannot add different types"

result = function(5, "hello")
print(result)

result2 = function(5, 10)
print(result2)