import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

filename = "2.txt"
search = "妹"


with open("2.txt",encoding="utf8") as file:
    lines = []
    
    for line in file:
        if line[0].isdigit():
            l = next(file)
            lines.append( (line[-12:],l,) )


    tql = [item[0].translate(non_bmp_map) for item in lines if search in item[1]]
    dis = []
    found = []
    for name in tql:
        if(name not in found):
            dis.append((name,tql.count(name)))
            found.append(name)
            

    print(search)
    print()
    dis.sort(key=lambda x: x[1],reverse=True)
    for name in dis:
        print(name)
