
def calculate_bmi(feet, inch, weight):
    # Step 1
    kg = weight * 0.45

    # Returns height in inches
    height_inch = calculate_height(feet, inch)

    # Step 2
    height_meter = height_inch * 0.025

    # Step 3
    height_meter *= height_meter

    # Step 4
    result = kg / height_meter

    return result


def calculate_height(feet, inch):
    flag = feet * 12
    flag += inch

    return flag