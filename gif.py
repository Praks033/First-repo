import imageio.v3 as iio

filenames = ['team-pic1.png', 'team-pic2.png']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('team.gif', images, duration = 500, loop = 0)
# after this on cmd type
# cd file storage location
# python3 create_gif.py