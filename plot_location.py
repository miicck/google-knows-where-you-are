import matplotlib.image  as mpimg
import matplotlib.pyplot as plt

lines = open("Location History.json").read().split("\n")

LON_RATIO  = 4.5373041734578935e-05
LAT_RATIO  = -7.594202898550724e-05
LON_OFFSET = 2773.4298665872457
LAT_OFFSET = 42462.55072463768

lats  = []
longs = [] 
for l in lines:
    if "longitude" in l:
        lon = float(l.split(":")[-1].replace(",",""))
        lon *= LON_RATIO
        lon += LON_OFFSET
        longs.append(lon)
    elif "latitude" in l:
        lat = float(l.split(":")[-1].replace(",",""))
        lat *= LAT_RATIO
        lat += LAT_OFFSET
        lats.append(lat)

print("Plotting {0} location points...".format(len(lats)))
img = mpimg.imread("large-detailed-map-of-england.jpg")
plt.scatter(longs, lats, marker="+", color="red")
plt.imshow(img, alpha=0.7)
plt.show()
