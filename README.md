# TCIR
TCIR is a dataset "Tropical Cyclone for Image Recognition Dataset", collecting tropical cyclone data from geosynchronous satellite including 4 channels.
![N|Solid](sample_fig.png)

# Data Size
Including three sets of tropical cyclones from three different region.

| Region | Cyclone | Frame |
| ------ | ------ | ------ |
| West Pacific | 320 | 17104 |
| East Pacific | 247 | 14149 |
| Atlantic | 235 | 13707 |
| Total | 802 | 44960 |

# Frames
- 4 channel : 
    - IR1 : Infrared.
    - WV : Water vapor.
    - VIS : Visible.
    - PMW : Passive micro wave.
- From two datasets, both of them are open datasets.
    - IR1, WV, and VIS are from GridSAT.(https://www.ncdc.noaa.gov/gridsat/)
    - PMW rain rate is from CMORPH. (http://www.cpc.ncep.noaa.gov/products/janowiak/cmorph_description.html)
- Frame size
    - Tropical cyclone’s center is placed in the middle of the vector.
    - A radius of 7 degrees in both Latitude and longitude.
    - 201*201 data point -> distance between two data point = 14/200 (lon/lat)

# labels
