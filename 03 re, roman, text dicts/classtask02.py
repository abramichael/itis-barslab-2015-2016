templates = [
    "0",
    "00",
    "000",
    "01",
    "1",
    "10",
    "100",
    "1000",
    "02",
]

positions_digits = [
    ["I", "V", "X"],
    ["X", "L", "C"],
    ["C", "D", "M"],
    ["M", "", ""]
]

x = 2249
s = str(x)
res = ""

k = 0
while (x > 0 and k < 4):
    d = x % 10
    template  = templates[d - 1]
    res_string = "".join([positions_digits[k][int(c)] for c in template])
    res = res_string + res
    x = x / 10
    k += 1

print res


