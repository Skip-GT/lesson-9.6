def all_variants(text):
    b = len(text)
    for s in range(b):
        for j in range(s + 1, b + 1):
            yield text[s:j]


a = all_variants("abc")
for i in a:
    print(i)
