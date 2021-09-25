whittaker_biome = pd.read_csv('whittaker_biome.csv')
whittaker_biome['MAT'] = whittaker_biome.x
whittaker_biome['MAP'] = whittaker_biome.y*100
whittaker_biome['Color'] = whittaker_biome['biome']

whittaker_biome['Color'] = whittaker_biome['Color'].map({'Boreal forest': 'red',
                              'Subtropical desert': 'purple',
                              'Temperate forest':'orange',
                              'Temperate grassland desert':'green',
                              'Temperate rain forest':'blue',
                              'Tropical forest savanna':'cyan',
                              'Tropical rain forest':'slategrey',
                              'Tundra':'lime',
                              'Woodland shrubland':'yellow'})

fig, ax = plt.subplots(figsize=(8,6))
for title, group in whittaker_biome.groupby(['biome']):
    group.plot(x='MAT',y='MAP',ax=ax,color = group['Color'],
               label=title)
    plt.fill_between(group['MAT'],0,group['MAP'],facecolor = group['Color'], alpha = 0.3)

plt.legend(fontsize=11,loc='best')
