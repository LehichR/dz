# def strcounter(s):
#     for sym in set(s):
#         counter = 0
#         for sub_sum in s:
#             if sub_sum == sym:
#                 counter += 1
#                 print("-" * 50)
#             print(sym, counter)
#
#
# strcounter("aaabbbdddd")
#
# print("#" * 50)
#
# def strcounter_second(s):
#     for sym in s:
#         counter = 0
#         for sub_sum in s:
#             if sub_sum == sym:
#                 counter += 1
#                 print("-" * 50)
#             print(sym, counter)
#
#
# strcounter_second("aaabbbdddd")


# s = {
#     1: 10,
#     2: 200,
# }


s = "ddadsa"  # 6 symb
syms_counter = {}
count = 0

for sym in s:
    count += 1
    print(count, syms_counter)
    print("-" * 50)
    syms_counter[sym] = syms_counter.get(sym, 0) + 1
    print(count, syms_counter)
    print("#" * 50)
