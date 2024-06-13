'''
output = {
    'user.name': 'N',
    'contact.0': 1,
    'contact.1.some':'data'
}
'''
inp = {
    'user': {
        'name': 'N'
    },
    'contact': [1, {"some": "data"}]
}

def serializejson(inp):
    op={}
    def flatten(x,name=""):
        if type(x) is dict:
            for key in x:
                flatten(x[key],name+key+'.')
        elif type(x) is list:
            i=0
            for ele in x:
                flatten(ele,name+str(i)+'.')
                i+=1
        else:
            op[name[:-1]]=x
    flatten(inp)
    print(op)

serializejson(inp)