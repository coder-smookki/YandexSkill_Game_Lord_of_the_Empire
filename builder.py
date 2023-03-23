import yaml

def builder(q):
    q = q.replace("'", '"')

    arr = q.split("\n")
    resultArr = []
    for i in range(len(arr)):
        n = arr[i]
        # n = n[::-1].replace("    "[::-1], "- "[::-1], 1)[::-1]

        if n == "":
            continue

        if "true:" in n:
            n = n.replace("true", "onTrue")
            resultArr.append(n)
            continue

        if "false:" in n:
            n = n.replace("false", "onFalse")
            resultArr.append(n)
            continue

        if '"' in n:
            n = n.replace('"', 'response: "', 1)
            resultArr.append(n)
            continue

    result = "\n".join(resultArr)
    return yaml.load(result, Loader=yaml.Loader)




dokaji = """'докажи'
    true:
        'верю'
    false:
        'не верю, уходи >:('
"""

a = f"""
'ты король?'
true:
    {dokaji}
false:
    'тогда пока'
"""

print(builder(a))