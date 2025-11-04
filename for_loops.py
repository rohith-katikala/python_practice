# for loops = execute a block of code a fixed number of times.
#     You can iterate over a range, string, sequences, etc.

# for x in range(1,11):
#     print(x)


# for x in reversed(range(1,11)):
#     print(x)
#
# for x in range(1,11,2):
#     print(x)

# credit_card = "1928-1932-1039-2049"
# for x in credit_card:
#     print(x)

# for x in range(1,21):
#     if x == 13:
#         continue
#     else:
#         print(x)

for x in range(1,21):
    if x == 13:
        break
    else:
        print(x)