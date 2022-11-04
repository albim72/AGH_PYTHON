class MyDictSub(dict):

    def __missing__(self, key):
        return 'uwaga! brak klucza!'


konkurs = {'Alicja':78,'Robert':90,'Kazimierz':87}

print(konkurs['Alicja'])
# print(konkurs['Henio'])

md = MyDictSub(konkurs)
print(md['Robert'])
print(md['Henio'])
