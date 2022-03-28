import numpy as np

from imports import *


class Equations(Scene):
    def construct(self):
        text=Text("hello world")




class Scene1(ThreeDScene):
    def construct(self):
        # self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.5)
        self.set_camera_orientation(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000,zoom=0.5)
        tr = ValueTracker(3)






        axes = ThreeDAxes(x_range=[-6, 6, 2], y_range=[0, 11, 2], z_range=[-6, 6, 2], y_length=22, x_length=8,z_length=8)

        numberplane = NumberPlane(x_range=[-6, 6, 2], y_range=[-6, 6, 2], x_length=8, y_length=8,
                                  background_line_style={
                                      "stroke_color": BLUE,
                                      "stroke_width": 1,
                                      "stroke_opacity": 0.4,
                                  }).rotate(90 * DEGREES, RIGHT).move_to(axes.get_origin())


        # pure_complex_exp=always_redraw(lambda : ParametricFunction(lambda t: np.array([0.6 * np.real(  np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t,0.6 * np.imag(np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        curve1 = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.6 * np.real((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t,0.6 * np.imag((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t))  * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))

        realt_curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.6 * np.real((2 * np.sin(2 * np.pi * 0.5 * t) + 3 * np.cos(2 * np.pi * 0.1 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t, 0]), stroke_width=0,color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        imagt_curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0,2 * t, 0.6 * np.imag((2 * np.sin(2 * np.pi * 0.5 * t) + 3 * np.cos(2 * np.pi * 0.1 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=0,color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))

        real_area=always_redraw(lambda :axes.get_area_y(realt_curve,[0,10]))
        imag_area=always_redraw(lambda :axes.get_area_y(imagt_curve,[0,10]))


        # area1= always_redraw(lambda : Polygon(*([[0, -10, 0]] + [p for p in (ParametricFunction(lambda t: np.array([0.6*np.real((np.sin(3 * t) + 2 * np.cos(10 * t) + 3 * np.sin(5 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2*t,0]),stroke_width=0, color=YELLOW, t_range = np.array([-5, 5, 0.001]),dt=1)).points if -10 <= p[1] <= 9.99] + [[0, 9.99, 0]])).set_opacity(0.4).set_color([BLUE,GREEN]))


        # self.add(pure_complex_exp,axes)
        # self.add(axes,realt_curve,imagt_curve,real_area,imag_area)
        # self.add(axes,curve1,realt_curve,real_area)
        # self.wait()
        # self.play(tr.animate(run_time=0.5).set_value(3.3))
        # self.wait()

        # self.add(axes,numberplane,curve1)
        # self.wait()
        # self.move_camera(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000)
        # self.wait(0.5)
        # self.play(FadeIn(realt_curve,real_area))
        # self.wait()


        self.add(axes,numberplane,curve1,realt_curve,real_area)
        self.wait()
        self.play(tr.animate.set_value(0),run_time=3)
        self.wait()

        # self.add(axes,numberplane,curve1,realt_curve,real_area)
        # self.wait(0.5)
        # self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000,zoom=0.5)
        # self.wait(0.5)
        # self.move_camera(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000,zoom=0.5)
        # self.wait(0.5)




        # self.wait(0.5)
        # self.play(tr.animate(run_time=4).set_value(3))
        # self.wait()


class Scene11(ThreeDScene):
    def construct(self):
        # self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.5)
        self.set_camera_orientation(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000,zoom=0.5)
        tr = ValueTracker(0)






        axes = ThreeDAxes(x_range=[-6, 6, 2], y_range=[0, 11, 2], z_range=[-6, 6, 2], y_length=22, x_length=8,z_length=8)

        numberplane = NumberPlane(x_range=[-6, 6, 2], y_range=[-6, 6, 2], x_length=8, y_length=8,
                                  background_line_style={
                                      "stroke_color": BLUE,
                                      "stroke_width": 1,
                                      "stroke_opacity": 0.4,
                                  }).rotate(90 * DEGREES, RIGHT).move_to(axes.get_origin())


        # pure_complex_exp=always_redraw(lambda : ParametricFunction(lambda t: np.array([0.6 * np.real(  np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t,0.6 * np.imag(np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        curve1 = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.6 * np.real((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t,0.6 * np.imag((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t))  * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))

        realt_curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.6 * np.real((2 * np.sin(2 * np.pi * 0.5 * t) + 3 * np.cos(2 * np.pi * 0.1 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t, 0]), stroke_width=0,color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        imagt_curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0,2 * t, 0.6 * np.imag((2 * np.sin(2 * np.pi * 0.5 * t) + 3 * np.cos(2 * np.pi * 0.1 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=0,color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))

        real_area=always_redraw(lambda :axes.get_area_y(realt_curve,[0,10]))
        imag_area=always_redraw(lambda :axes.get_area_y(imagt_curve,[0,10]))


        # area1= always_redraw(lambda : Polygon(*([[0, -10, 0]] + [p for p in (ParametricFunction(lambda t: np.array([0.6*np.real((np.sin(3 * t) + 2 * np.cos(10 * t) + 3 * np.sin(5 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2*t,0]),stroke_width=0, color=YELLOW, t_range = np.array([-5, 5, 0.001]),dt=1)).points if -10 <= p[1] <= 9.99] + [[0, 9.99, 0]])).set_opacity(0.4).set_color([BLUE,GREEN]))


        # self.add(pure_complex_exp,axes)
        # self.add(axes,realt_curve,imagt_curve,real_area,imag_area)
        # self.add(axes,curve1,realt_curve,real_area)
        # self.wait()
        # self.play(tr.animate(run_time=0.5).set_value(3.3))
        # self.wait()

        # self.add(axes,numberplane,curve1)
        # self.wait()
        # self.move_camera(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000)
        # self.wait(0.5)
        # self.play(FadeIn(realt_curve,real_area))
        # self.wait()


        self.add(axes,numberplane,curve1,realt_curve,real_area)
        self.wait()
        self.play(tr.animate.set_value(-3),run_time=3)
        self.wait()

        # self.add(axes,numberplane,curve1,realt_curve,real_area)
        # self.wait(0.5)
        # self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000,zoom=0.5)
        # self.wait(0.5)
        # self.move_camera(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000,zoom=0.5)
        # self.wait(0.5)




        # self.wait(0.5)
        # self.play(tr.animate(run_time=4).set_value(3))
        # self.wait()


class Scene1_2(ThreeDScene):
    def construct(self):
        # self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.5)
        self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000,zoom=0.5)
        tr = ValueTracker(3)






        axes = ThreeDAxes(x_range=[-6, 6, 2], y_range=[0, 11, 2], z_range=[-6, 6, 2], y_length=22, x_length=8,z_length=8)

        numberplane = NumberPlane(x_range=[-6, 6, 2], y_range=[-6, 6, 2], x_length=8, y_length=8,
                                  background_line_style={
                                      "stroke_color": BLUE,
                                      "stroke_width": 1,
                                      "stroke_opacity": 0.4,
                                  }).rotate(90 * DEGREES, RIGHT).move_to(axes.get_origin())



        # pure_complex_exp=always_redraw(lambda : ParametricFunction(lambda t: np.array([0.6 * np.real(  np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t,0.6 * np.imag(np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        curve1 = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.6 * np.real((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t,0.6 * np.imag((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t))  * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))

        realt_curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.6 * np.real((2 * np.sin(2 * np.pi * 0.5 * t) + 3 * np.cos(2 * np.pi * 0.1 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t, 0]), stroke_width=0,color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        imagt_curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0,2 * t, 0.6 * np.imag((2 * np.sin(2 * np.pi * 0.5 * t) + 3 * np.cos(2 * np.pi * 0.1 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=0,color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))

        real_area=always_redraw(lambda :axes.get_area_y(realt_curve,[0,10]))
        imag_area=always_redraw(lambda :axes.get_area_y(imagt_curve,[0,10]))




        # area1= always_redraw(lambda : Polygon(*([[0, -10, 0]] + [p for p in (ParametricFunction(lambda t: np.array([0.6*np.real((np.sin(3 * t) + 2 * np.cos(10 * t) + 3 * np.sin(5 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2*t,0]),stroke_width=0, color=YELLOW, t_range = np.array([-5, 5, 0.001]),dt=1)).points if -10 <= p[1] <= 9.99] + [[0, 9.99, 0]])).set_opacity(0.4).set_color([BLUE,GREEN]))


        # self.add(pure_complex_exp,axes)
        # self.add(axes,realt_curve,imagt_curve,real_area,imag_area)
        # self.add(axes,curve1,realt_curve,real_area)
        # self.wait()
        # self.play(tr.animate(run_time=0.5).set_value(3.3))
        # self.wait()
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000)
        # axes.y_axis.rotate(90*DEGREES,[0,1,0])
        # self.add(axes,numberplane,curve1)
        # self.wait()
        # self.move_camera(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000,added_anims=[axes.y_axis.animate.rotate(90*DEGREES,[0,1,0]),axes.z_axis.animate.rotate(90*DEGREES,[0,0,1])])
        # self.wait(0.5)
        # self.play(FadeIn(imag_area))
        # self.wait()

        axes.y_axis.rotate(90 * DEGREES, [0, 1, 0])
        axes.z_axis.rotate(90 * DEGREES, [0, 0, 1])
        self.add(axes,numberplane,curve1,imagt_curve,imag_area)
        self.wait()
        self.play(tr.animate().set_value(0),run_time=3)
        self.wait()

        # self.add(axes, numberplane, curve1, imagt_curve, imag_area)
        # self.wait(0.5)
        # self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.5,added_anims=[axes.y_axis.animate.rotate(90*DEGREES,[0,1,0]),axes.z_axis.animate.rotate(90*DEGREES,[0,0,1])])
        # self.wait(0.5)
        # self.move_camera(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.5,added_anims=[axes.y_axis.animate.rotate(90*DEGREES,[0,1,0]),axes.z_axis.animate.rotate(90*DEGREES,[0,0,1])])
        # self.wait(0.5)

        # self.wait(0.5)
        # self.play(tr.animate(run_time=4).set_value(3))




class Scene1_22(ThreeDScene):
    def construct(self):
        # self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.5)
        self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000,zoom=0.5)
        tr = ValueTracker(0)






        axes = ThreeDAxes(x_range=[-6, 6, 2], y_range=[0, 11, 2], z_range=[-6, 6, 2], y_length=22, x_length=8,z_length=8)

        numberplane = NumberPlane(x_range=[-6, 6, 2], y_range=[-6, 6, 2], x_length=8, y_length=8,
                                  background_line_style={
                                      "stroke_color": BLUE,
                                      "stroke_width": 1,
                                      "stroke_opacity": 0.4,
                                  }).rotate(90 * DEGREES, RIGHT).move_to(axes.get_origin())



        # pure_complex_exp=always_redraw(lambda : ParametricFunction(lambda t: np.array([0.6 * np.real(  np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t,0.6 * np.imag(np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        curve1 = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.6 * np.real((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t,0.6 * np.imag((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t))  * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))

        realt_curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.6 * np.real((2 * np.sin(2 * np.pi * 0.5 * t) + 3 * np.cos(2 * np.pi * 0.1 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t, 0]), stroke_width=0,color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        imagt_curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0,2 * t, 0.6 * np.imag((2 * np.sin(2 * np.pi * 0.5 * t) + 3 * np.cos(2 * np.pi * 0.1 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=0,color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))

        real_area=always_redraw(lambda :axes.get_area_y(realt_curve,[0,10]))
        imag_area=always_redraw(lambda :axes.get_area_y(imagt_curve,[0,10]))




        # area1= always_redraw(lambda : Polygon(*([[0, -10, 0]] + [p for p in (ParametricFunction(lambda t: np.array([0.6*np.real((np.sin(3 * t) + 2 * np.cos(10 * t) + 3 * np.sin(5 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2*t,0]),stroke_width=0, color=YELLOW, t_range = np.array([-5, 5, 0.001]),dt=1)).points if -10 <= p[1] <= 9.99] + [[0, 9.99, 0]])).set_opacity(0.4).set_color([BLUE,GREEN]))


        # self.add(pure_complex_exp,axes)
        # self.add(axes,realt_curve,imagt_curve,real_area,imag_area)
        # self.add(axes,curve1,realt_curve,real_area)
        # self.wait()
        # self.play(tr.animate(run_time=0.5).set_value(3.3))
        # self.wait()
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000)
        # axes.y_axis.rotate(90*DEGREES,[0,1,0])
        # self.add(axes,numberplane,curve1)
        # self.wait()
        # self.move_camera(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000,added_anims=[axes.y_axis.animate.rotate(90*DEGREES,[0,1,0]),axes.z_axis.animate.rotate(90*DEGREES,[0,0,1])])
        # self.wait(0.5)
        # self.play(FadeIn(imag_area))
        # self.wait()

        axes.y_axis.rotate(90 * DEGREES, [0, 1, 0])
        axes.z_axis.rotate(90 * DEGREES, [0, 0, 1])
        self.add(axes,numberplane,curve1,imagt_curve,imag_area)
        self.wait()
        self.play(tr.animate().set_value(-3),run_time=3)
        self.wait()

        # self.add(axes, numberplane, curve1, imagt_curve, imag_area)
        # self.wait(0.5)
        # self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.5,added_anims=[axes.y_axis.animate.rotate(90*DEGREES,[0,1,0]),axes.z_axis.animate.rotate(90*DEGREES,[0,0,1])])
        # self.wait(0.5)
        # self.move_camera(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.5,added_anims=[axes.y_axis.animate.rotate(90*DEGREES,[0,1,0]),axes.z_axis.animate.rotate(90*DEGREES,[0,0,1])])
        # self.wait(0.5)

        # self.wait(0.5)
        # self.play(tr.animate(run_time=4).set_value(3))





class Scene2(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000,zoom=0.8)
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000)
        ax = ThreeDAxes(x_range=[-1.5, 1.5, 0.25], y_range=[0, 27, 5], z_range=[-1.5, 1.5, 0.25], x_length=9,
                        z_length=9, y_length=12).scale(0.7)
        ax.x_axis.rotate(90*DEGREES,[1,0,0])
        numberplane = NumberPlane(x_range=[-1.5, 1.5, 0.25], y_range=[-1.5, 1.5, 0.25], x_length=9, y_length=9,
                                  background_line_style={
                                      "stroke_color": WHITE,
                                      "stroke_width": 1,
                                      "stroke_opacity": 0.4,
                                  }).scale(0.7).rotate(90 * DEGREES, RIGHT).move_to(ax.get_origin())
        # amp=ValueTracker(1)
        # complexExponential=always_redraw(lambda : MathTex(r'%0.1fe^{i \omega  t }'% amp.get_value(),color=RED).scale(1.5).rotate(90*DEGREES,[1,0,0]).move_to([2.2,0,2.9]))
        # circle=Circle(2.09,color=YELLOW,stroke_width=2).rotate(90*DEGREES,[1,0,0]).move_to(numberplane.get_origin())
        # smallCircle=Circle(1.2,color=YELLOW,stroke_width=2).rotate(90*DEGREES,[1,0,0]).move_to(numberplane.get_origin())
        # largeCircle=Circle(2.4,color=YELLOW,stroke_width=2).rotate(90*DEGREES,[1,0,0]).move_to(numberplane.get_origin())
        #
        # self.add(ax,numberplane,circle)
        # self.wait(0.5)
        # self.play(FadeIn(complexExponential))
        # self.wait(0.2)
        # self.play(Transform(circle,smallCircle),amp.animate.set_value(0.3),run_time=2)
        # self.wait()
        # self.play(Transform(circle,largeCircle),amp.animate.set_value(1.4),run_time=2)
        # self.wait()

        tr=ValueTracker(-3)
        pure_complex_exp= ParametricFunction(lambda t: np.array([2.1 * np.real(  np.exp(1j * 2 * np.pi * tr.get_value() * t)),2 * t,2.1 * np.imag(np.exp(1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 3.5, 0.001]), dt=1).align_to(numberplane,[0,-1,0])
        modulated_complex_exp = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.5 * np.real((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t,0.5 * np.imag((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t))  * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 3.5, 0.001]), dt=1).align_to(numberplane,[0,-1,0]))

        # self.play(Create(ax),Create(numberplane))
        # self.wait(0.5)
        # self.play(Create(pure_complex_exp,run_time=2),rate_function=rate_functions.ease_in_expo)
        # self.wait()
        # self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000,zoom=0.8)
        # self.wait()




        self.add(ax,numberplane,pure_complex_exp)
        group=VGroup(ax,numberplane,pure_complex_exp)
        self.wait()
        self.move_camera(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000,added_anims=[group.animate.scale(1.25)])
        self.wait()
        # self.play(tr.animate.set_value(3),run_time=2)
        # self.wait()
        # self.play(tr.animate.set_value(0),run_time=2)
        # self.wait()
        # self.play(tr.animate.set_value(3), run_time=2)
        # self.wait()



        # self.wait()
        # self.play(ReplacementTransform(pure_complex_exp,modulated_complex_exp))
        # self.wait()
        # self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES, distance=1000)
        # self.wait()



class ArbitraryFunction(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, distance=1000)
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000)
        tr=ValueTracker(1.5)
        ax1 = Axes(x_range=[0, 11, 2], y_range=[-4, 4, 2],y_length=3).shift(2.5*UP).rotate(90*DEGREES,[1,0,0]).shift([0,0,2.4])
        ax = ThreeDAxes(x_range=[-1.5, 1.5, 0.25], y_range=[0, 27, 5], z_range=[-1.5, 1.5, 0.25], x_length=9,z_length=9, y_length=22).scale(0.5).shift([0,0,-1.3])
        ax.x_axis.rotate(90 * DEGREES, [1, 0, 0])
        numberplane = NumberPlane(x_range=[-1.5, 1.5, 0.25], y_range=[-1.5, 1.5, 0.25], x_length=9, y_length=9,
                                  background_line_style={
                                      "stroke_color": BLUE,
                                      "stroke_width": 1,
                                      "stroke_opacity": 0.4,
                                  }).scale(0.5).rotate(90 * DEGREES, RIGHT).move_to(ax.get_origin())
        g1 = ax1.plot(lambda t: 0.6 * (2 * np.sin(2 * np.pi * 0.5 * t) + 3 * np.cos(2 * np.pi * 0.1 * t)),x_range=[0, 10, 0.01], color=YELLOW,stroke_width=1.5)
        modulated_complex_exponential = ParametricFunction(lambda t: np.array([0.4 * np.real((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)), t,0.4 * np.imag((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t))  * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).align_to(numberplane,[0,-1,0]).shift([0,0,-1.3])

        self.add(ax)
        # self.add_fixed_orientation_mobjects(ax1,g1)
        # self.add(ax1,g1)
        # self.play(FadeIn( ax,numberplane))
        # self.wait()
        # self.play(ReplacementTransform(g1.copy(),modulated_complex_exponential))
        # self.wait()
        #
        # self.remove(ax1,g1)
        # self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000)
        # self.wait()


        # self.add(ax,numberplane,modulated_complex_exponential)
        # self.wait()
        # self.play(tr.animate(run_time=3).set_value(3))
        # self.wait(0.2)
        # self.play(tr.animate(run_time=3).set_value(0))
        # self.wait(0.5)
        # self.play(tr.animate(run_time=4).set_value(2.5))
        # self.wait()
        # self.move_camera(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000)
        # self.wait()

        # self.add(ax,numberplane,modulated_complex_exponential)
        # group=VGroup(ax,numberplane,modulated_complex_exponential)
        # self.move_camera(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000,added_anims=[group.animate.shift([0,0,1])])
        # self.wait()




class ArbitraryFunction2D(Scene):
    def construct(self):
        ax1 = Axes(x_range=[0, 11, 2], y_range=[-4, 4, 2],y_length=3).shift(2.4*UP)
        g1 = ax1.get_graph(lambda t: 0.6 * (2 * np.sin(2 * np.pi * 0.5 * t) + 3 * np.cos(2 * np.pi * 0.1 * t)),x_range=[0, 10, 0.01], color=YELLOW,stroke_width=1.5)
        self.play(Create(ax1))
        self.play(Create(g1))
        self.wait()





class FT_integration(ThreeDScene):
    def construct(self):
        ax1 = Axes(x_range=[-10, 10, 2], y_range=[-2, 2, 1])
        ax2 = Axes(x_range=[-4, 4, 1], y_range=[-1, 5])
        ax3 = Axes(x_range=[-4, 4, 1], y_range=[-50, 250, 50])
        [g1, dot1] = TheSiGuy_lib.two_d_graph_from_csv(ax=ax1, csvFile='csv_files/area_integration/rect_function.csv')
        [g2, dot2] = TheSiGuy_lib.two_d_graph_from_csv(ax2, 'csv_files/area_integration/rect_amp_spectrum.csv')
        [g3, dot3] = TheSiGuy_lib.two_d_graph_from_csv(ax3, 'csv_files/area_integration/rect_phase_spectrum.csv')

        def rect(x, a):
            return 1 if abs(x) <= a else 0



        tr = ValueTracker(0.5)
        axes = ThreeDAxes(x_range=[-20, 20, 5], y_range=[-11, 11, 2], z_range=[-20, 20, 5], y_length=22, x_length=8,
                          z_length=8)
        curve1 = always_redraw(lambda: ParametricFunction(
            lambda t: np.array([
                 np.real(rect(t,2) * np.exp(
                    -1j * 2 * np.pi * tr.get_value() * t)),
                2 * t,
                np.imag(rect(t,2) * np.exp(
                    -1j * 2 * np.pi * tr.get_value() * t))
            ]), stroke_width=1.5, color=YELLOW, t_range=np.array([-5, 5, 0.001]), dt=1)
                               )
        ax = ThreeDAxes(x_range=[-1.5, 1.5, 0.25], y_range=[0, 27, 5], z_range=[-1.5, 1.5, 0.25], x_length=9,
                        z_length=9, y_length=12).scale(0.7)
        ax.x_axis.rotate(90 * DEGREES, [1, 0, 0])

        realt_curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([np.real(rect(t, 2) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t, 0]), stroke_width=0,color=YELLOW, t_range=np.array([-5, 5, 0.001]), dt=1))
        imagt_curve = always_redraw(lambda: ParametricFunction(lambda t: [0,2 * t,np.imag(rect(t,2) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)) ], stroke_width=0,color=YELLOW, t_range=np.array([-5, 5, 0.001]), dt=1))

        # area1= always_redraw(lambda : Polygon(*([[0, -10, 0]] + [p for p in (ParametricFunction(lambda t: np.array([0.6*np.real((np.sin(3 * t) + 2 * np.cos(10 * t) + 3 * np.sin(5 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2*t,0]),stroke_width=0, color=YELLOW, t_range = np.array([-5, 5, 0.001]),dt=1)).points if -10 <= p[1] <= 9.99] + [[0, 9.99, 0]])).set_opacity(0.4).set_color([BLUE,GREEN]))

        real_area = always_redraw(lambda: axes.get_area_y(realt_curve, [-10, 10]))
        imag_area = always_redraw(lambda: axes.get_area_y(imagt_curve, [-10, 10]))

        self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.5)
        self.add( axes,imagt_curve, imag_area)
        # self.wait()
        # self.play(tr.animate(run_time=2).set_value(2))
        # self.wait()



        #see imaginrary part
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.5)
        # axes.y_axis.rotate(90*DEGREES,[0,1,0])
        # axes.z_axis.rotate(90*DEGREES,[0,0,1])
        # self.add( axes,imagt_curve, imag_area)





        # self.add(g2, ax2, dot2)
        # self.wait()
        # self.play(MoveAlongPath(dot2, g2), run_time=10)
        # self.wait()


class Equations(Scene):
    def construct(self):
        variable_amp_complex_exponential=MathTex(r'x(t) \hspace{0.2 mm} e^{-j\omega t}').scale(3)
        # self.wait(0.3)
        # self.play(Write(variable_amp_complex_exponential),run_time=0.6)
        # self.wait()
        # w=ValueTracker(-22)
        # omega=always_redraw(lambda :MathTex(r'\omega=2\pi \hspace{0.7 mm} (%0.1f) \hspace{0.7 mm} t' %w.get_value() ,color=RED).scale(4))
        # fourier_transform_integral=MathTex(r'F({{x(t)}}{{)}}={{\int_{-\infty}^{\infty}}}{{x(t)}}{{e^{-jwt}}}dt').scale(2)
        # fourier_transform_integral_expanded=MathTex(r'F({{x(t)}})={{\int_{-\infty}^{\infty}}}{{x(t)}}{{cos( %0.1f t)dt}} -j\int_{-\infty}^{\infty}{{x(t)}}sin(%0.1f t)dt').shift(DOWN)

        # fourier_transform_integral[1].set_color(RED)
        # fourier_transform_integral[6].set_color(RED)
        # fourier_transform_integral_expanded[1].set_color(RED)
        # fourier_transform_integral_expanded[5].set_color(RED)
        # fourier_transform_integral_expanded[8].set_color(RED)
        # self.add(fourier_transform_integral[0],fourier_transform_integral[2],fourier_transform_integral[4],fourier_transform_integral[5])
        # self.play(Write(fourier_transform_integral[0]),run_time=0.3)
        # self.play(Write(fourier_transform_integral[2]),run_time=0.05)
        # self.wait(0.3)
        # self.play(FadeIn(fourier_transform_integral[1]),run_time=0.8)
        # self.wait(0.4)
        # self.play(Write(fourier_transform_integral[3]),run_time=0.8)
        # self.wait(0.3)
        # self.play(FadeIn(fourier_transform_integral[5]),run_time=1)
        # self.wait(0.5)
        # self.play(FadeIn(fourier_transform_integral[4]),run_time=1)
        # self.wait(0.2)
        # self.play(Write(fourier_transform_integral[6]),run_time=0.3)
        #
        # self.wait()

        # self.add(fourier_transform_integral)
        # self.wait(0.5)
        # self.play(fourier_transform_integral.animate(run_time=0.5).scale(0.5))
        #
        # self.play(fourier_transform_integral.animate(run_time=0.5).shift(2*UP))
        # self.wait(0.5)
        # self.play(Write(fourier_transform_integral_expanded[0]),run_time=0.1)
        # self.play(Write(fourier_transform_integral_expanded[1]),run_time=0.1)
        # self.play(Write(fourier_transform_integral_expanded[2]),run_time=0.1)
        # self.wait()
        # self.play(ReplacementTransform(fourier_transform_integral[4::].copy(),fourier_transform_integral_expanded[3:7]),ReplacementTransform(fourier_transform_integral[4::].copy(),fourier_transform_integral_expanded[7::]),run_time=0.5)
        # self.wait()

        # self.add(fourier_transform_integral_expanded[3:7],fourier_transform_integral[4::])
        # self.add(fourier_transform_integral_expanded[7::])

        # fourier_transform_integral_part1 = always_redraw(lambda :  MathTex(
        #     r'{{\int_{-\infty}^{\infty}}}{{x(t)}} \hspace{0.5 mm} {{cos( %0.1f \hspace{0.5 mm} t) \hspace{0.5 mm} dt}} ' % w.get_value()).scale(2.5))
        # fourier_transform_integral_part2 = always_redraw(lambda :  MathTex(
        #     r'-j\int_{-\infty}^{\infty} \hspace{0.5 mm} {{x(t)}}sin(%0.1f \hspace{0.5 mm} t) \hspace{0.5 mm} dt' % w.get_value()).scale(2.5))

        # inverse_fourier_transform=MathTex(r'x(t)=\frac{1}{2\pi} \hspace{0.4 mm} \int_{-\infty }^{\infty } X(\omega) \hspace{0.2 mm} e^{+j\omega t} \hspace{0.7 mm} d \omega ')

        # self.add(inverse_fourier_transform)
        self.play(Write(variable_amp_complex_exponential))
        self.wait()




        # self.play(Write(fourier_transform_integral_part1),run_time=1)
        # self.wait()
        # self.play(w.animate.set_value(22),run_time=6)
        # self.wait()



class Equations2(Scene):
    def construct(self):
        # variable_amp_complex_exponential=MathTex(r'x(t)e^{-j\omega_{o}t}').scale(3)
        # self.wait(0.3)
        # self.play(Write(variable_amp_complex_exponential),run_time=0.6)
        # self.wait()
        w=ValueTracker(-22)
        # omega=always_redraw(lambda :MathTex(r'\omega=2\pi \hspace{0.7 mm} (%0.1f) \hspace{0.7 mm} t' %w.get_value() ,color=RED).scale(4))
        # fourier_transform_integral=MathTex(r'F({{x(t)}}{{)}}={{\int_{-\infty}^{\infty}}}{{x(t)}}{{e^{-jwt}}}dt').scale(2)
        # fourier_transform_integral_expanded=MathTex(r'F({{x(t)}})={{\int_{-\infty}^{\infty}}}{{x(t)}}{{cos( %0.1f t)dt}} -j\int_{-\infty}^{\infty}{{x(t)}}sin(%0.1f t)dt').shift(DOWN)

        # fourier_transform_integral[1].set_color(RED)
        # fourier_transform_integral[6].set_color(RED)
        # fourier_transform_integral_expanded[1].set_color(RED)
        # fourier_transform_integral_expanded[5].set_color(RED)
        # fourier_transform_integral_expanded[8].set_color(RED)
        # self.add(fourier_transform_integral[0],fourier_transform_integral[2],fourier_transform_integral[4],fourier_transform_integral[5])
        # self.play(Write(fourier_transform_integral[0]),run_time=0.3)
        # self.play(Write(fourier_transform_integral[2]),run_time=0.05)
        # self.wait(0.3)
        # self.play(FadeIn(fourier_transform_integral[1]),run_time=0.8)
        # self.wait(0.4)
        # self.play(Write(fourier_transform_integral[3]),run_time=0.8)
        # self.wait(0.3)
        # self.play(FadeIn(fourier_transform_integral[5]),run_time=1)
        # self.wait(0.5)
        # self.play(FadeIn(fourier_transform_integral[4]),run_time=1)
        # self.wait(0.2)
        # self.play(Write(fourier_transform_integral[6]),run_time=0.3)
        #
        # self.wait()

        # self.add(fourier_transform_integral)
        # self.wait(0.5)
        # self.play(fourier_transform_integral.animate(run_time=0.5).scale(0.5))
        #
        # self.play(fourier_transform_integral.animate(run_time=0.5).shift(2*UP))
        # self.wait(0.5)
        # self.play(Write(fourier_transform_integral_expanded[0]),run_time=0.1)
        # self.play(Write(fourier_transform_integral_expanded[1]),run_time=0.1)
        # self.play(Write(fourier_transform_integral_expanded[2]),run_time=0.1)
        # self.wait()
        # self.play(ReplacementTransform(fourier_transform_integral[4::].copy(),fourier_transform_integral_expanded[3:7]),ReplacementTransform(fourier_transform_integral[4::].copy(),fourier_transform_integral_expanded[7::]),run_time=0.5)
        # self.wait()

        # self.add(fourier_transform_integral_expanded[3:7],fourier_transform_integral[4::])
        # self.add(fourier_transform_integral_expanded[7::])

        fourier_transform_integral_part1 = always_redraw(lambda :  MathTex(
            r'{{\int_{-\infty}^{\infty}}}{{x(t)}} \hspace{0.5 mm} {{cos( %0.1f \hspace{0.5 mm} t) \hspace{0.5 mm} dt}} ' % w.get_value()).scale(2.5))
        fourier_transform_integral_part2 = always_redraw(lambda :  MathTex(
            r'-j\int_{-\infty}^{\infty} \hspace{0.5 mm} {{x(t)}}sin(%0.1f \hspace{0.5 mm} t) \hspace{0.5 mm} dt' % w.get_value()).scale(2.5))


        self.play(Write(fourier_transform_integral_part2),run_time=1)
        self.wait()
        self.play(w.animate.set_value(22),run_time=6)
        self.wait()











class ThreeDParametricSpring(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=180 * DEGREES, theta=0 * DEGREES,focal_distance=1000,zoom=0.5)

        tr=ValueTracker(0.5)
        axes = ThreeDAxes(x_range=[-20, 20, 5], y_range=[-11, 11, 2], z_range=[-20, 20, 5], y_length=22, x_length=8,
                          z_length=8)
        curve1 =always_redraw(lambda : ParametricFunction(
            lambda t: np.array([
                0.6*np.real((np.sin(2*np.pi*3 * t) + 2 * np.cos(2*np.pi*10 * t) + 3 * np.sin(5 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),
                2*t,
                0.6*np.imag((np.sin(3 * t) + 2 * np.cos(10 * t) + 3 * np.sin(5 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t))
            ]),stroke_width=1.5, color=YELLOW, t_range = np.array([-5, 5, 0.001]),dt=1)
        )

        ralt_curve=always_redraw(lambda :ParametricFunction(lambda t: np.array([0.6*np.real((np.sin(3 * t) + 2 * np.cos(10 * t) + 3 * np.sin(5 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2*t,0]),stroke_width=0,color=YELLOW, t_range = np.array([-5, 5, 0.001]),dt=1))

        # area1= always_redraw(lambda : Polygon(*([[0, -10, 0]] + [p for p in (ParametricFunction(lambda t: np.array([0.6*np.real((np.sin(3 * t) + 2 * np.cos(10 * t) + 3 * np.sin(5 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2*t,0]),stroke_width=0, color=YELLOW, t_range = np.array([-5, 5, 0.001]),dt=1)).points if -10 <= p[1] <= 9.99] + [[0, 9.99, 0]])).set_opacity(0.4).set_color([BLUE,GREEN]))

        area= always_redraw(lambda :axes.get_area_y(ralt_curve,[-10,10]))



        self.add( ralt_curve,axes,curve1,area)
        # self.wait()
        # self.play(tr.animate(run_time=3).set_value(1))
        # self.wait()




class Scene3(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000,zoom=0.8)
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000)
        ax = ThreeDAxes(x_range=[-1.5, 1.5, 0.25], y_range=[0, 27, 5], z_range=[-1.5, 1.5, 0.25], x_length=9,
                        z_length=9, y_length=12).scale(0.7)
        ax.x_axis.rotate(90*DEGREES,[1,0,0])
        numberplane = NumberPlane(x_range=[-1.5, 1.5, 0.25], y_range=[-1.5, 1.5, 0.25], x_length=9, y_length=9,
                                  background_line_style={
                                      "stroke_color": WHITE,
                                      "stroke_width": 1,
                                      "stroke_opacity": 0.4,
                                  }).scale(0.7).rotate(90 * DEGREES, RIGHT).move_to(ax.get_origin())
        # amp=ValueTracker(1)
        # complexExponential=always_redraw(lambda : MathTex(r'%0.1fe^{i \omega  t }'% amp.get_value(),color=RED).scale(1.5).rotate(90*DEGREES,[1,0,0]).move_to([2.2,0,2.9]))
        # circle=Circle(2.09,color=YELLOW,stroke_width=2).rotate(90*DEGREES,[1,0,0]).move_to(numberplane.get_origin())
        # smallCircle=Circle(1.2,color=YELLOW,stroke_width=2).rotate(90*DEGREES,[1,0,0]).move_to(numberplane.get_origin())
        # largeCircle=Circle(2.4,color=YELLOW,stroke_width=2).rotate(90*DEGREES,[1,0,0]).move_to(numberplane.get_origin())
        #
        # self.add(ax,numberplane,circle)
        # self.wait(0.5)
        # self.play(FadeIn(complexExponential))
        # self.wait(0.2)
        # self.play(Transform(circle,smallCircle),amp.animate.set_value(0.3),run_time=2)
        # self.wait()
        # self.play(Transform(circle,largeCircle),amp.animate.set_value(1.4),run_time=2)
        # self.wait()

        tr=ValueTracker(2)
        pure_complex_exp=always_redraw(lambda : ParametricFunction(lambda t: np.array([2.1 * np.real(  np.exp(1j * 2 * np.pi * tr.get_value() * t)),2 * t,2.1 * np.imag(np.exp(1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 3.5, 0.001]), dt=1).align_to(numberplane,[0,-1,0]))
        modulated_complex_exp = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.5 * np.real((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t,0.5 * np.imag((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t))  * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 3.5, 0.001]), dt=1).align_to(numberplane,[0,-1,0]))

        # self.play(Create(ax),Create(numberplane))
        # self.play(Create(pure_complex_exp))
        # self.wait()
        # self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000,zoom=0.8)
        # self.wait()



        #
        # self.add(ax,numberplane,pure_complex_exp)
        # self.wait(0.5)
        # self.play(tr.animate.set_value(0),run_time=2)
        # self.wait(0.5)
        # self.play(tr.animate.set_value(-3),run_time=2)
        # self.wait()






        self.add(ax,numberplane,pure_complex_exp)
        self.wait(0.5)
        self.play(tr.animate.set_value(3),run_time=1)
        self.wait(0.5)
        self.play(tr.animate.set_value(0.5),run_time=1)
        self.wait(0.5)
        self.play(tr.animate.set_value(3), run_time=1)
        self.wait()



        # self.wait()
        # self.play(ReplacementTransform(pure_complex_exp,modulated_complex_exp))
        # self.wait()
        # self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES, distance=1000)
        # self.wait()




class ComplexRepresentation(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=0*DEGREES,theta=-90*DEGREES,focal_distance=1000,zoom=0.8)
        ax=Axes(x_range=[-1.5,1.5,0.25],y_range=[-1.5,1.5,0.25],x_length=9, y_length=9).set_opacity(0.5)
        dot=Dot(ax.c2p(1,1,0))
        mag_line=always_redraw(lambda : Line(ax.get_origin(),dot.get_center(),color=RED))
        vertical_line1=always_redraw(lambda: ax.get_vertical_line(dot.get_center(),color=YELLOW))
        horizontal_line1=always_redraw(lambda : ax.get_horizontal_line(vertical_line1.get_start(),color=YELLOW))
        angle=always_redraw(lambda : Angle(horizontal_line1,mag_line,quadrant=(1,1),radius=math.sqrt(dot.get_center()[0]**2+dot.get_center()[1]**2)/5,stroke_width=1.5,stroke_color=YELLOW))
        # real_brace=Brace(horizontal_line1,DOWN,color=GREEN)
        # imag_brace=Brace(vertical_line1,RIGHT,color= GREEN)
        real_brace_label=always_redraw(lambda : BraceLabel(horizontal_line1,"Thre \hspace{1 mm} Real \hspace{1 mm} Area",DOWN,font_size=30,color=GREEN))
        imag_brace_label=always_redraw(lambda : BraceLabel(vertical_line1,"The \hspace{1 mm} Imaginary \hspace{1 mm} Area",RIGHT,font_size=30,color=GREEN,))

        # lines=ax.get_lines_to_point(dot.get_center())
        # herzontal_line=always_redraw(lambda : Line(ax.get_origin(),mag_line.get_end*[1,0,0],stroke_color=YELLOW))
        # vertical_line=always_redraw(lambda : Line(herzontal_line.get_end(),dot.get_center(),color=YELLOW))
        numberplane = NumberPlane(x_range=[-1.5, 1.5, 0.25], y_range=[-1.5, 1.5, 0.25], x_length=9, y_length=9,background_line_style={"stroke_color": BLUE,"stroke_width": 1,"stroke_opacity": 0.6,},)
        self.add(numberplane,horizontal_line1,vertical_line1,mag_line,dot,angle,real_brace_label,imag_brace_label)
        self.wait()
        self.play(dot.animate.move_to(ax.c2p( 0.25,0.75,0)))
        self.wait()
        self.play(dot.animate.move_to(ax.c2p( 1,1,0)))
        self.wait()


class Scene111(ThreeDScene):
    def construct(self):
        # self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.5)
        self.set_camera_orientation(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000,zoom=0.5)
        tr = ValueTracker(0.5)






        axes = ThreeDAxes(x_range=[-6, 6, 2], y_range=[0, 11, 2], z_range=[-6, 6, 2], y_length=22, x_length=8,z_length=8)

        numberplane = NumberPlane(x_range=[-6, 6, 2], y_range=[-6, 6, 2], x_length=8, y_length=8,
                                  background_line_style={
                                      "stroke_color": BLUE,
                                      "stroke_width": 1,
                                      "stroke_opacity": 0.4,
                                  }).rotate(90 * DEGREES, RIGHT).move_to(axes.get_origin())


        # pure_complex_exp=always_redraw(lambda : ParametricFunction(lambda t: np.array([0.6 * np.real(  np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t,0.6 * np.imag(np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        curve1 = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.6 * np.real((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t,0.6 * np.imag((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t))  * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))

        realt_curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.6 * np.real((2 * np.sin(2 * np.pi * 0.5 * t) + 3 * np.cos(2 * np.pi * 0.1 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t, 0]), stroke_width=0,color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        imagt_curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0,2 * t, 0.6 * np.imag((2 * np.sin(2 * np.pi * 0.5 * t) + 3 * np.cos(2 * np.pi * 0.1 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=0,color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))

        real_area=always_redraw(lambda :axes.get_area_y(realt_curve,[0,10]))
        imag_area=always_redraw(lambda :axes.get_area_y(imagt_curve,[0,10]))


        # area1= always_redraw(lambda : Polygon(*([[0, -10, 0]] + [p for p in (ParametricFunction(lambda t: np.array([0.6*np.real((np.sin(3 * t) + 2 * np.cos(10 * t) + 3 * np.sin(5 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2*t,0]),stroke_width=0, color=YELLOW, t_range = np.array([-5, 5, 0.001]),dt=1)).points if -10 <= p[1] <= 9.99] + [[0, 9.99, 0]])).set_opacity(0.4).set_color([BLUE,GREEN]))


        # self.add(pure_complex_exp,axes)
        # self.add(axes,realt_curve,imagt_curve,real_area,imag_area)
        # self.add(axes,curve1,realt_curve,real_area)
        # self.wait()
        # self.play(tr.animate(run_time=0.5).set_value(3.3))
        # self.wait()

        # self.add(axes,numberplane,curve1)
        # self.wait()
        # self.move_camera(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000)
        # self.wait(0.5)
        # self.play(FadeIn(realt_curve,real_area))
        # self.wait()


        self.add(axes,numberplane,curve1,realt_curve,real_area)
        # self.wait()
        # self.play(tr.animate.set_value(0),run_time=2)
        # self.wait()



        # self.wait(0.5)
        # self.play(tr.animate(run_time=4).set_value(3))
        # self.wait()

class FTOutput(Scene):
    def construct(self):
        ax1 = Axes(x_range=[-3.25, 3.25, 1], y_range=[-0.5, 2.5, 0.75],y_length=3).shift(2.4*UP)
        xtracker=ValueTracker(2)
        [g1 , dot1] = TheSiGuy_lib.two_d_graph_from_csv(ax=ax1, csvFile='csv_files/area_integration/fig.csv')
        # [path,dot]=TheSiGuy_lib.create_dot_headed_path(g1,xtracker)
        [part1, dotpart2]=TheSiGuy_lib.two_d_graph_reversed_from_csv(ax=ax1,csvFile='csv_files/area_integration/figpart1.csv')
        [part2, dotpart2]=TheSiGuy_lib.two_d_graph_from_csv(ax=ax1,csvFile='csv_files/area_integration/figpart2.csv')
        [part2_reversed, dotpart2_reversed]=TheSiGuy_lib.two_d_graph_reversed_from_csv(ax=ax1,csvFile='csv_files/area_integration/figpart2_reversed.csv')
        [part3_reversed, dotpart3_reversed]=TheSiGuy_lib.two_d_graph_reversed_from_csv(ax=ax1,csvFile='csv_files/area_integration/figpart3.csv')

        dot=Dot(part3_reversed.get_start(),color=RED).scale(0.7)



        self.add(g1,ax1,dot)
        self.wait()
        self.play(MoveAlongPath(dot,part3_reversed),run_time=3)
        self.wait()
        # self.add(dot)
        # self.play(MoveAlongPath(dot,part1),run_time=2)
        # self.wait()

        # self.add(ax1,path,dot)
        # self.wait()
        # self.play(xtracker.animate.set_value(len(g1.points)),run_time=10,rate_function=rate_functions.linear)
        # self.wait()
        # ax1.plot_line_graph()
        # self.play(MoveAlongPath(dot,g1),run_time=5)
        # self.wait()
        # self.play(xtracker.animate.set_value(0),run_time=2)
        # self.wait()




from numpy import linspace,sqrt,sin,exp,convolve,abs, where

class RectFT(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=50 * DEGREES, focal_distance=1000, zoom=0.5)
        # self.set_camera_orientation(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000,zoom=0.5)
        tr = ValueTracker(1)

        def rect(x):
            return where(abs(x)<=2,1,0)






        axes = ThreeDAxes(x_range=[-1.5, 1.5, 0.5], y_range=[-12, 12, 2], z_range=[-1.5, 1.5, 0.5], y_length=22, x_length=8,z_length=8)


        numberplane = NumberPlane(x_range=[-6, 6, 2], y_range=[-6, 6, 2], x_length=8, y_length=8,
                                  background_line_style={
                                      "stroke_color": BLUE,
                                      "stroke_width": 1,
                                      "stroke_opacity": 0.4,
                                  }).rotate(90 * DEGREES, RIGHT).move_to(axes.get_origin())


        # pure_complex_exp=always_redraw(lambda : ParametricFunction(lambda t: np.array([0.6 * np.real(  np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t,0.6 * np.imag(np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        # curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.6 * np.real((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t,0.6 * np.imag((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t))  * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        #
        # realt_curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.6 * np.real((2 * np.sin(2 * np.pi * 0.5 * t) + 3 * np.cos(2 * np.pi * 0.1 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t, 0]), stroke_width=0,color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        # imagt_curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0,2 * t, 0.6 * np.imag((2 * np.sin(2 * np.pi * 0.5 * t) + 3 * np.cos(2 * np.pi * 0.1 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=0,color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))

        # real_area=always_redraw(lambda :axes.get_area_y(realt_curve,[0,10]))
        # imag_area=always_redraw(lambda :axes.get_area_y(imagt_curve,[0,10]))

        t_curve=always_redraw(lambda: axes.plot_parametric_curve(lambda t: np.array([ np.real((rect(t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),t,np.imag((rect(t))  * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]),color=YELLOW,stroke_width=1.5,t_range=[-10,10,0.001]))
        t_curve_constant=always_redraw(lambda: axes.plot_parametric_curve(lambda t: np.array([ np.real((rect(t)) * np.exp(-1j * 2 * np.pi * 1 * t)),t,np.imag((rect(t))  * np.exp(-1j * 2 * np.pi * 1 * t))]),color=YELLOW,stroke_width=1.5,t_range=[-10,10,0.001]))
        t_curve_constant_zerofreq=always_redraw(lambda: axes.plot_parametric_curve(lambda t: np.array([ np.real((rect(t)) * np.exp(-1j * 2 * np.pi * 0 * t)),t,np.imag((rect(t))  * np.exp(-1j * 2 * np.pi * 0 * t))]),color=YELLOW,stroke_width=1.5,t_range=[-10,10,0.001]))
        pure_complex_expo=always_redraw(lambda: axes.plot_parametric_curve(lambda t: np.array([ np.real(  np.exp(-1j * 2 * np.pi * tr.get_value() * t)),t,np.imag( np.exp(-1j * 2 * np.pi * tr.get_value() * t))]),color=YELLOW,stroke_width=1.5,t_range=[-10,10,0.001]))
        pure_complex_expo_constant=always_redraw(lambda: axes.plot_parametric_curve(lambda t: np.array([ np.real(  np.exp(-1j * 2 * np.pi * 1 * t)),t,np.imag( np.exp(-1j * 2 * np.pi * 1 * t))]),color=YELLOW,stroke_width=1.5,t_range=[-10,10,0.001]))




        self.add(axes,t_curve_constant)
        self.play(ReplacementTransform(t_curve_constant,t_curve_constant_zerofreq))
        # self.wait(0.5)
        # self.play(ReplacementTransform(t_curve_constant_zerofreq,t_curve_constant))
        # self.wait(0.5)
        # self.wait()
        # self.play(ReplacementTransform(pure_complex_expo,t_curve))
        # self.wait()

        # self.add(axes,t_curve)
        # area1= always_redraw(lambda : Polygon(*([[0, -10, 0]] + [p for p in (ParametricFunction(lambda t: np.array([0.6*np.real((np.sin(3 * t) + 2 * np.cos(10 * t) + 3 * np.sin(5 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2*t,0]),stroke_width=0, color=YELLOW, t_range = np.array([-5, 5, 0.001]),dt=1)).points if -10 <= p[1] <= 9.99] + [[0, 9.99, 0]])).set_opacity(0.4).set_color([BLUE,GREEN]))

        # self.play(Create(axes))
        # self.wait(0.5)
        # self.play(FadeIn(t_curve))
        # self.wait()

        # self.add(axes,t_curve)
        # self.wait()
        # self.play(tr.animate.set_value(0), run_time=3)
        # self.wait()
        # self.wait()
        # self.play(tr.animate.set_value(0))
        # self.wait()



        # self.add(pure_complex_exp,axes)
        # self.add(axes,realt_curve,imagt_curve,real_area,imag_area)
        # self.add(axes,curve1,realt_curve,real_area)
        # self.wait()
        # self.play(tr.animate(run_time=0.5).set_value(3.3))
        # self.wait()

        # self.add(axes,numberplane,curve1)
        # self.wait()
        # self.move_camera(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000)
        # self.wait(0.5)
        # self.play(FadeIn(realt_curve,real_area))
        # self.wait()


        # self.add(axes,numberplane,curve1,realt_curve,real_area)
        # self.wait()
        # self.play(tr.animate.set_value(0),run_time=3)
        # self.wait()

        # self.add(axes,numberplane,curve1,realt_curve,real_area)
        # self.wait(0.5)
        # self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000,zoom=0.5)
        # self.wait(0.5)
        # self.move_camera(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000,zoom=0.5)
        # self.wait(0.5)




        # self.wait(0.5)
        # self.play(tr.animate(run_time=4).set_value(3))
        # self.wait()

from numpy import linspace,sqrt,sin,exp,convolve,abs, where


class RectFT2(ThreeDScene):
    def construct(self):
        # self.set_camera_orientation(phi=70 * DEGREES, theta=50 * DEGREES, focal_distance=1000, zoom=0.5)
        self.set_camera_orientation(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000,zoom=0.5)
        tr = ValueTracker(0)

        def rect(x):
            return where(abs(x)<=2,1,0)






        axes = ThreeDAxes(x_range=[-1.5, 1.5, 0.5], y_range=[-12, 12, 2], z_range=[-1.5, 1.5, 0.5], y_length=22, x_length=8,z_length=8)


        numberplane = NumberPlane(x_range=[-6, 6, 2], y_range=[-6, 6, 2], x_length=8, y_length=8,
                                  background_line_style={
                                      "stroke_color": BLUE,
                                      "stroke_width": 1,
                                      "stroke_opacity": 0.4,
                                  }).rotate(90 * DEGREES, RIGHT).move_to(axes.get_origin())


        # pure_complex_exp=always_redraw(lambda : ParametricFunction(lambda t: np.array([0.6 * np.real(  np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t,0.6 * np.imag(np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        # curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.6 * np.real((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t,0.6 * np.imag((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t))  * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        #
        # realt_curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.6 * np.real((2 * np.sin(2 * np.pi * 0.5 * t) + 3 * np.cos(2 * np.pi * 0.1 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t, 0]), stroke_width=0,color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        # imagt_curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0,2 * t, 0.6 * np.imag((2 * np.sin(2 * np.pi * 0.5 * t) + 3 * np.cos(2 * np.pi * 0.1 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=0,color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))

        # real_area=always_redraw(lambda :axes.get_area_y(realt_curve,[0,10]))
        # imag_area=always_redraw(lambda :axes.get_area_y(imagt_curve,[0,10]))

        t_curve=always_redraw(lambda: axes.plot_parametric_curve(lambda t: np.array([ np.real((rect(t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),t,np.imag((rect(t))  * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]),color=YELLOW,stroke_width=1.5,t_range=[-10,10,0.001]))

        # self.add(axes,t_curve)
        # area1= always_redraw(lambda : Polygon(*([[0, -10, 0]] + [p for p in (ParametricFunction(lambda t: np.array([0.6*np.real((np.sin(3 * t) + 2 * np.cos(10 * t) + 3 * np.sin(5 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2*t,0]),stroke_width=0, color=YELLOW, t_range = np.array([-5, 5, 0.001]),dt=1)).points if -10 <= p[1] <= 9.99] + [[0, 9.99, 0]])).set_opacity(0.4).set_color([BLUE,GREEN]))

        self.add(axes,t_curve)
        self.wait()
        self.move_camera(phi=70 * DEGREES, theta=50 * DEGREES, focal_distance=1000, zoom=0.5)
        self.wait()


        # self.play(Create(axes))
        # self.wait(0.5)
        # self.play(FadeIn(t_curve))
        # self.wait()

        # self.add(axes,t_curve)
        # self.wait()
        # self.play(tr.animate.set_value(0), run_time=3)
        # self.wait()
        # self.wait()
        # self.play(tr.animate.set_value(0))
        # self.wait()



        # self.add(pure_complex_exp,axes)
        # self.add(axes,realt_curve,imagt_curve,real_area,imag_area)
        # self.add(axes,curve1,realt_curve,real_area)
        # self.wait()
        # self.play(tr.animate(run_time=0.5).set_value(3.3))
        # self.wait()

        # self.add(axes,numberplane,curve1)
        # self.wait()
        # self.move_camera(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000)
        # self.wait(0.5)
        # self.play(FadeIn(realt_curve,real_area))
        # self.wait()


        # self.add(axes,numberplane,curve1,realt_curve,real_area)
        # self.wait()
        # self.play(tr.animate.set_value(0),run_time=3)
        # self.wait()

        # self.add(axes,numberplane,curve1,realt_curve,real_area)
        # self.wait(0.5)
        # self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000,zoom=0.5)
        # self.wait(0.5)
        # self.move_camera(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000,zoom=0.5)
        # self.wait(0.5)




        # self.wait(0.5)
        # self.play(tr.animate(run_time=4).set_value(3))
        # self.wait()



class RectFT3(ThreeDScene):
    def construct(self):
        # self.set_camera_orientation(phi=70 * DEGREES, theta=50 * DEGREES, focal_distance=1000, zoom=0.5)
        self.set_camera_orientation(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000,zoom=0.5)
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000,zoom=0.5)

        tr = ValueTracker(0)

        def rect(x):
            return where(abs(x)<=2,1,0)






        axes = ThreeDAxes(x_range=[-1.5, 1.5, 0.5], y_range=[-12, 12, 2], z_range=[-1.5, 1.5, 0.5], y_length=22, x_length=8,z_length=8)


        numberplane = NumberPlane(x_range=[-6, 6, 2], y_range=[-6, 6, 2], x_length=8, y_length=8,
                                  background_line_style={
                                      "stroke_color": BLUE,
                                      "stroke_width": 1,
                                      "stroke_opacity": 0.4,
                                  }).rotate(90 * DEGREES, RIGHT).move_to(axes.get_origin())


        # pure_complex_exp=always_redraw(lambda : ParametricFunction(lambda t: np.array([0.6 * np.real(  np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t,0.6 * np.imag(np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        # curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.6 * np.real((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t,0.6 * np.imag((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t))  * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        #
        # realt_curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.6 * np.real((2 * np.sin(2 * np.pi * 0.5 * t) + 3 * np.cos(2 * np.pi * 0.1 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t, 0]), stroke_width=0,color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        # imagt_curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0,2 * t, 0.6 * np.imag((2 * np.sin(2 * np.pi * 0.5 * t) + 3 * np.cos(2 * np.pi * 0.1 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=0,color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))

        # real_area=always_redraw(lambda :axes.get_area_y(realt_curve,[0,10]))
        # imag_area=always_redraw(lambda :axes.get_area_y(imagt_curve,[0,10]))

        t_curve=always_redraw(lambda: axes.plot_parametric_curve(lambda t: np.array([ np.real((rect(t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),t,np.imag((rect(t))  * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]),color=YELLOW,stroke_width=1.5,t_range=[-10,10,0.001]))



        realt_curve = always_redraw(lambda: axes.plot_parametric_curve(
            lambda t: np.array([np.real((rect(t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)), t, 0]),
            stroke_width=0, color=YELLOW, t_range=np.array([-10, 10, 0.001])))
        imagt_curve = always_redraw(lambda: axes.plot_parametric_curve(
            lambda t: np.array([0, t, np.imag((rect(t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]),
            stroke_width=0, color=YELLOW, t_range=np.array([-10, 10, 0.001])))

        real_area = always_redraw(lambda: axes.get_area_y(realt_curve, [-10, 10]))
        imag_area = always_redraw(lambda: axes.get_area_y(imagt_curve, [-10, 10]))

        # self.add(axes,t_curve)
        # area1= always_redraw(lambda : Polygon(*([[0, -10, 0]] + [p for p in (ParametricFunction(lambda t: np.array([0.6*np.real((np.sin(3 * t) + 2 * np.cos(10 * t) + 3 * np.sin(5 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2*t,0]),stroke_width=0, color=YELLOW, t_range = np.array([-5, 5, 0.001]),dt=1)).points if -10 <= p[1] <= 9.99] + [[0, 9.99, 0]])).set_opacity(0.4).set_color([BLUE,GREEN]))

        self.add(axes,t_curve,realt_curve,real_area)
        self.wait()
        self.play(tr.animate.set_value(3.5),run_time=3)
        self.wait()



class RectFT4(ThreeDScene):
    def construct(self):
        # self.set_camera_orientation(phi=70 * DEGREES, theta=50 * DEGREES, focal_distance=1000, zoom=0.5)
        self.set_camera_orientation(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000,zoom=0.5)
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000,zoom=0.5)

        tr = ValueTracker(3.5)

        def rect(x):
            return where(abs(x)<=2,1,0)






        axes = ThreeDAxes(x_range=[-1.5, 1.5, 0.5], y_range=[-12, 12, 2], z_range=[-1.5, 1.5, 0.5], y_length=22, x_length=8,z_length=8)


        numberplane = NumberPlane(x_range=[-6, 6, 2], y_range=[-6, 6, 2], x_length=8, y_length=8,
                                  background_line_style={
                                      "stroke_color": BLUE,
                                      "stroke_width": 1,
                                      "stroke_opacity": 0.4,
                                  }).rotate(90 * DEGREES, RIGHT).move_to(axes.get_origin())


        # pure_complex_exp=always_redraw(lambda : ParametricFunction(lambda t: np.array([0.6 * np.real(  np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t,0.6 * np.imag(np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        # curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.6 * np.real((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t,0.6 * np.imag((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t))  * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        #
        # realt_curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.6 * np.real((2 * np.sin(2 * np.pi * 0.5 * t) + 3 * np.cos(2 * np.pi * 0.1 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t, 0]), stroke_width=0,color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        # imagt_curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0,2 * t, 0.6 * np.imag((2 * np.sin(2 * np.pi * 0.5 * t) + 3 * np.cos(2 * np.pi * 0.1 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=0,color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))

        # real_area=always_redraw(lambda :axes.get_area_y(realt_curve,[0,10]))
        # imag_area=always_redraw(lambda :axes.get_area_y(imagt_curve,[0,10]))

        t_curve=always_redraw(lambda: axes.plot_parametric_curve(lambda t: np.array([ np.real((rect(t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),t,np.imag((rect(t))  * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]),color=YELLOW,stroke_width=1.5,t_range=[-10,10,0.001]))

        realt_curve = always_redraw(lambda: axes.plot_parametric_curve(
            lambda t: np.array([np.real((rect(t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)), t, 0]),
            stroke_width=0, color=YELLOW, t_range=np.array([-10, 10, 0.001])))
        imagt_curve = always_redraw(lambda: axes.plot_parametric_curve(
            lambda t: np.array([0, t, np.imag((rect(t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]),
            stroke_width=0, color=YELLOW, t_range=np.array([-10, 10, 0.001])))

        real_area = always_redraw(lambda: axes.get_area_y(realt_curve, [-10, 10]))
        imag_area = always_redraw(lambda: axes.get_area_y(imagt_curve, [-10, 10]))

        # self.add(axes,t_curve)
        # area1= always_redraw(lambda : Polygon(*([[0, -10, 0]] + [p for p in (ParametricFunction(lambda t: np.array([0.6*np.real((np.sin(3 * t) + 2 * np.cos(10 * t) + 3 * np.sin(5 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2*t,0]),stroke_width=0, color=YELLOW, t_range = np.array([-5, 5, 0.001]),dt=1)).points if -10 <= p[1] <= 9.99] + [[0, 9.99, 0]])).set_opacity(0.4).set_color([BLUE,GREEN]))

        self.add(axes,t_curve,realt_curve,real_area)
        self.wait()
        self.play(tr.animate.set_value(0),run_time=3)
        self.wait()



class RectFT5(ThreeDScene):
    def construct(self):
        # self.set_camera_orientation(phi=70 * DEGREES, theta=50 * DEGREES, focal_distance=1000, zoom=0.5)
        self.set_camera_orientation(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000,zoom=0.5)
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000,zoom=0.5)

        tr = ValueTracker(0)

        def rect(x):
            return where(abs(x)<=2,1,0)






        axes = ThreeDAxes(x_range=[-1.5, 1.5, 0.5], y_range=[-12, 12, 2], z_range=[-1.5, 1.5, 0.5], y_length=22, x_length=8,z_length=8)


        numberplane = NumberPlane(x_range=[-6, 6, 2], y_range=[-6, 6, 2], x_length=8, y_length=8,
                                  background_line_style={
                                      "stroke_color": BLUE,
                                      "stroke_width": 1,
                                      "stroke_opacity": 0.4,
                                  }).rotate(90 * DEGREES, RIGHT).move_to(axes.get_origin())


        # pure_complex_exp=always_redraw(lambda : ParametricFunction(lambda t: np.array([0.6 * np.real(  np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t,0.6 * np.imag(np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        # curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.6 * np.real((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t,0.6 * np.imag((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t))  * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        #
        # realt_curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.6 * np.real((2 * np.sin(2 * np.pi * 0.5 * t) + 3 * np.cos(2 * np.pi * 0.1 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t, 0]), stroke_width=0,color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        # imagt_curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0,2 * t, 0.6 * np.imag((2 * np.sin(2 * np.pi * 0.5 * t) + 3 * np.cos(2 * np.pi * 0.1 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=0,color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))

        # real_area=always_redraw(lambda :axes.get_area_y(realt_curve,[0,10]))
        # imag_area=always_redraw(lambda :axes.get_area_y(imagt_curve,[0,10]))

        t_curve=always_redraw(lambda: axes.plot_parametric_curve(lambda t: np.array([ np.real((rect(t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),t,np.imag((rect(t))  * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]),color=YELLOW,stroke_width=1.5,t_range=[-10,10,0.001]))

        # self.add(axes,t_curve)
        # area1= always_redraw(lambda : Polygon(*([[0, -10, 0]] + [p for p in (ParametricFunction(lambda t: np.array([0.6*np.real((np.sin(3 * t) + 2 * np.cos(10 * t) + 3 * np.sin(5 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2*t,0]),stroke_width=0, color=YELLOW, t_range = np.array([-5, 5, 0.001]),dt=1)).points if -10 <= p[1] <= 9.99] + [[0, 9.99, 0]])).set_opacity(0.4).set_color([BLUE,GREEN]))

        realt_curve = always_redraw(lambda: axes.plot_parametric_curve(
            lambda t: np.array([np.real((rect(t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)), t, 0]),
            stroke_width=0, color=YELLOW, t_range=np.array([-10, 10, 0.001])))
        imagt_curve = always_redraw(lambda: axes.plot_parametric_curve(
            lambda t: np.array([0, t, np.imag((rect(t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]),
            stroke_width=0, color=YELLOW, t_range=np.array([-10, 10, 0.001])))

        real_area = always_redraw(lambda: axes.get_area_y(realt_curve, [-10, 10]))
        imag_area = always_redraw(lambda: axes.get_area_y(imagt_curve, [-10, 10]))


        self.add(axes,t_curve,realt_curve,real_area)
        self.wait()
        self.play(tr.animate.set_value(-3.5),run_time=3)
        self.wait()




class RectFT3_2(ThreeDScene):
    def construct(self):
        # self.set_camera_orientation(phi=70 * DEGREES, theta=50 * DEGREES, focal_distance=1000, zoom=0.5)
        # self.set_camera_orientation(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000,zoom=0.5)
        self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000,zoom=0.5)

        tr = ValueTracker(0)

        def rect(x):
            return where(abs(x)<=2,1,0)






        axes = ThreeDAxes(x_range=[-1.5, 1.5, 0.5], y_range=[-12, 12, 2], z_range=[-1.5, 1.5, 0.5], y_length=22, x_length=8,z_length=8)


        numberplane = NumberPlane(x_range=[-6, 6, 2], y_range=[-6, 6, 2], x_length=8, y_length=8,
                                  background_line_style={
                                      "stroke_color": BLUE,
                                      "stroke_width": 1,
                                      "stroke_opacity": 0.4,
                                  }).rotate(90 * DEGREES, RIGHT).move_to(axes.get_origin())


        # pure_complex_exp=always_redraw(lambda : ParametricFunction(lambda t: np.array([0.6 * np.real(  np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t,0.6 * np.imag(np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        # curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.6 * np.real((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t,0.6 * np.imag((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t))  * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        #
        # realt_curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.6 * np.real((2 * np.sin(2 * np.pi * 0.5 * t) + 3 * np.cos(2 * np.pi * 0.1 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t, 0]), stroke_width=0,color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        # imagt_curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0,2 * t, 0.6 * np.imag((2 * np.sin(2 * np.pi * 0.5 * t) + 3 * np.cos(2 * np.pi * 0.1 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=0,color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))

        # real_area=always_redraw(lambda :axes.get_area_y(realt_curve,[0,10]))
        # imag_area=always_redraw(lambda :axes.get_area_y(imagt_curve,[0,10]))

        t_curve=always_redraw(lambda: axes.plot_parametric_curve(lambda t: np.array([ np.real((rect(t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),t,np.imag((rect(t))  * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]),color=YELLOW,stroke_width=1.5,t_range=[-10,10,0.001]))

        # self.add(axes,t_curve)
        # area1= always_redraw(lambda : Polygon(*([[0, -10, 0]] + [p for p in (ParametricFunction(lambda t: np.array([0.6*np.real((np.sin(3 * t) + 2 * np.cos(10 * t) + 3 * np.sin(5 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2*t,0]),stroke_width=0, color=YELLOW, t_range = np.array([-5, 5, 0.001]),dt=1)).points if -10 <= p[1] <= 9.99] + [[0, 9.99, 0]])).set_opacity(0.4).set_color([BLUE,GREEN]))

        realt_curve = always_redraw(lambda: axes.plot_parametric_curve(
            lambda t: np.array([np.real((rect(t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)), t, 0]),
            stroke_width=0, color=YELLOW, t_range=np.array([-10, 10, 0.001])))
        imagt_curve = always_redraw(lambda: axes.plot_parametric_curve(
            lambda t: np.array([0, t, np.imag((rect(t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]),
            stroke_width=0, color=YELLOW, t_range=np.array([-10, 10, 0.001])))

        real_area = always_redraw(lambda: axes.get_area_y(realt_curve, [-10, 10]))
        imag_area = always_redraw(lambda: axes.get_area_y(imagt_curve, [-10, 10]))


        axes.y_axis.rotate(90*DEGREES,[0,1,0])
        axes.z_axis.rotate(90*DEGREES,[0,0,1])


        self.add(axes,t_curve,imagt_curve,imag_area)
        self.wait()
        self.play(tr.animate.set_value(3.5),run_time=3)
        self.wait()



class RectFT4_2(ThreeDScene):
    def construct(self):
        # self.set_camera_orientation(phi=70 * DEGREES, theta=50 * DEGREES, focal_distance=1000, zoom=0.5)
        # self.set_camera_orientation(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000,zoom=0.5)
        self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000,zoom=0.5)

        tr = ValueTracker(3.5)

        def rect(x):
            return where(abs(x)<=2,1,0)






        axes = ThreeDAxes(x_range=[-1.5, 1.5, 0.5], y_range=[-12, 12, 2], z_range=[-1.5, 1.5, 0.5], y_length=22, x_length=8,z_length=8)


        numberplane = NumberPlane(x_range=[-6, 6, 2], y_range=[-6, 6, 2], x_length=8, y_length=8,
                                  background_line_style={
                                      "stroke_color": BLUE,
                                      "stroke_width": 1,
                                      "stroke_opacity": 0.4,
                                  }).rotate(90 * DEGREES, RIGHT).move_to(axes.get_origin())


        # pure_complex_exp=always_redraw(lambda : ParametricFunction(lambda t: np.array([0.6 * np.real(  np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t,0.6 * np.imag(np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        # curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.6 * np.real((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t,0.6 * np.imag((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t))  * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        #
        # realt_curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.6 * np.real((2 * np.sin(2 * np.pi * 0.5 * t) + 3 * np.cos(2 * np.pi * 0.1 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t, 0]), stroke_width=0,color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        # imagt_curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0,2 * t, 0.6 * np.imag((2 * np.sin(2 * np.pi * 0.5 * t) + 3 * np.cos(2 * np.pi * 0.1 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=0,color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))

        # real_area=always_redraw(lambda :axes.get_area_y(realt_curve,[0,10]))
        # imag_area=always_redraw(lambda :axes.get_area_y(imagt_curve,[0,10]))

        t_curve=always_redraw(lambda: axes.plot_parametric_curve(lambda t: np.array([ np.real((rect(t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),t,np.imag((rect(t))  * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]),color=YELLOW,stroke_width=1.5,t_range=[-10,10,0.001]))

        # self.add(axes,t_curve)
        # area1= always_redraw(lambda : Polygon(*([[0, -10, 0]] + [p for p in (ParametricFunction(lambda t: np.array([0.6*np.real((np.sin(3 * t) + 2 * np.cos(10 * t) + 3 * np.sin(5 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2*t,0]),stroke_width=0, color=YELLOW, t_range = np.array([-5, 5, 0.001]),dt=1)).points if -10 <= p[1] <= 9.99] + [[0, 9.99, 0]])).set_opacity(0.4).set_color([BLUE,GREEN]))

        realt_curve = always_redraw(lambda: axes.plot_parametric_curve(
            lambda t: np.array([np.real((rect(t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)), t, 0]),
            stroke_width=0, color=YELLOW, t_range=np.array([-10, 10, 0.001])))
        imagt_curve = always_redraw(lambda: axes.plot_parametric_curve(
            lambda t: np.array([0, t, np.imag((rect(t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]),
            stroke_width=0, color=YELLOW, t_range=np.array([-10, 10, 0.001])))

        real_area = always_redraw(lambda: axes.get_area_y(realt_curve, [-10, 10]))
        imag_area = always_redraw(lambda: axes.get_area_y(imagt_curve, [-10, 10]))

        axes.y_axis.rotate(90 * DEGREES, [0, 1, 0])
        axes.z_axis.rotate(90 * DEGREES, [0, 0, 1])


        self.add(axes,t_curve,imagt_curve,imag_area)
        self.wait()
        self.play(tr.animate.set_value(0),run_time=3)
        self.wait()



class RectFT5_2(ThreeDScene):
    def construct(self):
        # self.set_camera_orientation(phi=70 * DEGREES, theta=50 * DEGREES, focal_distance=1000, zoom=0.5)
        # self.set_camera_orientation(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000,zoom=0.5)
        self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000,zoom=0.5)

        tr = ValueTracker(0)

        def rect(x):
            return where(abs(x)<=2,1,0)






        axes = ThreeDAxes(x_range=[-1.5, 1.5, 0.5], y_range=[-12, 12, 2], z_range=[-1.5, 1.5, 0.5], y_length=22, x_length=8,z_length=8)


        numberplane = NumberPlane(x_range=[-6, 6, 2], y_range=[-6, 6, 2], x_length=8, y_length=8,
                                  background_line_style={
                                      "stroke_color": BLUE,
                                      "stroke_width": 1,
                                      "stroke_opacity": 0.4,
                                  }).rotate(90 * DEGREES, RIGHT).move_to(axes.get_origin())


        # pure_complex_exp=always_redraw(lambda : ParametricFunction(lambda t: np.array([0.6 * np.real(  np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t,0.6 * np.imag(np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        # curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.6 * np.real((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t,0.6 * np.imag((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t))  * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        #
        # realt_curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.6 * np.real((2 * np.sin(2 * np.pi * 0.5 * t) + 3 * np.cos(2 * np.pi * 0.1 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t, 0]), stroke_width=0,color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        # imagt_curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0,2 * t, 0.6 * np.imag((2 * np.sin(2 * np.pi * 0.5 * t) + 3 * np.cos(2 * np.pi * 0.1 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=0,color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))

        # real_area=always_redraw(lambda :axes.get_area_y(realt_curve,[0,10]))
        # imag_area=always_redraw(lambda :axes.get_area_y(imagt_curve,[0,10]))

        t_curve=always_redraw(lambda: axes.plot_parametric_curve(lambda t: np.array([ np.real((rect(t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),t,np.imag((rect(t))  * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]),color=YELLOW,stroke_width=1.5,t_range=[-10,10,0.001]))

        # self.add(axes,t_curve)
        # area1= always_redraw(lambda : Polygon(*([[0, -10, 0]] + [p for p in (ParametricFunction(lambda t: np.array([0.6*np.real((np.sin(3 * t) + 2 * np.cos(10 * t) + 3 * np.sin(5 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2*t,0]),stroke_width=0, color=YELLOW, t_range = np.array([-5, 5, 0.001]),dt=1)).points if -10 <= p[1] <= 9.99] + [[0, 9.99, 0]])).set_opacity(0.4).set_color([BLUE,GREEN]))

        realt_curve = always_redraw(lambda: axes.plot_parametric_curve(
            lambda t: np.array([np.real((rect(t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)), t, 0]),
            stroke_width=0, color=YELLOW, t_range=np.array([-10, 10, 0.001])))
        imagt_curve = always_redraw(lambda: axes.plot_parametric_curve(
            lambda t: np.array([0, t, np.imag((rect(t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]),
            stroke_width=0, color=YELLOW, t_range=np.array([-10, 10, 0.001])))

        real_area = always_redraw(lambda: axes.get_area_y(realt_curve, [-10, 10]))
        imag_area = always_redraw(lambda: axes.get_area_y(imagt_curve, [-10, 10]))

        axes.y_axis.rotate(90 * DEGREES, [0, 1, 0])
        axes.z_axis.rotate(90 * DEGREES, [0, 0, 1])


        self.add(axes,t_curve,imagt_curve,imag_area)
        self.wait()
        self.play(tr.animate.set_value(-3.5),run_time=3)
        self.wait()





class RectFT7(ThreeDScene):
    def construct(self):
        # self.set_camera_orientation(phi=70 * DEGREES, theta=50 * DEGREES, focal_distance=1000, zoom=0.5)
        self.set_camera_orientation(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000,zoom=0.5)
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000,zoom=0.5)

        tr = ValueTracker(-3.5)

        def rect(x):
            return where(abs(x)<=2,1,0)






        axes = ThreeDAxes(x_range=[-1.5, 1.5, 0.5], y_range=[-12, 12, 2], z_range=[-1.5, 1.5, 0.5], y_length=22, x_length=8,z_length=8)


        numberplane = NumberPlane(x_range=[-6, 6, 2], y_range=[-6, 6, 2], x_length=8, y_length=8,
                                  background_line_style={
                                      "stroke_color": BLUE,
                                      "stroke_width": 1,
                                      "stroke_opacity": 0.4,
                                  }).rotate(90 * DEGREES, RIGHT).move_to(axes.get_origin())


        # pure_complex_exp=always_redraw(lambda : ParametricFunction(lambda t: np.array([0.6 * np.real(  np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t,0.6 * np.imag(np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        # curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.6 * np.real((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t,0.6 * np.imag((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t))  * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        #
        # realt_curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.6 * np.real((2 * np.sin(2 * np.pi * 0.5 * t) + 3 * np.cos(2 * np.pi * 0.1 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t, 0]), stroke_width=0,color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        # imagt_curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0,2 * t, 0.6 * np.imag((2 * np.sin(2 * np.pi * 0.5 * t) + 3 * np.cos(2 * np.pi * 0.1 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=0,color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))

        # real_area=always_redraw(lambda :axes.get_area_y(realt_curve,[0,10]))
        # imag_area=always_redraw(lambda :axes.get_area_y(imagt_curve,[0,10]))

        t_curve=always_redraw(lambda: axes.plot_parametric_curve(lambda t: np.array([ np.real((rect(t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),t,np.imag((rect(t))  * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]),color=YELLOW,stroke_width=1.5,t_range=[-10,10,0.001]))

        # self.add(axes,t_curve)
        # area1= always_redraw(lambda : Polygon(*([[0, -10, 0]] + [p for p in (ParametricFunction(lambda t: np.array([0.6*np.real((np.sin(3 * t) + 2 * np.cos(10 * t) + 3 * np.sin(5 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2*t,0]),stroke_width=0, color=YELLOW, t_range = np.array([-5, 5, 0.001]),dt=1)).points if -10 <= p[1] <= 9.99] + [[0, 9.99, 0]])).set_opacity(0.4).set_color([BLUE,GREEN]))

        realt_curve = always_redraw(lambda: axes.plot_parametric_curve(
            lambda t: np.array([np.real((rect(t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)), t, 0]),
            stroke_width=0, color=YELLOW, t_range=np.array([-10, 10, 0.001])))
        imagt_curve = always_redraw(lambda: axes.plot_parametric_curve(
            lambda t: np.array([0, t, np.imag((rect(t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]),
            stroke_width=0, color=YELLOW, t_range=np.array([-10, 10, 0.001])))

        real_area = always_redraw(lambda: axes.get_area_y(realt_curve, [-10, 10]))
        imag_area = always_redraw(lambda: axes.get_area_y(imagt_curve, [-10, 10]))


        self.add(axes,realt_curve,real_area)
        self.wait()
        self.play(tr.animate.set_value(3.5),run_time=6)
        self.wait()





class RectFT7_2(ThreeDScene):
    def construct(self):
        # self.set_camera_orientation(phi=70 * DEGREES, theta=50 * DEGREES, focal_distance=1000, zoom=0.5)
        # self.set_camera_orientation(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000,zoom=0.5)
        self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000,zoom=0.5)

        tr = ValueTracker(-3.5)

        def rect(x):
            return where(abs(x)<=2,1,0)






        axes = ThreeDAxes(x_range=[-1.5, 1.5, 0.5], y_range=[-12, 12, 2], z_range=[-1.5, 1.5, 0.5], y_length=22, x_length=8,z_length=8)


        numberplane = NumberPlane(x_range=[-6, 6, 2], y_range=[-6, 6, 2], x_length=8, y_length=8,
                                  background_line_style={
                                      "stroke_color": BLUE,
                                      "stroke_width": 1,
                                      "stroke_opacity": 0.4,
                                  }).rotate(90 * DEGREES, RIGHT).move_to(axes.get_origin())


        # pure_complex_exp=always_redraw(lambda : ParametricFunction(lambda t: np.array([0.6 * np.real(  np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t,0.6 * np.imag(np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        # curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.6 * np.real((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t,0.6 * np.imag((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t))  * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        #
        # realt_curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.6 * np.real((2 * np.sin(2 * np.pi * 0.5 * t) + 3 * np.cos(2 * np.pi * 0.1 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t, 0]), stroke_width=0,color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        # imagt_curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0,2 * t, 0.6 * np.imag((2 * np.sin(2 * np.pi * 0.5 * t) + 3 * np.cos(2 * np.pi * 0.1 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=0,color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))

        # real_area=always_redraw(lambda :axes.get_area_y(realt_curve,[0,10]))
        # imag_area=always_redraw(lambda :axes.get_area_y(imagt_curve,[0,10]))

        t_curve=always_redraw(lambda: axes.plot_parametric_curve(lambda t: np.array([ np.real((rect(t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),t,np.imag((rect(t))  * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]),color=YELLOW,stroke_width=1.5,t_range=[-10,10,0.001]))

        # self.add(axes,t_curve)
        # area1= always_redraw(lambda : Polygon(*([[0, -10, 0]] + [p for p in (ParametricFunction(lambda t: np.array([0.6*np.real((np.sin(3 * t) + 2 * np.cos(10 * t) + 3 * np.sin(5 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2*t,0]),stroke_width=0, color=YELLOW, t_range = np.array([-5, 5, 0.001]),dt=1)).points if -10 <= p[1] <= 9.99] + [[0, 9.99, 0]])).set_opacity(0.4).set_color([BLUE,GREEN]))

        realt_curve = always_redraw(lambda: axes.plot_parametric_curve(
            lambda t: np.array([np.real((rect(t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)), t, 0]),
            stroke_width=0, color=YELLOW, t_range=np.array([-10, 10, 0.001])))
        imagt_curve = always_redraw(lambda: axes.plot_parametric_curve(
            lambda t: np.array([0, t, np.imag((rect(t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]),
            stroke_width=0, color=YELLOW, t_range=np.array([-10, 10, 0.001])))

        real_area = always_redraw(lambda: axes.get_area_y(realt_curve, [-10, 10]))
        imag_area = always_redraw(lambda: axes.get_area_y(imagt_curve, [-10, 10]))

        axes.y_axis.rotate(90 * DEGREES, [0, 1, 0])
        axes.z_axis.rotate(90 * DEGREES, [0, 0, 1])


        self.add(axes,imagt_curve,imag_area)
        self.wait()
        self.play(tr.animate.set_value(3.5),run_time=6)
        self.wait()



class RectFT8(ThreeDScene):
    def construct(self):
        # self.set_camera_orientation(phi=70 * DEGREES, theta=50 * DEGREES, focal_distance=1000, zoom=0.5)
        self.set_camera_orientation(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000,zoom=0.5)
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000,zoom=0.5)

        tr = ValueTracker(-3.5)

        def rect(x):
            return where(abs(x)<=2,1,0)






        axes = ThreeDAxes(x_range=[-1.5, 1.5, 0.5], y_range=[-12, 12, 2], z_range=[-1.5, 1.5, 0.5], y_length=22, x_length=8,z_length=8)


        numberplane = NumberPlane(x_range=[-6, 6, 2], y_range=[-6, 6, 2], x_length=8, y_length=8,
                                  background_line_style={
                                      "stroke_color": BLUE,
                                      "stroke_width": 1,
                                      "stroke_opacity": 0.4,
                                  }).rotate(90 * DEGREES, RIGHT).move_to(axes.get_origin())


        # pure_complex_exp=always_redraw(lambda : ParametricFunction(lambda t: np.array([0.6 * np.real(  np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t,0.6 * np.imag(np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        # curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.6 * np.real((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t,0.6 * np.imag((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t))  * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        #
        # realt_curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.6 * np.real((2 * np.sin(2 * np.pi * 0.5 * t) + 3 * np.cos(2 * np.pi * 0.1 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t, 0]), stroke_width=0,color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        # imagt_curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0,2 * t, 0.6 * np.imag((2 * np.sin(2 * np.pi * 0.5 * t) + 3 * np.cos(2 * np.pi * 0.1 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=0,color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))

        # real_area=always_redraw(lambda :axes.get_area_y(realt_curve,[0,10]))
        # imag_area=always_redraw(lambda :axes.get_area_y(imagt_curve,[0,10]))

        t_curve=always_redraw(lambda: axes.plot_parametric_curve(lambda t: np.array([ np.real((rect(t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),t,np.imag((rect(t))  * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]),color=YELLOW,stroke_width=0.5,t_range=[-10,10,0.001]))

        # self.add(axes,t_curve)
        # area1= always_redraw(lambda : Polygon(*([[0, -10, 0]] + [p for p in (ParametricFunction(lambda t: np.array([0.6*np.real((np.sin(3 * t) + 2 * np.cos(10 * t) + 3 * np.sin(5 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2*t,0]),stroke_width=0, color=YELLOW, t_range = np.array([-5, 5, 0.001]),dt=1)).points if -10 <= p[1] <= 9.99] + [[0, 9.99, 0]])).set_opacity(0.4).set_color([BLUE,GREEN]))

        realt_curve = always_redraw(lambda: axes.plot_parametric_curve(
            lambda t: np.array([np.real((rect(t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)), t, 0]),
            stroke_width=0, color=YELLOW, t_range=np.array([-10, 10, 0.001])))
        imagt_curve = always_redraw(lambda: axes.plot_parametric_curve(
            lambda t: np.array([0, t, np.imag((rect(t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]),
            stroke_width=0, color=YELLOW, t_range=np.array([-10, 10, 0.001])))

        real_area = always_redraw(lambda: axes.get_area_y(realt_curve, [-10, 10]))
        imag_area = always_redraw(lambda: axes.get_area_y(imagt_curve, [-10, 10]))


        self.add(axes,t_curve,realt_curve,real_area)
        # self.wait()
        # self.play(tr.animate.set_value(3.5),run_time=6)
        # self.wait()


class RectFT6(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=50 * DEGREES, focal_distance=1000, zoom=0.5)
        # self.set_camera_orientation(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000,zoom=0.5)
        tr = ValueTracker(0)

        def rect(x):
            return where(abs(x)<=2,1,0)






        axes = ThreeDAxes(x_range=[-1.5, 1.5, 0.5], y_range=[-12, 12, 2], z_range=[-1.5, 1.5, 0.5], y_length=22, x_length=8,z_length=8)


        numberplane = NumberPlane(x_range=[-6, 6, 2], y_range=[-6, 6, 2], x_length=8, y_length=8,
                                  background_line_style={
                                      "stroke_color": BLUE,
                                      "stroke_width": 1,
                                      "stroke_opacity": 0.4,
                                  }).rotate(90 * DEGREES, RIGHT).move_to(axes.get_origin())


        # pure_complex_exp=always_redraw(lambda : ParametricFunction(lambda t: np.array([0.6 * np.real(  np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t,0.6 * np.imag(np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        # curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.6 * np.real((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t,0.6 * np.imag((2*np.sin(2*np.pi*0.5*t)+3*np.cos(2*np.pi*0.1*t))  * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        #
        # realt_curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.6 * np.real((2 * np.sin(2 * np.pi * 0.5 * t) + 3 * np.cos(2 * np.pi * 0.1 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),2 * t, 0]), stroke_width=0,color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))
        # imagt_curve = always_redraw(lambda: ParametricFunction(lambda t: np.array([0,2 * t, 0.6 * np.imag((2 * np.sin(2 * np.pi * 0.5 * t) + 3 * np.cos(2 * np.pi * 0.1 * t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=0,color=YELLOW, t_range=np.array([0, 10, 0.001]), dt=1).shift([0,-11,0]))

        # real_area=always_redraw(lambda :axes.get_area_y(realt_curve,[0,10]))
        # imag_area=always_redraw(lambda :axes.get_area_y(imagt_curve,[0,10]))

        t_curve=always_redraw(lambda: axes.plot_parametric_curve(lambda t: np.array([ np.real((rect(t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),t,np.imag((rect(t))  * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]),color=YELLOW,stroke_width=1.5,t_range=[-10,10,0.001]))

        realt_curve = always_redraw(lambda: axes.plot_parametric_curve (lambda t: np.array([np.real((rect(t)) * np.exp(-1j * 2 * np.pi * tr.get_value() * t)),t, 0]), stroke_width=0,color=YELLOW, t_range=np.array([-10, 10, 0.001])))
        imagt_curve = always_redraw(lambda: axes.plot_parametric_curve (lambda t: np.array([0,t, np.imag((rect(t))  * np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=0,color=YELLOW, t_range=np.array([-10, 10, 0.001])))

        real_area=always_redraw(lambda :axes.get_area_y(realt_curve,[-10,10]))
        imag_area=always_redraw(lambda :axes.get_area_y(imagt_curve,[-10,10]))

        self.add(axes,t_curve,realt_curve,imagt_curve,real_area,imag_area)





class RectFT2D(Scene):
    def construct(self):
        tracker=ValueTracker(-3.5)
        a=4
        h=1
        def rect(x):
            return where(abs(x)<=0.5,1,0)

        t_ax = Axes(x_range=[-10, 10, 5], y_range=[-0.25, 1.25, 0.25],y_length=3,tips=False).shift(1.8*UP)
        f_ax = Axes(x_range=[-4, 4, 1], y_range=[-1, 4, 1],y_length=4,tips=False).shift(1.8*UP)
        ph_ax = Axes(x_range=[-4, 4, 1], y_range=[-50, 200, 50],y_length=4,tips=False).shift(1.8*UP)

        func=t_ax.plot(lambda t: rect(t),x_range=[-10,10,0.001],discontinuities=[-0.5,0.5])
        f_response= always_redraw(lambda : f_ax.plot(lambda f:np.abs(a*h*np.sinc((2*np.pi*f*a)/(2*np.pi))),x_range=[-3.5,3.5,0.001],stroke_width=2))
        [f_response2,fresdot]=  TheSiGuy_lib.two_d_graph_from_csv(f_ax,'csv_files/area_integration/rect_amp_spectrum.csv',2,color=BLUE)
        ph_response=  ph_ax.plot(lambda f:np.angle(a*h*np.sinc((2*np.pi*f*a)/(2*np.pi)))*180/np.pi,x_range=[-3.5,3.5,0.01],stroke_width=2)
        [ph_response2,dotph]=TheSiGuy_lib.two_d_graph_from_csv(ph_ax,'csv_files/area_integration/rect_phase_spectrum.csv',2,color=BLUE)
        [t_signal,dotph]=TheSiGuy_lib.two_d_graph_from_csv(t_ax,'csv_files/area_integration/rect_function.csv',2)
        f_brace=BraceLabel(f_ax,'Magnitude \hspace{1 mm} Response ',DOWN,color=BLUE)
        ph_brace=BraceLabel(ph_ax,'Phase \hspace{1 mm} Response ',DOWN,color=BLUE)
        # l=len(f_response.points)
        # t=MathTex(l)
        # self.add(t)


        # self.add(ph_ax,ph_response2,ph_brace)


        # self.add(t_signal,t_ax)
        # self.add(ph_ax,ph_response2)
        # self.add(ph_ax)
        # self.wait()
        # self.play(Create(t_signal))
        # self.wait()


        # self.play(Create(f_ax),Write(f_brace),run_time=1)
        # self.add(f_ax,f_brace)
        # self.wait()
        # self.add(f_response)
        # self.play(tracker.animate.set_value(3.5),run_time=6)
        # self.wait()

        # self.play(Create(ph_ax),Write(ph_brace))
        # self.wait()
        # self.play(Create(ph_response2), run_time=6)
        # self.wait()

        self.add(f_ax)
        self.wait(0.5)
        self.play(Create(f_response2))
        self.wait(0.5)

        # self.add(ph_ax)
        # self.wait(0.5)
        # self.play(Create(ph_response2))
        # self.wait(0.5)



