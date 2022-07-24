import numpy as np

from imports import *
# from pylab import *
import itertools as it

class WaveCompressExpand(Scene):
    def construct(self):
        x=ValueTracker(0)
        y=ValueTracker(0)
        circle_position=ValueTracker(0)
        dot=always_redraw(lambda : Dot(point=[x.get_value(),y.get_value(),0]))

        # radii=[]
        # circles=Group()


        # for i,p in enumerate( np.arange(0,4,0.5) ):
        #
        #     r=ValueTracker(0)
        #     radii.append(r)
        #
        #
        # for i,p in enumerate( np.arange(0,4,0.5) ):
        #
        #     c=always_redraw(lambda : Circle(radius=radii[i].get_value()).shift(p*RIGHT))
        #     circles.add(c)
        #
        #
        # anims=[r.animate(run_time=2).set_value(20) for r in radii]
        # g=Group(*circles)

        # self.add(*circles)
        # self.play(AnimationGroup(*anims,group=g,lag_ratio=0.3))



        r1=ValueTracker(1)
        c1=always_redraw(lambda : Circle(radius=r1.get_value()).shift(0.1*RIGHT))

        r2 = ValueTracker(2)
        c2 = always_redraw(lambda: Circle(radius=r2.get_value()).shift(0.2 * RIGHT))

        r3 = ValueTracker(3)
        c3 = always_redraw(lambda: Circle(radius=r3.get_value()).shift(0.3 * RIGHT))

        r4 = ValueTracker(4)
        c4 = always_redraw(lambda: Circle(radius=r4.get_value()).shift(0.4 * RIGHT))

        anims=(r1.animate(run_time=2).set_value(30),r2.animate(run_time=2).set_value(30),r3.animate(run_time=2).set_value(30),r4.animate(run_time=2).set_value(30))
        g = Group(c1,c2,c3,c4)
        self.add(g)
        self.play(AnimationGroup(*anims, group=g, lag_ratio=0.3))


        self.wait()


class PureSine(Scene):
    def construct(self):
        ax=Axes()
        sin=ax.plot(lambda t:2*np.sin(1.5*t),color=YELLOW)
        # self.play(Create(sin),run_time=2)
        # self.wait()
        puresin_freq=MathTex(r'f_{\mathrm{c}}')
        puresin_freq_rect=SurroundingRectangle(puresin_freq,color=RED,stroke_width=1.5,buff=MED_SMALL_BUFF)

        shifted_freq=MathTex(r'\left(1-\frac{v \cos (\phi)}{c_{0}}\right) f_{\mathrm{c}}')
        shifted_freq_rect=SurroundingRectangle(shifted_freq,color=RED,stroke_width=1.5,buff=MED_SMALL_BUFF)

        # self.play(Write(shifted_freq),Create(shifted_freq_rect))
        # self.wait()

        self.play(Write(puresin_freq), Create(puresin_freq_rect))
        self.wait(2)
        self.play(ReplacementTransform(puresin_freq,shifted_freq),ReplacementTransform(puresin_freq_rect,shifted_freq_rect),run_time=2)
        self.wait()



class FTCurves(ThreeDScene):
    def construct(self):

        # self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.7)  # 3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7) #xz plane
        axes = ThreeDAxes(x_range=[-5.25, 5.25, 1], y_range=[0, 10, 2], z_range=[-1, 1, 0.5], x_length=15,
                          y_length=14, z_length=4)


        # axes.y_axis.rotate(90*DEGREES,[0,1,0])
        # axes.z_axis.rotate(90*DEGREES,[0,0,1])

        axes.x_axis.rotate(90*DEGREES,[1,0,0])

        [x, y, z] = TheSiGuy_lib.csv_to_xyz('csv_files/phase_res_of_rect.csv')
        components = []
        mag_responses = []
        pha_responses = []

        for f in np.round(np.arange(-5, 5, 0.1), 2):
            index = x.index(f)
            component = axes.plot_parametric_curve(
                lambda t: np.array([f, t, np.abs(np.sinc(f)) * np.cos(2 * np.pi * f * t + np.angle(np.sinc(f)))]),
                stroke_width=2, color=PURPLE_A, t_range=[0, 10, 0.01]).set_stroke(YELLOW, 2)
            mag_spectrum = axes.plot_parametric_curve(lambda t: np.array([t, 0, np.abs(np.sinc(t))]),
                                                      stroke_width=4,
                                                      color=RED, t_range=[-5, f, 0.01])
            # pha_spectrum=axes.plot_parametric_curve(lambda t:np.array([t,10,np.angle(np.sinc(t))*(1/10)]),stroke_width=4,color=PURPLE_A,t_range=[-5,f,0.01])
            [pha_spectrum, g] = axes.plot_line_graph(x_values=x[0:index + 1], y_values=y[0:index + 1],
                                                     z_values=z[0:index + 1]).set_stroke(GOLD, 4)
            components.append(component)
            mag_responses.append(mag_spectrum)
            pha_responses.append(pha_spectrum)

        mag_response = axes.plot_parametric_curve(lambda t: np.array([t, 0, np.sinc(t)]), t_range=[-5, 5],
                                                  stroke_width=2, color=YELLOW)

        self.add(components[0], axes)
        for i, curve in enumerate(components):
            # self.play(Transform(propagating_wave_curves[0],i))
            # self.remove(propagating_wave_curves[i-1])
            components[i - 1].set_stroke([BLUE, GREEN], 0.8)
            self.add(components[i])
            self.remove(mag_responses[i - 1])
            self.add(mag_responses[i])
            self.wait(0.1)
        self.wait()


        # self.add(axes)


        # self.add(axes)
        # self.add(mag_response)
        # self.wait()


class FTCurves3(ThreeDScene):
    def construct(self):

        # self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.7)  # 3d view
        self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7) #xz plane
        axes = ThreeDAxes(x_range=[-5.25, 5.25, 1], y_range=[0, 10, 2], z_range=[-1, 1, 0.5], x_length=15,
                          y_length=14, z_length=4)




        [x, y, z] = TheSiGuy_lib.csv_to_xyz('csv_files/rect.csv')
        components = []
        mag_responses = []
        pha_responses = []

        for f in np.round(np.arange(-5, 5, 0.1), 2):
            index = x.index(f)
            component = axes.plot_parametric_curve(
                lambda t: np.array([f, t, np.abs(np.sinc(f)) * np.cos(2 * np.pi * f * t + np.angle(np.sinc(f)))]),
                stroke_width=2, color=PURPLE_A, t_range=[0, 10, 0.01]).set_stroke(YELLOW, 2)
            mag_spectrum = axes.plot_parametric_curve(lambda t: np.array([t, 0, np.abs(np.sinc(t))]),
                                                      stroke_width=4,
                                                      color=RED, t_range=[-5, f, 0.01])
            # pha_spectrum=axes.plot_parametric_curve(lambda t:np.array([t,10,np.angle(np.sinc(t))*(1/10)]),stroke_width=4,color=PURPLE_A,t_range=[-5,f,0.01])
            [pha_spectrum, g] = axes.plot_line_graph(x_values=x[0:index + 1], y_values=y[0:index + 1],
                                                     z_values=z[0:index + 1]).set_stroke(GOLD, 4)
            components.append(component)
            mag_responses.append(mag_spectrum)
            pha_responses.append(pha_spectrum)

        mag_response = axes.plot_parametric_curve(lambda t: np.array([t, 0, np.sinc(t)]), t_range=[-5, 5],
                                                  stroke_width=2, color=YELLOW)

        self.add(components[0], axes)
        for i, curve in enumerate(components):
            # self.play(Transform(propagating_wave_curves[0],i))
            # self.remove(propagating_wave_curves[i-1])
            components[i - 1].set_stroke([BLUE, GREEN], 0.8)
            self.add(components[i])
            self.remove(mag_responses[i - 1])
            self.add(mag_responses[i])
            self.wait(0.1)
        self.wait()


        # self.add(axes)


        # self.add(axes)
        # self.add(mag_response)
        # self.wait()





class FTCurves2(ThreeDScene):
    def construct(self):

        # self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.7)  # 3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7) #xz plane
        axes = ThreeDAxes(x_range=[-5.25, 5.25, 1], y_range=[0, 10, 2], z_range=[-1, 1, 0.5], x_length=15, y_length=14,z_length=4)
        [x, y, z] = TheSiGuy_lib.csv_to_xyz('csv_files/phase_res_of_rect.csv')

        # axes.y_axis.rotate(90 * DEGREES, [0, 1, 0])
        # axes.z_axis.rotate(90 * DEGREES, [0, 0, 1])

        axes.x_axis.rotate(90*DEGREES,[1,0,0])


        components = []
        mag_responses = []
        pha_responses = []

        mag_responses2 = []
        pha_responses2= []

        for f in np.round(np.arange(-5, 5, 0.1),2):
            index=x.index(f)
            component = axes.plot_parametric_curve(
                lambda t: np.array([f, t, np.abs(np.sinc(f)) * np.cos(2 * np.pi * f * t + np.angle(np.sinc(f)))]),
                stroke_width=2, color=PURPLE_A, t_range=[0, 10, 0.01]).set_stroke([BLUE, GREEN], 0.8)
            mag_spectrum = axes.plot_parametric_curve(lambda t: np.array([t, 0, np.abs(np.sinc(t))]), stroke_width=4,
                                                      color=RED, t_range=[-5, f, 0.01])
            # pha_spectrum=axes.plot_parametric_curve(lambda t:np.array([t,10,np.angle(np.sinc(t))*(1/10)]),stroke_width=4,color=PURPLE_A,t_range=[-5,f,0.01])
            [pha_spectrum, g] = axes.plot_line_graph(x_values=x[0:index+1], y_values=y[0:index+1], z_values=z[0:index+1]).set_stroke(GOLD , 4)
            components.append(component)
            mag_responses.append(mag_spectrum)
            pha_responses.append(pha_spectrum)

        components2=[]
        for f in np.round(np.arange(-5, 5, 0.1),2):
            index=x.index(f)
            component = axes.plot_parametric_curve(
                lambda t: np.array([f, t, np.abs(np.sinc(0.7*f)) * np.cos(2 * np.pi * 0.7*f * t + np.angle(np.sinc(0.7*f)))]),
                stroke_width=2, color=PURPLE_A, t_range=[0, 10, 0.01]).set_stroke([BLUE, GREEN], 0.8)
            mag_spectrum = axes.plot_parametric_curve(lambda t: np.array([t, 0, np.abs(np.sinc(0.7*t))]), stroke_width=4,
                                                      color=RED, t_range=[-5, f, 0.01])
            # pha_spectrum=axes.plot_parametric_curve(lambda t:np.array([t,10,np.angle(np.sinc(t))*(1/10)]),stroke_width=4,color=PURPLE_A,t_range=[-5,f,0.01])
            [pha_spectrum, g] = axes.plot_line_graph(x_values=x[0:index+1], y_values=y[0:index+1], z_values=z[0:index+1]).set_stroke(GOLD , 4)
            components2.append(component)
            mag_responses2.append(mag_spectrum)
            pha_responses2.append(pha_spectrum)

        mag_response=axes.plot_parametric_curve(lambda t:np.array([t,0,np.abs(np.sinc(t))]),t_range=[-5,5],stroke_width=4,color=RED)
        mag_response2=axes.plot_parametric_curve(lambda t:np.array([t,0,np.abs(np.sinc(0.7*t))]),t_range=[-5,5],stroke_width=4,color=RED)

        transforms=[ReplacementTransform(a,b) for a,b in zip(components,components2)]

        # self.add(components[0], axes)
        # for i, curve in enumerate(components):
        #     # self.play(Transform(propagating_wave_curves[0],i))
        #     # self.remove(propagating_wave_curves[i-1])
        #     components[i - 1].set_stroke([BLUE, GREEN], 0.8)
        #     self.add(components[i])
        #     self.remove(mag_responses[i-1])
        #     # self.remove(pha_responses[i-1])
        #     self.add(mag_responses[i])
        #     # self.add(pha_responses[i])
        #     self.wait(0.2)
        # self.wait()

        self.add(axes,*components,mag_response)
        self.wait()
        self.play(ReplacementTransform(mag_response,mag_response2),*transforms,run_time=2)
        self.wait()


        # self.add(axes)
        # self.add(mag_response)
        # self.wait()


class Equations(Scene):
    def construct(self):
        # self.camera.background_color = "#101010"

        fc=MathTex(r'f_{c}')
        self.add(fc)

        # general_function=MathTex(r's(t) \hspace{2 mm} \leftrightarrow \hspace{2 mm} S(f)')
        # received_signal=MathTex(r'R(f)=h S(\alpha f) ,  \quad \text { Where} \quad \alpha=1-\frac{v \cos (\phi)}{c_{0}}').shift(DOWN)
        # received_signal_rect=SurroundingRectangle(received_signal,buff=MED_SMALL_BUFF,stroke_width=1.5,color=BLUE)
        # general_function_rect=SurroundingRectangle(general_function,buff=MED_SMALL_BUFF,stroke_width=1.5,color=BLUE)
        #
        # # bandlimited_frequency_domain=MathTex(r'R(f) \approx h S(f-\frac{v \cos (\phi)}{c_{0}} f_{\mathrm{c}})')
        # # bandlimited_frequency_domain_rect=SurroundingRectangle(bandlimited_frequency_domain,color=BLUE,stroke_width=1.5,buff=MED_SMALL_BUFF)
        #
        # alphaf=MathTex(r'\alpha f=f-\frac{v \cos (\phi)}{c_{0}} f \approx f-\frac{v \cos (\phi)}{c_{0}} f_{\mathrm{c}}')
        # alphaf_rect=SurroundingRectangle(alphaf,buff=MED_SMALL_BUFF,stroke_width=1.5,color=BLUE)

        # title=Text('The Doppler Effect')

        # speed_of_light=MathTex(r'c_{0} \text{   is the speed of light}')

        # eq=MathTex(r'f_{\mathrm{r}}=f_{\mathrm{t}}+\frac{v \cos (\theta )}{c_{0}} f_{\mathrm{t}}')
        # eq2=MathTex(r'f_{\mathrm{r}}= f_{\mathrm{t}}-\frac{v \cos (\theta )}{c_{0}} f_{\mathrm{t}}')
        # eq_rect = SurroundingRectangle(eq, buff=MED_SMALL_BUFF, stroke_width=1.5,color=BLUE)

        # feedback=Text('Your feedback is important ')

        # self.play(Write(general_function))
        # self.play(Create(general_function_rect))
        # self.wait()

        # self.play(Write(received_signal))
        # self.play(Create(received_signal_rect))
        # self.wait()

        # self.play(Write(bandlimited_frequency_domain))
        # self.play(Create(bandlimited_frequency_domain_rect))
        # self.wait()

        # self.play(Write(alphaf))
        # self.play(Create(alphaf_rect))
        # self.wait()

        # self.play(Write(eq))
        # self.play(Create(eq_rect))
        # self.wait(2)
        # self.play(ReplacementTransform(eq,eq2))
        # # self.play(ShowCreationThenFadeOut(SurroundingRectangle(eq[1],stroke_width=1.1,buff=MED_SMALL_BUFF)))
        # self.wait()

        # self.play(Write(feedback))
        # self.wait()
        # self.play(Write(speed_of_light))
        # self.wait()


class GeneralTFunction(Scene):
    def construct(self):
        alpha=ValueTracker(0.8)
        ax1=Axes(x_range=[-10,10,2],y_range=[-1,1,0.5],y_length=3,x_length=12,tips=False)
        ax2=Axes(x_range=[-5,5,1],y_range=[-1,1,0.5],y_length=3,x_length=8,tips=False).shift(2*DOWN+2.5*LEFT)

        [transmit_signal,dot]=TheSiGuy_lib.two_d_graph_from_csv(ax1,csvFile='csv_files/rect_function.csv',stroke_width=2)

        mag_response = always_redraw(lambda :ax2.plot(lambda t: np.abs(np.sinc(alpha.get_value()*t)), x_range=[-5, 5],
                                                  stroke_width=2, color=RED))

        # self.add(ax1,ax2,transmit_signal,mag_response)
        # self.play(Create(ax1),Create(ax2))
        # self.play(Create(transmit_signal),run_time=2)
        # self.play(Create(mag_response),run_time=2)
        # self.wait()
        # self.add(ax1,ax2)

        # self.play(Create(ax2))
        # self.play(Create(mag_response))
        # self.wait()
        # self.play(alpha.animate(run_time=2).set_value(1.5))
        # self.wait(0.1)
        # self.play(alpha.animate(run_time=2).set_value(0.4))
        # self.wait()


        self.play(Create(ax1))
        self.play(Create(transmit_signal),run_time=2)
        self.wait()


class Bandlimited(Scene):
    def construct(self):
        ax=Axes(x_range=[-2,10,6],y_range=[-2,2,1],x_length=12,y_length=4,tips=False)
        # self.add(ax)

        self.play(Create(ax))
        self.wait()
