total_area=0
def calc_area(length,width=5):
    global total_area
    area=length*width
    total_area+=area
    print(f"Area: {area}, Total Area: {total_area}")

calc_area(6,10)
calc_area(5)