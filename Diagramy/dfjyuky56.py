s = "(AB)(!CD)"
# Split the string and extract parts between brackets
parts = s.split("(")
print(parts)
res = [p.split(")")[0] for p in parts if ")" in p]
print(res)