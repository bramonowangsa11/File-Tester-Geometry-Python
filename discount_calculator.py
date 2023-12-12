def calculate_discount(volume):
    if volume >= 1000:
        return 0.1
    elif volume >= 500:
        return 0.05
    else:
        return 0.0