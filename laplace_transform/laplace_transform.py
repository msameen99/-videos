import numpy as np

from imports import *
from pylab import *
################### showing the general complex exponentials in the s plane ############################
# don't forget to get the scene from all camera positions

class CEWithS(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=50 * DEGREES, focal_distance=1000, zoom=0.7)  # 3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7) #xz plane x axis must be rotated 90 degree
        axes = ThreeDAxes(x_range=[-1.5,1.5,0.5], y_range=[0, 12, 2], z_range=[-1.5, 1.5,0.5],x_length=6,z_length=6)
        # axes2 = ThreeDAxes(x_range=[-1.5, 1.5, 1], y_range=[0, 42, 10], z_range=[-1.5, 1.5, 1], x_length=10,z_length=10)
        # axes.y_axis.rotate(90*DEGREES,[0,1,0])
        # axes.z_axis.rotate(90*DEGREES,[0,0,1])

        sigma=ValueTracker(0)
        omega=ValueTracker(0)

        s_curve=always_redraw(lambda : axes.plot_parametric_curve(lambda t: np.array([np.real(np.exp(-1*(sigma.get_value()+1j*2*np.pi*omega.get_value())*t)),t,np.imag(np.exp(-1*(sigma.get_value()+1j*2*omega.get_value()*np.pi)*t))]),stroke_width=1,color=YELLOW,t_range=[0,10,0.001]))
        # self.add(axes,s_curve)
        # self.wait()
        # self.play(sigma.animate(run_time=2).set_value(0))
        # self.wait(0.3)
        # self.play(sigma.animate(run_time=2).set_value(1))
        # self.wait(0.3)
        # self.play(sigma.animate(run_time=2).set_value(-0.2))
        # self.wait()

        self.play(Create(axes))
        self.wait(0.5)
        self.play(Create(s_curve))
        self.wait(0.5)
        self.play(omega.animate(run_time=1,rate_func=rate_functions.linear).set_value(2))
        self.wait()
        self.play(omega.animate(run_time=10,rate_func=rate_functions.linear).set_value(-2))
        self.wait()



class CEWithSTwoD(Scene):
    def construct(self):
        # self.set_camera_orientation(phi=70 * DEGREES, theta=50 * DEGREES, focal_distance=1000, zoom=0.7)  # 3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7) #xz plane x axis must be rotated 90 degree
        ax = Axes(x_range=[0, 12, 2], y_range=[-1.5,1.5,0.5],x_length=7)
        # axes2 = ThreeDAxes(x_range=[-1.5, 1.5, 1], y_range=[0, 42, 10], z_range=[-1.5, 1.5, 1], x_length=10,z_length=10)
        # axes.y_axis.rotate(90*DEGREES,[0,1,0])
        # axes.z_axis.rotate(90*DEGREES,[0,0,1])

        sigma=ValueTracker(0)
        omega=ValueTracker(0)

        curve=always_redraw(lambda :ax.plot(lambda t: np.real(np.exp((sigma.get_value()+1j*2*np.pi*omega.get_value())*t)),color=YELLOW,stroke_width=1,x_range=[0,11,0.001]))

        # self.add(ax,curve)
        # self.add(axes,s_curve)
        # self.wait()
        # self.play(sigma.animate(run_time=2).set_value(0))
        # self.wait(0.3)
        # self.play(sigma.animate(run_time=2).set_value(1))
        # self.wait(0.3)
        # self.play(sigma.animate(run_time=2).set_value(-0.2))
        # self.wait()
        #____________________________
        self.play(Create(ax))
        self.wait(0.5)
        self.play(Create(curve))
        self.wait(0.5)
        self.play(sigma.animate(run_time=2,rate_func=rate_functions.linear).set_value(-0.5))
        self.wait()
        self.play(omega.animate(run_time=4,rate_func=rate_functions.linear).set_value(1.5))
        self.wait()
        #_______________________




class CEWithSTwoD_2(Scene):
    def construct(self):
        # self.set_camera_orientation(phi=70 * DEGREES, theta=50 * DEGREES, focal_distance=1000, zoom=0.7)  # 3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7) #xz plane x axis must be rotated 90 degree
        ax = Axes(x_range=[0, 12, 2], y_range=[-1.5,1.5,0.5],x_length=7)
        # axes2 = ThreeDAxes(x_range=[-1.5, 1.5, 1], y_range=[0, 42, 10], z_range=[-1.5, 1.5, 1], x_length=10,z_length=10)
        # axes.y_axis.rotate(90*DEGREES,[0,1,0])
        # axes.z_axis.rotate(90*DEGREES,[0,0,1])

        sigma=ValueTracker(0)
        omega=ValueTracker(0)

        curve=always_redraw(lambda :ax.plot(lambda t: np.real(np.exp((sigma.get_value()+1j*2*np.pi*omega.get_value())*t)),color=YELLOW,stroke_width=1,x_range=[0,11,0.001]))

        # self.add(ax,curve)
        # self.add(axes,s_curve)
        # self.wait()
        # self.play(sigma.animate(run_time=2).set_value(0))
        # self.wait(0.3)
        # self.play(sigma.animate(run_time=2).set_value(1))
        # self.wait(0.3)
        # self.play(sigma.animate(run_time=2).set_value(-0.2))
        # self.wait()
        #____________________________
        self.play(Create(ax))
        self.wait(0.5)
        self.play(Create(curve))
        self.wait(0.5)
        # self.play(sigma.animate(run_time=2,rate_func=rate_functions.linear).set_value(-0.5))
        # self.wait()
        self.play(omega.animate(run_time=3,rate_func=rate_functions.linear).set_value(2))
        self.wait()
        self.play(omega.animate(run_time=3, rate_func=rate_functions.linear).set_value(-2))
        self.wait()
        #_______________________





class CEWithS2(ThreeDScene):
    def construct(self):
        # self.set_camera_orientation(phi=70 * DEGREES, theta=50 * DEGREES, focal_distance=1000, zoom=0.7)  # 3d view
        self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7) #xz plane x axis must be rotated 90 degree


        axes2 = ThreeDAxes(x_range=[-2, 3, 0.5], y_range=[-20, 20, 5], z_range=[0, 4, 1], x_length=15,
                          y_length=14).shift([0, 0, -3])

        axes2.y_axis.rotate(90*DEGREES,[0,1,0])
        axes2.z_axis.rotate(90*DEGREES,[0,0,1])

        fourier_mag_graph = axes2.plot_parametric_curve(lambda omeg: np.array([0, omeg, np.abs(
            (np.exp(0 + 1j * omeg) - np.exp(-1 * (0 + 1j * omeg))) / (0 + 1j * omeg))]), stroke_width=2,
                                               color=YELLOW, t_range=[-20, 20, 0.01])
        dot= Dot3D(fourier_mag_graph.get_start())

        axes = ThreeDAxes(x_range=[-2, 2, 0.5], y_range=[0, 12, 2], z_range=[-2, 2, 1], x_length=6,
                          z_length=6)
        # axes2 = ThreeDAxes(x_range=[-1.5, 1.5, 1], y_range=[0, 42, 10], z_range=[-1.5, 1.5, 1], x_length=10,z_length=10)
        # axes.y_axis.rotate(90*DEGREES,[0,1,0])
        # axes.z_axis.rotate(90*DEGREES,[0,0,1])

        sigma = ValueTracker(0)
        omega = ValueTracker(0)
        # s_curve = always_redraw(lambda: axes.plot_parametric_curve(lambda t: np.array(
        #     [np.real(  axes2.p2c (dot.get_center())[2] *np.exp(-1 * (sigma.get_value() + 1j  * axes2.p2c (dot.get_center())[1]) * t)), t,
        #      np.imag(axes2.p2c (dot.get_center())[2] *np.exp(-1 * (sigma.get_value() + 1j *  axes2.p2c (dot.get_center())[1]) * t))]), stroke_width=1,
        #                                                            color=YELLOW, t_range=[0, 11.5, 0.001]))


        self.add(axes2,fourier_mag_graph,dot)
        self.wait()
        self.play(MoveAlongPath(dot,fourier_mag_graph,run_time=10),rate_func=rate_functions.linear)
        self.wait()


class CEWithS2_2(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=50 * DEGREES, focal_distance=1000, zoom=0.7)  # 3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7) #xz plane x axis must be rotated 90 degree

        axes2 = ThreeDAxes(x_range=[-2, 3, 0.5], y_range=[-20, 20, 5], z_range=[0, 4, 1], x_length=15,
                          y_length=14).shift([0, 0, -3])

        fourier_mag_graph =  axes2.plot_parametric_curve(lambda omeg: np.array([-1, omeg, np.abs(
            (np.exp(-1 + 1j * omeg) - np.exp(-1 * (-1 + 1j * omeg))) / (-1 + 1j * omeg))]), stroke_width=2,
                                               color=YELLOW, t_range=[-20, 20, 0.01])
        dot= Dot3D(fourier_mag_graph.get_start())

        axes = ThreeDAxes(x_range=[-2, 2, 0.5], y_range=[0, 12, 2], z_range=[-2, 2, 1], x_length=6,
                          z_length=6)
        # axes2 = ThreeDAxes(x_range=[-1.5, 1.5, 1], y_range=[0, 42, 10], z_range=[-1.5, 1.5, 1], x_length=10,z_length=10)
        # axes.y_axis.rotate(90*DEGREES,[0,1,0])
        # axes.z_axis.rotate(90*DEGREES,[0,0,1])

        sigma = ValueTracker(0.5)
        omega = ValueTracker(0)
        # s_curve = always_redraw(lambda: axes.plot_parametric_curve(lambda t: np.array(
        #     [np.real(  axes2.p2c (dot.get_center())[2] *np.exp(-1 * (sigma.get_value() + 1j  * axes2.p2c (dot.get_center())[1]) * t)), t,
        #      np.imag(axes2.p2c (dot.get_center())[2] *np.exp(-1 * (sigma.get_value() + 1j *  axes2.p2c (dot.get_center())[1]) * t))]), stroke_width=1,
        #                                                            color=YELLOW, t_range=[0, 11.5, 0.001]))


        # self.add(axes2.set_opacity(0),fourier_mag_graph.set_opacity(0),dot.set_opacity(0),axes,s_curve)
        self.add(axes2, fourier_mag_graph, dot)
        self.wait()
        self.play(MoveAlongPath(dot,fourier_mag_graph,run_time=10),rate_func=rate_functions.linear)
        self.wait()


class CEWithS3(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=50 * DEGREES, focal_distance=1000, zoom=0.7)  # 3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7) #xz plane x axis must be rotated 90 degree

        axes2 = ThreeDAxes(x_range=[-2, 3, 0.5], y_range=[-20, 20, 5], z_range=[0, 4, 1], x_length=15,
                          y_length=14).shift([0, 0, -3])

        fourier_mag_graph = axes2.plot_parametric_curve(lambda omeg: np.array([0, omeg, np.abs(
            (np.exp(0 + 1j * omeg) - np.exp(-1 * (0 + 1j * omeg))) / (0 + 1j * omeg))]), stroke_width=2,
                                               color=YELLOW, t_range=[-20, 20, 0.01])

        fourier_mag_graph2 = axes2.plot_parametric_curve(lambda omeg: np.array([-1, omeg, np.abs(
            (np.exp(-1 + 1j * omeg) - np.exp(-1 * (-1 + 1j * omeg))) / (-1 + 1j * omeg))]), stroke_width=2,
                                                        color=YELLOW, t_range=[-20, 20, 0.01])


        dot= Dot3D(fourier_mag_graph.get_start())
        dot2= Dot3D(fourier_mag_graph2.get_start())

        # axes = ThreeDAxes(x_range=[-2, 2, 0.5], y_range=[0, 12, 2], z_range=[-2, 2, 1], x_length=6,
        #                   z_length=6)
        # axes2 = ThreeDAxes(x_range=[-1.5, 1.5, 1], y_range=[0, 42, 10], z_range=[-1.5, 1.5, 1], x_length=10,z_length=10)
        # axes.y_axis.rotate(90*DEGREES,[0,1,0])
        # axes.z_axis.rotate(90*DEGREES,[0,0,1])

        # sigma = ValueTracker(0)
        # omega = ValueTracker(0)
        # s_curve = always_redraw(lambda: axes.plot_parametric_curve(lambda t: np.array(
        #     [np.real(  axes2.p2c (dot.get_center())[2] *np.exp(-1 * (sigma.get_value() + 1j  * axes2.p2c (dot.get_center())[1]) * t)), t,
        #      np.imag(axes2.p2c (dot.get_center())[2] *np.exp(-1 * (sigma.get_value() + 1j *  axes2.p2c (dot.get_center())[1]) * t))]), stroke_width=1,
        #                                                            color=YELLOW, t_range=[0, 10, 0.001]))



#____________
        axes = ThreeDAxes(x_range=[-2, 2, 0.5], y_range=[0, 12, 2], z_range=[-2, 2, 1], x_length=6,
                          z_length=6)
        # axes2 = ThreeDAxes(x_range=[-1.5, 1.5, 1], y_range=[0, 42, 10], z_range=[-1.5, 1.5, 1], x_length=10,z_length=10)
        # axes.y_axis.rotate(90*DEGREES,[0,1,0])
        # axes.z_axis.rotate(90*DEGREES,[0,0,1])

        sigma = ValueTracker(0.2)
        omega = ValueTracker(0)
        s_curve = always_redraw(lambda: axes.plot_parametric_curve(lambda t: np.array(
            [np.real(axes2.p2c(dot.get_center())[2] * np.exp(
                -1 * (sigma.get_value() + 1j * axes2.p2c(dot.get_center())[1]) * t)), t,
             np.imag(axes2.p2c(dot.get_center())[2] * np.exp(
                 -1 * (sigma.get_value() + 1j * axes2.p2c(dot.get_center())[1]) * t))]), stroke_width=1,
                                                                   color=YELLOW, t_range=[0, 11.5, 0.001]))

#_____________


        # self.add(axes2,fourier_mag_graph)
        # self.wait(0.5)
        # self.play(ReplacementTransform(fourier_mag_graph.copy(),fourier_mag_graph2))
        # self.play(FadeIn(dot2),run_time=0.5)
        # self.wait(0.5)
        # self.play(MoveAlongPath(dot2,fourier_mag_graph2,run_time=10),rate_func=rate_functions.linear)
        # self.wait()
        self.add(axes,s_curve)


###################### animating fourier transform is decomopsed into linear combination of sinusoids (rectangular function) ############################
# don't forget to get the scene from all camera positions

class FTCurves(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.7)  # 3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7) #xz plane
        axes = ThreeDAxes(x_range=[-5.25, 5.25, 1], y_range=[0, 10, 2], z_range=[-1, 1, 0.5], x_length=15, y_length=14,z_length=4)
        [x, y, z] = TheSiGuy_lib.csv_to_xyz('csv_files/phase_res_of_rect.csv')
        components = []
        mag_responses = []
        pha_responses = []

        for f in np.round(np.arange(-5, 5, 0.1),2):
            index=x.index(f)
            component = axes.plot_parametric_curve(
                lambda t: np.array([f, t, np.abs(np.sinc(f)) * np.cos(2 * np.pi * f * t + np.angle(np.sinc(f)))]),
                stroke_width=2, color=PURPLE_A, t_range=[0, 10, 0.01]).set_stroke(YELLOW , 2)
            mag_spectrum = axes.plot_parametric_curve(lambda t: np.array([t, 0, np.abs(np.sinc(t))]), stroke_width=4,
                                                      color=RED, t_range=[-5, f, 0.01])
            # pha_spectrum=axes.plot_parametric_curve(lambda t:np.array([t,10,np.angle(np.sinc(t))*(1/10)]),stroke_width=4,color=PURPLE_A,t_range=[-5,f,0.01])
            [pha_spectrum, g] = axes.plot_line_graph(x_values=x[0:index+1], y_values=y[0:index+1], z_values=z[0:index+1]).set_stroke(GOLD , 4)
            components.append(component)
            mag_responses.append(mag_spectrum)
            pha_responses.append(pha_spectrum)

        mag_response=axes.plot_parametric_curve(lambda t:np.array([t,0,np.sinc(t)]),t_range=[-5,5],stroke_width=2,color=YELLOW)

        self.add(components[0], axes)
        for i, curve in enumerate(components):
            # self.play(Transform(propagating_wave_curves[0],i))
            # self.remove(propagating_wave_curves[i-1])
            components[i - 1].set_stroke([BLUE, GREEN], 0.8)
            self.add(components[i])
            self.remove(mag_responses[i-1])
            self.remove(pha_responses[i-1])
            self.add(mag_responses[i])
            self.add(pha_responses[i])
            self.wait(0.2)
        self.wait()


        # self.add(axes)
        # self.add(mag_response)
        # self.wait()






###################### animating fourier transform is decomopsed into linear combination of sinusoids (exponential function) ############################
# don't forget to get the scene from all camera positions

class FTCurves2 (ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.7)  # 3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7) #xz plane
        axes = ThreeDAxes(x_range=[-5, 5, 5], y_range=[0, 10, 5], z_range=[-1, 1, 0.5], x_length=15, y_length=14)

        components = []
        freq_responses = []

        for f in np.arange(-5, 5, 0.5):
            component = axes.plot_parametric_curve(lambda t: np.array([f, t, np.abs(1/(1+1j*f)) * np.cos(2 * np.pi * f * t + np.angle(1/(1+1j*f)))]),
                                                   stroke_width=2, color=YELLOW, t_range=[0, 10, 0.01])
            freq_response = axes.plot_parametric_curve(lambda t: np.array([t, 0, np.abs(1/(1+1j*t))]), stroke_width=4,
                                                       color=RED, t_range=[-5, f, 0.01])
            components.append(component)
            freq_responses.append(freq_response)



        self.add(components[0], axes)
        for i, curve in enumerate(components):
            # self.play(Transform(propagating_wave_curves[0],i))
            # self.remove(propagating_wave_curves[i-1])
            components[i - 1].set_stroke([BLUE, GREEN], 0.8)
            self.add(components[i])
            self.remove(freq_responses[i - 1])
            self.add(freq_responses[i])
            self.wait(0.2)
        self.wait()




###################### animating fourier transform is decomopsed into linear combination of sinusoids (rectangular function) ############################
# don't forget to get the scene from all camera positions

class FTCurves3(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.7)  # 3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7) #xz plane
        axes = ThreeDAxes(x_range=[-5, 5, 5], y_range=[0, 10, 5], z_range=[-1, 1, 0.5], x_length=15, y_length=14)

        components = []
        freq_responses = []

        for f in np.arange(-5, 5, 0.6):
            component = axes.plot_parametric_curve(lambda t: np.array([f, t, np.abs(1/(1j*f)) * np.cos(2 * np.pi * f * t + np.abs(1/(1j*f)))]),
                                                   stroke_width=2, color=YELLOW, t_range=[0, 10, 0.01])
            freq_response = axes.plot_parametric_curve(lambda t: np.array([t, 0, np.abs(1/(1j*t))]), stroke_width=4,
                                                       color=RED, t_range=[-5, f, 0.01])
            components.append(component)
            freq_responses.append(freq_response)



        self.add(components[0], axes)
        for i, curve in enumerate(components):
            # self.play(Transform(propagating_wave_curves[0],i))
            # self.remove(propagating_wave_curves[i-1])
            components[i - 1].set_stroke([BLUE, GREEN], 0.8)
            self.add(components[i])
            self.remove(freq_responses[i - 1])
            self.add(freq_responses[i])
            self.wait(0.2)
        self.wait()


###################### animating magnitude and phase responses ############################
# don't forget to get the scene from all camera positions

class FTMagPhaseResponse(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.7)  # 3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7) #xz plane
        axes = ThreeDAxes(x_range=[-5.25, 5.25, 1], y_range=[0, 10, 2], z_range=[-1, 1, 0.5], x_length=15, y_length=14,z_length=4)
        axes2 = ThreeDAxes(x_range=[-5.25, 5.25, 1], y_range=[0, 10, 2], z_range=[-1, 1, 0.5], x_length=15, y_length=14,z_length=4).shift(-2.5*OUT)
        axes2.x_axis.rotate(90*DEGREES,[1,0,0])
        [x, y, z] = TheSiGuy_lib.csv_to_xyz('csv_files/phase_res_of_rect.csv')
        components = []
        mag_responses = []
        pha_responses = []

        for f in np.round(np.arange(-5, 5, 0.1), 2):
            index = x.index(f)
            component = axes.plot_parametric_curve(
                lambda t: np.array([f, t, np.abs(np.sinc(f)) * np.cos(2 * np.pi * f * t + np.angle(np.sinc(f)))]),
                stroke_width=2, color=PURPLE_A, t_range=[0, 10, 0.01]).set_stroke([GREEN,BLUE], 1)
            mag_spectrum = axes.plot_parametric_curve(lambda t: np.array([t, 0, np.abs(np.sinc(t))]), stroke_width=4,
                                                      color=RED, t_range=[-5, f, 0.01])
            # pha_spectrum=axes.plot_parametric_curve(lambda t:np.array([t,10,np.angle(np.sinc(t))*(1/10)]),stroke_width=4,color=PURPLE_A,t_range=[-5,f,0.01])
            [pha_spectrum, g] = axes.plot_line_graph(x_values=x[0:index + 1], y_values=y[0:index + 1],
                                                     z_values=z[0:index + 1]).set_stroke(PURPLE_A, 4)
            components.append(component)
            mag_responses.append(mag_spectrum)
            pha_responses.append(pha_spectrum)
        mag_response=axes.plot_parametric_curve(lambda t:np.array([t,0,np.sinc(t)]),t_range=[-5,5],stroke_width=2,color=YELLOW)


        [phase_response_in_the_second_axis,g2]=axes2.plot_line_graph(x,y,z).set_stroke(PURPLE_A, 2)
        sinusoids=VGroup(*components)
        thewholegraph=[axes,mag_responses[-1],pha_responses[-1]]
        self.add(axes,sinusoids,*mag_responses[-1],*pha_responses[-1] )
        self.wait(0.5)
        self.move_camera(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7,added_anims=[axes.x_axis.animate().rotate(90*DEGREES,[1,0,0]),mag_responses[-1].animate.set_stroke(RED,2),pha_responses[-1].animate.set_stroke(PURPLE_A,2)])
        self.wait(1)
        self.play(FadeOut(sinusoids))
        self.wait(0.5)
        self.play(*[m.animate(run_time=0.3).shift(2.5*OUT) for m in thewholegraph])
        self.wait()
        self.play(Create(axes2),run_time=0.5)
        self.wait(0.5)
        self.play(Transform(pha_responses[-1],phase_response_in_the_second_axis),run_time=0.5)
        self.wait()

        # for i, curve in enumerate(components):
        #     # self.play(Transform(propagating_wave_curves[0],i))
        #     # self.remove(propagating_wave_curves[i-1])
        #     components[i - 1].set_stroke([BLUE, GREEN], 0.8)
        #     self.add(components[i])
        #     self.remove(mag_responses[i-1])
        #     self.remove(pha_responses[i-1])
        #     self.add(mag_responses[i])
        #     self.add(pha_responses[i])
        #     self.wait(0.2)
        # self.wait()


        # self.add(axes)
        # self.add(mag_response)
        # self.wait()


###################### animating magnitude and phase responses (surface) ############################
# don't forget to get the scene from all camera positions

class FTMagPhaseResponse_surf(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.7)  # 3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7) #xz plane
        axes = ThreeDAxes(x_range=[-5, 5, 5], y_range=[0, 10, 5], z_range=[-1, 1, 0.5],x_length=15,y_length=14)

        components = []
        mag_responses=[]
        pha_responses=[]

        for f in np.arange(-5,5,0.5):
            component=axes.plot_parametric_curve(lambda t: np.array([f,t,np.abs(np.sinc(f))* np.cos(2*np.pi*f*t+np.angle(np.sinc(f)))]),stroke_width=2,color=PURPLE_A,t_range=[0,10,0.01]).set_stroke([BLUE, GREEN], 2)
            mag_spectrum=axes.plot_parametric_curve(lambda t:np.array([t,0,np.abs(np.sinc(t))]),stroke_width=4,color=RED,t_range=[-5,f,0.01])
            pha_spectrum=axes.plot_parametric_curve(lambda t:np.array([t,10,np.angle(np.sinc(t))*(1/10)]),stroke_width=4,color=PURPLE_A,t_range=[-5,f,0.01])
            components.append(component)
            mag_responses.append(mag_spectrum)
            pha_responses.append(pha_spectrum)

        mag_response=axes.plot_parametric_curve(lambda t:np.array([t,0,np.sinc(t)]),t_range=[-5,5],stroke_width=2,color=YELLOW)

        surface = []
        for ind in range(len(components)-1):

            pts1=components[ind].points
            pts2=components[ind+1].points
            pts2rev=pts2[::-1]
            polygon = Polygon(*pts1,*pts2rev,fill_opacity=1,stroke_opacity=0,fill_color=[BLUE, GREEN])
            surface.append(polygon)


        sinusoids=VGroup(*components)
        self.add(axes,*surface,*mag_responses[-1],*pha_responses[-1] )
        # self.wait(0.5)
        # self.move_camera(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7,added_anims=[*[sinusoid.animate.set_opacity(0.5) for sinusoid in components],mag_responses[-1].animate.set_stroke(RED,2),pha_responses[-1].animate.set_stroke(PURPLE_A,2)])
        # self.wait(0.5)
        # for i, curve in enumerate(components):
        #     # self.play(Transform(propagating_wave_curves[0],i))
        #     # self.remove(propagating_wave_curves[i-1])
        #     components[i - 1].set_stroke([BLUE, GREEN], 0.8)
        #     self.add(components[i])
        #     self.remove(mag_responses[i-1])
        #     self.remove(pha_responses[i-1])
        #     self.add(mag_responses[i])
        #     self.add(pha_responses[i])
        #     self.wait(0.2)
        # self.wait()


        # self.add(axes)
        # self.add(mag_response)
        # self.wait()




class LTCurvesRect(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.7)  # 3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7) #xz plane
        axes = ThreeDAxes(x_range=[-2, 3, 0.5], y_range=[-20, 20, 5], z_range=[0, 4, 1],x_length=15,y_length=14).shift([0,0,-3])

        components_pos = []
        components_neg = []
        envelops=[]

        for sigma in np.arange(0,3.1,0.1):
            component=axes.plot_parametric_curve(lambda omega: np.array([sigma,omega,np.abs((np.exp(sigma+1j*omega)-np.exp(-1*(sigma+1j*omega)))/(sigma+1j*omega))]),stroke_width=2,color=YELLOW,t_range=[-20,20,0.01])
            # freq_response=axes.plot_parametric_curve(lambda t:np.array([t,0,np.sinc(t)]),stroke_width=4,color=RED,t_range=[-5,f,0.01])
            components_pos.append(component)
            # envelops.append(freq_response)

        for sigma in np.arange(-2,0.1,0.1):
            component=axes.plot_parametric_curve(lambda omega: np.array([sigma,omega,np.abs((np.exp(sigma+1j*omega)-np.exp(-1*(sigma+1j*omega)))/(sigma+1j*omega))]),stroke_width=2,color=YELLOW,t_range=[-20,20,0.01])
            # freq_response=axes.plot_parametric_curve(lambda t:np.array([t,0,np.sinc(t)]),stroke_width=4,color=RED,t_range=[-5,f,0.01])
            components_neg.append(component)
            # envelops.append(freq_response)
        components_neg.reverse()
        mag_response=axes.plot_parametric_curve(lambda t:np.array([t,0,np.sinc(t)]),t_range=[-5,5],stroke_width=2,color=YELLOW)

        surface_pos = []
        surface_neg = []
        for ind in range(len(components_pos) - 1):
            pts1 = components_pos[ind].points
            pts2 = components_pos[ind + 1].points
            pts2rev = pts2[::-1]
            polygon = Polygon(*pts1, *pts2rev, fill_opacity=0.2, stroke_opacity=0, fill_color=[GREEN,BLUE])
            surface_pos.append(polygon)
        for ind in range(len(components_neg) - 1):
            pts1 = components_neg[ind].points
            pts2 = components_neg[ind + 1].points
            pts2rev = pts2[::-1]
            polygon = Polygon(*pts1, *pts2rev, fill_opacity=0.2, stroke_opacity=0, fill_color=[GREEN,BLUE])
            surface_neg.append(polygon)

#______________animating surface creation curve by curve___________________________

        # self.add(components_neg[0], axes)
        # self.wait()
        # for i, curve in enumerate(components_neg):
        #     # self.play(Transform(propagating_wave_curves[0],i))
        #     # self.remove(propagating_wave_curves[i-1])
        #     components_neg[i - 1].set_stroke([BLUE, GREEN], 0.8)
        #     self.add(components_neg[i])
        #     if (i == 0):
        #         continue
        #     else:
        #         self.add(surface_neg[i - 1])
        #
        #     # self.remove(freq_responses[i-1])
        #     # self.add(freq_responses[i])
        #     self.wait(0.2)
        # self.wait()
        # for i, curve in enumerate(components_pos):
        #     # self.play(Transform(propagating_wave_curves[0],i))
        #     # self.remove(propagating_wave_curves[i-1])
        #     components_pos[i - 1].set_stroke([BLUE, GREEN], 0.4)
        #     self.add(components_pos[i])
        #     if (i==0):
        #         continue
        #     else:
        #         self.add(surface_pos[i-1])
        #
        #     # self.remove(freq_responses[i-1])
        #     # self.add(freq_responses[i])
        #     self.wait(0.2)
        # self.wait()
        # self.play(components_pos[0].animate(run_time=1).set_stroke(RED, 6))
        # self.wait()
#___________fourier transform is just a slice of laplace transform___________________________________


        # new_components_pos=[c.set_stroke([BLUE, GREEN], 0.8) for c in components_pos]
        # new_components_neg=[c.set_stroke([BLUE, GREEN], 0.8) for c in components_neg]
        # new_components_pos[0].set_stroke(RED, 6)
        # self.add(axes,*new_components_pos,*new_components_neg,*surface_neg,*surface_pos)
        # self.wait(0.2)
        # self.play(new_components_pos[0].animate(run_time=1).set_stroke([BLUE, GREEN],0.8))
        # self.wait()
#_________________________ S Plane ________________________________
        # new_components_pos=[c.set_stroke([BLUE, GREEN], 0.8) for c in components_pos]
        # new_components_neg=[c.set_stroke([BLUE, GREEN], 0.8) for c in components_neg]
        # self.add(axes,*new_components_pos,*new_components_neg,*surface_neg,*surface_pos)
        # self.wait()
        # self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.4,run_time=2,added_anims=[FadeOut(*components_pos,*components_neg,*surface_neg,*surface_pos,run_time=1)])
        # self.wait()

#______________ fourier graph ______________________________________________
        # axes.y_axis.rotate(90*DEGREES,[0,1,0])
        # axes.z_axis.rotate(90*DEGREES,[0,0,1])
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)
        # self.play(Create(axes),run_time=0.8)
        # self.wait(0.3)
        # self.play(Create(components_neg[0]),run_time=2)
        # self.wait()
        # self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.7,added_anims=[axes.y_axis.animate().rotate(90*DEGREES,[0,1,0]),axes.z_axis.animate().rotate(90*DEGREES,[0,0,1])],run_time=1.5)
        # self.wait()
#_____________________________________________________________________
        self.add(axes)
        self.wait(0.5)
        self.add(components_pos[0])
        self.wait(0.5)
        self.add(components_pos[9])
        self.wait(0.5)
        self.add(components_pos[19])
        self.wait(2)
        for i in random.shuffle(components_pos):
            self.add(i)
            self.wait(0.2)
        self.wait(3)
#______________________________________________________________
class LTCurvesExponential(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.5)  # 3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7) #xz plane
        axes = ThreeDAxes(x_range=[-6, 3, 2], y_range=[-20, 20, 5], z_range=[0, 2, 0.5],x_length=15,y_length=14).shift([0,0,-3])

        components_pos = []
        components_neg = []
        envelops=[]
        pole_location=ValueTracker(1)

        for sigma in np.arange(0,3.4,1):
            component=axes.plot_parametric_curve(lambda omega: np.array([sigma,omega,np.abs((1/((sigma+1j*omega+5))  ))]),stroke_width=1,color=YELLOW,t_range=[-20,20,0.01])
            # freq_response=axes.plot_parametric_curve(lambda t:np.array([t,0,np.sinc(t)]),stroke_width=4,color=RED,t_range=[-5,f,0.01])
            components_pos.append(component)
            # envelops.append(freq_response)

        for sigma in np.arange(-6,0.5,1):
            component=axes.plot_parametric_curve(lambda omega: np.array([sigma,omega,np.abs((1/((sigma+1j*omega+5))))]),stroke_width=1,color=YELLOW,t_range=[-20,20,0.01],use_smoothing=False)
            # freq_response=axes.plot_parametric_curve(lambda t:np.array([t,0,np.sinc(t)]),stroke_width=4,color=RED,t_range=[-5,f,0.01])
            components_neg.append(component)
            # envelops.append(freq_response)
        components_neg.reverse()
        mag_response=axes.plot_parametric_curve(lambda t:np.array([t,0,np.sinc(t)]),t_range=[-5,5],stroke_width=2,color=YELLOW)


#______________generating the surface________________________________________
        # surface_pos = []
        # surface_neg = []
        # for ind in range(len(components_pos) - 1):
        #     pts1 = components_pos[ind].points
        #     pts2 = components_pos[ind + 1].points
        #     pts2rev = pts2[::-1]
        #     polygon = Polygon(*pts1, *pts2rev, fill_opacity=0.2, stroke_opacity=0, fill_color=[GREEN,BLUE])
        #     surface_pos.append(polygon)
        # for ind in range(len(components_neg) - 1):
        #     pts1 = components_pos[ind].points
        #     pts2 = components_pos[ind + 1].points
        #     pts2rev = pts2[::-1]
        #     polygon = Polygon(*pts1, *pts2rev, fill_opacity=0.2, stroke_opacity=0, fill_color=[GREEN,BLUE])
        #     surface_neg.append(polygon)

#______________animating surface creation curve by curve___________________________

        # self.add(components_neg[0], axes)
        # self.wait()
        # for i, curve in enumerate(components_neg):
        #     # self.play(Transform(propagating_wave_curves[0],i))
        #     # self.remove(propagating_wave_curves[i-1])
        #     components_neg[i - 1].set_stroke([BLUE, GREEN], 0.8)
        #     self.add(components_neg[i])
        #     # self.remove(freq_responses[i-1])
        #     # self.add(freq_responses[i])
        #     self.wait(0.2)
        # self.wait()
        # for i, curve in enumerate(components_pos):
        #     # self.play(Transform(propagating_wave_curves[0],i))
        #     # self.remove(propagating_wave_curves[i-1])
        #     components_pos[i - 1].set_stroke([BLUE, GREEN], 0.4)
        #     self.add(components_pos[i])
        #     if (i==0):
        #         continue
        #     else:
        #         self.add(surface_pos[i-1])
        #
        #     # self.remove(freq_responses[i-1])
        #     # self.add(freq_responses[i])
        #     self.wait(0.1)
        # self.wait()
#___________fourier transform is just a slice of laplace transform___________________________________

        self.add(axes)
        self.wait(0.5)
        self.play(Create(components_pos[0]))
        self.wait(0.5)
        self.play(Create(components_neg[1]))
        self.wait(0.5)
        self.play(Create(components_neg[2]))
        self.wait(0.2)
        self.add(components_neg[3])
        self.wait(0.2)
        self.add(components_neg[4])
        self.wait(0.2)
        self.add(components_neg[5])
        self.wait(0.2)
        self.add(components_neg[6])


        self.wait(0.2)
        self.add(components_pos[1])
        self.wait(0.2)
        self.add(components_pos[2])
        self.wait(0.2)
        self.add(components_pos[3])


        self.wait()
        self.play(components_neg[5].animate.set_stroke(color=RED,width=2))
        self.wait()


        # self.play(pole_location.animate(run_time=2).set_value(6))
        # self.wait()
        # self.play(pole_location.animate(run_time=2).set_value(1))
        # self.wait()
        # self.wait()
        # self.play(components_pos[0].animate(run_time=1).set_stroke(RED,6))
        # self.wait()



#____________________________________________________________________________________________________
########################################################################################################################
#_______________animating points in the magnitude and phase surfaces in the s plane_____________________________________

class Try(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.7)  # 3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7) #xz plane
        # self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.5) #xy plane
        axes = ThreeDAxes(x_range=[-2, 3, 0.5], y_range=[-20, 20, 5], z_range=[0, 4, 1],x_length=15,y_length=14).shift([0,0,-3])
        xlbl=axes.get_x_axis_label('x').scale(3)
        ylbl=axes.get_y_axis_label('y').scale(3)
        zlbl=axes.get_z_axis_label('z').scale(3)

        components_pos = []
        components_neg = []
        envelops=[]

        for sigma in np.arange(0,2.1,0.1):
            component=axes.plot_parametric_curve(lambda omega: np.array([sigma,omega,np.abs((np.exp(sigma+1j*omega)-np.exp(-1*(sigma+1j*omega)))/(sigma+1j*omega))]),stroke_width=2,color=YELLOW,t_range=[-20,20,0.01])
            # freq_response=axes.plot_parametric_curve(lambda t:np.array([t,0,np.sinc(t)]),stroke_width=4,color=RED,t_range=[-5,f,0.01])
            components_pos.append(component)
            # envelops.append(freq_response)

        # surface = []
        # for ind in range(len(components_pos) - 1):
        #     pts1 = components_pos[ind].points
        #     pts2 = components_pos[ind + 1].points
        #     pts2rev = pts2[::-1]
        #     polygon = Polygon(*pts1, *pts2rev, fill_opacity=0.2, stroke_opacity=0, fill_color=[BLUE, GREEN])
        #     surface.append(polygon)
        x=ValueTracker(-2)
        radius=ValueTracker(100)
        dot = always_redraw(lambda :Dot3D(axes.input_to_graph_point(x=x.get_value(), graph=components_pos[-1]),color=RED))
        dot2 = always_redraw(lambda :Dot(axes.c2p(*[axes.p2c(dot.get_center())[0],axes.p2c(dot.get_center())[1],0]),color=BLUE).scale(1))
        vertical_line=always_redraw(lambda : DashedLine(dot.get_center(),dot2.get_center(),stroke_width=1))

        lines=always_redraw(lambda :axes.get_lines_to_point(dot2.get_center()))
        self.play(GrowFromCenter(dot, run_time=0.5))
        self.add(axes,xlbl,ylbl,zlbl,*components_pos,dot2,lines,vertical_line)
        self.wait()

        self.wait()
        self.play(x.animate.set_value(2))
        self.wait(3)

        # self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.5,added_anims=[FadeOut(xlbl,ylbl,zlbl,*components_pos,dot,vertical_line)])
        # self.wait()


#____________________________________________________________________________________________________________
        # self.add(axes)
        # self.add(mag_response)
        # self.wait()


class PoleZeroSurface(ThreeDScene):
    def func(self, u, v):
        return np.array([u, v, np.abs(1/(u+1j*v-3))])
    def construct(self):
        # self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.7)  # 3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7) #xz plane
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7) #xz plane

        axes = ThreeDAxes(x_range=[-6, 6, 3], y_range=[-5, 5, 5], z_range=[0, 20, 5], x_length=15, y_length=14)

        axes = ThreeDAxes(x_range=[-4, 4], x_length=8)
        surface = Surface(
            lambda u, v: axes.c2p(*self.func(u, v)),
            u_range=[-4, 6],
            v_range=[0, TAU]
        )

        self.add(axes, surface)




class AdditionOfComplexExoponentials(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.5)
        # self.set_camera_orientation(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000,zoom=0.5)
        tr = ValueTracker(1)






        axes = ThreeDAxes(x_range=[-2, 2, 0.5], y_range=[0, 11, 2], z_range=[-2, 2, 0.5], y_length=22, x_length=8,z_length=8)

        numberplane = NumberPlane(x_range=[-6, 6, 2], y_range=[-6, 6, 2], x_length=8, y_length=8,
                                  background_line_style={
                                      "stroke_color": BLUE,
                                      "stroke_width": 1,
                                      "stroke_opacity": 0.4,
                                  }).rotate(90 * DEGREES, RIGHT).move_to(axes.get_origin())


        CE1=axes.plot_parametric_curve(lambda t: np.array([np.real(  np.exp(-1j * 2 * np.pi * tr.get_value() * t)),t,np.imag(np.exp(-1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=RED, t_range=np.array([0, 10, 0.01]))
        GE1=axes.plot_parametric_curve(lambda t: np.array([np.real(  np.exp((-0.5-1j * 2 * np.pi * tr.get_value()) * t)),t,np.imag(np.exp((-0.5-1j * 2 * np.pi * tr.get_value()) * t))]), stroke_width=1.5, color=RED, t_range=np.array([0, 10, 0.01]))
        CE2=axes.plot_parametric_curve(lambda t: np.array([np.real(  np.exp(1j * 2 * np.pi * tr.get_value() * t)),t,np.imag(np.exp(1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=BLUE, t_range=np.array([0, 10, 0.001]))
        GE2=axes.plot_parametric_curve(lambda t: np.array([np.real(  np.exp((-0.5+1j * 2 * np.pi * tr.get_value()) * t)),t,np.imag(np.exp((-0.5+1j * 2 * np.pi * tr.get_value()) * t))]), stroke_width=1.5, color=BLUE, t_range=np.array([0, 10, 0.01]))

        ce_addition = axes.plot_parametric_curve(lambda t: np.array([1 * np.real(np.exp(-1j * 2 * np.pi * tr.get_value() * t)+np.exp(1j * 2 * np.pi * tr.get_value() * t)), t,1 * np.imag( np.exp(-1j * 2 * np.pi * tr.get_value() * t)+np.exp(1j * 2 * np.pi * tr.get_value() * t))]), stroke_width=1.5, color=YELLOW, t_range=[0, 10, 0.01])
        ge_addition = axes.plot_parametric_curve(lambda t: np.array([1 * np.real(np.exp((-0.5-1j * 2 * np.pi * tr.get_value() )* t)+np.exp((-0.5+1j * 2 * np.pi * tr.get_value() )* t)), t,1 * np.imag( np.exp((-0.5-1j * 2 * np.pi * tr.get_value()) * t)+np.exp((-0.5+1j * 2 * np.pi * tr.get_value()) * t))]), stroke_width=1.5, color=YELLOW, t_range=[0, 10, 0.01])
        # self.add(axes,CE1,CE2)
        self.play(Create(axes),run_time=0.7)
        self.wait(0.3)
        self.play(Create(GE1))
        self.wait(0.3)
        self.play(Create(GE2))
        self.wait()
        self.play(ReplacementTransform(GE1,ge_addition),ReplacementTransform(GE2,ge_addition))
        self.wait(0.5)
        self.move_camera(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.5)
        self.wait()


####################### finding the laplace transform from poles and zeros vectors #####################################
class PoleZeroLT(Scene):
    def construct(self):
        ax=Axes(x_range=[-5,5],y_range=[-5,5])
        ax=Axes(x_range=[-2,2],y_range=[-5,5])
        x_pos=ValueTracker(-0.5)
        y_pos=ValueTracker(4)

        p_x=ValueTracker(0)
        p_y=ValueTracker(0)

        p1x=ValueTracker(-0.5)
        p1y=ValueTracker(3)
        p2x=ValueTracker(-4)
        p2y=ValueTracker(0.5)

        s_point=always_redraw(lambda :Dot(ax.c2p(x_pos.get_value(),y_pos.get_value(),0),color=RED).scale(0.7))

        pole1 =always_redraw(lambda : Cross(stroke_width=2).move_to(ax.c2p(-2,3)).scale(0.08))
        pole2 =always_redraw(lambda : Cross(stroke_width=2).move_to(ax.c2p(-2,-3)).scale(0.08))
        zero1=always_redraw(lambda : Circle(stroke_width=2).move_to(ax.c2p(-1,0,0)).scale(0.08))

        pole = always_redraw(lambda: Cross(stroke_width=2).move_to(ax.c2p(p_x.get_value(), p_y.get_value())).scale(0.15))

        pole1_vect=always_redraw(lambda : Arrow(pole1.get_center(),s_point,buff=0,stroke_width=1,tip_length=0.08,color=YELLOW))
        pole2_vect=always_redraw(lambda : Arrow(pole2.get_center(),s_point,buff=0,stroke_width=1,tip_length=0.08,color=YELLOW))
        zero1_vect=always_redraw(lambda : Arrow(zero1.get_center(),s_point,buff=0,stroke_width=1,tip_length=0.08,color=YELLOW))

        p1=always_redraw(lambda : Dot().move_to(ax.c2p(p1x.get_value(),p1y.get_value())).scale(0.5))
        p2=always_redraw(lambda : Dot().move_to(ax.c2p(p2x.get_value(),p2y.get_value())).scale(0.5))
        p1_vect=always_redraw(lambda : Arrow(ax.get_origin(),p1.get_center(),buff=0,stroke_width=1,tip_length=0.13,color=YELLOW))
        p2_vect=always_redraw(lambda : Arrow(ax.get_origin(),p2.get_center(),buff=0,stroke_width=1,tip_length=0.13,color=YELLOW))
        p1p2_vect=always_redraw(lambda : Arrow(p2.get_center(),p1.get_center(),buff=0,stroke_width=1,tip_length=0.13,color=RED))


        transfer_function=MathTex(r'H(s)=K \frac{\left(s-z_{1}\right) \left(s-z_{2}\right) \ldots\left(s-z_{m-1}\right)\left(s-z_{m}\right)}{\left(s-p_{1}\right)\left(s-p_{2}\right) \ldots\left(s-p_{n-1}\right)\left(s-p_{n}\right)}').scale(0.5).shift(3*UP+3.5*RIGHT)
        transfer_function_rect=SurroundingRectangle(transfer_function,buff=MED_SMALL_BUFF,stroke_width=1)
        mag_and_phase_res=MathTex(r'\begin{aligned} |H(s)| &=K \frac{N_{1} \ldots N_{m}}{D_{1} \ldots D_{n}} \\ \angle H(s) &=\left(\theta_{1}+\ldots+\theta_{n}\right)-\left(\phi_{1}+\ldots+\phi_{n}\right) \end{aligned}').scale(0.5).shift(3*DOWN+3.5*RIGHT)
        mag_and_phase_res_rect=SurroundingRectangle(mag_and_phase_res,buff=MED_SMALL_BUFF,stroke_width=1)

        # self.add(ax,pole1,pole2,zero1,s_point,pole1_vect,pole2_vect,zero1_vect)
        # self.add(transfer_function,transfer_function_rect,ax,p1,p2)
        # self.play(FadeIn(ax,run_time=0.5))
        # self.wait(0.2)
        # self.play(FadeIn(p1,run_time=0.5))
        # self.wait(0.2)
        #
        # self.play(Create(p1_vect))
        # self.wait(0.2)
        # self.play(FadeIn(p2, run_time=0.5))
        # self.wait(0.2)
        # self.play(Create(p2_vect))
        # self.wait(0.2)
        # self.play(Create(p1p2_vect))
        # self.wait()
        # self.add(ax,p1,p2,p1_vect,p2_vect,p1p2_vect)
        # self.wait()
        # self.play(Write(transfer_function),FadeOut(p1,p2,p1_vect,p2_vect,p1p2_vect))
        # self.play(Create(transfer_function_rect))
        # self.wait(0.3)
        # self.play(FadeIn(pole1,pole2,zero1))
        # self.wait()
        #___________________________
        # self.add(ax,pole1,pole2,zero1,transfer_function,transfer_function_rect)
        # self.wait()
        # self.play(FadeIn(s_point),run_time=0.5)
        # self.wait(0.5)
        # self.play(Create(zero1_vect))
        # self.wait(0.5)
        # self.play(Create(pole1_vect),Create(pole2_vect))
        # self.wait()
        #______________________

        # self.add(ax, pole1, pole2, zero1, transfer_function, transfer_function_rect,s_point,zero1_vect,pole1_vect,pole2_vect,mag_and_phase_res,mag_and_phase_res_rect)
        # self.wait()
        # self.play(Write(mag_and_phase_res))
        # self.play(Create(mag_and_phase_res_rect))
        # self.wait()


        #________________________________________________
        # self.add(ax, pole1, pole2, zero1, transfer_function, transfer_function_rect, s_point, zero1_vect, pole1_vect,pole2_vect, mag_and_phase_res, mag_and_phase_res_rect)
        # self.wait()
        # self.play(FadeOut(transfer_function,transfer_function_rect,mag_and_phase_res,mag_and_phase_res_rect))
        # self.play(x_pos.animate.set_value(0),y_pos.animate.set_value(-5),run_time=0.5)
        # self.wait()
        # self.play(x_pos.animate.set_value(0),y_pos.animate.set_value(5),run_time=10)
        # self.wait()

        #___________________________
        # self.play(x_pos.animate.set_value(1),y_pos.animate.set_value(0))
        # self.wait()

        # self.play(Create(ax))
        # self.wait(0.5)
        # self.play(Create(curve))
        # self.wait(0.5)
        # self.play(sigma.animate(run_time=2, rate_func=rate_functions.linear).set_value(-0.5))
        # self.wait()
        # self.play(omega.animate(run_time=4, rate_func=rate_functions.linear).set_value(1.5))
        # self.wait()


        self.play(Create(ax))
        self.wait(0.5)
        self.play(FadeIn(pole))
        self.wait(0.5)
        self.play(p_y.animate(run_time=3, rate_func=rate_functions.linear).set_value(2))
        self.wait()
        self.play(p_y.animate(run_time=3, rate_func=rate_functions.linear).set_value(-2))
        self.wait()
#________________________equations____________________________________________


########################################################################################################################


class Equations1(Scene):
    def construct(self):
        inv_fourier_transform_eq=MathTex(r'x(t) = \frac{1}{2\pi }\int_{-\infty }^{\infty }X(\omega ) \hspace{0.5 mm} e^{j\omega t }d\omega ').scale(1).shift(2.5*UP)
        inv_fourier_transform_surect=SurroundingRectangle(inv_fourier_transform_eq,buff=MED_SMALL_BUFF,stroke_width=1)
        inv_fourier_transform_approximation_eq=MathTex(r'x(t)= \lim_{\Delta  \omega \to 0 } \hspace{1 mm} \frac{1}{2\pi }\sum_{n=-\infty }^{\infty }X(n \Delta  \omega ) \hspace{1 mm} e^{j n \Delta  \omega t } \hspace{1 mm} \Delta  \omega ')
        inv_fourier_transform_approximation_decomposed_eq=MathTex(r'x(t)= \frac{1}{2\pi } \hspace{0.2 mm}  ( ...+ {{X(-3 \hspace{0.3 mm} n \Delta  \omega ) \hspace{1 mm} e^{-3 \hspace{0.1 mm} j \hspace{0.1 mm} n \Delta  \omega t }}}+{{X(-2 \hspace{0.3 mm} n \Delta  \omega ) \hspace{1 mm} e^{-2 \hspace{0.1 mm} j \hspace{0.1 mm} n \Delta  \omega t }}}+{{X(-1 \hspace{0.3 mm} n \Delta  \omega ) \hspace{1 mm} e^{-1 \hspace{0.1 mm} j \hspace{0.1 mm} n \Delta  \omega t }}}+{{X(0 )}}+{{X(1 \hspace{0.3 mm} n \Delta  \omega ) \hspace{1 mm} e^{1 \hspace{0.1 mm} j \hspace{0.1 mm} n \Delta  \omega t }}}+{{X(2 \hspace{0.3 mm} n \Delta  \omega ) \hspace{1 mm} e^{2 \hspace{0.1 mm} j \hspace{0.1 mm} n \Delta  \omega t }}}+{{X(3 \hspace{0.3 mm} n \Delta  \omega ) \hspace{1 mm} e^{3 \hspace{0.1 mm} j \hspace{0.1 mm} n \Delta  \omega t }}}+... )').scale(0.4)
        inv_fourier_transform_approximation_decomposed_rearranged_eq=MathTex(r' x(t)= {{\frac{1}{2\pi } \hspace{0.2 mm}  X(0) \hspace{1 mm}  \hspace{1 mm}}} + {{(X(-1 \hspace{0.3 mm} n \Delta  \omega ) \hspace{1 mm} e^{-1 \hspace{0.1 mm} j \hspace{0.1 mm} n \Delta  \omega t }+X(1 \hspace{0.3 mm} n \Delta  \omega ) \hspace{1 mm} e^{1 \hspace{0.1 mm} j \hspace{0.1 mm} n \Delta  \omega t }) \hspace{1 mm}  \hspace{1 mm}}} + {{(X(-2 \hspace{0.3 mm} n \Delta  \omega ) \hspace{1 mm} e^{-2 \hspace{0.1 mm} j \hspace{0.1 mm} n \Delta  \omega t }+X(2 \hspace{0.3 mm} n \Delta  \omega ) \hspace{1 mm} e^{2 \hspace{0.1 mm} j \hspace{0.1 mm} n \Delta  \omega t }) \hspace{1 mm}  \hspace{1 mm}}}+ {{(X(-3 \hspace{0.3 mm} n \Delta  \omega ) \hspace{1 mm} e^{-3 \hspace{0.1 mm} j \hspace{0.1 mm} n \Delta  \omega t }+X(3 \hspace{0.3 mm} n \Delta  \omega ) \hspace{1 mm} e^{3 \hspace{0.1 mm} j \hspace{0.1 mm} n \Delta  \omega t })}} +...').scale(0.395).shift(1*DOWN)
        inv_fourier_transform_approximation_decomposed_rearranged_eq_sub1=MathTex(r'2 \hspace{0.3 mm} X(1 \hspace{0.3 mm} n \Delta  \omega ) \hspace{1 mm} cos(1 \hspace{0.1 mm} j \hspace{0.1 mm} n \Delta  \omega t )').scale(0.4).move_to(inv_fourier_transform_approximation_decomposed_rearranged_eq[3]).set_color(PURPLE)
        inv_fourier_transform_approximation_decomposed_rearranged_eq_sub2=MathTex(r'2 \hspace{0.3 mm} X(2 \hspace{0.3 mm} n \Delta  \omega ) \hspace{1 mm} cos(2 \hspace{0.1 mm} j \hspace{0.1 mm} n \Delta  \omega t )').scale(0.4).move_to(inv_fourier_transform_approximation_decomposed_rearranged_eq[5]).set_color(BLUE)
        inv_fourier_transform_approximation_decomposed_rearranged_eq_sub3=MathTex(r'2 \hspace{0.3 mm} X(3 \hspace{0.3 mm} n \Delta  \omega ) \hspace{1 mm} cos(3 \hspace{0.1 mm} j \hspace{0.1 mm} n \Delta  \omega t )').scale(0.4).move_to(inv_fourier_transform_approximation_decomposed_rearranged_eq[7]).set_color(GREEN)
        euler_formula = MathTex(r'2 \hspace{0.3 mm} cos(\omega t)=e^{jn \hspace{0.1 mm} \omega t} + e^{-\hspace{0.1 mm}jn \hspace{0.1 mm} \omega t}')
        componentssurect1=SurroundingRectangle(inv_fourier_transform_approximation_decomposed_eq[1],stroke_width=0.8)
        componentssurect2=SurroundingRectangle(inv_fourier_transform_approximation_decomposed_eq[13],stroke_width=0.8)
        componentssurect3=SurroundingRectangle(inv_fourier_transform_approximation_decomposed_eq[3],stroke_width=0.8)
        componentssurect4=SurroundingRectangle(inv_fourier_transform_approximation_decomposed_eq[11],stroke_width=0.8)
        componentssurect5=SurroundingRectangle(inv_fourier_transform_approximation_decomposed_eq[5],stroke_width=0.8)
        componentssurect6=SurroundingRectangle(inv_fourier_transform_approximation_decomposed_eq[9],stroke_width=0.8)

        fourier_transform_eq=MathTex(r'X(\omega ) = \int_{-\infty }^{\infty }x(t) \hspace{0.5 mm} e^{-j\omega t} \hspace{0.4 mm} dt')
        laplace_transform_eq=MathTex(r'X(s) = \int_{-\infty }^{\infty }x(t) \hspace{0.5 mm} e^{-st} \hspace{0.4 mm} dt')
        s=MathTex(r's= \sigma + j\omega ')
        sigma=MathTex(r'\sigma').scale(20)
        jw=MathTex(r'j\omega').scale(15)
        laplace_transform_sjw_eq = MathTex(r' X(s) = \int_{-\infty }^{\infty }x(t) \hspace{0.5 mm} e^{-(\sigma+j\omega)  t} \hspace{0.4 mm} dt')
        laplace_transform_sjw_expanded_eq = MathTex(r' X(s ) = \int_{-\infty }^{\infty }x(t) \hspace{0.5 mm} e^{-\sigma t} \hspace{0.5 mm} e^{-j\omega  t} \hspace{0.4 mm} dt')
        laplace_transform_sjw_expanded2_eq = MathTex(r' X(s) = \int_{-\infty }^{\infty }(x(t) \hspace{0.5 mm} e^{-\sigma t} \hspace{0.5 mm}) \hspace{2 mm} e^{-j\omega  t} \hspace{0.4 mm} dt')


        inv_fourier_transform_approximation_decomposed_eq[1].set_color(GREEN)
        inv_fourier_transform_approximation_decomposed_eq[13].set_color(GREEN)
        inv_fourier_transform_approximation_decomposed_eq[3].set_color(BLUE)
        inv_fourier_transform_approximation_decomposed_eq[11].set_color(BLUE)
        inv_fourier_transform_approximation_decomposed_eq[5].set_color(PURPLE)
        inv_fourier_transform_approximation_decomposed_eq[9].set_color(PURPLE)

        inv_fourier_transform_approximation_decomposed_rearranged_eq[3].set_color(PURPLE)
        inv_fourier_transform_approximation_decomposed_rearranged_eq[5].set_color(BLUE)
        inv_fourier_transform_approximation_decomposed_rearranged_eq[7].set_color(GREEN)

        # self.add(inv_fourier_transform_approximation_decomposed_eq[7])

        # self.play(Write(inv_fourier_transform_eq),run_time=0.7)
        # self.wait(0.5)

        # self.add(inv_fourier_transform_eq.shift(2*UP))
        #_____________________________________________________________
        # self.play(Write(inv_fourier_transform_eq,run_time=0.7),Create(inv_fourier_transform_surect,run_time=1.2),)
        # self.play(ReplacementTransform(inv_fourier_transform_eq.copy(),inv_fourier_transform_approximation_eq))
        # self.wait(1)
        # self.play(ReplacementTransform(inv_fourier_transform_approximation_eq,inv_fourier_transform_approximation_decomposed_eq))
        # self.wait()
        # self.play(ShowCreationThenFadeOut(componentssurect1),ShowCreationThenFadeOut(componentssurect2))
        # self.play(ReplacementTransform(inv_fourier_transform_approximation_decomposed_eq[1].copy(),inv_fourier_transform_approximation_decomposed_rearranged_eq[3]),
        #           ReplacementTransform(inv_fourier_transform_approximation_decomposed_eq[13].copy(),
        #                                inv_fourier_transform_approximation_decomposed_rearranged_eq[3]),
        #
        #
        #           )
        # self.play(ShowCreationThenFadeOut(componentssurect3), ShowCreationThenFadeOut(componentssurect4))
        # self.play(ReplacementTransform(inv_fourier_transform_approximation_decomposed_eq[3].copy(),
        #                                inv_fourier_transform_approximation_decomposed_rearranged_eq[5]),
        #           ReplacementTransform(inv_fourier_transform_approximation_decomposed_eq[11].copy(),
        #                                inv_fourier_transform_approximation_decomposed_rearranged_eq[5]),)
        # self.play(ShowCreationThenFadeOut(componentssurect5), ShowCreationThenFadeOut(componentssurect6))
        # self.play(ReplacementTransform(inv_fourier_transform_approximation_decomposed_eq[5].copy(),
        #                                inv_fourier_transform_approximation_decomposed_rearranged_eq[7]),
        #           ReplacementTransform(inv_fourier_transform_approximation_decomposed_eq[9].copy(),
        #                                inv_fourier_transform_approximation_decomposed_rearranged_eq[7]),)
        # self.play(FadeIn(inv_fourier_transform_approximation_decomposed_rearranged_eq[1]),FadeIn(inv_fourier_transform_approximation_decomposed_rearranged_eq[2]),FadeIn(inv_fourier_transform_approximation_decomposed_rearranged_eq[4]),FadeIn(inv_fourier_transform_approximation_decomposed_rearranged_eq[6]),FadeIn(inv_fourier_transform_approximation_decomposed_rearranged_eq[0]),FadeIn(inv_fourier_transform_approximation_decomposed_rearranged_eq[8]),run_time=0.7)
        # self.wait()
        # self.play(ReplacementTransform(inv_fourier_transform_approximation_decomposed_rearranged_eq[3],inv_fourier_transform_approximation_decomposed_rearranged_eq_sub1),ReplacementTransform(inv_fourier_transform_approximation_decomposed_rearranged_eq[5],inv_fourier_transform_approximation_decomposed_rearranged_eq_sub2),ReplacementTransform(inv_fourier_transform_approximation_decomposed_rearranged_eq[7],inv_fourier_transform_approximation_decomposed_rearranged_eq_sub3))
        # self.wait()
#_____________________________________________________________________________________________
        # self.wait(0.2)
        # self.play(GrowFromCenter(sigma),run_time=0.5)
        # self.wait()
        #
        self.wait(0.2)
        self.play(GrowFromCenter(jw),run_time=0.5)
        self.wait()



class Equations3(Scene):
    def construct(self):
        inv_fourier_transform_eq=MathTex(r'x(t) = \frac{1}{2\pi }\int_{-\infty }^{\infty }X(\omega ) \hspace{0.5 mm} e^{j\omega t }d\omega ').scale(1).shift(2.5*UP)
        inv_fourier_transform_surect=SurroundingRectangle(inv_fourier_transform_eq,buff=MED_SMALL_BUFF,stroke_width=1)
        inv_fourier_transform_approximation_eq=MathTex(r'x(t)= \lim_{\Delta  \omega \to 0 } \hspace{1 mm} \frac{1}{2\pi }\sum_{n=-\infty }^{\infty }X(n \Delta  \omega ) \hspace{1 mm} e^{j n \Delta  \omega t } \hspace{1 mm} \Delta  \omega ')
        inv_fourier_transform_approximation_decomposed_eq=MathTex(r'x(t)= \frac{1}{2\pi } \hspace{0.2 mm}  ( ...+ {{X(-3 \hspace{0.3 mm} n \Delta  \omega ) \hspace{1 mm} e^{-3 \hspace{0.1 mm} j \hspace{0.1 mm} n \Delta  \omega t }}}+{{X(-2 \hspace{0.3 mm} n \Delta  \omega ) \hspace{1 mm} e^{-2 \hspace{0.1 mm} j \hspace{0.1 mm} n \Delta  \omega t }}}+{{X(-1 \hspace{0.3 mm} n \Delta  \omega ) \hspace{1 mm} e^{-1 \hspace{0.1 mm} j \hspace{0.1 mm} n \Delta  \omega t }}}+{{X(0 )}}+{{X(1 \hspace{0.3 mm} n \Delta  \omega ) \hspace{1 mm} e^{1 \hspace{0.1 mm} j \hspace{0.1 mm} n \Delta  \omega t }}}+{{X(2 \hspace{0.3 mm} n \Delta  \omega ) \hspace{1 mm} e^{2 \hspace{0.1 mm} j \hspace{0.1 mm} n \Delta  \omega t }}}+{{X(3 \hspace{0.3 mm} n \Delta  \omega ) \hspace{1 mm} e^{3 \hspace{0.1 mm} j \hspace{0.1 mm} n \Delta  \omega t }}}+... )').scale(0.4)
        inv_fourier_transform_approximation_decomposed_rearranged_eq=MathTex(r' x(t)= {{\frac{1}{2\pi } \hspace{0.2 mm}  X(0) \hspace{1 mm}  \hspace{1 mm}}} + {{(X(-1 \hspace{0.3 mm} n \Delta  \omega ) \hspace{1 mm} e^{-1 \hspace{0.1 mm} j \hspace{0.1 mm} n \Delta  \omega t }+X(1 \hspace{0.3 mm} n \Delta  \omega ) \hspace{1 mm} e^{1 \hspace{0.1 mm} j \hspace{0.1 mm} n \Delta  \omega t }) \hspace{1 mm}  \hspace{1 mm}}} + {{(X(-2 \hspace{0.3 mm} n \Delta  \omega ) \hspace{1 mm} e^{-2 \hspace{0.1 mm} j \hspace{0.1 mm} n \Delta  \omega t }+X(2 \hspace{0.3 mm} n \Delta  \omega ) \hspace{1 mm} e^{2 \hspace{0.1 mm} j \hspace{0.1 mm} n \Delta  \omega t }) \hspace{1 mm}  \hspace{1 mm}}}+ {{(X(-3 \hspace{0.3 mm} n \Delta  \omega ) \hspace{1 mm} e^{-3 \hspace{0.1 mm} j \hspace{0.1 mm} n \Delta  \omega t }+X(3 \hspace{0.3 mm} n \Delta  \omega ) \hspace{1 mm} e^{3 \hspace{0.1 mm} j \hspace{0.1 mm} n \Delta  \omega t })}} +...').scale(0.395).shift(1*DOWN)
        inv_fourier_transform_approximation_decomposed_rearranged_eq_sub1=MathTex(r'2 \hspace{0.3 mm} X(1 \hspace{0.3 mm} n \Delta  \omega ) \hspace{1 mm} cos(1 \hspace{0.1 mm} j \hspace{0.1 mm} n \Delta  \omega t )').scale(0.4).move_to(inv_fourier_transform_approximation_decomposed_rearranged_eq[3]).set_color(PURPLE)
        inv_fourier_transform_approximation_decomposed_rearranged_eq_sub2=MathTex(r'2 \hspace{0.3 mm} X(2 \hspace{0.3 mm} n \Delta  \omega ) \hspace{1 mm} cos(2 \hspace{0.1 mm} j \hspace{0.1 mm} n \Delta  \omega t )').scale(0.4).move_to(inv_fourier_transform_approximation_decomposed_rearranged_eq[5]).set_color(BLUE)
        inv_fourier_transform_approximation_decomposed_rearranged_eq_sub3=MathTex(r'2 \hspace{0.3 mm} X(3 \hspace{0.3 mm} n \Delta  \omega ) \hspace{1 mm} cos(3 \hspace{0.1 mm} j \hspace{0.1 mm} n \Delta  \omega t )').scale(0.4).move_to(inv_fourier_transform_approximation_decomposed_rearranged_eq[7]).set_color(GREEN)
        euler_formula = MathTex(r'2 \hspace{0.3 mm} cos(\omega t)=e^{jn \hspace{0.1 mm} \omega t} + e^{-\hspace{0.1 mm}jn \hspace{0.1 mm} \omega t}')
        componentssurect1=SurroundingRectangle(inv_fourier_transform_approximation_decomposed_eq[1],stroke_width=0.8)
        componentssurect2=SurroundingRectangle(inv_fourier_transform_approximation_decomposed_eq[13],stroke_width=0.8)
        componentssurect3=SurroundingRectangle(inv_fourier_transform_approximation_decomposed_eq[3],stroke_width=0.8)
        componentssurect4=SurroundingRectangle(inv_fourier_transform_approximation_decomposed_eq[11],stroke_width=0.8)
        componentssurect5=SurroundingRectangle(inv_fourier_transform_approximation_decomposed_eq[5],stroke_width=0.8)
        componentssurect6=SurroundingRectangle(inv_fourier_transform_approximation_decomposed_eq[9],stroke_width=0.8)

        laplace_transform_eq=MathTex(r'X(s) = \int_{-\infty }^{\infty }x(t) \hspace{0.5 mm} e^{-{{s}}t} \hspace{0.4 mm} dt').shift(2*UP)
        laplace_transform_surect=always_redraw(lambda : SurroundingRectangle(laplace_transform_eq,buff=MED_LARGE_BUFF,stroke_width=0.5))
        laplace_transform_sjw_eq = MathTex(r' X(s) = \int_{-\infty }^{\infty }x(t) \hspace{0.5 mm} e^{-(\sigma+j\omega)  t} \hspace{0.4 mm} dt').move_to(laplace_transform_eq)
        laplace_transform_sjw_expanded_eq = MathTex(r' X(s ) = \int_{-\infty }^{\infty }x(t) \hspace{0.5 mm} e^{-\sigma t} \hspace{0.5 mm} e^{-j\omega  t} \hspace{0.4 mm} dt').move_to(laplace_transform_eq)
        laplace_transform_sjw_expanded2_eq = MathTex(r' X(s) = \int_{-\infty }^{\infty }(x(t) \hspace{0.5 mm} e^{-\sigma t} \hspace{0.5 mm}) \hspace{2 mm} e^{-j\omega  t} \hspace{0.4 mm} dt').move_to(laplace_transform_eq)
        fourier_transform_eq=always_redraw(lambda : MathTex(r'X(\omega ) = \int_{-\infty }^{\infty }x(t) \hspace{0.5 mm} e^{-j\omega t} \hspace{0.4 mm} dt').next_to(laplace_transform_surect,DOWN,buff=MED_LARGE_BUFF))
        line = always_redraw(lambda: Line(3 * LEFT, 3 * RIGHT, stroke_width=0.1, color=YELLOW).next_to(fourier_transform_eq, DOWN,buff=MED_SMALL_BUFF))
        s =always_redraw(lambda : MathTex(r'{{s=}} {{\sigma + j\omega}} ',color=RED).next_to(line, DOWN,buff=MED_SMALL_BUFF))
        s_exponent =always_redraw(lambda : MathTex(r'{{s=}} {{(\sigma + j\omega)}} ').scale(0.5).move_to(laplace_transform_eq[1]))





        inv_fourier_transform_approximation_decomposed_eq[1].set_color(GREEN)
        inv_fourier_transform_approximation_decomposed_eq[13].set_color(GREEN)
        inv_fourier_transform_approximation_decomposed_eq[3].set_color(BLUE)
        inv_fourier_transform_approximation_decomposed_eq[11].set_color(BLUE)
        inv_fourier_transform_approximation_decomposed_eq[5].set_color(PURPLE)
        inv_fourier_transform_approximation_decomposed_eq[9].set_color(PURPLE)

        inv_fourier_transform_approximation_decomposed_rearranged_eq[3].set_color(PURPLE)
        inv_fourier_transform_approximation_decomposed_rearranged_eq[5].set_color(BLUE)
        inv_fourier_transform_approximation_decomposed_rearranged_eq[7].set_color(GREEN)


#_____________________________________
        self.play(Write(laplace_transform_eq,run_time=0.9),Create(laplace_transform_surect,run_time=1.2))
        self.wait()
        self.play(Write(fourier_transform_eq),run_time=0.9)
        self.wait(0.5)
        # self.play(Create(line))
        # self.wait(0.5)
        self.play(ReplacementTransform(laplace_transform_eq[1].copy(),s))
        self.wait(0.5)
        self.play(Transform(laplace_transform_eq,laplace_transform_sjw_eq))
        self.wait(0.5)
        self.play(Transform(laplace_transform_eq,laplace_transform_sjw_expanded_eq))
        self.wait(0.5)
        self.play(Transform(laplace_transform_eq, laplace_transform_sjw_expanded2_eq))
        self.wait(0.5)

        self.add(laplace_transform_sjw_expanded2_eq)
#_________________________________

        # self.add(inv_fourier_transform_approximation_decomposed_eq[7])

        # self.play(Write(inv_fourier_transform_eq),run_time=0.7)
        # self.wait(0.5)

        # self.add(inv_fourier_transform_eq.shift(2*UP))
        # self.play(Write(inv_fourier_transform_eq,run_time=0.7),Create(inv_fourier_transform_surect,run_time=1.2),)
        # self.play(ReplacementTransform(inv_fourier_transform_eq.copy(),inv_fourier_transform_approximation_eq))
        # self.wait(1)
        # self.play(ReplacementTransform(inv_fourier_transform_approximation_eq,inv_fourier_transform_approximation_decomposed_eq))
        # self.wait()
        # self.play(ShowCreationThenFadeOut(componentssurect1),ShowCreationThenFadeOut(componentssurect2))
        # self.play(ReplacementTransform(inv_fourier_transform_approximation_decomposed_eq[1].copy(),inv_fourier_transform_approximation_decomposed_rearranged_eq[3]),
        #           ReplacementTransform(inv_fourier_transform_approximation_decomposed_eq[13].copy(),
        #                                inv_fourier_transform_approximation_decomposed_rearranged_eq[3]),
        #
        #
        #           )
        # self.play(ShowCreationThenFadeOut(componentssurect3), ShowCreationThenFadeOut(componentssurect4))
        # self.play(ReplacementTransform(inv_fourier_transform_approximation_decomposed_eq[3].copy(),
        #                                inv_fourier_transform_approximation_decomposed_rearranged_eq[5]),
        #           ReplacementTransform(inv_fourier_transform_approximation_decomposed_eq[11].copy(),
        #                                inv_fourier_transform_approximation_decomposed_rearranged_eq[5]),)
        # self.play(ShowCreationThenFadeOut(componentssurect5), ShowCreationThenFadeOut(componentssurect6))
        # self.play(ReplacementTransform(inv_fourier_transform_approximation_decomposed_eq[5].copy(),
        #                                inv_fourier_transform_approximation_decomposed_rearranged_eq[7]),
        #           ReplacementTransform(inv_fourier_transform_approximation_decomposed_eq[9].copy(),
        #                                inv_fourier_transform_approximation_decomposed_rearranged_eq[7]),)
        # self.play(FadeIn(inv_fourier_transform_approximation_decomposed_rearranged_eq[1]),FadeIn(inv_fourier_transform_approximation_decomposed_rearranged_eq[2]),FadeIn(inv_fourier_transform_approximation_decomposed_rearranged_eq[4]),FadeIn(inv_fourier_transform_approximation_decomposed_rearranged_eq[6]),FadeIn(inv_fourier_transform_approximation_decomposed_rearranged_eq[0]),FadeIn(inv_fourier_transform_approximation_decomposed_rearranged_eq[8]),run_time=0.7)
        # self.wait()
        # self.play(ReplacementTransform(inv_fourier_transform_approximation_decomposed_rearranged_eq[3],inv_fourier_transform_approximation_decomposed_rearranged_eq_sub1),ReplacementTransform(inv_fourier_transform_approximation_decomposed_rearranged_eq[5],inv_fourier_transform_approximation_decomposed_rearranged_eq_sub2),ReplacementTransform(inv_fourier_transform_approximation_decomposed_rearranged_eq[7],inv_fourier_transform_approximation_decomposed_rearranged_eq_sub3))
        # self.wait()




################ sum rational function plot ####################################

class Rational(Scene):
    def construct(self):
        ax=Axes(x_range=[-10,10,2],y_range=[0,10,2])
        # r1=ax.plot(lambda t:np.abs (1/(t+2)),use_smoothing=False,stroke_width=1,color=BLUE)
        #
        # r2_right=ax.plot(lambda t:np.abs(1/(t+4)),use_smoothing=False,stroke_width=1,color=BLUE,x_range=[-4.01,10])
        # r2_left=ax.plot(lambda t:np.abs(1/(t+4)),use_smoothing=False,stroke_width=1,color=BLUE,x_range=[-10,-4.01])
        # sum=ax.plot(lambda t:np.abs ( 1/(t+5))+np.abs ( 1/(t+2)),use_smoothing=False,stroke_width=2,color=YELLOW)
        # self.add(ax,r1,r2_right,r2_left,sum)

        [r1,dot]=TheSiGuy_lib.two_d_graph_from_csv(ax,'csv_files/first_rational.csv',stroke_width=1,color=RED)
        [r2,dot]=TheSiGuy_lib.two_d_graph_from_csv(ax,'csv_files/second_rational.csv',stroke_width=1,color=RED)
        [sum,dot]=TheSiGuy_lib.two_d_graph_from_csv(ax,'csv_files/sumof2rationals.csv',stroke_width=2)
        # self.add(ax,r1,r2,sum)

        self.play(GrowFromCenter(ax),run_time=0.3)
        self.wait(0.1)
        self.play(FadeIn(r1),run_time=0.5)
        self.wait(0.1)
        self.play(FadeIn(r2),run_time=0.5)
        self.wait(0.2)
        self.play(Create(sum))
        self.wait()







from imports import *




class Equations2(Scene):
    def construct(self):

        lti_diff_eq=MathTex(r'\frac{\mathrm{d^2  \hspace{0.5 mm} x } }{\mathrm{d} \hspace{0.2 mm} t^2} +3\frac{\mathrm{d  \hspace{0.5 mm} x } }{\mathrm{d} \hspace{0.2 mm} t} +2x=e^{-t}  \hspace{10 mm}').scale(1).shift(3*UP)
        diff_property=MathTex(r'\frac{\mathrm{d  x } }{\mathrm{d} t} \hspace{3 mm} \leftrightarrow \hspace{3 mm} sX(s)-X(0^{-})').shift(0.5*UP)
        int_property=MathTex(r'\int_{0^{-}}^{t} x(\tau )d\tau \hspace{3 mm} \leftrightarrow  \hspace{3 mm} \frac{X(s)}{s}').shift(2*DOWN)
        initial_cond=MathTex(r'x\left(0^{+}\right)=2 , \quad \frac{d x}{d t}\left(0^{+}\right)=0',color=BLUE).scale(0.5).next_to(lti_diff_eq,RIGHT,buff=LARGE_BUFF)
        algebric_equ=MathTex(r's^{2} X(s)-s x\left(0^{+}\right)-\frac{d x}{d t}\left(0^{+}\right)+3 s X(s)-3 x\left(0^{+}\right)+2 X(s)=\frac{1}{s+1}').scale(0.7).shift(0.5*UP)
        solution_to_algebric_eq=MathTex(r'X(s)=\frac{2 s^{2}+8 s+7}{s^3+4s^2+5s+2}').shift(2*DOWN)
        solution_to_algebric_eq_factored=MathTex(r'X(s)=\frac{2 s^{2}+8 s+7}{(s+1)^{2}(s+2)}').shift(3*UP)
        setofpoles=MathTex(r'X(s)=\frac{-1}{s+2}+\frac{3}{s+1}+\frac{1}{(s+1)^{2}}').shift(0.5*UP)
        time_response=MathTex(r'x(t)=-e^{-2 t}+3 e^{-t}+t e^{-t}').shift((2*DOWN))
        transfer_func=MathTex(r'X(s)=\frac{(s+3)}{(s+1)(s+5)}')

        self.play(Write(transfer_func))
        self.wait(0.2)

        rect=SurroundingRectangle(transfer_func,buff=MED_LARGE_BUFF)
        self.play(Create(rect))
        self.wait()

        # self.add(solution_to_algebric_eq_factored)
        # self.wait()
        # self.play(ReplacementTransform(solution_to_algebric_eq_factored.copy(),setofpoles))
        # self.wait()
        # self.play(ReplacementTransform(setofpoles.copy(),time_response))
        # self.wait()

        # self.add(lti_diff_eq)
        # self.wait(0.5)
        # self.play(Write(initial_cond))
        # self.wait()
        # self.play(ReplacementTransform(lti_diff_eq.copy(),algebric_equ))
        # self.wait()
        # self.play(ReplacementTransform(algebric_equ.copy(),solution_to_algebric_eq))
        # self.wait()
        # self.play(ReplacementTransform(solution_to_algebric_eq,solution_to_algebric_eq_factored))
        # self.wait()
        # self.add(lti_diff_eq,diff_property,int_property)
        # t= MarkupText("hello world hello")
        # self.add(t)


        # self.play(Write(lti_diff_eq))
        # self.wait()
        # self.play(Write(diff_property))
        # self.wait()
        # self.play(Write(int_property))
        # self.wait()
        # self.play(FadeOut(diff_property,int_property))


class Try(ThreeDScene):
    def construct(self):
        # self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.7)  # 3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7) #xz plane
        # ax=ThreeDAxes(x_range=[-5,5,1],y_range=[0,10,1],z_range=[-1,2,1])
        # [x,y,z]=TheSiGuy_lib.csv_to_xyz('csv_files/phase_res_of_rect.csv')
        # [g,dot]=ax.plot_line_graph(x,y,z)
        # [graph,dot]=TheSiGuy_lib.two_d_graph_from_csv(ax,'csv_files/phase_res_of_rect.csv')
        # polygon=Polygon([0,0,0],[0,1,0],[1,1,0],[1,0,0],fill_opacity=1,stroke_opacity=0)
        axes=ThreeDAxes(x_range=[-5,5],y_range=[0,10],z_range=[-1,1],z_length=6)
        axes2=ThreeDAxes(x_range=[-5,5],y_range=[0,10],z_range=[0,1],z_length=3)
        self.add(axes)
        self.wait()
        self.play(Transform(axes,axes2))
        self.wait()

class TransferFunction(Scene):
    def construct(self):
        ax=Axes(x_range=[-20,20,5],y_range=[0,0.7,0.2],y_length=4)
        ax2=Axes(x_range=[-20,20,5],y_range=[-1.5,1.5,0.5],y_length=4)
        mag_res=ax.plot(lambda t:abs((1j*t+3)/((1j*t+1)*(1j*t+5))),color=YELLOW)
        phase_res=ax2.plot(lambda t:angle((1j*t+3)/((1j*t+1)*(1j*t+5))),color=YELLOW)
        # self.add(ax2,phase_res)

        # self.wait(2.5)
        # self.play(Create(ax))
        # self.play(Create(mag_res,run_time=10))
        # self.wait()

        self.wait(2.5)
        self.play(Create(ax2))
        self.play(Create(phase_res, run_time=10))
        self.wait()


class Equations4(Scene):
    def construct(self):
        exponential=MathTex(r'e^{(\sigma + j\omega)t }').scale(3)
        exponential_rect=SurroundingRectangle(exponential,buff=MED_SMALL_BUFF,stroke_width=1)
        lti_diff_eq=MathTex(r'a_{n} \cdot \frac{d^{n} y(t)}{d t^{n}}+a_{n-1} \cdot \frac{d^{n-1}}{d t^{n-1}} y(t)+\cdots \cdot a_{0} y(t)=b_{m} \cdot \frac{d^{m}}{d t^{m}} x(t)+b_{m-1} \cdot \frac{d^{m-1}}{d t^{m-1}} x(t)+\cdots+b_{0} x(t)').scale(0.5).shift(2*DOWN)
        lti_diff_eq_rect=SurroundingRectangle(lti_diff_eq,buff=MED_SMALL_BUFF,stroke_width=1)
        lti_sys=MarkupText('LTI Systems')
        lti_sys_rect=SurroundingRectangle(lti_sys,buff=MED_SMALL_BUFF,color=YELLOW,stroke_width=2)

        la_of_exp=MathTex(r'e^{-pt} \hspace{2 mm} \leftrightarrow \hspace{2 mm} \frac{A}{s+p}')
        la_of_exp_rect=SurroundingRectangle(la_of_exp,buff=MED_SMALL_BUFF,stroke_width=1,color=BLUE)

        s=MathTex(r's=\sigma +j\omega ').scale(2)
        sigma=MathTex(r'\sigma').scale(30)
        jw=MathTex(r'j\omega').scale(15)


        stab_cond=MathTex(r'\lim _{t \rightarrow \infty} \sum_{i=1}^{n} C_{i} e^{p_{i} t}=0')
        stab_cond_rect=SurroundingRectangle(lti_sys,buff=MED_LARGE_BUFF,color=YELLOW,stroke_width=2)

        self.add(sigma)

        # self.play(Write(stab_cond))
        # self.play(Create(stab_cond_rect))
        # self.wait(5)

        # self.play(Write(la_of_exp))
        # self.play(Create(la_of_exp_rect))
        # self.wait(3)

        # diff_opr=MathTex(r'\frac{\mathrm{d} }{\mathrm{d} x}').scale(0.7)
        # int_opr=MathTex(r'\int ').scale(0.7).shift(2*DOWN)
        # diff_opr_rect=SurroundingRectangle(diff_opr,stroke_width=2,buff=MED_SMALL_BUFF,color=RED)
        # int_opr_rect=SurroundingRectangle(int_opr,stroke_width=2,buff=MED_SMALL_BUFF,color=RED)

        # f=MathTex(r'e^{ct}').shift(3*LEFT)
        # ff=MathTex(r'e^{ct}').shift(2*DOWN+3*LEFT)
        # df=MathTex(r'c\hspace{0.5 mm}e^{ct}').shift(3*RIGHT)
        # intf=MathTex(r'\frac{1}{c}\hspace{0.5 mm}e^{ct}').shift(2*DOWN+3*RIGHT)

        # first_arr_1=Arrow(f.get_right(),diff_opr_rect.get_left(),stroke_width=1,tip_length=0.2,color=BLUE)
        # first_arr_2=Arrow(ff.get_right(),int_opr_rect.get_left(),stroke_width=1,tip_length=0.2,color=BLUE)
        # second_arr_1=Arrow(diff_opr_rect.get_right(),df.get_left(),stroke_width=1,tip_length=0.2,color=BLUE)
        # second_arr_2=Arrow(int_opr_rect.get_right(),intf.get_left(),stroke_width=1,tip_length=0.2,color=BLUE)
        #
        # self.play(Write(diff_opr),Write(int_opr))
        # self.play(Create(diff_opr_rect),Create(int_opr_rect))
        # self.play(Write(f), Write(ff))
        # self.play(GrowArrow(first_arr_1),GrowArrow( first_arr_2))
        # self.play(GrowArrow(second_arr_1),GrowArrow(second_arr_2))
        # self.play(Write(df), Write(intf))
        # self.wait()
        #
        #
        #
        # self.add(diff_opr,int_opr,diff_opr_rect,int_opr_rect,first_arr_1,first_arr_2,second_arr_1,second_arr_2,f,ff,df,intf)

        # self.play(Write(lti_sys))
        # self.play(Create(lti_sys_rect))
        # self.wait()
        # self.add(lti_sys,lti_sys_rect)
        # self.wait()
        # self.play(ReplacementTransform(lti_sys.copy(),lti_diff_eq))
        # self.play(Create(lti_diff_eq_rect))
        # self.wait()
        # self.add(exponential)
        # self.wait(0.5)
        # self.play(Create(exponential_rect))
        # self.wait()
        # self.add(lti_diff_eq,lti_diff_eq_rect)
        # self.play(Write(exponential))
        # self.wait()

        # self.play(Write(exponential))
        # self.play(Create(exponential_rect))
        # self.wait()


class Equations5(Scene):
    def construct(self):

        nth_order_diff_eq=MathTex(r'y^{\prime \prime}+p(x) y^{\prime}+q(x) y=0').shift(3*UP)
        nth_order_diff_eq_sol=MathTex(r'y=c_{1} y_{1}+c_{2} y_{2}').shift(1.5*UP)

        nth_order_diff_eq_rect=SurroundingRectangle(nth_order_diff_eq,stroke_width=1,buff=MED_SMALL_BUFF)
        nth_order_diff_eq_sol_rect=SurroundingRectangle(nth_order_diff_eq_sol,stroke_width=1,buff=MED_SMALL_BUFF)

        text1=Text('Where y1 and y2 are linearly independent solutions',color=BLUE,font="Open Sans").scale(0.6)
        linear_independent_set1=MathTex(r'sin(t) \hspace{2 mm} \leftrightarrow  \hspace{2 mm} cos(t)')
        linear_independent_set2=MathTex(r'e^{3t} \hspace{3 mm} \leftrightarrow \hspace{3 mm} e^{5t}').shift(DOWN)
        not_linear_independent_set=MathTex(r'x \hspace{3 mm} \leftrightarrow \hspace{3 mm}  5x').shift(2*DOWN)
        cross1=Cross(not_linear_independent_set,stroke_width=2)

        laplace_transform_eq=MathTex(r'X(s) = \int_{-\infty }^{\infty }x(t) \hspace{0.5 mm} e^{-st} \hspace{0.4 mm} dt').shift(2*UP)
        laplace_transform_eq_rect=SurroundingRectangle(laplace_transform_eq,stroke_width=1,buff=MED_SMALL_BUFF)

        fourier_transform_eq = MathTex(r'X(\omega ) = \int_{-\infty }^{\infty }x(t) \hspace{0.5 mm} e^{-j\omega t} \hspace{0.4 mm} dt').shift(DOWN)
        fourier_transform_eq_rect=SurroundingRectangle(fourier_transform_eq,stroke_width=1,buff=MED_SMALL_BUFF)

        linear_comp_of_exp=MathTex(r'y_{h}(t)=\sum_{i=1}^{n} C_{i} e^{\lambda_{i} t}').shift(2.5*UP)
        linear_comp_of_exp_rect=SurroundingRectangle(linear_comp_of_exp,stroke_width=1,buff=MED_SMALL_BUFF)

        linear_comp_of_rationals=MathTex(r'y_{h}(t)=\sum_{i=1}^{n} \frac{C_{i}}{s+\lambda_{i}}').shift(0.5*DOWN)
        linear_comp_of_rationals_rect=SurroundingRectangle(linear_comp_of_rationals,stroke_width=1,buff=MED_SMALL_BUFF)

        self.play(Write(linear_comp_of_exp))
        self.play(Create(linear_comp_of_exp_rect))
        self.wait(0.5)
        self.play(ReplacementTransform(linear_comp_of_exp.copy(),linear_comp_of_rationals))
        self.play(Create(linear_comp_of_rationals_rect))
        self.wait(0.5)


        # self.add(linear_comp_of_exp,linear_comp_of_exp_rect,linear_comp_of_rationals,linear_comp_of_rationals_rect)




        # self.add(nth_order_diff_eq,nth_order_diff_eq_rect,nth_order_diff_eq_sol,nth_order_diff_eq_sol_rect,text1)

        # self.play(Write(nth_order_diff_eq))
        # self.play(Create(nth_order_diff_eq_rect))
        # self.wait(0.5)
        # self.play(Write(nth_order_diff_eq_sol))
        # self.play(Create(nth_order_diff_eq_sol_rect))
        # self.wait(0.5)
        # self.play(Write(text1))
        # self.wait()


        # self.play(Write(linear_independent_set1))
        # self.wait()
        # self.play(Write(linear_independent_set2))
        # self.wait()
        # self.play(Write(not_linear_independent_set ))
        # self.wait(0.5)
        # self.play(Create(cross1))
        # self.wait()

        # self.play(Write(laplace_transform_eq),Write(fourier_transform_eq))
        # self.play(Create(laplace_transform_eq_rect),Create(fourier_transform_eq_rect))
        # self.wait()




class PosSurf(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.7)  # 3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7) #xz plane
        # self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.5) #xy plane
        axes = ThreeDAxes(x_range=[-2, 3, 0.5], y_range=[-20, 20, 5], z_range=[0, 4, 1],x_length=15,y_length=14).shift([0,0,-3])
        # xlbl=axes.get_x_axis_label('x').scale(3)
        # ylbl=axes.get_y_axis_label('y').scale(3)
        # zlbl=axes.get_z_axis_label('z').scale(3)

        components_pos = []
        components_neg = []
        envelops=[]

        for sigma in np.arange(0,2.1,0.1):
            component=axes.plot_parametric_curve(lambda omega: np.array([sigma,omega,np.abs((np.exp(sigma+1j*omega)-np.exp(-1*(sigma+1j*omega)))/(sigma+1j*omega))]),stroke_width=2,color=YELLOW,t_range=[-20,20,0.01])
            # freq_response=axes.plot_parametric_curve(lambda t:np.array([t,0,np.sinc(t)]),stroke_width=4,color=RED,t_range=[-5,f,0.01])
            components_pos.append(component)
            # envelops.append(freq_response)

        # surface = []
        # for ind in range(len(components_pos) - 1):
        #     pts1 = components_pos[ind].points
        #     pts2 = components_pos[ind + 1].points
        #     pts2rev = pts2[::-1]
        #     polygon = Polygon(*pts1, *pts2rev, fill_opacity=0.2, stroke_opacity=0, fill_color=[BLUE, GREEN])
        #     surface.append(polygon)
        x=ValueTracker(-10)
        radius=ValueTracker(100)
        dot = always_redraw(lambda :Dot3D(axes.input_to_graph_point(x=x.get_value(), graph=components_pos[-1]),color=RED))
        dot2 = always_redraw(lambda :Dot(axes.c2p(*[axes.p2c(dot.get_center())[0],axes.p2c(dot.get_center())[1],0]),color=BLUE).scale(1))
        vertical_line=always_redraw(lambda : DashedLine(dot.get_center(),dot2.get_center(),stroke_width=1))

        lines=always_redraw(lambda :axes.get_lines_to_point(dot2.get_center(),color=BLUE))
        self.play(GrowFromCenter(dot, run_time=0.5))
        self.add(axes,*components_pos,dot2,lines,vertical_line)
        self.wait()

        self.wait()
        self.play(x.animate.set_value(10),run_time=2)
        self.wait(3)

        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.5,added_anims=[FadeOut(*components_pos,dot,vertical_line)])
        self.wait()


class NegSurf(ThreeDScene):
    def construct(self):

        # self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.5)  # 3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7) #xz plane
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.5) #xy plane



