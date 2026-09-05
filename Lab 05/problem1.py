text = "hello .py"

result = " ".join(word[::-1] for word in text.split())

print("Sample string: ", text)
print("Expected Result: ", result)