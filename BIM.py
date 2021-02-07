def bim_body(name, height, weight):
    bim = weight / (height **2)
    print(f"Index body weight is {bim}")
    if bim < 25:
        return print(f"{name} doesn't have extra weight")
    else:
        return print(f"{name} has extra weight")


while True:
    name = input("Please enter your name: ")
    height = float(input("Please ener your height in meters: "))
    weihgt = int(input("Please eneter your weihgt: "))
    bim_body(name, height, weihgt)

