#57
def soz_teskari(text):
    return ' '.join(text.split()[::-1])

print(soz_teskari("men python organayapman"))

#58
def nol_oxiri(lst):
    nol = [x for x in lst if x==0]
    boshqa = [x for x in lst if x!=0]
    return boshqa + nol

print(nol_oxiri([1,0,3,0,5,6]))

#59
def tuple_list(t):
    return list(t)

print(tuple_list((1,2,3)))

#60
def list_tuple(lst):
    return tuple(lst)

print(list_tuple([4,5,6]))

#61
def kalit_bormi(d,k):
    return k in d

print(kalit_bormi({"a":1,"b":2},"a"))
