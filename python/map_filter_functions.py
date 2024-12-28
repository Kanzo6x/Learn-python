names=['amr','ahmed','zeyad','yousef','amar','basem']
def find_name(name):
    if name[0]=='a':
        return name

map_name = map(find_name,names)
print(map_name)
for x in map_name:
    print(x,end=' ')
print()

filter_name = filter(find_name,names)
print(filter_name)
for x in filter_name:
    print(x,end=' ')