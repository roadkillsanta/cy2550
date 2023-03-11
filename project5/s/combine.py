
def list_to_dict(list):
    dict = {}
    for item in list:
        unp = item.split(':')
        dict[unp[0]] = unp[1].split("\n")[0]
    return dict


shadow = list_to_dict(open('nie.e@northeastern.edu.shadow', 'r').readlines())
cracked = list_to_dict(open('cracked.txt', 'r').readlines())
combined = []

out = open("out.txt", "w")

for item in shadow.items():
    try:
        print("item: "+item[0]+", value: "+cracked[item[1]])
        out.write(item[0] + ":" + cracked[item[1]] + "\n")
    except:
        print("item: "+item[0]+", value: ")
        out.write(item[0] + ":\n")



