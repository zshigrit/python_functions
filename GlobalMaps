import matplotlib.pyplot as plt
#plt.style.use("ggplot")
plt.style.use('classic')

import cartopy.crs as ccrs
#axis.scatter([120],[30],zorder=1)
map_projection = ccrs.Robinson(central_longitude=0)
data_transform = ccrs.PlateCarree()
#fig = plt.figure(figsize=[12,5])
#axis = fig.add_subplot(1,1,1, projection=map_projection,zorder=0)
axis = plt.axes(projection=map_projection,zorder=0)
axis.coastlines()
axis.gridlines(draw_labels=True)
axis.stock_img()# natural earth color
axis.scatter([0],[0],transform=data_transform,zorder=1)
#axis.scatter([-50,0,50],[-50,0,50],transform=data_transform,zorder=1)
#axis.scatter([-179,0,179],[-89,0,89],transform=ccrs.PlateCarree(),zorder=1)
