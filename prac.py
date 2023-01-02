#Program that converts weight in KGs to Pounds and vice verser 

weight = int(input("Input weight: "))
weight_unit = input("(K)g or (L)bs: ")

if weight_unit.upper() == "K":
    convert = weight // 0.45
    print(f"You weigh {convert} pounds")
else:
    convert = weight * 0.45
    print(f"You weigh  {convert} kilos")