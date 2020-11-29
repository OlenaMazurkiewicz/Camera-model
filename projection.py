import camera
import numpy as geek
import matplotlib.pylab as plt


# Загружаем точки изображения

points = geek.loadtxt('house.p3d').T
points = geek.vstack((points, geek.ones(points.shape[1])))

# Настраиваем камеру

P = geek.hstack((geek.eye(3), geek.array([[0], [0], [-10]])))
cam = camera.Camera(P)
x = cam.project(points)

# Изображаем проекцию на графике

plt.figure()
plt.plot(x[0], x[1], 'k.')
plt.show()
