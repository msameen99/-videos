import numpy as np

from imports import *
class PropagatingWave(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=50 * DEGREES, focal_distance=1000, zoom=0.5)  #3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7) #xz plane
        axes=ThreeDAxes(x_range=[0,42,10],y_range=[0,42,10],z_range=[-1.5,1.5,1])
        axes2 = ThreeDAxes(x_range=[-1.5, 1.5, 1], y_range=[0, 42, 10], z_range=[-1.5, 1.5, 1], x_length=10, z_length=10)
        # axes.y_axis.rotate(90*DEGREES,[0,1,0])
        # axes.z_axis.rotate(90*DEGREES,[0,0,1])

        axes.x_axis.rotate(90 * DEGREES, [1, 0, 0])
        w=1
        beta=0.5
        time=ValueTracker(10)

        x_label=axes.get_x_axis_label('time')
        y_label=axes.get_y_axis_label('distance')
        z_label=axes.get_z_axis_label('amplitude')


        propagating_wave_curves=[]
        for t in np.arange(0,41,0.6):
            propagating_wave_curve=axes.plot_parametric_curve(lambda l: np.array([t,l,np.cos(t-beta*l)]),stroke_width=2,color=YELLOW,t_range=[0,40,0.1])
            propagating_wave_equation=MathTex(r'')
            propagating_wave_curves.append(propagating_wave_curve)






        # self.add(axes,x_label,y_label,z_label,propagating_wave_curves[40],propagating_wave_curves[20],propagating_wave_curves[30],propagating_wave_curves[10])
        self.play(Create(axes,run_time=0.5))
        self.play(Create(propagating_wave_curves[0]))
        self.wait(0.5)
        self.add(propagating_wave_curves[0],axes)
        for i,curve in enumerate(propagating_wave_curves):
            # self.play(Transform(propagating_wave_curves[0],i))
            # self.remove(propagating_wave_curves[i-1])
            propagating_wave_curves[i-1].set_stroke([BLUE,GREEN],0.8)
            self.add(propagating_wave_curves[i])
            self.wait(0.3)
        self.wait()

        # propagating_wave_graph=always_redraw(lambda : axes2.plot_parametric_curve(lambda l: [np.real(np.exp(1j*(w*time.get_value()-beta*l))),l,np.imag(np.exp(1j*(w*time.get_value()-beta*l)))],color=YELLOW,stroke_width=1,t_range=[0,40,0.01]))
        # reverse_propagating_wave_graph=always_redraw(lambda : axes2.plot_parametric_curve(lambda l: [np.real(np.exp(1j*(w*time.get_value()+beta*l))),l,np.imag(np.exp(1j*(w*time.get_value()+beta*l)))],color=RED,stroke_width=1,t_range=[0,40,0.01]))
        # self.add(axes2,propagating_wave_graph)
        # self.wait()
        # self.play(time.animate.set_value(30),run_time=3)
        # self.wait()
        #
        # self.add(axes2,reverse_propagating_wave_graph,propagating_wave_graph)
        # self.wait()
        # self.play(time.animate.set_value(30),run_time=3)
        # self.wait()
        #
        # surface=Surface(lambda u,v: np.array([u,v,np.cos(w*u-beta*v)]),u_range=[0,42],v_range=[0,42])
        # self.add(surface)

        # propagating_curve2=always_redraw(lambda : axes.plot_parametric_curve(lambda t: [t,t,np.cos(w*time.get_value()-0.5*t)],t_range=[0,40],color=RED,stroke_width=1.5))
        # self.add(axes,propagating_curve2)
        # self.wait()
        # self.play(time.animate.set_value(30),run_time=3)
        # self.wait()






class PropagatingWave2(ThreeDScene):
    def construct(self):
        # self.set_camera_orientation(phi=70 * DEGREES, theta=50 * DEGREES, focal_distance=1000, zoom=0.5)  #3d view
        self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7) #xz plane
        axes=ThreeDAxes(x_range=[0,42,10],y_range=[0,42,10],z_range=[-1.5,1.5,1])
        axes2 = ThreeDAxes(x_range=[-1.5, 1.5, 1], y_range=[0, 42, 10], z_range=[-1.5, 1.5, 1], x_length=10, z_length=10)
        axes.y_axis.rotate(90*DEGREES,[0,1,0])
        axes.z_axis.rotate(90*DEGREES,[0,0,1])

        axes.x_axis.rotate(90 * DEGREES, [1, 0, 0])
        w=1
        beta=0.5
        time=ValueTracker(10)

        x_label=axes.get_x_axis_label('time')
        y_label=axes.get_y_axis_label('distance')
        z_label=axes.get_z_axis_label('amplitude')


        propagating_wave_curves=[]
        for t in np.arange(0,41,0.6):
            propagating_wave_curve=axes.plot_parametric_curve(lambda l: np.array([t,l,np.cos(t-beta*l)]),stroke_width=2,color=YELLOW,t_range=[0,40,0.1])
            propagating_wave_equation=MathTex(r'')
            propagating_wave_curves.append(propagating_wave_curve)






        # self.add(axes,x_label,y_label,z_label,propagating_wave_curves[40],propagating_wave_curves[20],propagating_wave_curves[30],propagating_wave_curves[10])


        #_______________
        self.play(Create(axes,run_time=0.5))
        self.play(Create(propagating_wave_curves[0]))
        self.wait(0.5)
        self.add(propagating_wave_curves[0],axes)
        for i,curve in enumerate(propagating_wave_curves):
            # self.play(Transform(propagating_wave_curves[0],i))
            # self.remove(propagating_wave_curves[i-1])
            propagating_wave_curves[i-1].set_stroke([BLUE,GREEN],0.8)
            self.add(propagating_wave_curves[i])
            self.wait(0.3)
        self.wait()
        #__________________________________
        # self.add(axes)







        # propagating_wave_graph=always_redraw(lambda : axes2.plot_parametric_curve(lambda l: [np.real(np.exp(1j*(w*time.get_value()-beta*l))),l,np.imag(np.exp(1j*(w*time.get_value()-beta*l)))],color=YELLOW,stroke_width=1,t_range=[0,40,0.01]))
        # reverse_propagating_wave_graph=always_redraw(lambda : axes2.plot_parametric_curve(lambda l: [np.real(np.exp(1j*(w*time.get_value()+beta*l))),l,np.imag(np.exp(1j*(w*time.get_value()+beta*l)))],color=RED,stroke_width=1,t_range=[0,40,0.01]))
        # self.add(axes2,propagating_wave_graph)
        # self.wait()
        # self.play(time.animate.set_value(30),run_time=3)
        # self.wait()
        #
        # self.add(axes2,reverse_propagating_wave_graph,propagating_wave_graph)
        # self.wait()
        # self.play(time.animate.set_value(30),run_time=3)
        # self.wait()
        #
        # surface=Surface(lambda u,v: np.array([u,v,np.cos(w*u-beta*v)]),u_range=[0,42],v_range=[0,42])
        # self.add(surface)

        # propagating_curve2=always_redraw(lambda : axes.plot_parametric_curve(lambda t: [t,t,np.cos(w*time.get_value()-0.5*t)],t_range=[0,40],color=RED,stroke_width=1.5))
        # self.add(axes,propagating_curve2)
        # self.wait()
        # self.play(time.animate.set_value(30),run_time=3)
        # self.wait()








class PropagatingWave3(ThreeDScene):
    def construct(self):
        # self.set_camera_orientation(phi=70 * DEGREES, theta=50 * DEGREES, focal_distance=1000, zoom=0.5)  #3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7) #xz plane
        axes=ThreeDAxes(x_range=[0,42,10],y_range=[0,42,10],z_range=[-1.5,1.5,1])
        axes2 = ThreeDAxes(x_range=[-1.5, 1.5, 1], y_range=[0, 42, 10], z_range=[-1.5, 1.5, 1], x_length=10, z_length=10)
        axes.y_axis.rotate(90*DEGREES,[0,1,0])
        # axes.z_axis.rotate(90*DEGREES,[0,0,1])

        axes.x_axis.rotate(90 * DEGREES, [1, 0, 0])
        w=1
        beta=0.5
        time=ValueTracker(10)

        x_label=axes.get_x_axis_label('time')
        y_label=axes.get_y_axis_label('distance')
        z_label=axes.get_z_axis_label('amplitude')


        propagating_wave_curves=[]
        for t in np.arange(0,41,0.6):
            propagating_wave_curve=axes.plot_parametric_curve(lambda l: np.array([t,l,np.cos(t-beta*l)]),stroke_width=2,color=YELLOW,t_range=[0,40,0.1])
            propagating_wave_equation=MathTex(r'')
            propagating_wave_curves.append(propagating_wave_curve)






        # self.add(axes,x_label,y_label,z_label,propagating_wave_curves[40],propagating_wave_curves[20],propagating_wave_curves[30],propagating_wave_curves[10])


        #_______________
        self.play(Create(axes,run_time=0.5))
        self.play(Create(propagating_wave_curves[0]))
        self.wait(0.5)
        self.add(propagating_wave_curves[0],axes)
        for i,curve in enumerate(propagating_wave_curves):
            # self.play(Transform(propagating_wave_curves[0],i))
            # self.remove(propagating_wave_curves[i-1])
            propagating_wave_curves[i-1].set_stroke([BLUE,GREEN],0.8)
            self.add(propagating_wave_curves[i])
            self.wait(0.3)
        self.wait()
        #__________________________________
        # self.add(axes)







        # propagating_wave_graph=always_redraw(lambda : axes2.plot_parametric_curve(lambda l: [np.real(np.exp(1j*(w*time.get_value()-beta*l))),l,np.imag(np.exp(1j*(w*time.get_value()-beta*l)))],color=YELLOW,stroke_width=1,t_range=[0,40,0.01]))
        # reverse_propagating_wave_graph=always_redraw(lambda : axes2.plot_parametric_curve(lambda l: [np.real(np.exp(1j*(w*time.get_value()+beta*l))),l,np.imag(np.exp(1j*(w*time.get_value()+beta*l)))],color=RED,stroke_width=1,t_range=[0,40,0.01]))
        # self.add(axes2,propagating_wave_graph)
        # self.wait()
        # self.play(time.animate.set_value(30),run_time=3)
        # self.wait()
        #
        # self.add(axes2,reverse_propagating_wave_graph,propagating_wave_graph)
        # self.wait()
        # self.play(time.animate.set_value(30),run_time=3)
        # self.wait()
        #
        # surface=Surface(lambda u,v: np.array([u,v,np.cos(w*u-beta*v)]),u_range=[0,42],v_range=[0,42])
        # self.add(surface)

        # propagating_curve2=always_redraw(lambda : axes.plot_parametric_curve(lambda t: [t,t,np.cos(w*time.get_value()-0.5*t)],t_range=[0,40],color=RED,stroke_width=1.5))
        # self.add(axes,propagating_curve2)
        # self.wait()
        # self.play(time.animate.set_value(30),run_time=3)
        # self.wait()


















class PropagatingWaveDistanceChange(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=50 * DEGREES, focal_distance=1000, zoom=0.5)  #3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7) #xz plane
        axes=ThreeDAxes(x_range=[0,42,10],y_range=[0,42,10],z_range=[-1.5,1.5,1])
        axes2 = ThreeDAxes(x_range=[-1.5, 1.5, 1], y_range=[0, 42, 10], z_range=[-1.5, 1.5, 1], x_length=10, z_length=10)
        # axes.y_axis.rotate(90*DEGREES,[0,1,0])
        # axes.z_axis.rotate(90*DEGREES,[0,0,1])
        axes.x_axis.rotate(90*DEGREES,[1,0,0])

        axes.x_axis.rotate(90 * DEGREES, [1, 0, 0])
        w=1
        beta=0.5
        time=ValueTracker(10)

        x_label=axes.get_x_axis_label('time')
        y_label=axes.get_y_axis_label('distance')
        z_label=axes.get_z_axis_label('amplitude')


        propagating_wave_curves=[]
        dots=[]
        for l in np.arange(0,41,2):
            propagating_wave_curve=axes.plot_parametric_curve(lambda t: np.array([t,l,np.cos(t-beta*l)]),stroke_width=2,color=YELLOW,t_range=[0,40,0.1])
            dot=Dot3D(propagating_wave_curve.get_end())
            propagating_wave_equation=MathTex(r'')
            propagating_wave_curves.append(propagating_wave_curve)
            dots.append(dot)






        # self.add(axes,x_label,y_label,z_label,propagating_wave_curves[40],propagating_wave_curves[20],propagating_wave_curves[30],propagating_wave_curves[10])

        self.play(Create(axes,run_time=0.5))
        self.play(Create(propagating_wave_curves[0]))
        # self.add(dots[0])
        self.wait(0.5)
        self.add(propagating_wave_curves[0],axes)
        for i,curve in enumerate(propagating_wave_curves):
            # self.play(Transform(propagating_wave_curves[0],i))
            # self.remove(propagating_wave_curves[i-1])
            propagating_wave_curves[i-1].set_stroke([BLUE,GREEN],0.8)
            self.add(propagating_wave_curves[i])
            self.wait(0.7)
        self.wait()
        # move_alog_time=[MoveAlongPath(i,j.reverse_points(),run_time=20, rate_func=rate_functions.linear) for i,j in zip(dots,propagating_wave_curves)]
        # self.play(*move_alog_time)
        # self.wait()

        # self.add(axes)

        # propagating_wave_graph=always_redraw(lambda : axes2.plot_parametric_curve(lambda l: [np.real(np.exp(1j*(w*time.get_value()-beta*l))),l,np.imag(np.exp(1j*(w*time.get_value()-beta*l)))],color=YELLOW,stroke_width=1,t_range=[0,40,0.01]))
        # reverse_propagating_wave_graph=always_redraw(lambda : axes2.plot_parametric_curve(lambda l: [np.real(np.exp(1j*(w*time.get_value()+beta*l))),l,np.imag(np.exp(1j*(w*time.get_value()+beta*l)))],color=RED,stroke_width=1,t_range=[0,40,0.01]))
        # self.add(axes2,propagating_wave_graph)
        # self.wait()
        # self.play(time.animate.set_value(30),run_time=3)
        # self.wait()
        #
        # self.add(axes2,reverse_propagating_wave_graph,propagating_wave_graph)
        # self.wait()
        # self.play(time.animate.set_value(30),run_time=3)
        # self.wait()
        #
        # surface=Surface(lambda u,v: np.array([u,v,np.cos(w*u-beta*v)]),u_range=[0,42],v_range=[0,42])
        # self.add(surface)

        # propagating_curve2=always_redraw(lambda : axes.plot_parametric_curve(lambda t: [t,t,np.cos(w*time.get_value()-0.5*t)],t_range=[0,40],color=RED,stroke_width=1.5))
        # self.add(axes,propagating_curve2)
        # self.wait()
        # self.play(time.animate.set_value(30),run_time=3)
        # self.wait()


class PropagatingWaveDistanceChange2(ThreeDScene):
    def construct(self):
        # self.set_camera_orientation(phi=70 * DEGREES, theta=50 * DEGREES, focal_distance=1000, zoom=0.5)  #3d view
        self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7) #xz plane
        axes=ThreeDAxes(x_range=[0,42,10],y_range=[0,42,10],z_range=[-1.5,1.5,1])
        axes2 = ThreeDAxes(x_range=[-1.5, 1.5, 1], y_range=[0, 42, 10], z_range=[-1.5, 1.5, 1], x_length=10, z_length=10)
        axes.y_axis.rotate(90*DEGREES,[0,1,0])
        axes.z_axis.rotate(90*DEGREES,[0,0,1])

        axes.x_axis.rotate(90 * DEGREES, [1, 0, 0])
        w=1
        beta=0.5
        time=ValueTracker(10)

        x_label=axes.get_x_axis_label('time')
        y_label=axes.get_y_axis_label('distance')
        z_label=axes.get_z_axis_label('amplitude')


        propagating_wave_curves=[]
        dots=[]
        for l in np.arange(0,41,2):
            propagating_wave_curve=axes.plot_parametric_curve(lambda t: np.array([t,l,np.cos(t-beta*l)]),stroke_width=2,color=YELLOW,t_range=[0,40,0.1])
            dot=Dot3D(propagating_wave_curve.get_end())
            propagating_wave_equation=MathTex(r'')
            propagating_wave_curves.append(propagating_wave_curve)
            dots.append(dot)






        # self.add(axes,x_label,y_label,z_label,propagating_wave_curves[40],propagating_wave_curves[20],propagating_wave_curves[30],propagating_wave_curves[10])

        self.play(Create(axes,run_time=0.5))
        self.play(Create(propagating_wave_curves[0]))
        # self.add(dots[0])
        self.wait(0.5)
        self.add(propagating_wave_curves[0],axes)
        for i,curve in enumerate(propagating_wave_curves):
            # self.play(Transform(propagating_wave_curves[0],i))
            # self.remove(propagating_wave_curves[i-1])
            propagating_wave_curves[i-1].set_stroke([BLUE,GREEN],0.8)
            self.add(propagating_wave_curves[i])
            self.wait(0.7)
        self.wait()
        # move_alog_time=[MoveAlongPath(i,j.reverse_points(),run_time=20, rate_func=rate_functions.linear) for i,j in zip(dots,propagating_wave_curves)]
        # self.play(*move_alog_time)
        # self.wait()


        # self.add(axes)

        # propagating_wave_graph=always_redraw(lambda : axes2.plot_parametric_curve(lambda l: [np.real(np.exp(1j*(w*time.get_value()-beta*l))),l,np.imag(np.exp(1j*(w*time.get_value()-beta*l)))],color=YELLOW,stroke_width=1,t_range=[0,40,0.01]))
        # reverse_propagating_wave_graph=always_redraw(lambda : axes2.plot_parametric_curve(lambda l: [np.real(np.exp(1j*(w*time.get_value()+beta*l))),l,np.imag(np.exp(1j*(w*time.get_value()+beta*l)))],color=RED,stroke_width=1,t_range=[0,40,0.01]))
        # self.add(axes2,propagating_wave_graph)
        # self.wait()
        # self.play(time.animate.set_value(30),run_time=3)
        # self.wait()
        #
        # self.add(axes2,reverse_propagating_wave_graph,propagating_wave_graph)
        # self.wait()
        # self.play(time.animate.set_value(30),run_time=3)
        # self.wait()
        #
        # surface=Surface(lambda u,v: np.array([u,v,np.cos(w*u-beta*v)]),u_range=[0,42],v_range=[0,42])
        # self.add(surface)

        # propagating_curve2=always_redraw(lambda : axes.plot_parametric_curve(lambda t: [t,t,np.cos(w*time.get_value()-0.5*t)],t_range=[0,40],color=RED,stroke_width=1.5))
        # self.add(axes,propagating_curve2)
        # self.wait()
        # self.play(time.animate.set_value(30),run_time=3)
        # self.wait()

class PropagatingWaveDistanceChange3(ThreeDScene):
    def construct(self):
        # self.set_camera_orientation(phi=70 * DEGREES, theta=50 * DEGREES, focal_distance=1000, zoom=0.5)  #3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7) #xz plane
        axes=ThreeDAxes(x_range=[0,42,10],y_range=[0,42,10],z_range=[-1.5,1.5,1])
        axes2 = ThreeDAxes(x_range=[-1.5, 1.5, 1], y_range=[0, 42, 10], z_range=[-1.5, 1.5, 1], x_length=10, z_length=10)
        # axes.y_axis.rotate(90*DEGREES,[0,1,0])
        # axes.z_axis.rotate(90*DEGREES,[0,0,1])

        axes.x_axis.rotate(90 * DEGREES, [1, 0, 0])
        w=1
        beta=0.5
        time=ValueTracker(10)

        x_label=axes.get_x_axis_label('time')
        y_label=axes.get_y_axis_label('distance')
        z_label=axes.get_z_axis_label('amplitude')


        propagating_wave_curves=[]
        dots=[]
        for l in np.arange(0,41,2):
            propagating_wave_curve=axes.plot_parametric_curve(lambda t: np.array([t,l,np.cos(t-beta*l)]),stroke_width=2,color=YELLOW,t_range=[0,40,0.1])
            dot=Dot3D(propagating_wave_curve.get_end())
            propagating_wave_equation=MathTex(r'')
            propagating_wave_curves.append(propagating_wave_curve)
            dots.append(dot)






        # self.add(axes,x_label,y_label,z_label,propagating_wave_curves[40],propagating_wave_curves[20],propagating_wave_curves[30],propagating_wave_curves[10])


        self.play(Create(axes,run_time=0.5))
        self.play(Create(propagating_wave_curves[0]))
        # self.add(dots[0])
        self.wait(0.5)
        self.add(propagating_wave_curves[0],axes)
        for i,curve in enumerate(propagating_wave_curves):
            # self.play(Transform(propagating_wave_curves[0],i))
            # self.remove(propagating_wave_curves[i-1])
            propagating_wave_curves[i-1].set_stroke([BLUE,GREEN],0.8)
            self.add(propagating_wave_curves[i])
            self.wait(0.7)
        self.wait()
        # move_alog_time=[MoveAlongPath(i,j.reverse_points(),run_time=20, rate_func=rate_functions.linear) for i,j in zip(dots,propagating_wave_curves)]
        # self.play(*move_alog_time)
        # self.wait()

        # self.add(axes)

        # propagating_wave_graph=always_redraw(lambda : axes2.plot_parametric_curve(lambda l: [np.real(np.exp(1j*(w*time.get_value()-beta*l))),l,np.imag(np.exp(1j*(w*time.get_value()-beta*l)))],color=YELLOW,stroke_width=1,t_range=[0,40,0.01]))
        # reverse_propagating_wave_graph=always_redraw(lambda : axes2.plot_parametric_curve(lambda l: [np.real(np.exp(1j*(w*time.get_value()+beta*l))),l,np.imag(np.exp(1j*(w*time.get_value()+beta*l)))],color=RED,stroke_width=1,t_range=[0,40,0.01]))
        # self.add(axes2,propagating_wave_graph)
        # self.wait()
        # self.play(time.animate.set_value(30),run_time=3)
        # self.wait()
        #
        # self.add(axes2,reverse_propagating_wave_graph,propagating_wave_graph)
        # self.wait()
        # self.play(time.animate.set_value(30),run_time=3)
        # self.wait()
        #
        # surface=Surface(lambda u,v: np.array([u,v,np.cos(w*u-beta*v)]),u_range=[0,42],v_range=[0,42])
        # self.add(surface)

        # propagating_curve2=always_redraw(lambda : axes.plot_parametric_curve(lambda t: [t,t,np.cos(w*time.get_value()-0.5*t)],t_range=[0,40],color=RED,stroke_width=1.5))
        # self.add(axes,propagating_curve2)
        # self.wait()
        # self.play(time.animate.set_value(30),run_time=3)
        # self.wait()





class ElectromagneticWave2(Scene):
    def construct(self):
        # self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=1)

        l=ValueTracker(0)
        beta=ValueTracker(1.5)
        k = ValueTracker(2 * np.pi) # spatial propagation constant
        lamda=4000
        w = 4  # angular frequency
        Exm = 2 # electric field amplitude
        Hym = 3 # magnetic field amplitude
        x = np.arange(0,3,0.01) # space representative point

        d1x=ValueTracker(-5)
        d2x=ValueTracker(5)

        borders_of_sin1=ValueTracker(-5)
        borders_of_sin2=ValueTracker(5)

        ax=Axes()
        # xy_plene=TheSiGuy_lib.xy_plane(axis=axes)
        Ey=always_redraw(lambda : ax.plot_parametric_curve(lambda t: np.array([t,Exm*np.cos(l.get_value() -beta.get_value()*t),0]),t_range=[borders_of_sin1.get_value(),borders_of_sin2.get_value()],color=BLUE,stroke_width=2))
        # Hz=always_redraw(lambda : ax.plot_parametric_curve(lambda t: np.array([0,t,Hym*np.cos(l.get_value() -beta*t)]),t_range=[-5,5],color=RED,stroke_width=2))

        dot1=always_redraw(lambda :Dot(ax.i2gp(d1x.get_value(),Ey),color=GREEN))
        line1=always_redraw(lambda :DashedLine(ax.c2p(d1x.get_value(),2,0),dot1.get_center(),stroke_width=1))
        label1= always_redraw(lambda : MathTex(r'%0.1f' %ax.p2c(dot1.get_center())[1],color=RED).scale(0.8).next_to(dot1,LEFT))


        dot2 = always_redraw(lambda: Dot(ax.i2gp(d2x.get_value(), Ey),color=GREEN))
        line2 = always_redraw(lambda: DashedLine(ax.c2p(d2x.get_value(), 2, 0), dot2.get_center(), stroke_width=1))
        label2 = always_redraw(lambda : MathTex(r'%0.1f' %ax.p2c(dot2.get_center())[1],color=RED).scale(0.8).next_to(dot2,RIGHT))




        self.play(Create(ax))
        self.play(FadeIn(Ey))
        self.play(FadeIn(label2,label1,dot2,dot1),Create(line2),Create(line1))
        self.wait(0.2)
        self.play(l.animate(rate_func=rate_functions.linear,run_time=5).set_value(20))
        self.wait(2)

        #___________________________ animating changing the circuit element's dimension_________________________________

        # self.play(d1x.animate().set_value(-0.1),d2x.animate().set_value(0.1))
        # self.wait()
        # self.play(borders_of_sin1.animate().set_value(-0.1), borders_of_sin2.animate().set_value(0.1))
        # self.wait()


        #____________________________________________________ animating changing the signal freq __________________________

        # self.play(beta.animate.set_value(0.2),run_time=4)
        # self.wait()

        #______________________________________________________________________________________________________________


class Equations(Scene):
    def construct(self):

        propagating_wave_curves_forumulas = []
        rects=[]
        for t in np.arange(0, 41, 0.6):
            propagating_wave_curve_formula_original = MathTex(
                r'{{E_{x}(t,z)}} = {{ E_{x}^{+} \hspace{0.01 mm} \cos (\omega t -\beta z)}}')
            propagating_wave_curve_formula = MathTex(
                r'{{E_{x}(t,z)}} =  E_{x}^{+} \hspace{0.01 mm} \cos (\omega \hspace{0.5 mm} (%0.1f) -\beta z)' % t)
            rect=SurroundingRectangle(propagating_wave_curve_formula,buff=MED_SMALL_BUFF,stroke_width=1.3)
            # propagating_wave_curve_formula[2].set_color(RED)
            propagating_wave_curves_forumulas.append(propagating_wave_curve_formula)
            rects.append(rect)

        # self.add(propagating_wave_curves_forumulas[0],rects[0])
        # for i, formula in enumerate(propagating_wave_curves_forumulas):
        #     # self.play(Transform(propagating_wave_curves[0],i))
        #     # self.remove(propagating_wave_curves[i-1])
        #     # propagating_wave_curves[i - 1].set_stroke([BLUE, GREEN], 0.8)
        #     self.remove(propagating_wave_curves_forumulas[i-1],rects[i-1])
        #     self.add(propagating_wave_curves_forumulas[i],rects[i])
        #     self.wait(0.3)
        # self.wait()

        self.play(Create(rects[0],run_time=0.5))
        self.play(Write(propagating_wave_curves_forumulas[0],run_time=1))
        self.wait(0.5)


class SinPulse(Scene):
    def construct(self):

        x_limit=ValueTracker(7)
        y_limit=ValueTracker(4)
        freq=ValueTracker(2)
        phase=ValueTracker(0)
        ax=always_redraw(lambda :Axes(x_length=14,y_length=8,x_range=[-1*x_limit.get_value(),x_limit.get_value()],y_range=[-1*y_limit.get_value(),y_limit.get_value()]).set_opacity(0))
        sin=always_redraw(lambda :ax.plot(lambda t:0.5*np.sin(freq.get_value()*t + phase.get_value() ),color=RED,stroke_width=2,x_range=[-1*3.14/freq.get_value(),3.14/freq.get_value()]))


        # self.add(sin)
        self.add(ax)
        # self.play(Create(sin))
        self.add(sin)
        self.wait()
        # self.play(x_limit.animate.set_value(1.57))

        # self.play(freq.animate(run_time=3).set_value(2))
        # self.wait()
        # self.play(freq.animate(run_time=3).set_value(0.1))
        # self.wait()
        self.play(phase.animate.set_value(130),run_time=30,rate_func=rate_functions.linear)
        self.wait()

class Equations(Scene):
    def construct(self):
        eq1=MathTex(r'T  \hspace{3 mm}  > >  \hspace{3 mm}  t_{r}')
        eq2=MathTex(r'\frac{1}{f}  \hspace{3 mm}  > >  \hspace{3 mm}  \frac{l}{v}').shift(1.6*DOWN)
        eq3=MathTex(r'\frac{v}{f}  \hspace{3 mm}  > >  \hspace{3 mm}  l').shift(1.6*DOWN)
        wavelength=MathTex(r'\lambda ').move_to(eq2[0][1])
        v=MathTex(r'v').move_to(eq2[0][0])
        group=VGroup(eq2,eq1)
        rect=SurroundingRectangle(group,GREEN,stroke_width=1.7,buff=MED_SMALL_BUFF)


        self.play(Write(eq1))
        self.wait()
        self.play(ReplacementTransform(eq1[0][3:5].copy(), eq2[0][5:8]))
        self.wait(0.5)
        self.play(ReplacementTransform(eq1[0][0].copy(), eq2[0][0:3]))
        self.add(eq2)
        self.wait()
        self.play(ReplacementTransform(eq2[0][7],v),FadeOut(eq2[0][0]),FadeOut(eq2[0][6]),eq2[0][5].animate.move_to(eq2[0][6]))
        self.remove(eq2[0])
        # self.add(eq3)
        self.wait()
        self.play(ReplacementTransform(eq2[0][0:4],wavelength),FadeOut(v,run_time=0.4))
        self.wait()
        self.play(Create(rect))
        self.wait()
        # self.play(FadeIn(eq3),FadeOut(eq2))
        # self.wait()


class Equations2(Scene):
    def construct(self):

        # wavelengh=MathTex(r'\lambda  \hspace{3 mm} <<  \hspace{3 mm} d')
        # rect=SurroundingRectangle(wavelengh,buff=MED_SMALL_BUFF,stroke_width=1.7)

        num_of_sections=MathTex(r'\frac{5585 \hspace{2 mm} km}{1 \hspace{2 mm} cm} \hspace{1 mm} = \hspace{1 mm} 558500000')
        rect = SurroundingRectangle(num_of_sections, buff=MED_SMALL_BUFF, stroke_width=1,color=BLUE)

        self.play(Write(num_of_sections))
        self.play(Create(rect))
        self.wait()


class Equations3(Scene):
    def construct(self):
        self.camera.background_color = "#101010"
        eq3=MathTex(r'Z_{i n}=\frac{j \omega L}{2} \pm \sqrt{-\frac{(\omega L)^{2}}{4}+\frac{L}{C}}')
        loverc=MathTex(r'\sqrt{\frac{L}{C}}').move_to(eq3[0][5:9])
        cross1=Cross(eq3[0][13:20],stroke_width=1.5)
        cross2=Cross(eq3[0][5:9],stroke_width=1.5)
        # self.play(Write(eq3))
        # self.wait()

        # self.add(eq3[0][21:25])
        # self.add(eq3[0][13:20])
        # self.add(eq3[0][5:9])
        self.add(eq3)
        self.wait()
        self.play(Create(cross1),Create(cross2))
        self.wait()
        # self.play(FadeOut(cross1,cross2))
        self.play(ReplacementTransform(eq3[0][4:],loverc),ReplacementTransform(cross1,loverc),ReplacementTransform(cross2,loverc))
        self.wait()
        self.play(Create())

class Equations3(Scene):
    def construct(self):

        loverc=MathTex(r'\sqrt{\frac{L}{C}}')
        self.play(Write(loverc))
        self.wait()


class Equations4(Scene):
    def construct(self):
        # wave_eq1=MathTex(r'\frac{d^{2} v(t,l)}{d l^{2}}=\gamma^{2} V(t,l)')
        # wave_eq2=MathTex(r'\frac{d^{2} I(t,l)}{d l^{2}}=\gamma^{2} I(t,l)').shift(1.6*DOWN)
        # gamma=MathTex(r'\gamma^{2}=(R+j \omega L)(G +j \omega C)')
        # group=Group(wave_eq1,wave_eq2)
        # rect=SurroundingRectangle(group,stroke_width=1,buff=MED_SMALL_BUFF)
        # self.play(Write(wave_eq1))
        # self.play(Write(wave_eq2))
        # self.play(Create(rect))
        # self.wait()

        # self.add(wave_eq1,wave_eq2)
        # self.play(Create(gamma))
        # self.wait()

        voltage=MathTex(r'v(l, t)=v^{+} \hspace{0.5 mm} e^{-\alpha l}  e^{j (\omega t-\beta l)}+v^{-} \hspace{0.5 mm} e^{\alpha l}  e^{j (\omega t+\beta l)}')
        current=MathTex(r'I(l, t)=I^{+} \hspace{0.5 mm} e^{-\alpha l}  e^{j (\omega t-\beta l)}+I^{-} \hspace{0.5 mm} e^{\alpha l}  e^{j (\omega t+\beta l)}')
        gamma=MathTex(r'\gamma = \alpha +j \beta ')
        vcross=Cross(voltage[0][22:],stroke_width=1)
        icross=Cross(current[0][22:],stroke_width=1)
        vreal=MathTex(r'v(l,t)=v^{+} \cos (\omega t-\beta l)')
        ireal=MathTex(r'I(l,t)=I^{+} \cos (\omega t-\beta l)')

        currentfromvoltage=MathTex(r'I(x, t)=\frac{v(l, t)}{Z_{o}}')

        # self.play(Write(current))
        # self.wait()
        # self.play(Write(gamma))
        # self.wait()

        # self.add(voltage)
        # self.wait()
        # self.play(Create(vcross))
        # self.wait(0.2)
        # self.play(FadeOut(vcross,voltage[0][22:]))
        # self.play(voltage[0][0:22].animate.shift(1.6*RIGHT))
        # self.wait()
        #
        # vlosscross = Cross(voltage[0][9:13], stroke_width=1)
        # ilosscross = Cross(current[0][9:13], stroke_width=1)
        #
        # self.play(Create(vlosscross))
        # self.wait()
        # self.play(ReplacementTransform(voltage[0][0:22], vreal), ReplacementTransform(vlosscross, vreal))
        # self.wait()

        # self.add(current)
        # self.wait()
        # self.play(Create(icross))
        # self.wait(0.2)
        # self.play(FadeOut(icross, current[0][22:]))
        # self.play(current[0][0:22].animate.shift(1.6 * RIGHT))
        # self.wait()
        #
        # vlosscross = Cross(voltage[0][9:13], stroke_width=1)
        # ilosscross = Cross(current[0][9:13], stroke_width=1)
        #
        # self.play(Create(ilosscross))
        # self.wait()
        # self.play(ReplacementTransform(current[0][0:22],ireal),ReplacementTransform(ilosscross,ireal))
        # self.wait()

        # self.add(current[0][9:13])


        self.play(Write(currentfromvoltage))
        self.wait()


class VoltageCurrentDistributionAlongTheLine(Scene):
    def construct(self):
        self.camera.background_color = "#101010"

        vreal = MathTex(r'v(l,t)=v^{+} \cos (\omega t-\beta l)',color=BLUE).shift(2.8*UP)
        ireal = MathTex(r'I(l,t)=I^{+} \cos (\omega t-\beta l)',color=RED).shift(1.8*UP)

        omega=5
        t=[0,1,2,3,4,5,6,7,8,9]
        ax=Axes()
        rectangle=Rectangle(width=12,height=4,stroke_width=1,fill_color=BLACK,fill_opacity=1).shift(1.2*DOWN)

        voltages=[]
        currents=[]

        self.add(vreal,ireal)

        for i in t:
            voltage_wave=ax.plot(function=lambda l:np.cos(omega*i-l),stroke_width=1,color=BLUE).shift(0.2*DOWN)
            current_wave=ax.plot(function=lambda l:np.cos(omega*i-l)/3,stroke_width=1,color=RED).shift(0.2*DOWN)
            voltages.append(voltage_wave)
            currents.append(current_wave)

        self.add(rectangle)
        self.add(voltages[0], currents[0])
        self.play(ReplacementTransform(vreal.copy(),voltages[0]))
        self.play(ReplacementTransform(ireal.copy(),currents[0]))


        for v,i in zip(voltages,currents):

            self.add(v,i)
            self.wait()
            self.remove(v, i)


class Equations5(Scene):
    def construct(self):
        self.camera.background_color = "#101010"

        vreal = MathTex(r'v(l,t)=v^{+} \cos (\omega t-\beta l)')

        eqs=[]
        for t in np.arange(0, 41, 0.6):

            vreal = MathTex(r'v(l,%0.1f)=v^{+} \cos (\omega *(%0.1f)-\beta l)'%(t,t))
            eqs.append(vreal)


        for i,curve in enumerate(eqs):
            # self.play(Transform(propagating_wave_curves[0],i))
            # self.remove(propagating_wave_curves[i-1])
            self.add(eqs[i])
            self.wait(0.3)
            self.remove(eqs[i])
        self.add(eqs[-1])





class Equations7(Scene):
    def construct(self):
        self.camera.background_color = "#101010"

        vreal = MathTex(r'v(l,t)=v^{+} \cos (\omega t-\beta l)')
        beta=MathTex(r'\beta=\frac{2\pi}{\lambda}').shift(1.4*DOWN)
        self.add(vreal)
        self.wait()
        self.play(ReplacementTransform(vreal[0][16].copy(),beta))
        self.wait()

        # eqs = []
        # for l in np.arange(0, 41, 2):
        #     # vreal = MathTex(r'v(l,%0.1f)=v^{+} \cos (\omega *(%0.1f)-\beta l)' % (t, t))
        #     vreal = MathTex(r'v(%0.1f,t)=v^{+} \cos (\omega t-\beta *(%0.1f))' % (l, l))
        #     eqs.append(vreal)
        #
        # for i,curve in enumerate(eqs):
        #     # self.play(Transform(propagating_wave_curves[0],i))
        #     # self.remove(propagating_wave_curves[i-1])
        #     self.add(eqs[i])
        #     self.wait(0.7)
        #     self.remove(eqs[i])
        # self.add(eqs[-1])

        # self.wait()






class Equations6(Scene):
    def construct(self):
        text=Text(r'Transmission Lines: An Introduction')
        self.play(Write(text))
        self.wait()
