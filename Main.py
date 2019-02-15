import cal
num1 = None

print("=============== This Is A Calculator! ===============\n")

while True:

    if num1 == None: sequn = input("> ")
    else: sequn = str(num1)+input("> "+str(num1))

    if 'x' in sequn or 'X' in sequn:
        print("Goodbye!")
        break

    for i in sequn:
        if i not in cal.validdigs and i not in cal.validops and i not in cal.validfuncs:
            print("You have entered an invalid key!")
            break

    if sequn[0] not in cal.validdigs and sequn[0] not in cal.validfuncs[4:]:
        print("You must start with a number!")
        continue

    op = sequn.lstrip('-')
    op = op.strip('0123456789.')
    try:
        nums = sequn.split(op)
        if nums[0] != "":
            num1 = float(nums[0])
        if nums[1] != "":
            num2 = float(nums[1])
    except:
        print("Enter real numbers, jackass!")
        num1 = None
        nums = ""
        continue

    if len(op) > 1:
        print("You can't enter multiple operators!")
    if op not in cal.validfuncs:
        num1 = cal.calculator_basic(num1, num2, op)
    elif op in cal.validfuncs[6:9]:
        stored = cal.calculator_funcs(num1, op)
    elif op in cal.validfuncs[4:5]:
        num1 = cal.calculator_funcs(stored, op)
    else:
        num1 = cal.calculator_funcs(num1, op)
