import datetime, db

with open("db.csv", encoding='UTF-8') as f:
    iterlines = iter(f)
    header = next(iterlines)
    headerItems = header.split("\t")
    headerItems = [headerItems[0], headerItems[1], headerItems[2], headerItems[7], headerItems[9], headerItems[11], headerItems[12], headerItems[14], headerItems[17]]
    out = open("out_min.csv", "a+", encoding='UTF-8')
    out.write("\t".join(headerItems) + "\n")

    for line in iterlines:
        items = line.split("\t")
        items = [items[0], items[1], items[2], items[7], items[9], items[11], items[12], items[14], items[17]]
        out.write("\t".join(items) + "\n")
        #f.write("\t".join(items))