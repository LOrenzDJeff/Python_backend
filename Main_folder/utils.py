import numpy as np

def find_radius(RSRP):
    h = 60
    f = 3.6
    Ptx = 41    
    Prx = RSRP + 10 * np.log10(600)
    PL = Ptx - Prx
    m = (PL - 28 - 20 * np.log10(f)) / 22
    radius = (10 ** (m))
    radius = np.sqrt(radius ** 2 - h ** 2)
    print(f"radius = {radius:.10f} m")
    return radius

def m_to_grad(x, y, oldx, oldy):
    lat = oldx + ((180 * x) / (6371 * np.cos(55 * np.pi / 180) * np.pi))
    lon = oldy + ((180 * y) / (6371 * np.pi))
    print(f"lat = {lat:.10f}, lon = {lon:.10f}")
    return lat, lon

def grad_to_m(x, y):
    xkm = (6371 * np.cos(55 * np.pi / 180) * x * np.pi) /  180
    ykm = (6371 * y * np.pi) /  180
    return xkm, ykm
    
def find_m(x1, y1, x2, y2):
    x = x1 - x2
    y = y1 - y2
    x, y = grad_to_m(x, y)
    return x, y
