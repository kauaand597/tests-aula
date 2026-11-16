let1 = input("1ª letra: ")
let2 = input("2ª letra: ")
let3 = input("3ª letra: ")

l1, l2, l3 = let1.lower(), let2.lower(), let3.lower()

if l1 < l2 < l3 or l3 < l2 < l1:
    print(f"A letra do meio é {let2}")
elif l2 < l1 < l3 or l3 < l1 < l2:
    print(f"A letra do meio é {let1}")
else:
    print(f"A letra do meio é {let3}")