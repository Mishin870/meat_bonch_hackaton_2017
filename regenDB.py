count = 100
out = open("out.csv", "w", encoding='UTF-8')

with open("input.csv", encoding='UTF-8') as f:
    iterlines = iter(f)
    header = next(iterlines)
    headerItems = header.split("\t")
    out.write("\t".join(headerItems))
    i = 0
    for line in iterlines:
        items = line.split("\t")
        out.write("\t".join(items))
        i = i + 1
        if i >= count:
            break