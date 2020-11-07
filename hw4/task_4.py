src_l = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
res_for_check = [23, 1, 3, 10, 4, 11]

res = [el for el in range(len(src_l)) if src_l.count(el) == 1]
print(res == res_for_check)
