import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation 

class pendulum:
    def __init__(self, g, l, w0, th0):
        self.g = g
        self.h=0.01
        self.l = l
        self.w0 = w0
        self.th0 = th0
        self.time_steps = np.arange(0, 5, self.h)
        self.pos_vals = []

    def RK4(self, f, x, t):
        k1 = self.h*f(x,t)
        k2 = self.h*f(x + .5*k1, t + .5*self.h)
        k3 = self.h*f(x + .5*k2, t + .5*self.h)
        k4 = self.h*f(x + k3, t + self.h)
        return x + 1/6 *(k1 + 2*k2 + 2*k3 + k4)

    def pendulum_diffeq(self,params, t):
        theta, omega = params
        theta_t = omega
        omega_t = -(self.g / self.l) * np.sin(theta)
        return np.array([theta_t, omega_t])

    def gen_positions(self):
        omega = self.w0
        theta = self.th0

        for time in self.time_steps:
            self.pos_vals.append(theta)
            theta, omega = self.RK4(self.pendulum_diffeq, np.array([theta, omega]), time)

    def animate_pendulum(self):
        fig = plt.figure()
        line, = plt.plot([], 'bo', markersize=20)
        line2, = plt.plot([], 'b')
        plt.xlim(-self.l, self.l)
        plt.ylim(-self.l, self.l)
        plt.close()

        def animate(frame):
            line.set_data(self.l*np.sin(self.pos_vals[frame]), self.l*(1-np.cos(self.pos_vals[frame])))
            line2.set_data([0, self.l*np.sin(self.pos_vals[frame])], [1, self.l*(1-np.cos(self.pos_vals[frame]))])
            

        anim = FuncAnimation(fig, animate, frames=len(self.pos_vals), interval=16.7)
        writervideo = animation.FFMpegWriter(fps=60)
        path = str(self.g) + str(self.l) + str(self.w0) + str(self.th0)
        path = path.replace('.', '_') + '.mp4'
        anim.save(<PATH TO SAVE FILE>, writer=writervideo)
        # print(a)
        # print(dir(a))
        return path
