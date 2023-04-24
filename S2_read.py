import numpy as np
import rasterio
from rasterio import plot

file = 'D:\DATA\Sentinel-2\S2A_MSIL1C_20190408T030541_N0207_R075_T49QCA_20190408T060305\S2A_MSIL1C_20190408T030541_N0207_R075_T49QCA_20190408T060305.jpg'

plot.show(file)

with rasterio.open(file) as src:
    b, g, r = src.read(1), src.read(2), src.read(3)
    rgb = np.array([r, g, b])
    meta = src.meta.copy()

meta.updata