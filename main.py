def prep():
    ll = [1,55,"hello",15.5]

    dic1 =  {0:1,1:111,2:"hello",3:15.5}
    ll2 = []
    dic2 = {}

    ll2.append(656)
    dic2["stdlyg"] = 9595
    print(dic2["stdlyg"])

def register():
    name = input("Give me your name?")
    id = ("Give me your ID")
    dic_name = {}
    dic_id = {}
    dic_name[name] = id
    print(dic_name["armand"])
    dic_id[id] = name
    print(dic_id)
#register()
def get():
    dic1 =  {0:1,1:111,2:"hello",3:15.5}
    print(dic1.keys())
    print(dic1.values())
    print(dic1.items())
get()