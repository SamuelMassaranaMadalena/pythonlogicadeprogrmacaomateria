s = 0
for um in range(101):
    if um < 50:
        print(um + 1)
    elif um == 50:
        print(um)
    elif um > 50:
        s = s + 2
        print(um - (1 * s))
