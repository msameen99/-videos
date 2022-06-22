import numpy as np

from imports import *
# from pylab import *
import itertools as it


class GauessElectricLaw(Scene):
    def construct(self):
        charge_pos=ValueTracker(0)
        x_offset=8
        y_offset=4
        pos_charge=always_redraw(lambda : Dot(color=RED,radius=0.24,point=[charge_pos.get_value(),0,0]))
        neg_charge=always_redraw(lambda : Dot(color=YELLOW,radius=0.24,point=[charge_pos.get_value(),0,0]))

        pos_charge_without_offset = always_redraw(lambda: Dot(color=RED, radius=0.24, point=[0, 0, 0]))
        neg_charge_without_offset = always_redraw(lambda: Dot(color=YELLOW, radius=0.24, point=[0, 0, 0]))

        pos_func = lambda pos: np.array([1*pos[0],1*pos[1],0]-pos_charge.get_center())
        neg_func = lambda pos: np.array([-1*pos[0],-1*pos[1],0]+neg_charge.get_center())
        pos_func_without_offset = lambda pos: np.array([1 * pos[0], 1 * pos[1], 0] )
        neg_func_without_offset = lambda pos: np.array([-1 * pos[0], -1 * pos[1], 0] )
        pos_field=always_redraw(lambda : ArrowVectorField(pos_func,x_range=[pos_charge.get_center()[0]-x_offset,pos_charge.get_center()[0]+x_offset],y_range=[pos_charge.get_center()[1]-y_offset,pos_charge.get_center()[1]+y_offset]))
        neg_field=always_redraw(lambda : ArrowVectorField(neg_func,x_range=[neg_charge.get_center()[0]-x_offset,neg_charge.get_center()[0]+x_offset],y_range=[neg_charge.get_center()[1]-y_offset,neg_charge.get_center()[1]+y_offset]))
        pos_field_without_offset=always_redraw(lambda : ArrowVectorField(pos_func_without_offset))
        neg_field_without_offset=always_redraw(lambda : ArrowVectorField(neg_func_without_offset))

        pos_streamlines=always_redraw(lambda :StreamLines(pos_func))
        neg_streamlines=always_redraw(lambda :StreamLines(neg_func))
        pos_streamlines_without_offset = always_redraw(lambda: StreamLines(pos_func_without_offset))
        neg_streamlines_without_offset = always_redraw(lambda: StreamLines(neg_func_without_offset))

        # rectangle=SurroundingRectangle(pos_field_without_offset)
        # self.add(rectangle)

        # self.add(dot)
        # self.play(pos_streamlines.create())
        # self.wait()
        # self.play(dot.animate.shift(2*RIGHT))
        # self.wait()

        # self.add(pos_streamlines)
        # pos_streamlines.start_animation(warm_up=False, flow_speed=0.5, time_width=0.5)
        # self.wait(1)
        # self.play(pos_streamlines.end_animation())

        #_______________________________________________________________________________

        # self.play(GrowFromCenter(pos_charge_without_offset))
        # self.wait()
        # self.play(FadeIn(pos_field_without_offset))
        # self.wait()
        # self.add(pos_streamlines_without_offset)
        # pos_streamlines_without_offset.start_animation(warm_up=False, flow_speed=2, time_width=1)
        # self.wait(5)
        # self.play(pos_streamlines_without_offset.end_animation())

        #--------------------------------------- animating moving positvie charge_______________________________________
        self.add(pos_charge,pos_field_without_offset)
        self.wait()
        self.play(charge_pos.animate(run_time=5,rate_func=rate_functions.linear).shift(16*RIGHT))
        self.wait()

        #------------------------------------- animating moving negative charge ________________________________________
        # self.add(neg_charge, neg_field_without_offset)
        # self.wait()
        # self.play(neg_charge.animate(run_time=5, rate_func=rate_functions.linear).shift(16 * RIGHT))
        # self.wait()

        # --------------------- animating moving negative charge back and forth ________________________________________
        # self.add(neg_charge, neg_field_without_offset)
        # self.wait(0.5)
        # self.play(charge_pos.animate(run_time=2, rate_func=rate_functions.linear).set_value(5))
        # self.wait(0.1)
        # self.play(charge_pos.animate(run_time=2, rate_func=rate_functions.linear).set_value(-5))
        # self.wait(0.1)
        # self.wait(0.5)



class GauessElectricLaw2(Scene):
    def construct(self):
        charge_pos=ValueTracker(0)
        x_offset=8
        y_offset=4
        pos_charge=always_redraw(lambda : Dot(color=RED,radius=0.24,point=[charge_pos.get_value(),0,0]))
        neg_charge=always_redraw(lambda : Dot(color=YELLOW,radius=0.24,point=[charge_pos.get_value(),0,0]))

        pos_charge_without_offset = always_redraw(lambda: Dot(color=RED, radius=0.24, point=[0, 0, 0]))
        neg_charge_without_offset = always_redraw(lambda: Dot(color=YELLOW, radius=0.24, point=[0, 0, 0]))

        pos_func = lambda pos: np.array([1*pos[0],1*pos[1],0]-pos_charge.get_center())
        neg_func = lambda pos: np.array([-1*pos[0],-1*pos[1],0]+neg_charge.get_center())
        pos_func_without_offset = lambda pos: np.array([1 * pos[0], 1 * pos[1], 0] )
        neg_func_without_offset = lambda pos: np.array([-1 * pos[0], -1 * pos[1], 0] )
        pos_field=always_redraw(lambda : ArrowVectorField(pos_func,x_range=[pos_charge.get_center()[0]-x_offset,pos_charge.get_center()[0]+x_offset],y_range=[pos_charge.get_center()[1]-y_offset,pos_charge.get_center()[1]+y_offset]))
        neg_field=always_redraw(lambda : ArrowVectorField(neg_func,x_range=[neg_charge.get_center()[0]-x_offset,neg_charge.get_center()[0]+x_offset],y_range=[neg_charge.get_center()[1]-y_offset,neg_charge.get_center()[1]+y_offset]))
        pos_field_without_offset=always_redraw(lambda : ArrowVectorField(pos_func_without_offset))
        neg_field_without_offset=always_redraw(lambda : ArrowVectorField(neg_func_without_offset))

        pos_streamlines=always_redraw(lambda :StreamLines(pos_func))
        neg_streamlines=always_redraw(lambda :StreamLines(neg_func))
        pos_streamlines_without_offset = always_redraw(lambda: StreamLines(pos_func_without_offset))
        neg_streamlines_without_offset = always_redraw(lambda: StreamLines(neg_func_without_offset))

        # rectangle=SurroundingRectangle(pos_field_without_offset)
        # self.add(rectangle)

        # self.add(dot)
        # self.play(pos_streamlines.create())
        # self.wait()
        # self.play(dot.animate.shift(2*RIGHT))
        # self.wait()

        self.add(neg_streamlines)
        neg_streamlines.start_animation(warm_up=False, flow_speed=0.5, time_width=0.5)
        self.wait(1)
        self.play(neg_streamlines.end_animation())

        #_______________________________________________________________________________

        # self.play(GrowFromCenter(pos_charge_without_offset))
        # self.wait()
        # self.play(FadeIn(pos_field_without_offset))
        # self.wait()
        # self.add(pos_streamlines_without_offset)
        # pos_streamlines_without_offset.start_animation(warm_up=False, flow_speed=2, time_width=1)
        # self.wait(5)
        # self.play(pos_streamlines_without_offset.end_animation())

        #--------------------------------------- animating moving positvie charge_______________________________________
        # self.add(pos_charge,pos_field_without_offset)
        # self.wait()
        # self.play(pos_charge.animate(run_time=5,rate_func=rate_functions.linear).shift(16*RIGHT))
        # self.wait()

        #------------------------------------- animating moving negative charge ________________________________________
        # self.add(neg_charge, neg_field_without_offset)
        # self.wait()
        # self.play(neg_charge.animate(run_time=5, rate_func=rate_functions.linear).shift(16 * RIGHT))
        # self.wait()

        # --------------------- animating moving negative charge back and forth ________________________________________
        # self.add(neg_charge, neg_field_without_offset)
        # self.wait(0.5)
        # self.play(charge_pos.animate(run_time=2, rate_func=rate_functions.linear).set_value(5))
        # self.wait(0.1)
        # self.play(charge_pos.animate(run_time=2, rate_func=rate_functions.linear).set_value(-5))
        # self.wait(0.1)
        # self.wait(0.5)


class Box(Scene):
    def construct(self):
        box=Rectangle()
        self.add(box)

class Test(ThreeDScene):
    def construct(self):
        # func=lambda pos:np.array([pos[1],-1*pos[0],0])
        func=lambda pos:np.array([pos[1],-pos[0],0])
        field=ArrowVectorField(func,color=BLUE)
        # field=ArrowVectorField(func,x_range=[-20,20],y_range=[-20,20],color=BLUE)
        stream_lines = StreamLines(
            func,

        )
        # mask =Annulus(inner_radius=3.1,outer_radius=10,fill_color=BLACK,stroke_width=0)
        self.add(field)
        # self.move_camera(phi=50 * DEGREES, theta=-60 * DEGREES,focal_distance=1000)
        # self.wait()
        # self.add(stream_lines)
        # self.play(stream_lines.create())

        # self.wait()
        # self.wait()
        # self.add(streamline)
        # self.play(streamline.create())

        self.add(stream_lines)
        stream_lines.start_animation(warm_up=False, flow_speed=0.4)
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)
        # self.wait(3)

class Test2(ThreeDScene):
    def construct(self):
        i = 1  # Amps in the wire
        mu = 1.26 * 10 ** (-6)


        # points = [x * RIGHT + y * UP
        #           for x in np.arange(-5, 5, 1)
        #           for y in np.arange(-5, 5, 1)
        #           ]  # List of vectors pointing to each grid point
        #
        # vec_field = []  # Empty list to use in for loop
        # for point in points:
        #     field = [-1*point[1]/np.sqrt(point[0]**2+point[1]**2)*exp(-(point[0]**2+point[1]**2)),point[0]/sqrt(point[1]**2+point[1]**2)*exp(-1*(point[0]**2+point[1]**2)),0]  # Constant field up and to right
        #     result = Vector(field).shift(point)  # Create vector and shift it to grid point
        #     vec_field.append(result)  # Append to list
        #
        # draw_field = VGroup(*vec_field)  # Pass list of vectors to create a VGroup

        func=lambda p:(np.array([p[1],-1*p[0],0]))*np.exp(-0.1*(p[0]**2+p[1]**2))
        field=ArrowVectorField(func,colors=[YELLOW,ORANGE,GRAY,DARK_GRAY,BLACK],min_color_scheme_value=1,max_color_scheme_value=4,x_range=[-20,20],y_range=[-20,20])
        stream_lines=StreamLines(func)
        self.add_foreground_mobject(field)
        self.move_camera(phi=50 * DEGREES, theta=-60 * DEGREES, focal_distance=1000,run_time=0.5)
        # self.wait()
        self.wait(0.5)
        self.play(ShowPassingFlash(stream_lines,run_time=3))
        self.wait()

class BiotSavart(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=1)
        i = 1  # Amps in the wire
        mu = 1.26 * 10 ** (-6)
        func=lambda p: np.array([(mu/(2*np.pi))*(i/np.sqrt((p[0])**2+(p[1])**2))*(-np.sin(np.arctan2(p[1],p[0]))),(mu/(2*np.pi))*(i/np.sqrt((p[0])**2+(p[1])**2))*(np.cos(np.arctan2(p[1],p[0]))),0])
        field = ArrowVectorField(func,x_range=[-7,7,0.6],y_range=[-4,4,0.6],z_range=[0,3],three_dimensions=True,colors=[RED,ORANGE,GRAY,DARK_GRAY,BLACK])
        self.add(field)

class MagneticMonopole(Scene):
    def construct(self):
        n = 1
        e = 8.85 * 10 ** (-12)


        # func=lambda p:[(3*p[0]*p[1])/(4*np.pi*e/(np.sqrt(p[0]**2+p[1]**2)**5)),n/(4*np.pi*e)*(3*p[1]**2/np.sqrt(p[0]**2+p[1]**2)**5-1/np.sqrt(p[0]**2+p[1]**2)**3),0]
        func=lambda p:np.array([(n/(4*np.pi*e)*(3*p[0]*p[1])/np.sqrt(p[0]**2+p[1]**2)**5)/10000,(n/(4*np.pi*e)*(3*p[1]**2/np.sqrt(p[0]**2+p[1]**2)**5-1/np.sqrt(p[0]**2+p[1]**2)**3))/10000,0])
        func2=lambda p:np.array([(n/(4*np.pi)*(3*p[0]*p[1])/np.sqrt(p[0]**2+p[1]**2)**5),(n/(4*np.pi)*(3*p[1]**2/np.sqrt(p[0]**2+p[1]**2)**5-1/np.sqrt(p[0]**2+p[1]**2)**3)),0])*(p[0]**2+p[1]**2)*10
        plan=NumberPlane()
        # func=VectorField.shift_func(func,np.array([-1,-1,0]))
        field=ArrowVectorField(func,x_range=[-7,7,0.6],y_range=[-4,4,0.6])
        sl=StreamLines(func2,stroke_width=1.5,)
        self.add_foreground_mobject (field)

        self.wait(0.5)
        self.play(sl.create(run_time=1))
        self.wait(0.5)
        # self.play(sl.create())

        self.add(sl)
        sl.start_animation(warm_up=False, flow_speed=1.5)
        self.wait(sl.virtual_time / sl.flow_speed)
        self.wait(14)

class MagneticDipole(Scene):
    def construct(self):
        d=ValueTracker(1.5) #distance from orgin
        func=lambda p: np.array([ (p[0]-d.get_value())/((p[0]-d.get_value())**2+p[1]**2+0.1)-(p[0]+d.get_value())/((p[0]+d.get_value())**2+p[1]**2+0.1),p[1]/((p[0]-d.get_value())**2+p[1]**2+0.1)-p[1]/((p[0]+d.get_value())**2+p[1]**2+0.1),0])*4
        field=always_redraw(lambda: ArrowVectorField(func))
        sl=always_redraw(lambda: StreamLines(func,stroke_width=2))
        self.add_foreground_mobject(field)
        self.wait()
        self.play(sl.create(run_time=1))
        self.add(sl)

        self.wait(0.5)
        self.play(d.animate.set_value(0.01),run_time=5)
        self.wait(0.5)

        sl.start_animation(warm_up=False, flow_speed=1)
        self.wait(sl.virtual_time / sl.flow_speed)
        self.add(field,sl)
        self.wait(12)


class ElectricDipole(Scene):
    def construct(self):
        d = ValueTracker(4)  # distance from orgin
        x0=3
        y0=2
        x1=-5
        y1=-3
        func = lambda p: np.array([(p[0]-x0)/((p[0]-x0)**2+(p[1]-y0)**2)**(3/2) - (p[0]-x1)/((p[0]-x1)**2+(p[1]-y1)**2)**(3/2),(p[1]-y0)/((p[0]-x0)**2+(p[1]-y0)**2)**(3/2)-(p[1]-y1)/((p[0]-x1)**2+(p[1]-y1)**2)**(3/2),0])*(np.sqrt(((p[0]-x1)**2+(p[1]-y1)**2))>0.5)*4
        field =ArrowVectorField(func,x_range=[-7,7,0.7],y_range=[-4,4,0.7])
        field = always_redraw(lambda: ArrowVectorField(func,x_range=[-7,7,0.6],y_range=[-4,4,0.6]))
        sl = always_redraw(lambda: StreamLines(func, stroke_width=2,x_range=[-7,7,0.6],y_range=[-4,4,0.6]))
        self.add_foreground_mobject(field)
        self.add(sl)

        sl.start_animation(warm_up=False, flow_speed=1)
        self.wait(5)

        # self.wait(0.5)
        # self.play(d.animate.set_value(0.1), run_time=3)
        # self.wait(0.5)

class ElectromagneticWave(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=1)

        l=ValueTracker(0)
        beta=2
        k = ValueTracker(2 * np.pi) # spatial propagation constant
        lamda=4000
        w = 4  # angular frequency
        Exm = 2 # electric field amplitude
        Hym = 3 # magnetic field amplitude
        x = np.arange(0,3,0.01) # space representative point

        axes=ThreeDAxes()
        xy_plene=TheSiGuy_lib.xy_plane(axis=axes)
        Ey=always_redraw(lambda : axes.plot_parametric_curve(lambda t: np.array([Exm*np.cos(l.get_value() -beta*t),t,0]),t_range=[-5,5],color=BLUE,stroke_width=2))
        Hz=always_redraw(lambda : axes.plot_parametric_curve(lambda t: np.array([0,t,Hym*np.cos(l.get_value() -beta*t)]),t_range=[-5,5],color=RED,stroke_width=2))
        self.add(axes,xy_plene)
        self.play(Create(Ey,rate_func=rate_functions.linear),Create(Hz,rate_func=rate_functions.linear),run_time=8)
        self.play(l.animate(rate_func=rate_functions.linear,run_time=3).set_value(-5))
        self.wait(0.5)

class Ampere(ThreeDScene):
    def construct(self):
        # self.set_camera_orientation(phi=50 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=1)
        # func=lambda p:np.array([p[1],-1*p[0],0])


        # amper's law in 3d ___________________________________________
        # func = lambda p: np.array([p[1], -1 * p[0], 0])
        # field=ArrowVectorField(func,three_dimensions=True,z_range=[-2,2,0.5],colors=[YELLOW,RED,GRAY,BLACK])
        # sl=StreamLines(func,three_dimensions=True,colors=[YELLOW,RED,GRAY,BLACK ],z_range=[-2,2,0.5])
        # self.add_foreground_mobject(field)
        # self.add(sl)
        #_________________________________________________

        # changing magnetic field in rotation direction___________________________________
        # func1 = lambda p: np.array([p[1], -1 * p[0], 0])
        # func2 = lambda p: np.array([-1 * p[1], p[0], 0])
        # func3 = lambda p: np.array([p[1], -1 * p[0], 0])
        # func4 = lambda p: np.array([-1 * p[1], p[0], 0])
        # field1=ArrowVectorField(func1)
        # field2=ArrowVectorField(func2)
        # field3=ArrowVectorField(func3)
        # field4=ArrowVectorField(func4)
        # self.add(field1)
        # self.wait()
        # self.play(Transform(field1,field2))
        # self.wait(0.1)
        # self.play(Transform(field1, field3))
        # self.wait(0.1)
        # self.play(Transform(field1, field4))
        # self.wait()
        #____________________________________________________


        # 2 wires magnetic field __________________________
        # self.set_camera_orientation(phi=70 * DEGREES, theta=-50 * DEGREES, focal_distance=1000, zoom=1)


        x0=-2
        y0=0
        x1=2
        y1=0
        i = -5  # Amps in the wire
        mu = 1.26 * 10 ** (-6)  # Magnetic constant
        mag_field_func = lambda p: np.array([ ((mu/(2*np.pi))*(i/np.sqrt(((p[0]-x0))**2+((p[1]-y0))**2)) * (-np.sin(np.arctan2((p[1]-y0),(p[0]-x0)))))-((mu/(2*np.pi))*(i/np.sqrt(((p[0]-x1))**2+((p[1]-y1))**2)) * (-np.sin(np.arctan2((p[1]-y1),(p[0]-x1))))) ,((mu/(2*np.pi))*(i/np.sqrt(((p[0]-x0))**2+((p[1]-y0))**2))* (np.cos(np.arctan2((p[1]-y0),(p[0]-x0)))))-((mu/(2*np.pi))*(i/np.sqrt(((p[0]-x1))**2+((p[1]-y1))**2))* (np.cos(np.arctan2((p[1]-y1),(p[0]-x1)))))  , 0])
        mag_field_func2 = lambda p: np.array([ ((mu/(2*np.pi))*(i/np.sqrt(((p[0]-x0))**2+((p[1]-y0))**2)) * (-np.sin(np.arctan2((p[1]-y0),(p[0]-x0)))))+((mu/(2*np.pi))*(i/np.sqrt(((p[0]-x1))**2+((p[1]-y1))**2)) * (-np.sin(np.arctan2((p[1]-y1),(p[0]-x1))))) ,((mu/(2*np.pi))*(i/np.sqrt(((p[0]-x0))**2+((p[1]-y0))**2))* (np.cos(np.arctan2((p[1]-y0),(p[0]-x0)))))+((mu/(2*np.pi))*(i/np.sqrt(((p[0]-x1))**2+((p[1]-y1))**2))* (np.cos(np.arctan2((p[1]-y1),(p[0]-x1)))))  , 0])
        mag_field_sl_func = lambda p: 3000000* np.array([ ((mu/(2*np.pi))*(i/np.sqrt(((p[0]-x0))**2+((p[1]-y0))**2)) * (-np.sin(np.arctan2((p[1]-y0),(p[0]-x0)))))-((mu/(2*np.pi))*(i/np.sqrt(((p[0]-x1))**2+((p[1]-y1))**2)) * (-np.sin(np.arctan2((p[1]-y1),(p[0]-x1))))) ,((mu/(2*np.pi))*(i/np.sqrt(((p[0]-x0))**2+((p[1]-y0))**2))* (np.cos(np.arctan2((p[1]-y0),(p[0]-x0)))))-((mu/(2*np.pi))*(i/np.sqrt(((p[0]-x1))**2+((p[1]-y1))**2))* (np.cos(np.arctan2((p[1]-y1),(p[0]-x1)))))  , 0])*(np.sqrt(((p[0]-x0)**2+(p[1]-y0)**2))>0.15)*(np.sqrt(((p[0]-x1)**2+(p[1]-y1)**2))>0.15)
        mag_field_sl_func2 = lambda p: 3000000* np.array([ ((mu/(2*np.pi))*(i/np.sqrt(((p[0]-x0))**2+((p[1]-y0))**2)) * (-np.sin(np.arctan2((p[1]-y0),(p[0]-x0)))))+((mu/(2*np.pi))*(i/np.sqrt(((p[0]-x1))**2+((p[1]-y1))**2)) * (-np.sin(np.arctan2((p[1]-y1),(p[0]-x1))))) ,((mu/(2*np.pi))*(i/np.sqrt(((p[0]-x0))**2+((p[1]-y0))**2))* (np.cos(np.arctan2((p[1]-y0),(p[0]-x0)))))+((mu/(2*np.pi))*(i/np.sqrt(((p[0]-x1))**2+((p[1]-y1))**2))* (np.cos(np.arctan2((p[1]-y1),(p[0]-x1)))))  , 0])*(np.sqrt(((p[0]-x0)**2+(p[1]-y0)**2))>0.15)*(np.sqrt(((p[0]-x1)**2+(p[1]-y1)**2))>0.15)
        electric_field_func=lambda p: np.array([-p[1],p[0],0])/np.sqrt(p[0]**4+p[1]**4)*6
        electric_field=ArrowVectorField(electric_field_func,x_range=[-12,12.,0.6],y_range=[-8,8,0.6],opacity=0.7).rotate(90*DEGREES,[1,0,0])
        electric_sl=StreamLines(electric_field_func,x_range=[-12,12],y_range=[-12,12],opacity=0.6).rotate(90*DEGREES,[1,0,0])
        mag_field=ArrowVectorField(mag_field_func,x_range=[-12,12,0.6],y_range=[-14,14,0.6])
        mag_field2=ArrowVectorField(mag_field_func2,x_range=[-12,12,0.6],y_range=[-14,14,0.6])
        mag_sl=StreamLines(mag_field_sl_func,x_range=[-12,12],y_range=[-12,12])
        mag_sl2=StreamLines(mag_field_sl_func2,x_range=[-12,12],y_range=[-12,12])
        # self.add_foreground_mobject(mag_field)
        # self.add(mag_sl,electric_sl)
        # self.add_foreground_mobject(electric_field)
        # self.wait()
        # self.move_camera(phi=70 * DEGREES, theta=-50 * DEGREES, focal_distance=1000, zoom=1,run_time=1)
        # self.wait()
        # self.move_camera(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=1,run_time=1)
        # self.wait()
        self.add_foreground_mobject(mag_field2)
        self.add(mag_sl2)



        # sl.start_animation(warm_up=False, flow_speed=1)
        # self.wait(sl.virtual_time / sl.flow_speed)
        # self.wait(0.2)

        #____________________________________________________________



#######################################################################################

class Equations(Scene):
    def construct(self):

        #_____________________________________ Maxwell equations ____________________________
        #_____________________________________ Differantial Form ____________________________
        # maxwell_equations_eq_diff_form=MathTex(r'\begin{aligned} \nabla \cdot E &=\frac{\rho}{\epsilon_{0}} \\ \nabla \cdot B &=0 \\ \nabla \times E &=-\frac{\partial B}{\partial t} \\ \nabla \times H &=J+\frac{\partial D}{\partial t} \end{aligned}',color=BLUE).scale(1.35).shift(3.3*LEFT)
        # maxwell_equations_eq_rect=SurroundingRectangle(maxwell_equations_eq_diff_form,buff=MED_SMALL_BUFF,color=WHITE,stroke_width=2)
        # maxwell_equations_eq_bg=BackgroundRectangle(maxwell_equations_eq_diff_form,color=BLUE,fill_opacity=0.05)
        # # self.add(maxwell_equations_eq_bg,maxwell_equations_eq,maxwell_equations_eq_rect)
        #
        # self.play(Write(maxwell_equations_eq_diff_form),run_time=3)
        # self.play(Create(maxwell_equations_eq_rect),FadeIn(maxwell_equations_eq_bg))
        # self.wait(10)
        #
        # text=MarkupText('Differantial Form',color=RED)
        # self.play(Write(text),run_time=1)
        # self.wait(10)

        #________________________________________Integral Form _______________________________

        # maxwell_equations_eq_int_form = MathTex(r'\begin{aligned} &\oint \mathbf{E} \cdot d \mathbf{A}=\frac{Q}{\varepsilon_{0}} \\ &\oint \mathbf{B} \cdot d \mathbf{A}=0 \\ &\oint \mathbf{E} \cdot d \mathbf{s}=-\frac{d \Phi_{m}}{d t} \\ &\oint \mathbf{B} \cdot d \mathbf{s}=\mu_{0} I+\varepsilon_{0} \mu_{0} \frac{d \Phi_{e}}{d t} \end{aligned}', color=BLUE).scale(1).shift(3.3 *RIGHT)
        # maxwell_equations_eq_rect=SurroundingRectangle(maxwell_equations_eq_int_form,buff=MED_SMALL_BUFF,color=WHITE,stroke_width=2)
        # maxwell_equations_eq_bg=BackgroundRectangle(maxwell_equations_eq_int_form,color=BLUE,fill_opacity=0.05)
        # # self.add(maxwell_equations_eq_bg,maxwell_equations_eq,maxwell_equations_eq_rect)
        #
        # self.play(Write(maxwell_equations_eq_int_form),run_time=3)
        # self.play(Create(maxwell_equations_eq_rect),FadeIn(maxwell_equations_eq_bg))
        # self.wait(10)

        # text = MarkupText('Integral Form', color=RED)
        # self.play(Write(text),run_time=1)
        # self.wait(10)

        #_____________________________________________ Gauess electric field_______________

        # diff_form = MarkupText("differential form").shift(2 * UP)
        # int_form = MarkupText("Integral form").shift(2 * UP)
        # gauess_electric_field=MathTex(r'\nabla \cdot E=\frac{\rho}{\epsilon_{0}}  \hspace{5 mm} \leftrightarrow \hspace{5 mm} \oint E \cdot d A=\frac{Q}{\epsilon_{0}}')
        # # self.add(gauess_electric_field)
        # rect=SurroundingRectangle(gauess_electric_field,buff=MED_SMALL_BUFF,stroke_width=2)
        # self.play(Write(gauess_electric_field))
        # self.play(Create(rect))
        # self.wait(3)


        #_____________________________________________ Gauess Magnetic field __________________________

        # diff_form=MarkupText("differential form").shift(2*UP)
        # int_form=MarkupText("Integral form").shift(2*UP)
        # gauess_magnetic_field=MathTex(r'\nabla \cdot B=0  \hspace{5 mm} \leftrightarrow \hspace{5 mm} \oint B \cdot \mathrm{d} A=0')
        # self.add(diff_form,int_form,gauess_magnetic_field)
        # rect = SurroundingRectangle(gauess_magnetic_field, buff=MED_SMALL_BUFF, stroke_width=2)
        # self.play(Write(gauess_magnetic_field),run_time=2)
        # self.play(Create(rect))
        # self.wait(3)

        #_____________________________________________ Faraday's Law ____________________________________

        # diff_form = MarkupText("differential form").shift(2 * UP)
        # int_form=MarkupText("Integral form").shift(2*UP)
        # faraday_law=MathTex(r'\nabla \times E=-\frac{\partial B}{\partial t}  \hspace{5 mm} \leftrightarrow \hspace{5 mm} \oint \vec{E} \cdot \overrightarrow{d s}=-\frac{d \Phi_{B}}{d t}')
        # # self.add(diff_form,int_form,faraday_law)
        # # self.play(Write(faraday_law,run_time=2))
        # rect = SurroundingRectangle(faraday_law, buff=MED_SMALL_BUFF, stroke_width=2)
        # self.play(Write(faraday_law),Create(rect), run_time=1)
        # # self.play(Create(rect))
        # self.wait(3)

        #_____________________________________________ Ampere Maxwell Law _________________________________

        # diff_form = MarkupText("differential form").shift(2 * UP)
        # int_form = MarkupText("Integral form").shift(2 * UP)
        # ampere_maxwell_law=MathTex(r'{{\nabla \times H=J}}+\frac{\partial D}{\partial t}  \hspace{5 mm} \leftrightarrow \hspace{5 mm} \oint \mathbf{B} \cdot d \mathbf{s}=\mu_{0} I+\varepsilon_{0} \mu_{0} \frac{d \Phi_{e}}{d t}').scale(0.53)
        # rect = SurroundingRectangle(ampere_maxwell_law, buff=MED_SMALL_BUFF, stroke_width=2)
        # self.add( ampere_maxwell_law[0],rect)
        #
        # self.play(Write(ampere_maxwell_law), run_time=2)
        # self.play(Create(rect))
        # self.wait(3)

        #______________________________________________ Continuity Equation _________________________________

        # continuity_equation = MathTex(r'\nabla \cdot \mathbf{J}=-\frac{\partial \rho}{\partial t}')
        # # self.add(diff_form, int_form, ampere_maxwell_law)
        # rect = SurroundingRectangle(continuity_equation, buff=MED_LARGE_BUFF, stroke_width=1.5)
        # self.play(Write(continuity_equation), run_time=1)
        # self.play(Create(rect))
        # self.wait(3)

        #______________________ Divergence of Ampere's law _________________________________________________

        # ampere_maxwell_law = MathTex(
        #     r'{{\nabla \times H=J}}+\frac{\partial D}{\partial t}  \hspace{5 mm} \leftrightarrow \hspace{5 mm} \oint \mathbf{B} \cdot d \mathbf{s}=\mu_{0} I+\varepsilon_{0} \mu_{0} \frac{d \Phi_{e}}{d t}').scale(
        #     0.53).shift(3*UP)
        # rect = SurroundingRectangle(ampere_maxwell_law, buff=0.15, stroke_width=1.3)
        # self.add(ampere_maxwell_law, rect)
        #
        # ampere_law=MathTex(r'\nabla \times \bar{H}=\bar{J}').shift(UP)
        # div_of_amperelaw = MathTex(r'\nabla \cdot(\nabla \times \bar{H})=\nabla \cdot \bar{J}')
        #
        # div_of_j=MathTex(r'0=\nabla \cdot \bar{J}').shift(DOWN)
        # cross = Cross(div_of_j,stroke_width=2)
        #
        #
        # # # self.add(diff_form, int_form, ampere_maxwell_law)
        # # rect = SurroundingRectangle(continuity_equation, buff=MED_LARGE_BUFF, stroke_width=1.5)
        # self.add(ampere_maxwell_law,rect)
        # self.wait(0.5)
        # self.play(ReplacementTransform(ampere_maxwell_law[0].copy(),ampere_law))
        # self.wait(0.5)
        # self.play(ReplacementTransform(ampere_law.copy(),div_of_amperelaw))
        # self.wait(0.5)
        # self.play(ReplacementTransform(div_of_amperelaw.copy(),div_of_j))
        # self.wait(2)
        # self.play(Create(cross))
        # # self.play(Create(rect))
        # self.wait(3)

        #_______________________________ continuity equation _____________________

        # gauesslaw=MathTex(r'{{\nabla \cdot \bar{D}}}=\rho').shift(DOWN)
        # # eq=MathTex(r'\nabla \cdot \bar{J} =  -\nabla \cdot\left(\frac{\partial \bar{D}}{\partial t}\right) ').shift(2.8*DOWN)
        # eq=MathTex(r'{{\nabla}} \cdot {{\bar{J}}} =  {{-}} \nabla {{\cdot}} \left( \frac{  \partial \bar{D}}{\partial t} \right) ').shift(2.8*DOWN)
        #
        #
        # continuity_equation = MathTex(r'\nabla \cdot \mathbf{J}= {{-\frac{\partial \rho}{\partial t} }}').shift((UP))
        # # self.add(diff_form, int_form, ampere_maxwell_law)
        # rect = SurroundingRectangle(continuity_equation, buff=MED_LARGE_BUFF, stroke_width=1.5)
        # rect2=SurroundingRectangle(eq,buff=MED_SMALL_BUFF,stroke_width=1.5)
        # # self.add(continuity_equation,rect,eq,gauesslaw)
        #
        # ampere_maxwell_law = MathTex(
        #     r'{{\nabla \times H=J}}}} + {{\frac{\partial D}{\partial t}}}  \hspace{5 mm} \leftrightarrow \hspace{5 mm} \oint \mathbf{B} \cdot d \mathbf{s}=\mu_{0} I+ \varepsilon_{0} \mu_{0} \frac{d \Phi_{e}}{d t} ').scale(
        #     0.8).shift(2.3*UP)
        #
        # ampere_maxwell_law2 = MathTex(
        #     r'{{\nabla \times H=J + \frac{\partial D}{\partial t}  \hspace{5 mm} \leftrightarrow \hspace{5 mm} \oint \mathbf{B} \cdot d \mathbf{s}=\mu_{0} I+}} \varepsilon_{0} \mu_{0} \frac{d \Phi_{e}}{d t} ').scale(
        #     0.8).shift(2.3 * UP)
        #
        # ampere_maxwell_law3 = MathTex(
        #     r'{{\nabla \times H}}=J + \frac{\partial D}{\partial t}  \hspace{5 mm} \leftrightarrow \hspace{5 mm} \oint \mathbf{B} \cdot d \mathbf{s}=\mu_{0} I+}} \varepsilon_{0} \mu_{0} \frac{d \Phi_{e}}{d t} ').scale(
        #     0.8).shift(2.3 * UP)
        #
        # ampere_maxwell_law4 = MathTex(
        #     r'\nabla \times H=J + \frac{\partial D}{\partial t}  \hspace{5 mm} \leftrightarrow \hspace{5 mm} {{\oint \mathbf{B} \cdot d \mathbf{s}}}=\mu_{0} I+}} \varepsilon_{0} \mu_{0} \frac{d \Phi_{e}}{d t} ').scale(
        #     0.8).shift(2.3 * UP)
        #
        # amprect = SurroundingRectangle(ampere_maxwell_law, buff=0.15, stroke_width=1.3)
        # # self.add(ampere_maxwell_law, amprect,ampere_maxwell_law2)
        #
        # faraday_law = MathTex(r'{{\nabla \times E}}=-\frac{\partial B}{\partial t}  \hspace{5 mm} \leftrightarrow \hspace{5 mm} \oint \vec{E} \cdot \overrightarrow{d s}=-\frac{d \Phi_{B}}{d t}').scale(0.8).shift(DOWN)
        # faraday_law2 = MathTex(r'\nabla \times E=-\frac{\partial B}{\partial t}  \hspace{5 mm} \leftrightarrow \hspace{5 mm} {{\oint \vec{E} \cdot \overrightarrow{d s}}}=-\frac{d \Phi_{B}}{d t}').scale(0.8).shift(DOWN)
        # faraday_law3 = MathTex(r'\nabla \times E={{-\frac{\partial B}{\partial t}}}  \hspace{5 mm} \leftrightarrow \hspace{5 mm} \oint \vec{E} \cdot \overrightarrow{d s}=-\frac{d \Phi_{B}}{d t}').scale(0.8).shift(DOWN)
        # faraday_law4 = MathTex(r'{{\nabla \times E}}={{-\frac{\partial B}{\partial t}}}  \hspace{5 mm} {{\leftrightarrow \hspace{5 mm}}} \oint {{\vec{E}}} \cdot {{\overrightarrow{d s}}} {{=}}  -\frac{d \Phi_{B}}{d t} ').scale(0.8).shift(DOWN)
        # # self.add(diff_form,int_form,faraday_law)
        # # self.play(Write(faraday_law,run_time=2))
        # rect3 = SurroundingRectangle(faraday_law, buff=MED_SMALL_BUFF, stroke_width=1.3)










        # self.wait()
        # self.play(ReplacementTransform(eq[7].copy(),ampere_maxwell_law2[1]),ReplacementTransform(eq[7].copy(),ampere_maxwell_law[2]))
        # self.wait()



        # self.add(continuity_equation,rect)
        # self.wait()
        # self.play(Write(gauesslaw))
        # self.wait()
        # self.play(ReplacementTransform(continuity_equation[0].copy(),eq[0]))
        # self.wait()
        # self.play(ReplacementTransform(continuity_equation[1].copy(),eq[1]),ReplacementTransform(gauesslaw[0].copy(),eq[1]))
        # self.wait()
        # self.play(ShowCreationThenFadeOut(rect2))
        # self.wait()


        # self.play(FadeOut(continuity_equation,rect,eq,gauesslaw))
        # self.play(ampere_maxwell_law.animate.shift(DOWN),ampere_maxwell_law2.animate.shift(DOWN),amprect.animate.shift(DOWN))
        # self.wait()
        #
        # self.play(Write(faraday_law), Create(rect3), run_time=1)
        # # self.play(Create(rect))
        # self.wait()

        # self.add(ampere_maxwell_law[2],ampere_maxwell_law2[1],faraday_law[0],faraday_law2[1],rect3)

        # self.play(ReplacementTransform(faraday_law[0].copy(),ampere_maxwell_law[2]),ReplacementTransform(faraday_law2[1].copy(),ampere_maxwell_law2[1]))


        # self.add(ampere_maxwell_law3[0],ampere_maxwell_law4[1],faraday_law3[1],faraday_law4[-1],rect3)

        # self.add(ampere_maxwell_law, faraday_law, amprect,rect3)
        # self.wait()
        # self.play(ReplacementTransform(faraday_law[0].copy(), ampere_maxwell_law[2]),ReplacementTransform(faraday_law2[1].copy(), ampere_maxwell_law2[1]),run_time=1)
        # self.wait()
        # self.play(ReplacementTransform(ampere_maxwell_law3[0].copy(),faraday_law3[1] ),ReplacementTransform( ampere_maxwell_law4[1].copy(),faraday_law4[-1]),run_time=1)
        # self.wait(0.2)
        # self.play(ReplacementTransform(faraday_law[0].copy(), ampere_maxwell_law[2]),
        #           ReplacementTransform(faraday_law2[1].copy(), ampere_maxwell_law2[1]), run_time=0.6)
        # self.wait(0.2)
        # self.play(ReplacementTransform(ampere_maxwell_law3[0].copy(), faraday_law3[1]),
        #           ReplacementTransform(ampere_maxwell_law4[1].copy(), faraday_law4[-1]), run_time=0.6)
        # self.wait(0.2)
        # self.play(ReplacementTransform(faraday_law[0].copy(), ampere_maxwell_law[2]),
        #           ReplacementTransform(faraday_law2[1].copy(), ampere_maxwell_law2[1]), run_time=0.6)
        # self.wait(0.2)
        # self.play(ReplacementTransform(ampere_maxwell_law3[0].copy(), faraday_law3[1]),
        #           ReplacementTransform(ampere_maxwell_law4[1].copy(), faraday_law4[-1]), run_time=0.6)
        # self.wait(0.2)
        # self.play(ReplacementTransform(faraday_law[0].copy(), ampere_maxwell_law[2]),
        #           ReplacementTransform(faraday_law2[1].copy(), ampere_maxwell_law2[1]), run_time=0.6)
        # self.wait(0.2)
        # self.play(ReplacementTransform(ampere_maxwell_law3[0].copy(), faraday_law3[1]),
        #           ReplacementTransform(ampere_maxwell_law4[1].copy(), faraday_law4[-1]), run_time=0.6)
        # self.wait()

        #_______________________________________________________________________
        # fourier_series=MarkupText('Fourier Series of Square Wave')
        # fourier_transform=MarkupText('Fourier Transform of Square Pulse ')
        # # self.play(Write(fourier_series),run_time=2)
        # self.play(Write(fourier_transform),run_time=2)

        stime=MathTex(r'\bar{E}, \bar{H} \hspace{1.5 mm} \sim \hspace{1.5 mm} e^{j \omega t}').shift(1.5*UP)
        first_derivative=MathTex(r'{{\frac{\partial}{\partial t} \equiv}} j \omega')
        second_derivative=MathTex(r'\frac{\partial^{2}}{\partial t^{2}} \equiv j \omega \cdot j \omega=-\omega^{2}').shift(1.5*DOWN)
        group=VGroup(stime,first_derivative,second_derivative)
        rect1=SurroundingRectangle(group,stroke_width=1.5,buff=MED_SMALL_BUFF)



        # th_maxwell_equations=MathTex(r'\begin{aligned} &\nabla \cdot \mathbf{E}=\frac{\rho}{\epsilon_{0}} \\ &\nabla \cdot \mathbf{B}=0 \\ &\nabla \times \mathbf{E}=-j \omega \mathbf{B} \\ &\nabla \times \mathbf{H}= \mathbf{J} + j \omega \mathbf{D} \end{aligned}',color=YELLOW).scale(1.15).shift(3.5*RIGHT+0.1*DOWN)

        # th_maxwell_equations=MathTex(r'\begin{aligned} &\nabla \cdot \mathbf{E}=\frac{\rho}{\epsilon_{0}} \\ &\nabla \cdot \mathbf{B}=0 \\ &\nabla \times \mathbf{E}=-j \omega \mathbf{B} \\ &\nabla \times \mathbf{H}= \mathbf{J} + j \omega \mathbf{D} \end{aligned}',color=YELLOW).scale(1.15).shift(3.5*RIGHT+0.1*DOWN)
        # th_maxwell_equations=MathTex(r"\begin{aligned}&\nabla \cdot \mathbf{E}=\frac{\rho}{\epsilon_{0}}\\ &\nabla \cdot \mathbf{B}=0 \\ &\nabla \times \mathbf{E}=-" , r"j \omega \mathbf{B}" ,r" \\ &\nabla \times \mathbf{H}= \mathbf{J} +" ,r" j \omega \mathbf{D}" ,r" \end{aligned}",color=YELLOW).scale(1.15).shift(3.5*RIGHT+0.1*DOWN)
        # th_maxwell_equations=MathTex(r'\begin{aligned} &\nabla \cdot \mathbf{E}=\frac{\rho}{\epsilon_{0}} \\ &\nabla \cdot \mathbf{B}=0 \\ &\nabla \times \mathbf{E}=-',   r'j \omega \mathbf{B}'  ,r' \\ &\nabla \times \mathbf{H}= \mathbf{J} +', r' j \omega \mathbf{D}', r'  \end{aligned}',color=YELLOW).scale(1.15).shift(3.5*RIGHT+0.1*DOWN)

        # m1=MathTex(r'\nabla \cdot \mathbf{E}=\frac{\rho}{\epsilon_{0}}',color=YELLOW)
        # m2=MathTex(r'\nabla \cdot \mathbf{B}=0',color=YELLOW)
        # m3=MathTex(r'\nabla \times \mathbf{E}=-{{j \omega}} \mathbf{B}',color=YELLOW)
        # m4=MathTex(r'\nabla \times \mathbf{H}= \mathbf{J} + {{j \omega}} \mathbf{D}',color=YELLOW)

        m1 = MathTex(r'\nabla \cdot \epsilon_{0} \mathbf{E}=\rho', color=YELLOW)
        m2 = MathTex(r'\nabla \cdot \mu_{0} \mathbf{H}=0', color=YELLOW)
        m3 = MathTex(r' {{\nabla \times E &}}= {{ - \mu_{0} \frac{\partial H}{\partial t}}}', color=YELLOW)
        m4 = MathTex(r'{{\nabla \times H &=J}} + {{\epsilon_{0} \frac{\partial E}{\partial t}}}', color=YELLOW)



        th_maxwell_equations=VGroup(m1,m2,m3,m4).arrange(DOWN,buff=0.5)

        th_maxwell_equations_rect = SurroundingRectangle(th_maxwell_equations, buff=MED_SMALL_BUFF,
                                                         color=WHITE, stroke_width=2)
        th_maxwell_equations_eq_bg=BackgroundRectangle(th_maxwell_equations,color=BLUE,fill_opacity=0.1)

        first_zero = MathTex(r'0',color=YELLOW).move_to(m3[3].get_center()).shift(0.7*LEFT)
        second_zero = MathTex(r'0',color=YELLOW).move_to(m4[2].get_center()).shift(0.47*LEFT)

        m21 = MathTex(r'\nabla \cdot \epsilon_{0} \mathbf{E}=\rho', color=YELLOW).shift(3.5*RIGHT)
        m22 = MathTex(r'\nabla \cdot \mu_{0} \mathbf{H}=0', color=YELLOW).shift(3.5*RIGHT)
        m23 = MathTex(r' {{\nabla \times E &}}= {{ - \mu_{0} \frac{\partial H}{\partial t}}}', color=YELLOW).shift(3.5*RIGHT)
        m24 = MathTex(r'{{\nabla \times H &=J}} + {{\epsilon_{0} \frac{\partial E}{\partial t}}}', color=YELLOW).shift(3.5*RIGHT)



        th_maxwell_equations2 = VGroup(m21, m22, m23, m24).arrange(DOWN, buff=0.5).shift(3.5*RIGHT)

        th_maxwell_equations_rect2 = SurroundingRectangle(th_maxwell_equations, buff=MED_SMALL_BUFF,
                                                         color=WHITE, stroke_width=2).shift(3.5*RIGHT)
        th_maxwell_equations_eq_bg2 = BackgroundRectangle(th_maxwell_equations, color=BLUE, fill_opacity=0.1).shift(3.5*RIGHT)


        w1 = MathTex(r'\nabla^{2} \bar{E}=-{{\omega^{2} \mu  \varepsilon_{o}}}  \bar{E}', color=BLUE)
        w2 = MathTex(r'\nabla^{2} \bar{H}=-{{\omega^{2} \mu \varepsilon_{o}}} \bar{H}', color=BLUE)
        wave_eq=VGroup(w1,w2).arrange(DOWN,buff=0.7).shift(3.5*LEFT)
        wave_eq_rect=SurroundingRectangle(wave_eq,buff=0.4,color=RED)

        esol=MathTex(r'{{E_{x}(z)=E_{x}^{+} e^{-j {{\beta}} z}}}+E_{x}^{-} e^{j \beta z}').scale(0.8)
        hsol=MathTex(r'H_{y}=\frac{\beta}{\omega \mu} E_{x}^{+} e^{-j \beta z}-\frac{\beta}{\omega \mu} E_{x}^{-} e^{j \beta z}').scale(0.8)
        sol = VGroup(esol, hsol).arrange(DOWN, buff=0.7).shift(3.5 * LEFT+1.5*DOWN)
        sol_rect=SurroundingRectangle(sol,buff=0.4,color=RED)

        ftw=MathTex(r'E_{x}(z)=E_{x}^{+} e^{-j {{\beta}} z}').shift(3*UP)
        ftw_rect=SurroundingRectangle(ftw,buff=MED_SMALL_BUFF,stroke_width=1.3)

        beta=MathTex(r'{{\beta^{2}=}}\omega^{2} \mu \varepsilon ').shift(3*RIGHT+2*DOWN)

        edl = MathTex(r'\oint \mathbf{E} \cdot dl =0',color=YELLOW).scale(0.9).shift(3.6*LEFT+1*UP)
        sigmavoltages=MathTex(r'\Sigma \hspace{1 mm} V =0',color=YELLOW).shift(3.6*LEFT+1*UP)

        kvlfromfar=MathTex(r' \nabla \cdot \mathbf{E} = 0',color=YELLOW).move_to(m1.get_center())

        divofbothsides=MathTex(r' {{\nabla \cdot (\nabla \times \mathbf{H})}} = \nabla \cdot \mathbf{J} ',color=YELLOW).scale(0.7).shift(3.5*RIGHT+1*UP)
        zero=MathTex(r' 0',color=YELLOW).move_to(divofbothsides[0].get_center()+[1.5,0,0]).scale(0.7)




        # self.add(maxwell_equations_eq_bg,maxwell_equations_eq,maxwell_equations_eq_rect)
        #________________________________
        # self.add(stime.shift(3.5*LEFT),first_derivative.shift(3.5*LEFT),second_derivative.shift(3.5*LEFT),rect1.shift(3.5*LEFT),th_maxwell_equations,th_maxwell_equations_eq_bg,th_maxwell_equations_rect)
        # self.wait()
        # # self.play(stime.animate.shift(3.5*LEFT),first_derivative.animate.shift(3.5*LEFT),second_derivative.animate.shift(3.5*LEFT),rect1.animate.shift(3.5*LEFT))
        # self.play(FadeOut(stime,first_derivative,second_derivative,rect1))
        # self.wait()
        #
        # self.play(ReplacementTransform(m3.copy(),w1),ReplacementTransform(m4.copy(),w1))
        # self.play(ReplacementTransform(m3.copy(),w2),ReplacementTransform(m4.copy(),w2))
        #
        # # self.add(th_maxwell_equations, th_maxwell_equations_rect, th_maxwell_equations_eq_bg)
        # # self.play(Write(th_maxwell_equations),Create(th_maxwell_equations_rect),FadeIn(th_maxwell_equations_eq_bg))
        # # self.wait()
        # # self.play(ReplacementTransform(first_derivative[1].copy(),m3[1]),ReplacementTransform(first_derivative[1].copy(),m4[1]),run_time=2)
        # self.wait()
        # self.play(Create(wave_eq_rect))
        # self.wait(2)
        # # self.play()
        # self.play(wave_eq.animate.shift(2 * UP), wave_eq_rect.animate.shift(2 * UP))
        # self.wait()
        # self.play(ReplacementTransform(wave_eq.copy(), sol),th_maxwell_equations.animate.shift(1.5*UP),th_maxwell_equations_eq_bg.animate.shift(1.5*UP),th_maxwell_equations_rect.animate.shift(1.5*UP))
        # self.wait()
        # self.play(ReplacementTransform(esol[1].copy(),beta[0]))
        # self.play(ReplacementTransform(w1[1].copy(),beta[1]),ReplacementTransform(w2[1].copy(),beta[1]))
        # self.wait()
        # self.play(Create(sol_rect))
        # self.wait(2)
        # self.play(FadeOut(wave_eq,wave_eq_rect,beta,th_maxwell_equations,th_maxwell_equations_rect,th_maxwell_equations_eq_bg))
        # self.wait(0.5)
        # self.play(ReplacementTransform(esol[0].copy(),ftw))
        # self.play(Create(ftw_rect),FadeOut(sol,sol_rect))
        # self.wait()

        # self.add(th_maxwell_equations,th_maxwell_equations_eq_bg,th_maxwell_equations_rect)
        # self.play(Write(m1))
        # self.play(Write(m2))
        # self.play(Write(m3))
        # self.play(Write(m4),Create(th_maxwell_equations_rect),FadeIn(th_maxwell_equations_eq_bg))
        # self.wait()

        th_maxwell_equations_rect.shift(3.5 * LEFT)
        th_maxwell_equations_eq_bg.shift(3.5 * LEFT)

        m3.shift(0.58 * RIGHT + 2.29 * UP + 3.5 * LEFT)
        m4.move_to(m21.get_center() + [0.8, 0, 0])
        self.add(th_maxwell_equations,th_maxwell_equations_eq_bg,th_maxwell_equations_rect,th_maxwell_equations_rect2,th_maxwell_equations_eq_bg2,kvlfromfar.shift(3.5*LEFT))
        self.remove(m1,m2,m3,m4[2],m4[1])

        # self.play(Transform(m3[3],first_zero),Transform(m4[2],second_zero))
        # self.play(FadeOut(m4[1],second_zero))
        # self.play(th_maxwell_equations.animate.become(VGroup(m1,m2,m3,m4).arrange(DOWN,buff=0.5)))

        # self.play(ReplacementTransform(m3.copy(),edl))
        # self.wait()
        # self.play(ReplacementTransform(edl,sigmavoltages))
        # self.wait()

        self.add(sigmavoltages)


        # m4.move_to(m21.get_center() + [0.8, 0, 0])

        # -----------------------------------------------------
        # self.play(ReplacementTransform(m4[0].copy(),divofbothsides))
        # self.wait()
        # self.play(ReplacementTransform(divofbothsides[1],zero))
        # self.play(zero.animate.shift(1*LEFT),divofbothsides.animate.shift(1*LEFT))
        # self.wait()
        # -------------------------------------------
        # self.add(m3)
        # self.wait()


        #__________________
        # self.play(Write(stime))
        # self.wait(0.5)
        # self.play(Write(first_derivative),Write(second_derivative))
        # self.wait(0.5)
        # # self.play(Write(second_derivative))
        # # self.wait(0.5)
        # self.play(Create(rect1))
        # self.wait()

        # self.play(Write(th_maxwell_equations),run_time=3)
        # self.play(Create(th_maxwell_equations_rect),FadeIn(th_maxwell_equations_eq_bg))
        # self.wait(10)


        # self.add(stime,first_derivative,second_derivative,rect1)
        # self.add(th_maxwell_equations)


class Equations2(Scene):
    def construct(self):
        speedofwavepropagation=MathTex(r'c=1 / \sqrt{\mu_{0} \varepsilon_{0}}').shift(DOWN)
        rect=SurroundingRectangle(speedofwavepropagation,buff=MED_SMALL_BUFF,stroke_width=1.3)
        # self.play(Write(speedofwavepropagation),Create(rect))

        dimension=MathTex(r'l \ll \lambda').shift(UP)
        rect2=SurroundingRectangle(dimension,buff=MED_SMALL_BUFF,stroke_width=1.3)

        kcl=MathTex(r'\sum I=0',color=YELLOW)
        group=Group(speedofwavepropagation,dimension,kcl)
        bg=BackgroundRectangle(group,color=BLUE,fill_opacity=0.1)
        rect3=SurroundingRectangle(kcl,buff=MED_SMALL_BUFF,stroke_width=1.3)
        self.add(bg)
        self.play(Write(kcl))
        self.wait()

        # self.play(Write(dimension),Create(rect2))
        #
        # self.wait()



class Appendix(Scene):
    def construct(self):

        charge_t=Text('Charge')
        charge_density_t=Text('Charge density')
        current_t=Text('Current')
        current_density_t=Text('Current density')
        electric_field_t=Text('Electric field')
        electric_flux_density_t=Text('Electric flux density')
        magnetic_field_t=Text('Magnetic field')
        magnetic_flux_density_t=Text('Magnetic flux density')
        magnetic_flux_density_t=Text('Magnetic flux density')
        permittivity_t=Text('Permittivity')
        permeability_t=Text('Permeability')

        t0 = Table(row_labels=[MathTex(r'\rho',color=YELLOW).scale(1.5) , MathTex(r'I',color=RED).scale(1.5),MathTex(r'J',color=YELLOW).scale(1.5),MathTex(r'\bar{E}',color=RED).scale(1.5),MathTex(r'\bar{D}= \varepsilon \bar{E}',color=YELLOW).scale(1.5),MathTex(r'\bar{H}',color=RED).scale(1.5),MathTex(r'\bar{B}= \mu \bar{H}',color=YELLOW).scale(1.5),MathTex(r'\varepsilon_{}',color=RED).scale(1.5),MathTex(r'\mu',color=YELLOW).scale(1.5),MathTex(r'\varepsilon_{0}',color=RED).scale(1.5),MathTex(r'\mu_{0}',color=YELLOW).scale(1.5),MathTex(r'\lambda ',color=RED).scale(1.5)],

                   table=[['Charge density'],
                          ['Current'],
                          ['Current density'],
                          ['Electric field'],
                          ['Electric flux density'],
                          ['Magnetic field'],
                          ['Magnetic flux density'],
                          ['Permittivity'],
                          ['Permeability'],
                          ['Permittivity of Free Space'],
                          ['Permeability of Free Space'],
                          ['Wavelength'],

                          ],
                   line_config={'stroke_width':1},


                   # col_labels=[MathTex(r'Symbol'),MathTex(r'Quantity')]

                   )




        t0.get_rows()[0].set_color(YELLOW)
        t0.get_rows()[1].set_color(RED)
        t0.get_rows()[2].set_color(YELLOW)
        t0.get_rows()[3].set_color(RED)
        t0.get_rows()[4].set_color(YELLOW)
        t0.get_rows()[5].set_color(RED)
        t0.get_rows()[6].set_color(YELLOW)
        t0.get_rows()[7].set_color(RED)
        t0.get_rows()[8].set_color(YELLOW)
        t0.get_rows()[9].set_color(RED)
        t0.get_rows()[10].set_color(YELLOW)
        t0.get_rows()[11].set_color(RED)
        # t0.get_rows()[12].set_color(YELLOW)

        t0.scale(0.4)

        # self.add(t0.scale(0.4))
        self.play(Create(t0),run_time=2)
        self.wait(2)


class TableExamples(Scene):
    def construct(self):
        t0 = Table(
            [["This", "is a"],
                ["simple", "Table in \\n Manim."]])
        t1 = Table(
            [["This", "is a"],
                ["simple", "Table."]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        t1.add_highlighted_cell((2, 2), color=YELLOW)
        t2 = Table(
            [["This", "is a"],
                ["simple", "Table."]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")],
            top_left_entry=Star().scale(0.3),
            include_outer_lines=True,
            arrange_in_grid_config={"cell_alignment": RIGHT})
        t2.add(t2.get_cell((2, 2), color=RED))
        t3 = Table(
            [["This", "is a"],
                ["simple", "Table."]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")],
            top_left_entry=Star().scale(0.3),
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": YELLOW})
        t3.remove(*t3.get_vertical_lines())
        g = Group(
            t0, t1, t2, t3
        ).scale(0.7).arrange_in_grid(buff=1)
        self.add(g)

class Sinusoid(Scene):
    def construct(self):
        ax=Axes(x_range=[0,5],y_range=[-1.5,1.5,0.5])
        sin=ax.plot(lambda t:np.cos(6*t),x_range=[0,4.8],color=YELLOW)
        self.add(ax,sin)

# class ComplexExp(ThreeDScene):
#     def construct(self):



class Equations3(Scene):
    def construct(self):
        # poscharge=MarkupText("Positive Charge Electric Field")
        # negcharge=MarkupText("Negative Charge Electric Field")
        # eul=MathTex(r'e^{-j\omega t}= \cos  (\omega t)-j \hspace{0.1 mm} \sin  (\omega t)')
        # rect=SurroundingRectangle(eul,stroke_width=1.3,buff=MED_LARGE_BUFF,color=BLUE)
        #
        # # self.play(Write(negcharge))
        # self.play(Write(eul),Create(rect))
        # self.wait()

        ftp1 = MathTex(r'{{E_{x}(z)}} = {{E_{x}^{+} e^{-j\beta z}}}').shift(2.8*UP)
        tvariation=MathTex(r'{{E_{x}(t)}} = {{e^{j \omega t}}}').shift(UP)
        ftp2=MathTex(r'{{E_{x}(t,z)}} = {{E_{x}^{+} e^{-j\beta z}}} \hspace{1.5 mm} {{e^{j \omega t}}}').shift(0.5*DOWN)
        ftp3=MathTex(r'{{E_{x}(t,z)}} = {{E_{x}^{+} e^{j( \omega t - \beta z)}}}').shift(0.5*DOWN)
        rect1=SurroundingRectangle(ftp1,stroke_width=1.3,buff=MED_SMALL_BUFF)
        rect2 = SurroundingRectangle(ftp2, stroke_width=1.3, buff=MED_SMALL_BUFF)
        rect3=SurroundingRectangle(ftp3,stroke_width=1.3,buff=MED_SMALL_BUFF)
        cos=MathTex(r'{{E_{x}(t,z)}} = {{ E_{x}^{+} \hspace{0.01 mm} \cos (\omega t -\beta z)}}').align_to(rect3,DOWN).shift(DOWN)
        cosrect=SurroundingRectangle(cos,stroke_width=1.3,buff=MED_SMALL_BUFF)

        self.add(ftp1,rect1)
        self.wait()
        self.play(Write(tvariation))

        # self.play(Write(ftp),Create(rect2))
        # self.wait()


        self.play(ReplacementTransform(ftp1[0].copy(),ftp2[0]),ReplacementTransform(tvariation[0].copy(),ftp2[0]))
        self.wait()
        self.play(ReplacementTransform(ftp1[1].copy(), ftp2[1]), ReplacementTransform(tvariation[1].copy(), ftp2[1]))
        self.play(ReplacementTransform(ftp1[2].copy(),ftp2[2]))
        self.play(ReplacementTransform(tvariation[2].copy(),ftp2[4]))
        self.wait()
        self.play(ReplacementTransform(ftp2[2:],ftp3[2:]))
        # self.play(Create(rect3))
        self.wait()
        self.play(ReplacementTransform(ftp3.copy(), cos))
        self.play(Create(cosrect))
        self.wait()

class Equations4(Scene):
    def construct(self):
        egl=MarkupText("Gauss’ Law for the Electric Field",color=BLUE)
        mgl=MarkupText("Gauss’ Law for the Magnetic Field",color=BLUE)
        fb=MarkupText("Your feedback is important")
        me=MarkupText("Maxwell Equations")
        self.play(Write(me))
        self.wait()








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

        # self.add(axes2,reverse_propagating_wave_graph,propagating_wave_graph)
        # self.wait()
        # self.play(time.animate.set_value(30),run_time=3)
        # self.wait()

        # surface=ParametricSurface(lambda u,v: np.array([u,v,np.cos(w*u-beta*v)]),u_range=[0,42],v_range=[0,42])
        # self.add(surface)

        # propagating_curve2=always_redraw(lambda : axes.plot_parametric_curve(lambda t: [t,t,np.cos(w*time.get_value()-0.5*t)],t_range=[0,40],color=RED,stroke_width=1.5))
        # self.add(axes,propagating_curve2)
        # self.wait()
        # self.play(time.animate.set_value(30),run_time=3)
        # self.wait()
