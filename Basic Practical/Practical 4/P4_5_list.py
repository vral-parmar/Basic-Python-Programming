#usign Loop
def chk(list):
    return len(set(list)) <= 1
print(chk(['aa','bb','cc','dd']))
print(chk([1,1,1]))

#USing Set and count
def chki(list):
    return all(i == list[0] for i in list)
print(chki(['aa','bb','cc','dd']))
print(chki([1,1,1]))

#using COunt 
def chk(list):
    return list.count(list[0]) == len(list)
print(chk(['aa','bb','cc','dd']))
print(chk([1,1,1]))