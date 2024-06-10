def calculate_signal_radius(rspr):
    if rspr > -80:
        return 5
    elif rspr > -90:
        return 3
    elif rspr > -100:
        return 1
    else:
        return 0.5