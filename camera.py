from scipy import linalg
import numpy as geek

# Инициализация модели камеры

class Camera():
    def __init__(self, P):
        self.P = P                    # проекционная матрица
        self.K = None                 # калибровочная матрица
        self.R = None                 # матрица поворота, описывающая ориентацию камеры
        self.t = None                 # вектор параллельного переноса
        self.c = None                 # координаты оптического центра (половина ширины и высоты изображения)

# проецирование точек из массива Х и нормирование координат

    def project(self, X):
        x = geek.dot(self.P, X)        # точка изображения х
        for i in range(3):
            x[i] /= x[2]
        return x

    @staticmethod
    def rotation_matrix(a):

        R = geek.eye(4)
        R[:3, :3] = linalg.expm([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
        return R

    def factor(self):
        K, R = linalg.rq(self.P[:, :3])
        T = geek.diag(geek.sign(geek.diag(K)))
        T[1, 1] *= -1

        self.K = geek.dot(K, T)
        self.R = geek.dot(T, R)
        self.t = geek.dot(linalg.inv(self.K), self.P[:, 3])

        return self.K, self.R, self.t

