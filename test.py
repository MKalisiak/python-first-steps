#
# def create_dict(list1, list2) -> dict:
#     place = {list1[i]: list2[i] for i in range(len(list2))}
#     return place
# countries = ["Angola", "Anglia", "Boliwia","Czechy", "Dania", "Polska"]
# names = ["Alibaba", "Andrzej", "Bożo", "Czarek", "Daniel", "Bambo"]
# # place = {}
# # print(place)
# # for i in range(len(names)):
# #     place[countries[i]] = names[i]
#
# # place={names[i]: countries[i] for i in range(len(countries))}
#
# place = create_dict(list1=names, list2=countries)
#
# print(place)

def power(base: int, pow: int) -> int:
    # return base to pow power
    # x, y = base, pow
    result = base**pow
    return result

mmm = power(2,4)
print(mmm)