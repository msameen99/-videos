import manim.cli.cfg.group
import numpy as np

from imports import *

class FTCurves(ThreeDScene):
    def construct(self):

        # self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.5)  # 3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.8)     #yz plane
        self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.8) #xz plane
        axes = ThreeDAxes(x_range=[0, 1*10**6, 0.2*1000000], y_range=[0, 10*10**-6, 2*10**-6], z_range=[-0.5, 2, 0.5], x_length=15, y_length=14,z_length=6).shift([0,0,-3])
        yz_plane = TheSiGuy_lib.yz_plane(axes)
        # xz_plane = TheSiGuy_lib.xz_plane(axes,GREEN)
        # ___________for yz plane______________
        # axes.z_axis.rotate(90*DEGREES,[0,0,1])
        # axes.y_axis.rotate(90*DEGREES,[0,1,0])
        #______________________________________
        #____________for xz plane______________
        axes.x_axis.rotate(90*DEGREES,[1,0,0])


        xm,ym,zm=TheSiGuy_lib.csv_to_xyz('csv/in_fdomain_mag.csv')
        xp,yp,zp=TheSiGuy_lib.csv_to_xyz('csv/in_fdomain_phase.csv')
        mag_res=axes.plot_line_graph(xm,ym,zm,add_vertex_dots=False,line_color=RED)
        phs_res=axes.plot_line_graph(xp,yp,zp,add_vertex_dots=False,line_color=TEAL_E)

        step=TheSiGuy_lib.three_d_graph_from_csv(axes,'csv/in_tdomain.csv',color=LIGHT_PINK,stroke_width=3)



        xp,yp,zp=TheSiGuy_lib.csv_to_xyz('csv/in_fdomain_phase.csv')
        freq=[]
        amp=[]
        phs=[]


        for i in np.arange(0,990,10):
            freq.append(xm[i])
        for i in np.arange(0,990,10):
            amp.append(zm[i])
        for i in np.arange(0,990,10):
            phs.append(zp[i])





        comps=[axes.plot_parametric_curve(lambda t: np.array([f, t, a * np.cos(2 * np.pi*f * t + p)]), stroke_width=2,color=GOLD, t_range=[0, 10*10**-6, 10**-9]) for f,a,p in zip(freq,amp,phs)]

        comps_acc = ["csv/step_comps/comp%i.csv" % num for num in range(1, 100)]
        graphs_acc = [TheSiGuy_lib.three_d_graph_from_csv(ax=axes, csvFile=file,color=YELLOW,stroke_width=3) for file in comps_acc]
        # self.add(axes, graphs_acc[0])
        self.play(Create(axes))
        self.wait(0.2)
        self.play(FadeIn(yz_plane),run_time=1)
        self.wait()
        self.play(Create(step),run_time=1)
        self.wait()



        ###################### ploting the components on time freq axis one by one #############################
        self.add(axes, graphs_acc[0],step)
        for i,curve in enumerate(comps):
            mag=axes.plot_line_graph(xm[:(i+1)*10],ym[:(i+1)*10],zm[:(i+1)*10],add_vertex_dots=False,line_color=RED,stroke_width=3)
            # phs=axes.plot_line_graph(xp[:(i+1)*10],yp[:(i+1)*10],zp[:(i+1)*10],add_vertex_dots=False,line_color=GOLD_E)
            # self.play(Transform(propagating_wave_curves[0],i))
            # self.remove(propagating_wave_curves[i-1])
            comps[i-1].set_stroke([BLUE,GREEN],0.8)
            self.remove(graphs_acc[i-1])
            self.add(comps[i])
            self.add(mag)
            # self.add(phs)
            self.add(graphs_acc[i])
            self.wait(0.4)
            self.remove(comps[0])
        self.wait()

class FTCurves2(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.5)  # 3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.8)     #yz plane
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.8) #xz plane
        axes = ThreeDAxes(x_range=[0, 1*10**6, 0.2*1000000], y_range=[0, 10*10**-6, 2*10**-6], z_range=[-0.5, 2, 0.5], x_length=15, y_length=14,z_length=6).shift([0,0,-3])
        yz_plane = TheSiGuy_lib.yz_plane(axes)
        # xz_plane = TheSiGuy_lib.xz_plane(axes,GREEN)
        # ___________for yz plane______________
        # axes.z_axis.rotate(90*DEGREES,[0,0,1])
        # axes.y_axis.rotate(90*DEGREES,[0,1,0])
        #______________________________________
        #____________for xz plane______________
        # axes.x_axis.rotate(90*DEGREES,[1,0,0])


        xm,ym,zm=TheSiGuy_lib.csv_to_xyz('csv/in_fdomain_mag.csv')
        xp,yp,zp=TheSiGuy_lib.csv_to_xyz('csv/in_fdomain_phase.csv')
        mag_res=axes.plot_line_graph(xm,ym,zm,add_vertex_dots=False,line_color=RED)
        phs_res=axes.plot_line_graph(xp,yp,zp,add_vertex_dots=False,line_color=TEAL_E)

        step=TheSiGuy_lib.three_d_graph_from_csv(axes,'csv/in_tdomain.csv',color=LIGHT_PINK,stroke_width=3)



        xp,yp,zp=TheSiGuy_lib.csv_to_xyz('csv/in_fdomain_phase.csv')
        freq=[]
        amp=[]
        phs=[]


        for i in np.arange(0,990,10):
            freq.append(xm[i])
        for i in np.arange(0,990,10):
            amp.append(zm[i])
        for i in np.arange(0,990,10):
            phs.append(zp[i])





        comps=[axes.plot_parametric_curve(lambda t: np.array([f, t, a * np.cos(2 * np.pi*f * t + p)]), stroke_width=2,color=GOLD, t_range=[0, 10*10**-6, 10**-9]) for f,a,p in zip(freq,amp,phs)]

        comps_acc = ["csv/step_comps/comp%i.csv" % num for num in range(1, 100)]
        graphs_acc = [TheSiGuy_lib.three_d_graph_from_csv(ax=axes, csvFile=file,color=YELLOW,stroke_width=3) for file in comps_acc]
        # self.add(axes, graphs_acc[0])
        self.play(Create(axes))
        self.wait(0.2)
        self.play(FadeIn(yz_plane),run_time=1)
        self.wait()
        self.play(Create(step),run_time=1)
        self.wait()



        ###################### ploting the components on time freq axis one by one #############################
        self.add(axes, graphs_acc[0],step)
        for i,curve in enumerate(comps):
            mag=axes.plot_line_graph(xm[:(i+1)*10],ym[:(i+1)*10],zm[:(i+1)*10],add_vertex_dots=False,line_color=RED,stroke_width=3)
            # phs=axes.plot_line_graph(xp[:(i+1)*10],yp[:(i+1)*10],zp[:(i+1)*10],add_vertex_dots=False,line_color=GOLD_E)
            # self.play(Transform(propagating_wave_curves[0],i))
            # self.remove(propagating_wave_curves[i-1])
            comps[i-1].set_stroke([BLUE,GREEN],0.8)
            self.remove(graphs_acc[i-1])
            self.add(comps[i])
            self.add(mag)
            # self.add(phs)
            self.add(graphs_acc[i])
            self.wait(0.4)
            self.remove(comps[0])
        self.wait()




class FTCurves3(ThreeDScene):
    def construct(self):

        # self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.5)  # 3d view
        self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.8)     #yz plane
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.8) #xz plane
        axes = ThreeDAxes(x_range=[0, 1*10**6, 0.2*1000000], y_range=[0, 10*10**-6, 2*10**-6], z_range=[-0.5, 2, 0.5], x_length=15, y_length=14,z_length=6).shift([0,0,-3])
        yz_plane = TheSiGuy_lib.yz_plane(axes)
        # xz_plane = TheSiGuy_lib.xz_plane(axes,GREEN)
        # ___________for yz plane______________
        axes.z_axis.rotate(90*DEGREES,[0,0,1])
        axes.y_axis.rotate(90*DEGREES,[0,1,0])
        #______________________________________
        #____________for xz plane______________
        # axes.x_axis.rotate(90*DEGREES,[1,0,0])


        xm,ym,zm=TheSiGuy_lib.csv_to_xyz('csv/in_fdomain_mag.csv')
        xp,yp,zp=TheSiGuy_lib.csv_to_xyz('csv/in_fdomain_phase.csv')
        mag_res=axes.plot_line_graph(xm,ym,zm,add_vertex_dots=False,line_color=RED)
        phs_res=axes.plot_line_graph(xp,yp,zp,add_vertex_dots=False,line_color=TEAL_E)

        step=TheSiGuy_lib.three_d_graph_from_csv(axes,'csv/in_tdomain.csv',color=LIGHT_PINK,stroke_width=3)



        xp,yp,zp=TheSiGuy_lib.csv_to_xyz('csv/in_fdomain_phase.csv')
        freq=[]
        amp=[]
        phs=[]


        for i in np.arange(0,990,10):
            freq.append(xm[i])
        for i in np.arange(0,990,10):
            amp.append(zm[i])
        for i in np.arange(0,990,10):
            phs.append(zp[i])





        comps=[axes.plot_parametric_curve(lambda t: np.array([f, t, a * np.cos(2 * np.pi*f * t + p)]), stroke_width=2,color=GOLD, t_range=[0, 10*10**-6, 10**-9]) for f,a,p in zip(freq,amp,phs)]

        comps_acc = ["csv/step_comps/comp%i.csv" % num for num in range(1, 100)]
        graphs_acc = [TheSiGuy_lib.three_d_graph_from_csv(ax=axes, csvFile=file,color=YELLOW,stroke_width=3) for file in comps_acc]
        # self.add(axes, graphs_acc[0])
        self.play(Create(axes))
        self.wait(0.2)
        self.play(FadeIn(yz_plane),run_time=1)
        self.wait()
        self.play(Create(step),run_time=1)
        self.wait()



        ###################### ploting the components on time freq axis one by one #############################
        self.add(axes, graphs_acc[0],step)
        for i,curve in enumerate(comps):
            mag=axes.plot_line_graph(xm[:(i+1)*10],ym[:(i+1)*10],zm[:(i+1)*10],add_vertex_dots=False,line_color=RED,stroke_width=3)
            # phs=axes.plot_line_graph(xp[:(i+1)*10],yp[:(i+1)*10],zp[:(i+1)*10],add_vertex_dots=False,line_color=GOLD_E)
            # self.play(Transform(propagating_wave_curves[0],i))
            # self.remove(propagating_wave_curves[i-1])
            comps[i-1].set_stroke([BLUE,GREEN],0.8)
            self.remove(graphs_acc[i-1])
            self.add(comps[i])
            self.add(mag)
            # self.add(phs)
            self.add(graphs_acc[i])
            self.wait(0.4)
            self.remove(comps[0])
        self.wait()



#______________________________________________________________________________________________________________________
#################################### lp filtered step #################################################################

class FTCurves_out(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.7)  # 3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7) #xz plane
        axes = ThreeDAxes(x_range=[0, 1*10**6, 1000000], y_range=[0, 10*10**-6, 2*10**-6], z_range=[-0.5, 2, 0.5], x_length=15, y_length=14,z_length=6).shift([0,0,-3]).scale(0.8)
        yz_plane = TheSiGuy_lib.yz_plane(axes)
        # xz_plane = TheSiGuy_lib.xz_plane(axes,GREEN)


        self.add(axes,yz_plane)
        xm,ym,zm=TheSiGuy_lib.csv_to_xyz('csv/out_fdomain_mag.csv')
        graph=axes.plot_line_graph(xm,ym,zm,add_vertex_dots=False,line_color=RED)
        self.add(axes,graph)

        xp,yp,zp=TheSiGuy_lib.csv_to_xyz('csv/out_fdomain_phase.csv')
        freq=[]
        amp=[]
        phs=[]


        for i in np.arange(0,990,10):
            freq.append(xm[i])
        for i in np.arange(0,990,10):
            amp.append(zm[i])
        for i in np.arange(0,990,10):
            phs.append(zp[i])


        comps=[axes.plot_parametric_curve(lambda t: np.array([f, t, a * np.cos(2 * np.pi*f * t + p*(np.pi/180))]), stroke_width=3,color=YELLOW, t_range=[0, 10*10**-6, 10**-9]) for f,a,p in zip(freq,amp,phs)]

        comps_acc = ["csv/lpf_step_comps/comp%i.csv" % num for num in range(1, 100)]
        graphs_acc = [TheSiGuy_lib.three_d_graph_from_csv(ax=axes, csvFile=file,color=YELLOW,stroke_width=2) for file in comps_acc]
        # self.add(axes, graphs_acc[0])



        # ploting the components on time freq axis one by one
        self.add(axes, graphs_acc[0])
        for i,curve in enumerate(comps):
            # self.play(Transform(propagating_wave_curves[0],i))
            # self.remove(propagating_wave_curves[i-1])
            comps[i-1].set_stroke([BLUE,GREEN],0.8)
            self.remove(graphs_acc[i-1])
            self.add(comps[i])
            self.add(graphs_acc[i])
            self.wait(0.5)
            self.remove(comps[0])
        self.wait()



#_____________________________________________________________________________
####################### creating step sinusoid by sinusoid ###################
class LPFStep(Scene):
    def construct(self):
        ax=Axes(x_range=[0,10*10**-6,1*10**-6],y_range=[0,1.2,0.2],x_length=13, y_length=5,)
        numberplane = NumberPlane(x_range=[0, 10 * 10 ** -6, 1 * 10 ** -6], y_range=[0, 2, 0.5], x_length=13, y_length=5, background_line_style={"stroke_width": 1, "stroke_opacity": 0.5, }, axis_config={"stroke_width": 1.5, "include_ticks": True, "include_tip": False})

        comps = ["csv/lpf_step_comps/comp%i.csv" % num for num in range(1, 100)]
        graphs = [TheSiGuy_lib.two_d_graph_from_csv(ax=numberplane, csvFile=file) for file in comps]
        self.add(numberplane,graphs[0])
        transforms = [Transform(graphs[0], graphs[ind], run_time=0.1) for ind in range(0, 99)]
        #
        for i, curve in enumerate(comps):
            # self.play(Transform(propagating_wave_curves[0],i))
            # self.remove(propagating_wave_curves[i-1])
            self.remove(graphs[i - 1])
            self.add(graphs[i])
            self.wait(0.4)
        self.wait()


        # g=TheSiGuy_lib.two_d_graph_from_csv(ax,'csv/lpf_step_comps/comp109.csv', color=YELLOW,stroke_width=2)
        # self.add(ax,g)

class Step(Scene):
    def construct(self):
        ax = Axes(x_range=[0, 10 * 10 ** -6, 1 * 10 ** -6], y_range=[0, 1, 0.25])
        numberplane = NumberPlane(x_range=[0, 10 * 10 ** -6, 1 * 10 ** -6], y_range=[0, 2, 0.5], x_length=13, y_length=5,background_line_style={"stroke_width": 1, "stroke_opacity": 0.5,},axis_config = {"stroke_width": 1.5, "include_ticks": True, "include_tip": False})
        xs,ys,zs=TheSiGuy_lib.csv_to_xyz('csv/in_tdomain.csv')
        step=numberplane.plot_line_graph(ys,zs,add_vertex_dots=False,line_color=LIGHT_PINK,stroke_width=2)
        comps = ["csv/step_comps/comp%i.csv" % num for num in range(1, 100)]
        graphs = [TheSiGuy_lib.two_d_graph_from_csv(ax=numberplane, csvFile=file) for file in comps]
        self.add(numberplane, graphs[0],step)
        transforms = [Transform(graphs[0], graphs[ind], run_time=0.1) for ind in range(0, 99)]
        #
        for i, curve in enumerate(comps):
            # self.play(Transform(propagating_wave_curves[0],i))
            # self.remove(propagating_wave_curves[i-1])
            self.remove(graphs[i - 1])
            self.add(graphs[i])
            self.wait(0.4)
        self.wait()


#__________________________________________________________________________________________________________________________
###################### phase responcse ##############################
class PhasePlots(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.8)  # xz plane
        axes = ThreeDAxes(x_range=[0, 1 * 10 ** 6, 0.2*1000000], y_range=[0, 10 * 10 ** -6, 2 * 10 ** -6],z_range=[-3.50, 0.5, 1.05], x_length=15, y_length=14, z_length=6,axis_config = {"stroke_width": 1.5, "include_ticks": True, "include_tip": False}).shift([0,0,2])
        ax = Axes(x_range=[0, 1*10**6, 0.2*1000000], y_range=[-3.50, 0.5, 1.05],axis_config = {"stroke_width": 1.5, "include_ticks": True, "include_tip": False},y_length=4)
        numberplane = NumberPlane(x_range=[0, 1*10**6, 1000000], y_range=[-4, 0.5, 0.5], x_length=15, y_length=6,background_line_style={"stroke_width": 1, "stroke_opacity": 0.5,},axis_config = {"stroke_width": 1.5, "include_ticks": True, "include_tip": False})
        xp1,yp1,zp1=TheSiGuy_lib.csv_to_xyz('csv/in_fdomain_phase.csv')
        axes.x_axis.rotate(90 * DEGREES, [1, 0, 0])


        self.play(Create(axes))
        self.wait(0.2)
        self.wait(1)
        self.wait()
        self.wait(1)
        self.wait()

        ###################### ploting the components on time freq axis one by one #############################

        for i in range(0,990,10):
            # mag = axes.plot_line_graph(xm[:(i + 1) * 10], ym[:(i + 1) * 10], zm[:(i + 1) * 10], add_vertex_dots=False,
            #                            line_color=RED)
            phs1=axes.plot_line_graph(xp1[:(i+1)],yp1[:(i+1)],zp1[:(i+1)],add_vertex_dots=False,line_color=ORANGE,stroke_width=3)
            # self.play(Transform(propagating_wave_curves[0],i))
            # self.remove(propagating_wave_curves[i-1])
            # comps[i - 1].set_stroke([BLUE, GREEN], 0.8)
            # self.remove(graphs_acc[i - 1])
            # self.add(comps[i])
            # self.add(mag)
            self.add(phs1)
            # self.add(graphs_acc[i])
            self.wait(0.4)
            # self.remove(comps[0])
        self.wait()


#######__________________________________________________________________________######################################
###################################### OUTPUT #########################################################################
class OutFTCurves(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.5)  # 3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.8)     #yz plane
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.8) #xz plane
        axes = ThreeDAxes(x_range=[0, 1*10**6, 0.2*1000000], y_range=[0, 10*10**-6, 2*10**-6], z_range=[-0.5, 2, 0.5], x_length=15, y_length=14,z_length=6).shift([0,0,-3])
        yz_plane = TheSiGuy_lib.yz_plane(axes)
        # xz_plane = TheSiGuy_lib.xz_plane(axes,GREEN)
        # ___________for yz plane______________
        # axes.z_axis.rotate(90*DEGREES,[0,0,1])
        # axes.y_axis.rotate(90*DEGREES,[0,1,0])
        #______________________________________
        #____________for xz plane______________
        # axes.x_axis.rotate(90*DEGREES,[1,0,0])


        xm,ym,zm=TheSiGuy_lib.csv_to_xyz('csv/out_fdomain_mag.csv')
        xp,yp,zp=TheSiGuy_lib.csv_to_xyz('csv/out_fdomain_phase.csv')
        mag_res=axes.plot_line_graph(xm,ym,zm,add_vertex_dots=False,line_color=RED)
        phs_res=axes.plot_line_graph(xp,yp,zp,add_vertex_dots=False,line_color=TEAL_E)

        step=TheSiGuy_lib.three_d_graph_from_csv(axes,'csv/out_tdomain.csv',color=LIGHT_PINK,stroke_width=3)



        xp,yp,zp=TheSiGuy_lib.csv_to_xyz('csv/out_fdomain_phase.csv')
        freq=[]
        amp=[]
        phs=[]


        for i in np.arange(0,990,10):
            freq.append(xm[i])
        for i in np.arange(0,990,10):
            amp.append(zm[i])
        for i in np.arange(0,990,10):
            phs.append(zp[i])





        comps=[axes.plot_parametric_curve(lambda t: np.array([f, t, a * np.cos(2 * np.pi*f * t + p)]), stroke_width=2,color=GOLD, t_range=[0, 10*10**-6, 10**-9]) for f,a,p in zip(freq,amp,phs)]

        comps_acc = ["csv/lpf_step_comps/comp%i.csv" % num for num in range(1, 100)]
        graphs_acc = [TheSiGuy_lib.three_d_graph_from_csv(ax=axes, csvFile=file,color=YELLOW,stroke_width=3) for file in comps_acc]
        # self.add(axes, graphs_acc[0])
        self.play(Create(axes))
        self.wait(0.2)
        self.play(FadeIn(yz_plane),run_time=1)
        self.wait()
        self.play(Create(step),run_time=1)
        self.wait()

        ###################### ploting the components on time freq axis one by one #############################
        self.add(axes, graphs_acc[0], step)
        for i, curve in enumerate(comps):
            mag = axes.plot_line_graph(xm[:(i + 1) * 10], ym[:(i + 1) * 10], zm[:(i + 1) * 10], add_vertex_dots=False,
                                       line_color=RED, stroke_width=3)
            # phs=axes.plot_line_graph(xp[:(i+1)*10],yp[:(i+1)*10],zp[:(i+1)*10],add_vertex_dots=False,line_color=GOLD_E)
            # self.play(Transform(propagating_wave_curves[0],i))
            # self.remove(propagating_wave_curves[i-1])
            comps[i - 1].set_stroke([BLUE, GREEN], 0.8)
            self.remove(graphs_acc[i - 1])
            self.add(comps[i])
            self.add(mag)
            # self.add(phs)
            self.add(graphs_acc[i])
            self.wait(0.4)
            self.remove(comps[0])
        self.wait()


class OutFTCurves2(ThreeDScene):
    def construct(self):

        # self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.5)  # 3d view
        self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.8)     #yz plane
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000,
        #                                     zoom=0.8)  # xz plane
        axes = ThreeDAxes(x_range=[0, 1 * 10 ** 6, 0.2 * 1000000], y_range=[0, 10 * 10 ** -6, 2 * 10 ** -6],
                                  z_range=[-0.5, 2, 0.5], x_length=15, y_length=14, z_length=6).shift([0, 0, -3])
        yz_plane = TheSiGuy_lib.yz_plane(axes)
        # xz_plane = TheSiGuy_lib.xz_plane(axes,GREEN)
        # ___________for yz plane______________
        axes.z_axis.rotate(90*DEGREES,[0,0,1])
        axes.y_axis.rotate(90*DEGREES,[0,1,0])
        # ______________________________________
        # ____________for xz plane______________
        # axes.x_axis.rotate(90 * DEGREES, [1, 0, 0])

        xm, ym, zm = TheSiGuy_lib.csv_to_xyz('csv/out_fdomain_mag.csv')
        xp, yp, zp = TheSiGuy_lib.csv_to_xyz('csv/out_fdomain_phase.csv')
        mag_res = axes.plot_line_graph(xm, ym, zm, add_vertex_dots=False, line_color=RED)
        phs_res = axes.plot_line_graph(xp, yp, zp, add_vertex_dots=False, line_color=TEAL_E)

        step = TheSiGuy_lib.three_d_graph_from_csv(axes, 'csv/out_tdomain.csv', color=LIGHT_PINK,
                                                           stroke_width=3)

        xp, yp, zp = TheSiGuy_lib.csv_to_xyz('csv/out_fdomain_phase.csv')
        freq = []
        amp = []
        phs = []

        for i in np.arange(0, 990, 10):
            freq.append(xm[i])
        for i in np.arange(0, 990, 10):
            amp.append(zm[i])
        for i in np.arange(0, 990, 10):
            phs.append(zp[i])

        comps = [axes.plot_parametric_curve(lambda t: np.array([f, t, a * np.cos(2 * np.pi * f * t + p)]),
                                            stroke_width=2, color=GOLD, t_range=[0, 10 * 10 ** -6, 10 ** -9])
                    for f, a, p in zip(freq, amp, phs)]

        comps_acc = ["csv/lpf_step_comps/comp%i.csv" % num for num in range(1, 100)]
        graphs_acc = [TheSiGuy_lib.three_d_graph_from_csv(ax=axes, csvFile=file, color=YELLOW, stroke_width=3)
                        for file in comps_acc]
        # self.add(axes, graphs_acc[0])
        self.play(Create(axes))
        self.wait(0.2)
        self.play(FadeIn(yz_plane), run_time=1)
        self.wait()
        self.play(Create(step), run_time=1)
        self.wait()









        ###################### ploting the components on time freq axis one by one #############################
        self.add(axes, graphs_acc[0],step)
        for i,curve in enumerate(comps):
            mag=axes.plot_line_graph(xm[:(i+1)*10],ym[:(i+1)*10],zm[:(i+1)*10],add_vertex_dots=False,line_color=RED,stroke_width=3)
            # phs=axes.plot_line_graph(xp[:(i+1)*10],yp[:(i+1)*10],zp[:(i+1)*10],add_vertex_dots=False,line_color=GOLD_E)
            # self.play(Transform(propagating_wave_curves[0],i))
            # self.remove(propagating_wave_curves[i-1])
            comps[i-1].set_stroke([BLUE,GREEN],0.8)
            self.remove(graphs_acc[i-1])
            self.add(comps[i])
            self.add(mag)
            # self.add(phs)
            self.add(graphs_acc[i])
            self.wait(0.4)
            self.remove(comps[0])
        self.wait()

class OutFTCurves3(ThreeDScene):
    def construct(self):

        # self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.5)  # 3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.8)  # yz plane
        self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000,
                                            zoom=0.8)  # xz plane
        axes = ThreeDAxes(x_range=[0, 1 * 10 ** 6, 0.2 * 1000000], y_range=[0, 10 * 10 ** -6, 2 * 10 ** -6],
                            z_range=[-0.5, 2, 0.5], x_length=15, y_length=14, z_length=6).shift([0, 0, -3])
        yz_plane = TheSiGuy_lib.yz_plane(axes)
        # xz_plane = TheSiGuy_lib.xz_plane(axes,GREEN)
        # ___________for yz plane______________
        # axes.z_axis.rotate(90 * DEGREES, [0, 0, 1])
        # axes.y_axis.rotate(90 * DEGREES, [0, 1, 0])
        # ______________________________________
        # ____________for xz plane______________
        axes.x_axis.rotate(90 * DEGREES, [1, 0, 0])

        xm, ym, zm = TheSiGuy_lib.csv_to_xyz('csv/out_fdomain_mag.csv')
        xp, yp, zp = TheSiGuy_lib.csv_to_xyz('csv/out_fdomain_phase.csv')
        mag_res = axes.plot_line_graph(xm, ym, zm, add_vertex_dots=False, line_color=RED)
        phs_res = axes.plot_line_graph(xp, yp, zp, add_vertex_dots=False, line_color=TEAL_E)

        step = TheSiGuy_lib.three_d_graph_from_csv(axes, 'csv/out_tdomain.csv', color=LIGHT_PINK,
                                                       stroke_width=3)

        xp, yp, zp = TheSiGuy_lib.csv_to_xyz('csv/out_fdomain_phase.csv')
        freq = []
        amp = []
        phs = []

        for i in np.arange(0, 990, 10):
            freq.append(xm[i])
        for i in np.arange(0, 990, 10):
             amp.append(zm[i])
        for i in np.arange(0, 990, 10):
            phs.append(zp[i])

        comps = [axes.plot_parametric_curve(lambda t: np.array([f, t, a * np.cos(2 * np.pi * f * t + p)]),
                                            stroke_width=2, color=GOLD, t_range=[0, 10 * 10 ** -6, 10 ** -9])
                    for f, a, p in zip(freq, amp, phs)]

        comps_acc = ["csv/lpf_step_comps/comp%i.csv" % num for num in range(1, 100)]
        graphs_acc = [TheSiGuy_lib.three_d_graph_from_csv(ax=axes, csvFile=file, color=YELLOW, stroke_width=3)
                        for file in comps_acc]
        # self.add(axes, graphs_acc[0])
        self.play(Create(axes))
        self.wait(0.2)
        self.play(FadeIn(yz_plane), run_time=1)
        self.wait()
        self.play(Create(step), run_time=1)
        self.wait()

        ###################### ploting the components on time freq axis one by one #############################
        self.add(axes, graphs_acc[0], step)
        for i, curve in enumerate(comps):
            mag = axes.plot_line_graph(xm[:(i + 1) * 10], ym[:(i + 1) * 10], zm[:(i + 1) * 10],
                                        add_vertex_dots=False, line_color=RED, stroke_width=3)
            # phs=axes.plot_line_graph(xp[:(i+1)*10],yp[:(i+1)*10],zp[:(i+1)*10],add_vertex_dots=False,line_color=GOLD_E)
            # self.play(Transform(propagating_wave_curves[0],i))
            # self.remove(propagating_wave_curves[i-1])
            comps[i - 1].set_stroke([BLUE, GREEN], 0.8)
            self.remove(graphs_acc[i - 1])
            self.add(comps[i])
            self.add(mag)
            # self.add(phs)
            self.add(graphs_acc[i])
            self.wait(0.4)
            self.remove(comps[0])
        self.wait()

class PhasePlots2(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000,
                                    zoom=0.8)  # xz plane
        axes = ThreeDAxes(x_range=[0, 1 * 10 ** 6, 0.2 * 1000000], y_range=[0, 10 * 10 ** -6, 2 * 10 ** -6],
                            z_range=[-3.50, 3.50, 1.05], x_length=15, y_length=14, z_length=6,
                            axis_config={"stroke_width": 1.5, "include_ticks": True, "include_tip": False}).shift(
            [0, 0, 0.5])
        ax = Axes(x_range=[0, 1 * 10 ** 6, 0.2 * 1000000], y_range=[-3.50, 0.5, 1.05],
                    axis_config={"stroke_width": 1.5, "include_ticks": True, "include_tip": False}, y_length=4)
        numberplane = NumberPlane(x_range=[0, 1 * 10 ** 6, 1000000], y_range=[-4, 0.5, 0.5], x_length=15,
                                    y_length=6, background_line_style={"stroke_width": 1, "stroke_opacity": 0.5, },
                                    axis_config={"stroke_width": 1.5, "include_ticks": True, "include_tip": False})
        xp1, yp1, zp1 = TheSiGuy_lib.csv_to_xyz('csv/out_fdomain_phase.csv')
        axes.x_axis.rotate(90 * DEGREES, [1, 0, 0])

        self.play(Create(axes))
        self.wait(0.2)
        self.wait(1)
        self.wait()
        self.wait(1)
        self.wait()

        ###################### ploting the components on time freq axis one by one #############################

        for i in range(0, 990, 10):
            # mag = axes.plot_line_graph(xm[:(i + 1) * 10], ym[:(i + 1) * 10], zm[:(i + 1) * 10], add_vertex_dots=False,
            #                            line_color=RED)
            phs1 = axes.plot_line_graph(xp1[:(i + 1)], yp1[:(i + 1)], zp1[:(i + 1)], add_vertex_dots=False,
                                            line_color=ORANGE, stroke_width=3)
            # self.play(Transform(propagating_wave_curves[0],i))
            # self.remove(propagating_wave_curves[i-1])
            # comps[i - 1].set_stroke([BLUE, GREEN], 0.8)
            # self.remove(graphs_acc[i - 1])
            # self.add(comps[i])
            # self.add(mag)
            self.add(phs1)
            # self.add(graphs_acc[i])
            self.wait(0.14)
            # self.remove(comps[0])
        self.wait()




class ComplexExp(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes(x_range=[-1.5, 1.5, 0.25], y_range=[0, 10.3, 2], z_range=[-1.5, 1.5, 0.25], x_length=9, z_length=9, y_length=15)
        numberplane = NumberPlane(x_range=[-1.5, 1.5, 0.25], y_range=[-1.5, 1.5, 0.25], x_length=9, y_length=9,
                                  background_line_style={
                                      "stroke_color": BLUE,
                                      "stroke_width": 0.7,
                                      "stroke_opacity": 1,}).rotate(90 * DEGREES, RIGHT).move_to(axes.get_origin())
        #___________________________________________________________________
        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.58)  # 3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        # axes.y_axis.rotate(90*DEGREES,[0,1,0])
        # axes.z_axis.rotate(-90*DEGREES,[0,0,1])
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7)  # xz plane
        # axes.x_axis.rotate(90 * DEGREES, [1, 0, 0])
        #___________________________________________________________________

        tvalue = ValueTracker(1)
        head_tracker = ValueTracker(10)
        amp_tracker=ValueTracker(1)
        ce1=always_redraw(lambda : axes.plot_parametric_curve(lambda t: [np.real(  np.exp(1j * (2 * np.pi * tvalue.get_value() * t ))),t,np.imag(np.exp(1j * (2 * np.pi * tvalue.get_value() * t )))], stroke_width=2, color=RED, t_range=np.array([0, head_tracker.get_value(), 0.01])))
        phs_tracker = ValueTracker(0.8)
        ce2=always_redraw(lambda : axes.plot_parametric_curve(lambda t: [amp_tracker.get_value()*np.real(  np.exp(1j * (2 * np.pi * tvalue.get_value() * t + phs_tracker.get_value()))),t,amp_tracker.get_value()*np.imag(np.exp(1j * (2 * np.pi * tvalue.get_value() * t +phs_tracker.get_value())))], stroke_width=2, color=YELLOW, t_range=np.array([0, head_tracker.get_value(), 0.01])))
        dot1 = always_redraw(lambda: Dot3D(ce1.get_end(),color=RED).scale(1.5))
        dot2 = always_redraw(lambda: Dot3D(ce2.get_end(),color=YELLOW).scale(1.5))
        expTheta = MathTex(r'c \hspace{0.6 mm}', r'e^{j ', r'(wt+\phi) }').scale(1.2).rotate(90 * DEGREES, RIGHT).move_to(axes.c2p(1, 0, 1))
        theta = MathTex(r'\theta ', color=RED).rotate(90 * DEGREES, RIGHT).move_to(axes.c2p(0.25, 0, 0.1))
        expasfunoftime = MathTex(r'c \hspace{0.6 mm} e^{j(wt+\phi)}').rotate(90 * DEGREES, RIGHT).move_to(axes.c2p(1, 0, 1))
        expasfunoftimemoving = always_redraw(lambda: MathTex(r'c \hspace{0.6 mm} e^{j(w *  %0.1f +\phi)}' % tvalue.get_value()).rotate(90 * DEGREES, RIGHT).move_to(axes.c2p(1, 0, 1)))
        euler_formula = MathTex(r'e^{j \omega  t} = cos(\omega  t)+j \hspace{0.7 mm} sin(\omega  t)')

        # vect = always_redraw(lambda: Arrow3D(axes.get_origin(), ce.get_points()[500], stroke_width=0.5, color=RED))
        vect1 = always_redraw(lambda: Arrow3D(axes.get_origin(), dot1.get_center(), stroke_width=0.5, color=PINK))
        vect2 = always_redraw(lambda: Arrow3D(axes.get_origin(), dot2.get_center(), stroke_width=0.5, color=PINK))
        dot_start1=always_redraw(lambda : Dot3D(ce1.get_start(),color=RED))
        dot_start2=always_redraw(lambda : Dot3D(ce2.get_start(),color=YELLOW))
        vect_start1 = always_redraw(lambda: Arrow3D(axes.get_origin(), dot_start1.get_center(), stroke_width=0.5, color=PINK))
        vect_start2 = always_redraw(lambda: Arrow3D(axes.get_origin(), dot_start2.get_center(), stroke_width=0.5, color=PINK))

        # self.add(numberplane, axes, ce1, ce2, dot1, dot2)
        # self.wait()
        # self.play(head_tracker.animate.set_value(10), run_time=20, rate_func=rate_functions.linear)
        # self.wait()

        # self.add(numberplane, axes)
        # self.play(FadeIn(dot_start2,vect_start2))
        # self.wait()
        # self.play(FadeIn(ce2,dot2))
        # self.wait()
        # self.play(head_tracker.animate.set_value(10), run_time=10, rate_func=rate_functions.linear)
        # self.wait()

        # self.add(numberplane, axes, dot_start2, vect_start2, ce2, dot2)
        # self.play(FadeOut(dot2))
        # self.wait()

        self.add(numberplane, axes, ce2, vect_start2, dot_start2)
        self.wait()
        self.play(amp_tracker.animate.set_value(1.5))
        self.play(amp_tracker.animate.set_value(1))
        self.wait()

        self.play(phs_tracker.animate.set_value(2))
        self.play(phs_tracker.animate.set_value(0.8))
        self.wait()




        # self.add(axes,ce,dot)

        # self.play(Create(numberplane))
        # self.play(Create(axes))
        # self.wait()
        # self.play(Write(expTheta))
        # self.play(FadeIn(dot))
        # self.wait()
        # self.play(ReplacementTransform(expTheta[0].copy(),vect),ReplacementTransform(expTheta[2].copy(),theta))
        # self.wait()
        # self.play(ReplacementTransform(theta,expTheta[2]))
        # self.wait()

        # self.add(numberplane, axes, expTheta, vect, dot)
        # self.wait()
        # self.play(FadeOut(expTheta,vect),FadeIn(ce))
        # self.remove(dot)
        # self.add(dot)
        # self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.58, added_anims=[axes.x_axis.animate.rotate(90*DEGREES,[1,0,0])],run_time=2)
        # self.wait()

        # self.add(numberplane,axes,expTheta,vect,ce,dot)
        # self.wait()
        # self.play(FadeOut(vect))
        # self.play(head_tracker.animate.set_value(10), run_time=25,rate_func=rate_functions.linear)
        # self.wait()

        # self.add(numberplane, axes,ce, dot)
        # self.play(FadeOut(dot))
        # self.play(FadeIn(dot_start),FadeIn(vect_start))
        # self.play(phs_tracker.animate.set_value(6.28),run_time=4)
        # self.wait()
        # self.play(phs_tracker.animate.set_value(0.5), run_time=4)
        # self.wait()



class ComplexExp2(ThreeDScene):
        def construct(self):
            axes = ThreeDAxes(x_range=[-1.5, 1.5, 0.25], y_range=[0, 10.3, 2], z_range=[-1.5, 1.5, 0.25], x_length=9,
                              z_length=9, y_length=15)
            numberplane = NumberPlane(x_range=[-1.5, 1.5, 0.25], y_range=[-1.5, 1.5, 0.25], x_length=9, y_length=9,
                                      background_line_style={
                                          "stroke_color": BLUE,
                                          "stroke_width": 0.7,
                                          "stroke_opacity": 1, }).rotate(90 * DEGREES, RIGHT).move_to(axes.get_origin())
            # ___________________________________________________________________
            # self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.6)  # 3d view
            self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
            axes.y_axis.rotate(90*DEGREES,[0,1,0])
            axes.z_axis.rotate(-90*DEGREES,[0,0,1])
            # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000,
            #                             zoom=0.7)  # xz plane
            # axes.x_axis.rotate(90 * DEGREES, [1, 0, 0])
            # ___________________________________________________________________

            tvalue = ValueTracker(1)
            amp_tracker = ValueTracker(1)
            head_tracker = ValueTracker(10)
            ce1 = always_redraw(lambda: axes.plot_parametric_curve(
                lambda t: [np.real(np.exp(1j * (2 * np.pi * tvalue.get_value() * t))), t,
                           np.imag(np.exp(1j * (2 * np.pi * tvalue.get_value() * t)))], stroke_width=2, color=RED,
                t_range=np.array([0, head_tracker.get_value(), 0.01])))
            phs_tracker = ValueTracker(2)
            ce2 = always_redraw(lambda: axes.plot_parametric_curve(
                lambda t: [amp_tracker.get_value()*np.real(np.exp(1j * (2 * np.pi * tvalue.get_value() * t + phs_tracker.get_value()))), t,
                           amp_tracker.get_value()*np.imag(np.exp(1j * (2 * np.pi * tvalue.get_value() * t + phs_tracker.get_value())))],
                stroke_width=2, color=YELLOW, t_range=np.array([0, head_tracker.get_value(), 0.01])))
            dot1 = always_redraw(lambda: Dot3D(ce1.get_end(), color=RED).scale(1.5))
            dot2 = always_redraw(lambda: Dot3D(ce2.get_end(), color=YELLOW).scale(1.5))
            expTheta = MathTex(r'c \hspace{0.6 mm}', r'e^{j ', r'(wt+\phi) }').scale(1.2).rotate(90 * DEGREES,
                                                                                                 RIGHT).move_to(
                axes.c2p(1, 0, 1))
            theta = MathTex(r'\theta ', color=RED).rotate(90 * DEGREES, RIGHT).move_to(axes.c2p(0.25, 0, 0.1))
            expasfunoftime = MathTex(r'c \hspace{0.6 mm} e^{j(wt+\phi)}').rotate(90 * DEGREES, RIGHT).move_to(
                axes.c2p(1, 0, 1))
            expasfunoftimemoving = always_redraw(
                lambda: MathTex(r'c \hspace{0.6 mm} e^{j(w *  %0.1f +\phi)}' % tvalue.get_value()).rotate(90 * DEGREES,
                                                                                                          RIGHT).move_to(
                    axes.c2p(1, 0, 1)))
            euler_formula = MathTex(r'e^{j \omega  t} = cos(\omega  t)+j \hspace{0.7 mm} sin(\omega  t)')

            # vect = always_redraw(lambda: Arrow3D(axes.get_origin(), ce.get_points()[500], stroke_width=0.5, color=RED))
            vect1 = always_redraw(lambda: Arrow3D(axes.get_origin(), dot1.get_center(), stroke_width=0.5, color=PINK))
            vect2 = always_redraw(lambda: Arrow3D(axes.get_origin(), dot2.get_center(), stroke_width=0.5, color=PINK))
            dot_start1 = always_redraw(lambda: Dot3D(ce1.get_start(), color=RED))
            dot_start2 = always_redraw(lambda: Dot3D(ce2.get_start(), color=YELLOW))
            vect_start1 = always_redraw(
                lambda: Arrow3D(axes.get_origin(), dot_start1.get_center(), stroke_width=0.5, color=PINK))
            vect_start2 = always_redraw(
                lambda: Arrow3D(axes.get_origin(), dot_start2.get_center(), stroke_width=0.5, color=PINK))

            # self.add(numberplane, axes, ce1, ce2, dot1, dot2)
            # self.wait()
            # self.play(head_tracker.animate.set_value(10), run_time=20, rate_func=rate_functions.linear)
            # self.wait()

            self.add(numberplane, axes, ce2, vect_start2, dot_start2)
            self.wait()
            self.play(amp_tracker.animate.set_value(1.5))
            self.play(amp_tracker.animate.set_value(1))
            self.wait()

            self.play(phs_tracker.animate.set_value(2))
            self.play(phs_tracker.animate.set_value(0.8))
            self.wait()



            # self.add(axes,ce,dot)

            # self.play(Create(numberplane))
            # self.play(Create(axes))
            # self.wait()
            # self.play(Write(expTheta))
            # self.play(FadeIn(dot))
            # self.wait()
            # self.play(ReplacementTransform(expTheta[0].copy(),vect),ReplacementTransform(expTheta[2].copy(),theta))
            # self.wait()
            # self.play(ReplacementTransform(theta,expTheta[2]))
            # self.wait()

            # self.add(numberplane, axes, expTheta, vect, dot)
            # self.wait()
            # self.move_camera(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7,
            #                  added_anims=[axes.y_axis.animate.rotate(90 * DEGREES, [0, 1, 0]),axes.z_axis.animate.rotate(90 * DEGREES, [0, 0, 1])], run_time=2)
            # self.wait()
            # self.add(numberplane,axes,expTheta,vect,ce,dot)
            # self.wait()
            # self.play(FadeOut(vect))
            # self.play(head_tracker.animate.set_value(10), run_time=16,rate_func=rate_functions.linear)
            # self.wait()

            # self.add(numberplane, axes, expTheta, vect, dot)
            # self.wait()
            # self.play(FadeOut(expTheta, vect), FadeIn(ce))
            # self.remove(dot)
            # self.add(dot)
            #
            # self.play(head_tracker.animate.set_value(10), run_time=25, rate_func=rate_functions.linear)
            # self.wait()

            # self.add(numberplane, axes, ce, dot)
            # self.play(FadeOut(dot))
            # self.play(FadeIn(dot_start), FadeIn(vect_start))
            # self.play(phs_tracker.animate.set_value(6.28), run_time=4)
            # self.wait()
            # self.play(phs_tracker.animate.set_value(0.5), run_time=4)
            # self.wait()



class ComplexExp3(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes(x_range=[-1.5, 1.5, 0.25], y_range=[0, 10.3, 2], z_range=[-1.5, 1.5, 0.25], x_length=9, z_length=9, y_length=15)
        numberplane = NumberPlane(x_range=[-1.5, 1.5, 0.25], y_range=[-1.5, 1.5, 0.25], x_length=9, y_length=9,
                                  background_line_style={
                                      "stroke_color": BLUE,
                                      "stroke_width": 0.7,
                                      "stroke_opacity": 1,}).rotate(90 * DEGREES, RIGHT).move_to(axes.get_origin())
        #___________________________________________________________________
        # self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.6)  # 3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        # axes.y_axis.rotate(90*DEGREES,[0,1,0])
        # axes.z_axis.rotate(-90*DEGREES,[0,0,1])
        self.set_camera_orientation(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.4)
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.4)  # xz plane
        # axes.x_axis.rotate(90 * DEGREES, [1, 0, 0])
        #___________________________________________________________________

        tvalue = ValueTracker(1)
        head_tracker = ValueTracker(10)
        amp_tracker = ValueTracker(1)
        ce1 = always_redraw(lambda: axes.plot_parametric_curve(
            lambda t: [np.real(np.exp(1j * (2 * np.pi * tvalue.get_value() * t))), t,
                       np.imag(np.exp(1j * (2 * np.pi * tvalue.get_value() * t)))], stroke_width=2, color=RED,
            t_range=np.array([0, head_tracker.get_value(), 0.01])))
        phs_tracker = ValueTracker(0.8)
        ce2 = always_redraw(lambda: axes.plot_parametric_curve(
            lambda t: [amp_tracker.get_value()*np.real(np.exp(1j * (2 * np.pi * tvalue.get_value() * t + phs_tracker.get_value()))), t,
                       amp_tracker.get_value()*np.imag(np.exp(1j * (2 * np.pi * tvalue.get_value() * t + phs_tracker.get_value())))],
            stroke_width=2, color=YELLOW, t_range=np.array([0, head_tracker.get_value(), 0.01])))
        dot1 = always_redraw(lambda: Dot3D(ce1.get_end(), color=RED).scale(1.5))
        dot2 = always_redraw(lambda: Dot3D(ce2.get_end(), color=YELLOW).scale(1.5))
        expTheta = MathTex(r'c \hspace{0.6 mm}', r'e^{j ', r'(wt+\phi) }').scale(1.2).rotate(90 * DEGREES,
                                                                                             RIGHT).move_to(
            axes.c2p(1, 0, 1))
        theta = MathTex(r'\theta ', color=RED).rotate(90 * DEGREES, RIGHT).move_to(axes.c2p(0.25, 0, 0.1))
        expasfunoftime = MathTex(r'c \hspace{0.6 mm} e^{j(wt+\phi)}').rotate(90 * DEGREES, RIGHT).move_to(
            axes.c2p(1, 0, 1))
        expasfunoftimemoving = always_redraw(
            lambda: MathTex(r'c \hspace{0.6 mm} e^{j(w *  %0.1f +\phi)}' % tvalue.get_value()).rotate(90 * DEGREES,
                                                                                                      RIGHT).move_to(
                axes.c2p(1, 0, 1)))
        euler_formula = MathTex(r'e^{j \omega  t} = cos(\omega  t)+j \hspace{0.7 mm} sin(\omega  t)')

        # vect = always_redraw(lambda: Arrow3D(axes.get_origin(), ce.get_points()[500], stroke_width=0.5, color=RED))
        vect1 = always_redraw(lambda: Arrow3D(axes.get_origin(), dot1.get_center(), stroke_width=0.5, color=PINK))
        vect2 = always_redraw(lambda: Arrow3D(axes.get_origin(), dot2.get_center(), stroke_width=0.5, color=PINK))
        dot_start1 = always_redraw(lambda: Dot3D(ce1.get_start(), color=RED))
        dot_start2 = always_redraw(lambda: Dot3D(ce2.get_start(), color=YELLOW))
        vect_start1 = always_redraw(
            lambda: Arrow3D(axes.get_origin(), dot_start1.get_center(), stroke_width=0.5, color=PINK))
        vect_start2 = always_redraw(
            lambda: Arrow3D(axes.get_origin(), dot_start2.get_center(), stroke_width=0.5, color=PINK))

        # self.add(numberplane, axes, ce1, ce2, dot1, dot2)
        # self.wait()
        # self.play(head_tracker.animate.set_value(10), run_time=20, rate_func=rate_functions.linear)
        # self.wait()

        # self.add(numberplane, axes)
        # self.play(FadeIn(dot_start2, vect_start2))
        # self.wait()
        # self.play(FadeIn(ce2, dot2))
        # self.wait()
        # self.play(head_tracker.animate.set_value(10), run_time=10, rate_func=rate_functions.linear)
        # self.wait()

        # self.add(numberplane,axes,dot_start2,vect_start2,ce2,dot2)
        # self.play(FadeOut(dot2))
        # self.wait()

        self.add(numberplane, axes, ce2, vect_start2, dot_start2)
        self.wait()
        self.play(amp_tracker.animate.set_value(1.5))
        self.play(amp_tracker.animate.set_value(1))
        self.wait()

        self.play(phs_tracker.animate.set_value(2))
        self.play(phs_tracker.animate.set_value(0.8))
        self.wait()



        # self.add(axes,ce,dot)

        # self.play(Create(numberplane))
        # self.play(Create(axes))
        # self.wait()
        # self.play(Write(expTheta))
        # self.play(FadeIn(dot))
        # self.wait()
        # self.play(ReplacementTransform(expTheta[0].copy(),vect),ReplacementTransform(expTheta[2].copy(),theta))
        # self.wait()
        # self.play(ReplacementTransform(theta,expTheta[2]))
        # self.wait()

        # self.add(numberplane, axes, expTheta, vect, dot)
        # self.wait()
        # self.move_camera(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.4  , added_anims=[axes.x_axis.animate.rotate(90*DEGREES,[1,0,0])],run_time=2)
        # self.wait()
        # self.add(numberplane,axes,expTheta,vect,ce,dot)
        # self.wait()
        # self.play(FadeOut(vect))
        # self.play(head_tracker.animate.set_value(10), run_time=16,rate_func=rate_functions.linear)
        # self.wait()

        # self.add(numberplane, axes, expTheta, vect, dot)
        # self.wait()
        # self.play(FadeOut(expTheta, vect), FadeIn(ce))
        # self.remove(dot)
        # self.add(dot)
        # self.play(head_tracker.animate.set_value(10), run_time=25, rate_func=rate_functions.linear)
        # self.wait()
        # self.add(axes)

        # self.add(numberplane, axes, ce, dot)
        # self.play(FadeOut(dot))
        # self.play(FadeIn(dot_start), FadeIn(vect_start))
        # self.play(phs_tracker.animate.set_value(6.28), run_time=4)
        # self.wait()
        # self.play(phs_tracker.animate.set_value(0.5), run_time=4)
        # self.wait()

class ComplexExp4(ThreeDScene):
        def construct(self):
            axes = ThreeDAxes(x_range=[-1.5, 1.5, 0.25], y_range=[0, 10.3, 2], z_range=[-1.5, 1.5, 0.25], x_length=9,
                              z_length=9, y_length=15)
            numberplane = NumberPlane(x_range=[-1.5, 1.5, 0.25], y_range=[-1.5, 1.5, 0.25], x_length=9, y_length=9,
                                      background_line_style={
                                          "stroke_color": BLUE,
                                          "stroke_width": 0.7,
                                          "stroke_opacity": 1, }).rotate(90 * DEGREES, RIGHT).move_to(axes.get_origin())
            # ___________________________________________________________________
            # self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.58)  # 3d view
            # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
            # axes.y_axis.rotate(90*DEGREES,[0,1,0])
            # axes.z_axis.rotate(-90*DEGREES,[0,0,1])
            self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7)  # xz plane
            axes.x_axis.rotate(90 * DEGREES, [1, 0, 0])
            # ___________________________________________________________________

            tvalue = ValueTracker(1)
            head_tracker = ValueTracker(10)
            amp_tracker = ValueTracker(1)
            amp_tracker=ValueTracker(1)
            ce1 = always_redraw(lambda: axes.plot_parametric_curve(
                lambda t: [np.real(np.exp(1j * (2 * np.pi * tvalue.get_value() * t))), t,
                           np.imag(np.exp(1j * (2 * np.pi * tvalue.get_value() * t)))], stroke_width=2, color=RED,
                t_range=np.array([0, head_tracker.get_value(), 0.01])))
            phs_tracker = ValueTracker(0.8)
            ce2 = always_redraw(lambda: axes.plot_parametric_curve(
                lambda t: [amp_tracker.get_value()*np.real(np.exp(1j * (2 * np.pi * tvalue.get_value() * t + phs_tracker.get_value()))), t,
                           amp_tracker.get_value()*np.imag(np.exp(1j * (2 * np.pi * tvalue.get_value() * t + phs_tracker.get_value())))],
                stroke_width=2, color=YELLOW, t_range=np.array([0, head_tracker.get_value(), 0.01])))
            dot1 = always_redraw(lambda: Dot3D(ce1.get_end(), color=RED).scale(1.5))
            dot2 = always_redraw(lambda: Dot3D(ce2.get_end(), color=YELLOW).scale(1.5))
            expTheta = MathTex(r'c \hspace{0.6 mm}', r'e^{j ', r'(wt+\phi) }').scale(1.2).rotate(90 * DEGREES,
                                                                                                 RIGHT).move_to(
                axes.c2p(1, 0, 1))
            theta = MathTex(r'\theta ', color=RED).rotate(90 * DEGREES, RIGHT).move_to(axes.c2p(0.25, 0, 0.1))
            expasfunoftime = MathTex(r'c \hspace{0.6 mm} e^{j(wt+\phi)}').rotate(90 * DEGREES, RIGHT).move_to(
                axes.c2p(1, 0, 1))
            expasfunoftimemoving = always_redraw(
                lambda: MathTex(r'c \hspace{0.6 mm} e^{j(w *  %0.1f +\phi)}' % tvalue.get_value()).rotate(90 * DEGREES,
                                                                                                          RIGHT).move_to(
                    axes.c2p(1, 0, 1)))
            euler_formula = MathTex(r'e^{j \omega  t} = cos(\omega  t)+j \hspace{0.7 mm} sin(\omega  t)')

            # vect = always_redraw(lambda: Arrow3D(axes.get_origin(), ce.get_points()[500], stroke_width=0.5, color=RED))
            vect1 = always_redraw(lambda: Arrow3D(axes.get_origin(), dot1.get_center(), stroke_width=0.5, color=PINK))
            vect2 = always_redraw(lambda: Arrow3D(axes.get_origin(), dot2.get_center(), stroke_width=0.5, color=PINK))
            dot_start1 = always_redraw(lambda: Dot3D(ce1.get_start(), color=RED))
            dot_start2 = always_redraw(lambda: Dot3D(ce2.get_start(), color=YELLOW))
            vect_start1 = always_redraw(
                lambda: Arrow3D(axes.get_origin(), dot_start1.get_center(), stroke_width=0.5, color=PINK))
            vect_start2 = always_redraw(
                lambda: Arrow3D(axes.get_origin(), dot_start2.get_center(), stroke_width=0.5, color=PINK))

            # self.add(numberplane, axes, ce1, ce2, dot1, dot2)
            # self.wait()
            # self.play(head_tracker.animate.set_value(10), run_time=20, rate_func=rate_functions.linear)
            # self.wait()

            # self.add(numberplane, axes)
            # self.play(FadeIn(dot_start2, vect_start2))
            # self.wait()
            # self.play(FadeIn(ce2, dot2))
            # self.wait()
            # self.play(head_tracker.animate.set_value(10), run_time=10, rate_func=rate_functions.linear)
            # self.wait()

            # self.add(numberplane, axes, dot_start2, vect_start2, ce2, dot2)
            # self.play(FadeOut(dot2))
            # self.wait()



            self.add(numberplane, axes, ce2, vect_start2, dot_start2)
            self.wait()
            self.play(amp_tracker.animate.set_value(1.5))
            self.play(amp_tracker.animate.set_value(1))
            self.wait()

            self.play(phs_tracker.animate.set_value(2))
            self.play(phs_tracker.animate.set_value(0.8))
            self.wait()




            # self.add(axes,ce,dot)

            # self.play(Create(numberplane))
            # self.play(Create(axes))
            # self.wait()
            # self.play(Write(expTheta))
            # self.play(FadeIn(dot))
            # self.wait()
            # self.play(ReplacementTransform(expTheta[0].copy(),vect),ReplacementTransform(expTheta[2].copy(),theta))
            # self.wait()
            # self.play(ReplacementTransform(theta,expTheta[2]))
            # self.wait()



            # self.add(numberplane, axes, expTheta, vect, dot)
            # self.wait()
            # self.play(FadeOut(expTheta, vect), FadeIn(ce))
            # self.remove(dot)
            # self.add(dot)
            # self.play(head_tracker.animate.set_value(10), run_time=25, rate_func=rate_functions.linear)
            # self.wait()

            # self.add(numberplane, axes, ce, dot)
            # self.play(FadeOut(dot))
            # self.play(FadeIn(dot_start), FadeIn(vect_start))
            # self.play(phs_tracker.animate.set_value(6.28), run_time=4)
            # self.wait()
            # self.play(phs_tracker.animate.set_value(0.5), run_time=4)
            # self.wait()



class CosAndSin(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes(x_range=[-1.5, 1.5, 0.25], y_range=[0, 10.3, 2], z_range=[-1.5, 1.5, 0.25], x_length=9, z_length=9, y_length=15)
        numberplane = NumberPlane(x_range=[-1.5, 1.5, 0.25], y_range=[-1.5, 1.5, 0.25], x_length=9, y_length=9,
                                  background_line_style={
                                      "stroke_color": BLUE,
                                      "stroke_width": 0.7,
                                      "stroke_opacity": 1,}).rotate(90 * DEGREES, RIGHT).move_to(axes.get_origin())
        #___________________________________________________________________
        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.4)  # 3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        # axes.y_axis.rotate(90*DEGREES,[0,1,0])
        # axes.z_axis.rotate(-90*DEGREES,[0,0,1])
        # self.set_camera_orientation(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.4)
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.4)  # xz plane
        # axes.x_axis.rotate(90 * DEGREES, [1, 0, 0])
        #___________________________________________________________________

        tvalue = ValueTracker(1)

        ce = always_redraw(lambda: axes.plot_parametric_curve(
            lambda t: [np.real(np.exp(1j * (2 * np.pi * tvalue.get_value() * t))), t,
                       np.imag(np.exp(1j * (2 * np.pi * tvalue.get_value() * t)))], stroke_width=2, color=YELLOW,
            t_range=np.array([0, 10, 0.01])))

        xyplan=TheSiGuy_lib.xy_plane(axes)

        self.add(numberplane,xyplan,axes,ce)

        # self.wait()
        # self.move_camera(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.4,run_time=3)
        # self.wait()

        self.wait()
        self.move_camera(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.4,added_anims=[axes.y_axis.animate.rotate(90*DEGREES,[0,1,0]),axes.z_axis.animate.rotate(-90*DEGREES,[0,0,1])],run_time=3)
        self.wait()




class SetOfAxes(Scene):
    def construct(self):
        angle=ValueTracker(0)
        x_cos=Arrow([-1,0,0],[4,0,0],stroke_width=2,max_tip_length_to_length_ratio=0.055)
        y_sin=Arrow([0,1,0],[0,-4,0],stroke_width=2,max_tip_length_to_length_ratio=0.055)

        arr=always_redraw(lambda : Arrow([0,0,0],[2,0,0],color=RED,buff=0,max_tip_length_to_length_ratio=0.12).rotate(angle.get_value()*DEGREES,about_point=[0,0,0]))

        # self.add(x_cos,y_sin,arr)
        self.play(Create(x_cos))
        self.play(Create(y_sin))
        self.wait()
        self.add(arr)

        self.play(angle.animate.set_value(-90),run_time=2)
        self.wait()
        # self.remove(arr)
        # angle.set_value(0)
        # self.add(arr)
        # self.wait()
        self.play(angle.animate.set_value(90),run_time=2)
        self.wait()
        # self.remove(arr)
        # angle.set_value(90)
        # self.add(arr)
        # self.wait()
        self.play(angle.animate.set_value(0), run_time=2)
        self.wait()





class Equations1(Scene):
    def construct(self):
        tvalue=ValueTracker(0.01)
        expasfunoftimemoving = always_redraw(lambda: MathTex(r'c \hspace{0.6 mm} e^{j(w *  %0.01f +\phi)}' % tvalue.get_value()))
        expasfunoftimemoving_rect=SurroundingRectangle(expasfunoftimemoving,GOLD,MED_SMALL_BUFF,stroke_width=1.5)
        euler_formula = MathTex(r'e^{j (\omega  t + \phi)} = cos(\omega  t + \phi)+j \hspace{0.7 mm} sin(\omega  t+ \phi)')

        # self.add(expasfunoftimemoving)
        # self.wait()
        # self.play(Create(expasfunoftimemoving_rect),run_time=1)
        # self.play(tvalue.animate.set_value(10), run_time=25, rate_func=rate_functions.linear)
        # self.wait()
        self.play(Write(euler_formula))
        self.wait()

class Equations2(Scene):
    def construct(self):
        euler_formula = MathTex(r'v_{m} \hspace{0.7 mm} e^{j (\omega  t + \phi)} = v_{m} \hspace{0.7 mm} cos(\omega  t + \phi)+j \hspace{1 mm} v_{m}  \hspace{0.7 mm} sin(\omega  t+ \phi)').shift(2.8*UP)
        euler_formula[0][0:2].set_color(RED)
        euler_formula[0][11:13].set_color(RED)
        euler_formula[0][24:26].set_color(RED)
        euler_formula[0][8].set_color(BLUE)
        euler_formula[0][20].set_color(BLUE)
        euler_formula[0][33].set_color(BLUE)
        euler_formula_2=MathTex(r'v_{m} \hspace{0.7 mm} cos(\omega  t + \phi) = Re(v_{m} \hspace{0.7 mm} e^{j (\omega  t + \phi)})').shift(1.5*UP)
        euler_formula_2[0][0:2].set_color(RED)
        euler_formula_2[0][15:17].set_color(RED)
        euler_formula_2[0][9].set_color(BLUE)
        euler_formula_2[0][23].set_color(BLUE)
        euler_formula_3 = MathTex(r'v_{m} \hspace{0.7 mm} cos(\omega  t + \phi) =Re(\hspace{0.7 mm} v_{m} \hspace{0.7 mm} e^{j \phi} \hspace{1 mm} e^{j \omega  t} \hspace{0.7 mm})').shift(0.2 * UP)
        euler_formula_3[0][0:2].set_color(RED)
        euler_formula_3[0][15:17].set_color(RED)
        euler_formula_3[0][9].set_color(BLUE)
        euler_formula_3[0][19].set_color(BLUE)
        t_cross=Cross(euler_formula_3[0][20:24],stroke_width=1.5)

        phasor_rect=SurroundingRectangle(euler_formula_3[0][15:20])
        phasor_angl_phs=MathTex(r'v_{m} \hspace{0.7 mm} \angle \phi').shift(1.2 * DOWN)
        phasor_angl_phs[0][0:2].set_color(RED)
        phasor_angl_phs[0][2:4].set_color(BLUE)





        # self.add(euler_formula)\

        # self.play(Write(euler_formula),run_time=3)
        # self.wait()
        # self.play(ReplacementTransform(euler_formula[0][11:22].copy(),euler_formula_2[0][0:11]))
        # self.play(Write(euler_formula_2[0][11:15]),rate_func=rate_functions.linear)
        # self.play(Write(euler_formula_2[0][25]),run_time=0.01,rate_func=rate_functions.linear)
        # self.wait()
        # self.play(ReplacementTransform(euler_formula[0][0:10].copy(),euler_formula_2[0][15:25]))
        # self.wait()
        # self.play(ReplacementTransform(euler_formula_2[0][0:15].copy(),euler_formula_3[0][0:15]),ReplacementTransform(euler_formula_2[0][25].copy(),euler_formula_3[0][24]))
        # self.wait()
        # self.play(ReplacementTransform(euler_formula_2[0][15:25].copy(),euler_formula_3[0][15:24]))
        # self.wait()

        # self.add(euler_formula[0][0:2])
        # self.add(euler_formula[0][8])
        # self.add(euler_formula[0][11:13])
        # self.add(euler_formula[0][20])
        # self.add(euler_formula[0][24:26])

        # self.add(euler_formula_2[0][0:2])
        # self.add(euler_formula_2[0][9])
        # self.add(euler_formula_2[0][15:17])
        # self.add(euler_formula_2[0][23])

        # self.add(euler_formula_2[0][0:11])
        # self.add(euler_formula[0][11:22])
        # self.add(euler_formula_2[0][11:15])
        # self.add(euler_formula_2[0][25])
        # self.add(euler_formula_2[0][15:25])
        # self.add(euler_formula[0][0:10])

        # self.add(euler_formula,euler_formula_2,euler_formula_3)
        # self.add(euler_formula_3[0][0:2])
        # self.add(euler_formula_3[0][9])
        # self.add(euler_formula_3[0][15:17])
        # self.add(euler_formula_3[0][15:20])
        # self.add(euler_formula_2[0][0:15])
        # self.add(euler_formula_2[0][25])
        # self.add(euler_formula_3[0][0:15])
        # self.add(euler_formula_3[0][24])

        # self.add(euler_formula,euler_formula_2,euler_formula_3)
        # self.add(euler_formula_3[0][19])
        # self.add(euler_formula_3[0][15:17])
        # self.add(phasor_angl_phs)

        # self.add(euler_formula_3, euler_formula_2, euler_formula)


        # self.add(euler_formula_3[0][15:20].animate.shift(0.5*RIGHT))

        # self.play(Write(euler_formula_3[0][0:11]))
        # self.wait()
        # self.play(Write(euler_formula_3[0][11:25]))
        # self.wait()
        # self.play(Create(t_cross))
        # self.play(FadeOut(t_cross),FadeOut(euler_formula_3[0][20:24]))
        # self.play(euler_formula_3[0][15:20].animate.shift(0.5*RIGHT))
        # self.wait()
        # self.play(ReplacementTransform(euler_formula_3[0][15:17].copy(), phasor_angl_phs[0:2]),
        #           ReplacementTransform(euler_formula_3[0][19].copy(), phasor_angl_phs[0][2:4]))
        # self.wait()


class Equations3(Scene):
    def construct(self):
        eq1=MathTex(r'\frac{d v}{d t}' , r'\quad  \Leftrightarrow  \quad' ,r' j \omega \mathbf{V}')
        eq2=MathTex(r'\int v d t', r' \quad \Leftrightarrow \quad' , r'\frac{\mathbf{V}}{j \omega}').shift(2*DOWN)

        eq1[0].set_color(RED)
        eq2[0].set_color(RED)
        eq1[2].set_color(BLUE)
        eq2[2].set_color(BLUE)

        self.play(Write(eq1))
        self.wait()
        self.play(Write(eq2))
        self.wait()



        # self.add(eq2,eq1)

class Equations3(Scene):
    def construct(self):
        self.camera.background_color = "#101010"
        # arr=Arrow([0,0,0],[0,-1.5,0],buff=0,stroke_width=8,max_tip_length_to_length_ratio=0.2,color=RED)
        # i_ = MathTex(r'i',color=RED).scale(3).next_to(arr,RIGHT)
        # self.add(i_,arr)

        # icos=MathTex(r'i=I_{m}  \hspace{0.1 mm} \cos (\omega t+\phi)',color=RED).scale(2)
        # self.play(Write(icos))
        # self.wait()

        # v_ = MathTex(r'v', color=YELLOW).scale(3)
        # p_=MathTex(r'+',color=YELLOW).scale(2).shift(3*UP)
        # n_=MathTex(r'-',color=YELLOW).scale(2).shift(3*DOWN)
        # self.add(v_,p_,n_)

        # vcos = MathTex(r'v=i R=R I_m \cos (\omega t+\phi)', color=YELLOW).scale(2)
        # self.play(Write(vcos))
        # self.wait()

        # iv_phsr=MathTex(r'\mathbf{I}=I_m \angle \phi  \hspace{2 mm}',r',' , r'\hspace{5 mm} \mathbf{V}=R I_m \angle \phi')
        # iv_phsr[0].set_color(RED)
        # iv_phsr[2].set_color(YELLOW)
        # self.play(Write(iv_phsr))
        # self.wait()

        # v_cap=MathTex(r'v=L \frac{d i}{d t}',color=YELLOW)
        # self.play(Write(v_cap))
        # self.wait()

        v_cap_phsr = MathTex(r'\mathbf{V}=j \omega L \mathbf{I}=j \omega L I_m \angle \phi', color=YELLOW)
        # self.play(Write(v_cap_phsr))
        # self.wait()

        j_ = MathTex(r'j=e^{j  \hspace{0.4 mm} 90^{\circ}}= \angle  \hspace{0.5 mm} 90^{\circ}').next_to(v_cap_phsr,2*DOWN)
        # self.play(Write(j_))
        # self.wait()

        v_cap_fnl = MathTex(r' \mathbf{V}=\omega L I_m   \hspace{1 mm} \angle  \hspace{1 mm} (\phi+90^{\circ})', color=YELLOW).next_to(j_,2*DOWN)
        # self.play(Write(v_cap_fnl))
        # self.wait()

        # self.add(v_cap_phsr[0][7])
        # self.add(v_cap_fnl[0][10:13])
        # self.add(v_cap_fnl[0][1:10])
        # self.add(v_cap_fnl[0][13])
        # self.add(j_[0][9:11])

        self.play(Write(v_cap_phsr))
        self.wait()
        self.play(ReplacementTransform(v_cap_phsr[0][7].copy(),j_[0][0]))
        self.play(Write(j_[0][1:]))
        self.wait()
        self.play(ReplacementTransform(v_cap_phsr[0][0].copy(),v_cap_fnl[0][0]))
        self.play(Write(v_cap_fnl[0][1:10]))
        self.add(v_cap_fnl[0][13])
        self.wait(0.3)
        self.play(ReplacementTransform(j_[0][9:11].copy(),v_cap_fnl[0][10:13]))
        self.wait()



class Equations4(Scene):
    def construct(self):
        self.camera.background_color = "#101010"

        vcos=MathTex(r'v=V_{m}  \hspace{0.1 mm} \cos (\omega t+\phi)',color=YELLOW).shift(3*UP)
        vphs=MathTex(r'\mathbf{V} = V_m   \hspace{0.5 mm} \angle \phi',color=YELLOW).shift(1.8*UP)
        icap=MathTex(r'i=C \frac{d v}{d t}',color=RED).shift(0.6*UP)
        iphs=MathTex(r'\mathbf{I}=j \omega C \mathbf{V}',color=RED).shift(0.6*DOWN)
        vfnl = MathTex(r'\mathbf{V}=\frac{\mathbf{I}}{j \omega C}', color=YELLOW).shift(1.8*DOWN)
        vlag=MathTex(r'\mathbf{V}=\frac{I_{m}\angle  \hspace{1 mm} (\phi-90^{\circ})}{\omega C}',color=YELLOW).shift(3.3*DOWN)

        # self.play(Write(vcos),Write(vphs))
        # self.wait()
        # self.play(Write(icap))
        # self.wait()
        # self.play(ReplacementTransform(icap[0][0].copy(),iphs[0][0]))
        # self.add(iphs[0][1])
        # self.play(ReplacementTransform(icap[0][2].copy(), iphs[0][4]))
        # self.play(ReplacementTransform(icap[0][3:8].copy(), iphs[0][2:4]),ReplacementTransform(icap[0][3:8].copy(), iphs[0][5]))
        # self.wait()
        # self.play(ReplacementTransform(iphs[0][5].copy(),vfnl[0][0]))
        # self.play(FadeIn(vfnl[0][1]),FadeIn(vfnl[0][3]))
        # self.play(ReplacementTransform(iphs[0][0].copy(),vfnl[0][2]))
        # self.play(ReplacementTransform(iphs[0][2:5].copy(),vfnl[0][4:7]))
        #
        # self.wait()


        # self.add(vcos,vphs,icap,iphs,vfnl)
        # self.add(iphs[0][2:4],iphs[0][5])
        # self.add(icap[0][3:8])
        # self.add(iphs[0][5])
        # self.add(vfnl[0][3],vfnl[0][1])

        # self.add(vcos,vphs,icap,iphs,vfnl,vlag)



        self.add(vcos,vphs,icap,iphs,vfnl)
        self.play(ReplacementTransform(vfnl[0][0:2].copy(),vlag[0][0:2]))
        self.play(FadeIn(vlag[0][12]))
        self.play(ReplacementTransform(vfnl[0][2].copy(),vlag[0][2:7]))
        self.play(ReplacementTransform(vfnl[0][4].copy(), vlag[0][7:11]))
        self.add(vlag[0][11])
        self.play(ReplacementTransform(vfnl[0][5:7].copy(),vlag[0][13:15]))
        self.wait()



        # self.add(vlag[0][2:7],vlag[0][11])
        # self.add(vfnl[0][5:7],vlag[0][13:15])





class Equations5(Scene):
    def construct(self):

        rlc1=MathTex(r'\mathbf{V}=R \mathbf{I}, \quad \mathbf{V}=j \omega L \mathbf{I}, \quad \mathbf{V}=\frac{\mathbf{I}}{j \omega C}').shift(2*UP)
        rlc1[0][2].set_color(BLUE)
        rlc1[0][7:10].set_color(BLUE)
        rlc1[0][16:19].set_color(BLUE)
        rlc1[0][0].set_color(YELLOW)
        rlc1[0][5].set_color(YELLOW)
        rlc1[0][12].set_color(YELLOW)
        rlc1[0][3].set_color(RED)
        rlc1[0][10].set_color(RED)
        rlc1[0][14].set_color(RED)

        rlc2=MathTex(r'\frac{\mathbf{V}}{\mathbf{I}}=R, \quad \frac{\mathbf{V}}{\mathbf{I}}=j \omega L, \quad \frac{\mathbf{V}}{\mathbf{I}}=\frac{1}{j \omega C}')
        rlc2[0][4].set_color(BLUE)
        rlc2[0][10:13].set_color(BLUE)
        rlc2[0][20:23].set_color(BLUE)
        rlc2[0][0].set_color(YELLOW)
        rlc2[0][6].set_color(YELLOW)
        rlc2[0][14].set_color(YELLOW)
        rlc2[0][2].set_color(RED)
        rlc2[0][8].set_color(RED)
        rlc2[0][16].set_color(RED)


        impedance=MathTex(r'\mathbf{Z}=R+j X',color=BLUE).scale(1).shift(1.5*DOWN)

        admittance=MathTex(r'\mathbf{Y}=\frac{1}{\mathbf{Z}}=\frac{\mathbf{I}}{\mathbf{V}}')
        admittance2=MathTex(r'\mathbf{Y}=G+j B',color=GOLD).shift(1.7*DOWN)

        admittance[0][0].set_color(GOLD)
        admittance[0][4].set_color(BLUE)
        admittance[0][6].set_color(RED)
        admittance[0][8].set_color(YELLOW)

        self.play(Write(admittance))
        self.wait()
        self.play(ReplacementTransform(admittance[0][0].copy(),admittance2))
        self.wait()

        # self.add(admittance)
        # self.wait()

        # self.play(Write(impedance))
        # self.wait()
        # self.add(rlc1,rlc2)
        # self.wait()
        #
        # self.play(ReplacementTransform(rlc2[0][4].copy(),impedance),ReplacementTransform(rlc2[0][10:13].copy(),impedance),ReplacementTransform(rlc2[0][20:23].copy(),impedance))
        #
        # self.wait()
        # self.add(impedance)

        # self.add(rlc1,rlc2)
        # self.add(rlc2[0][1],rlc2[0][7],rlc2[0][15])

        # self.play(Write(rlc1))
        # self.wait()
        # self.add(rlc1)


        # self.play(Write(rlc1))
        # self.wait(0.3)
        #
        # # self.add(rlc2[0][1], rlc2[0][7], rlc2[0][15])
        # self.play(FadeIn(rlc2[0][1]),FadeIn(rlc2[0][7]),FadeIn(rlc2[0][15]))
        # self.wait()
        # self.play(ReplacementTransform(rlc1[0][0].copy(),rlc2[0][0]),ReplacementTransform(rlc1[0][5].copy(),rlc2[0][6]),ReplacementTransform(rlc1[0][12].copy(),rlc2[0][14]))
        # self.play(ReplacementTransform(rlc1[0][3].copy(),rlc2[0][2]),ReplacementTransform(rlc1[0][10].copy(),rlc2[0][8]),ReplacementTransform(rlc1[0][14].copy(),rlc2[0][16]))
        # self.add(rlc2[0][3],rlc2[0][9],rlc2[0][17],rlc2[0][18:20])
        # self.play(ReplacementTransform(rlc1[0][2].copy(), rlc2[0][4]),
        #           ReplacementTransform(rlc1[0][7:10].copy(), rlc2[0][10:13]),
        #           ReplacementTransform(rlc1[0][16:19].copy(), rlc2[0][20:23]))
        # self.add(rlc2[0][5],rlc2[0][13],rlc2[0][5])
        # self.wait()

class Addition(ThreeDScene):
        def construct(self):
            axes = ThreeDAxes(x_range=[-1.5, 1.5, 0.25], y_range=[0, 10.3, 2], z_range=[-1.5, 1.5, 0.25], x_length=9,
                              z_length=9, y_length=15)
            numberplane = NumberPlane(x_range=[-1.5, 1.5, 0.25], y_range=[-1.5, 1.5, 0.25], x_length=9, y_length=9,
                                      background_line_style={
                                          "stroke_color": BLUE,
                                          "stroke_width": 0.7,
                                          "stroke_opacity": 1, }).rotate(90 * DEGREES, RIGHT).move_to(axes.get_origin())
            # ___________________________________________________________________
            self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.58)  # 3d view
            # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
            # axes.y_axis.rotate(90*DEGREES,[0,1,0])
            # axes.z_axis.rotate(-90*DEGREES,[0,0,1])
            # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7)  # xz plane
            # axes.x_axis.rotate(90 * DEGREES, [1, 0, 0])
            # ___________________________________________________________________

            # 0.7*np.exp(1j * (2 * np.pi *0.5 * t+0.4)

            tvalue = ValueTracker(1)
            head_tracker = ValueTracker(0.01)
            amp_tracker = ValueTracker(1)
            cet = always_redraw(lambda: axes.plot_parametric_curve(lambda t: [np.real(0.8*np.exp(1j * (2 * np.pi *0.5 * t+0.4)) + 0.5*np.exp(1j * (2 * np.pi *0.5 * t+1)) ), t, np.imag(0.8*np.exp(1j * (2 * np.pi *0.5 * t+0.4)) + 0.5*np.exp(1j * (2 * np.pi *0.5 * t+1)))], stroke_width=2, color=RED,t_range=np.array([0, head_tracker.get_value(), 0.1])))
            ce1 = always_redraw(lambda: axes.plot_parametric_curve(lambda t: [np.real(0.8*np.exp(1j * (2 * np.pi *0.5 * t+0.4))  ), t, np.imag(0.8*np.exp(1j * (2 * np.pi *0.5 * t+0.4)) )], stroke_width=2, color=BLUE,t_range=np.array([0, head_tracker.get_value(), 0.1])).set_opacity(0))
            ce2 = always_redraw(lambda: axes.plot_parametric_curve(lambda t: [np.real(0.5 * np.exp(1j * (2 * np.pi * 1 * t + 1))), t, np.imag(0.5 * np.exp(1j * (2 * np.pi * 1 * t + 1)))],stroke_width=2, color=GREEN, t_range=np.array([0, head_tracker.get_value(), 0.1])).set_opacity(0))
            phs_tracker = ValueTracker(0.8)

            dot_t=always_redraw(lambda :Dot3D(cet.get_end(),color=RED))
            dot_1=always_redraw(lambda :Dot3D(ce1.get_end(),color=BLUE).set_opacity(0))
            dot_2=always_redraw(lambda :Dot3D(ce2.get_end(),color=GREEN).set_opacity(0))

            vect1 = always_redraw(lambda: Arrow3D(axes.c2p(0,head_tracker.get_value(),0), dot_1.get_center(), stroke_width=0.5, color=PINK))
            vect2 = always_redraw(lambda: Arrow3D(dot_1.get_center(), dot_t.get_center(), stroke_width=0.5, color=LIGHT_BROWN))



            # dot1 = always_redraw(lambda: Dot3D(ce1.get_end(), color=RED).scale(1.5))
            # dot2 = always_redraw(lambda: Dot3D(ce2.get_end(), color=YELLOW).scale(1.5))
            # expTheta = MathTex(r'c \hspace{0.6 mm}', r'e^{j ', r'(wt+\phi) }').scale(1.2).rotate(90 * DEGREES,
            #                                                                                      RIGHT).move_to(
            #     axes.c2p(1, 0, 1))
            # theta = MathTex(r'\theta ', color=RED).rotate(90 * DEGREES, RIGHT).move_to(axes.c2p(0.25, 0, 0.1))
            # expasfunoftime = MathTex(r'c \hspace{0.6 mm} e^{j(wt+\phi)}').rotate(90 * DEGREES, RIGHT).move_to(
            #     axes.c2p(1, 0, 1))
            # expasfunoftimemoving = always_redraw(
            #     lambda: MathTex(r'c \hspace{0.6 mm} e^{j(w *  %0.1f +\phi)}' % tvalue.get_value()).rotate(90 * DEGREES,
            #                                                                                               RIGHT).move_to(
            #         axes.c2p(1, 0, 1)))
            # euler_formula = MathTex(r'e^{j \omega  t} = cos(\omega  t)+j \hspace{0.7 mm} sin(\omega  t)')
            #
            # # vect = always_redraw(lambda: Arrow3D(axes.get_origin(), ce.get_points()[500], stroke_width=0.5, color=RED))
            # vect1 = always_redraw(lambda: Arrow3D(axes.get_origin(), dot1.get_center(), stroke_width=0.5, color=PINK))
            # vect2 = always_redraw(lambda: Arrow3D(axes.get_origin(), dot2.get_center(), stroke_width=0.5, color=PINK))
            # dot_start1 = always_redraw(lambda: Dot3D(ce1.get_start(), color=RED))
            # dot_start2 = always_redraw(lambda: Dot3D(ce2.get_start(), color=YELLOW))
            # vect_start1 = always_redraw(
            #     lambda: Arrow3D(axes.get_origin(), dot_start1.get_center(), stroke_width=0.5, color=PINK))
            # vect_start2 = always_redraw(
            #     lambda: Arrow3D(axes.get_origin(), dot_start2.get_center(), stroke_width=0.5, color=PINK))


            self.add(axes,cet,dot_1,dot_t,vect1,vect2,ce1,ce2,dot_1,dot_2)
            self.play(head_tracker.animate.set_value(10),run_time=10)
            self.wait()


class Addition2(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(x_range=[-1.5, 1.5, 0.25], y_range=[0, 10.3, 2], z_range=[-1.5, 1.5, 0.25], x_length=9,
                          z_length=9, y_length=15)
        numberplane = NumberPlane(x_range=[-1.5, 1.5, 0.25], y_range=[-1.5, 1.5, 0.25], x_length=9, y_length=9,
                                  background_line_style={
                                      "stroke_color": BLUE,
                                      "stroke_width": 0.7,
                                      "stroke_opacity": 1, }).rotate(90 * DEGREES, RIGHT).move_to(axes.get_origin())
        # ___________________________________________________________________
        # self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.58)  # 3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        # axes.y_axis.rotate(90*DEGREES,[0,1,0])
        # axes.z_axis.rotate(-90*DEGREES,[0,0,1])
        self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7)  # xz plane
        axes.x_axis.rotate(90 * DEGREES, [1, 0, 0])
        # ___________________________________________________________________

        # 0.7*np.exp(1j * (2 * np.pi *0.5 * t+0.4)

        tvalue = ValueTracker(1)
        head_tracker = ValueTracker(0.01)
        amp_tracker = ValueTracker(1)
        cet = always_redraw(lambda: axes.plot_parametric_curve(lambda t: [
            np.real(0.8 * np.exp(1j * (2 * np.pi * 0.5 * t + 0.4)) + 0.5 * np.exp(1j * (2 * np.pi * 1 * t + 1))), t,
            np.imag(0.8 * np.exp(1j * (2 * np.pi * 0.5 * t + 0.4)) + 0.5 * np.exp(1j * (2 * np.pi * 1 * t + 1)))],
                                                               stroke_width=2, color=RED,
                                                               t_range=np.array([0, head_tracker.get_value(), 0.1])))
        dot_t = always_redraw(lambda: Dot3D(cet.get_end(), color=RED))
        ce1 = always_redraw(lambda: axes.plot_parametric_curve(
            lambda t: [np.real(0.8 * np.exp(1j * (2 * np.pi * 0.5 * t + 0.4))), t,
                       np.imag(0.8 * np.exp(1j * (2 * np.pi * 0.5 * t + 0.4)))], stroke_width=2, color=BLUE,
            t_range=np.array([0, head_tracker.get_value(), 0.1])).set_opacity(0))
        dot_1 = always_redraw(lambda: Dot3D(ce1.get_end(), color=BLUE).set_opacity(0))

        ce2 = always_redraw(lambda: axes.plot_parametric_curve(
            lambda t: [np.real(0.5 * np.exp(1j * (2 * np.pi * 0.5 * t + 1)))+axes.p2c(dot_1.get_center())[0], t,
                       np.imag(0.5 * np.exp(1j * (2 * np.pi * 0.5 * t + 1)))+axes.p2c(dot_1.get_center())[2]], stroke_width=2, color=GREEN,
            t_range=np.array([0, head_tracker.get_value(), 0.1])).set_opacity(0))
        dot_2 = always_redraw(lambda: Dot3D(ce2.get_end(), color=GREEN).set_opacity(0))






        vect1 = always_redraw(
            lambda: Arrow3D(axes.c2p(0, head_tracker.get_value(), 0), dot_1.get_center(), stroke_width=0.5, color=PINK))
        vect2 = always_redraw(
            lambda: Arrow3D(dot_1.get_center(), dot_2.get_center(), stroke_width=0.5, color=LIGHT_BROWN))

        # dot1 = always_redraw(lambda: Dot3D(ce1.get_end(), color=RED).scale(1.5))
        # dot2 = always_redraw(lambda: Dot3D(ce2.get_end(), color=YELLOW).scale(1.5))
        # expTheta = MathTex(r'c \hspace{0.6 mm}', r'e^{j ', r'(wt+\phi) }').scale(1.2).rotate(90 * DEGREES,
        #                                                                                      RIGHT).move_to(
        #     axes.c2p(1, 0, 1))
        # theta = MathTex(r'\theta ', color=RED).rotate(90 * DEGREES, RIGHT).move_to(axes.c2p(0.25, 0, 0.1))
        # expasfunoftime = MathTex(r'c \hspace{0.6 mm} e^{j(wt+\phi)}').rotate(90 * DEGREES, RIGHT).move_to(
        #     axes.c2p(1, 0, 1))
        # expasfunoftimemoving = always_redraw(
        #     lambda: MathTex(r'c \hspace{0.6 mm} e^{j(w *  %0.1f +\phi)}' % tvalue.get_value()).rotate(90 * DEGREES,
        #                                                                                               RIGHT).move_to(
        #         axes.c2p(1, 0, 1)))
        # euler_formula = MathTex(r'e^{j \omega  t} = cos(\omega  t)+j \hspace{0.7 mm} sin(\omega  t)')
        #
        # # vect = always_redraw(lambda: Arrow3D(axes.get_origin(), ce.get_points()[500], stroke_width=0.5, color=RED))
        # vect1 = always_redraw(lambda: Arrow3D(axes.get_origin(), dot1.get_center(), stroke_width=0.5, color=PINK))
        # vect2 = always_redraw(lambda: Arrow3D(axes.get_origin(), dot2.get_center(), stroke_width=0.5, color=PINK))
        # dot_start1 = always_redraw(lambda: Dot3D(ce1.get_start(), color=RED))
        # dot_start2 = always_redraw(lambda: Dot3D(ce2.get_start(), color=YELLOW))
        # vect_start1 = always_redraw(
        #     lambda: Arrow3D(axes.get_origin(), dot_start1.get_center(), stroke_width=0.5, color=PINK))
        # vect_start2 = always_redraw(
        #     lambda: Arrow3D(axes.get_origin(), dot_start2.get_center(), stroke_width=0.5, color=PINK))

        self.add(axes, cet, dot_1, dot_t, vect1, vect2, ce1, ce2, dot_1, dot_2)
        self.play(head_tracker.animate.set_value(10), run_time=3)
        self.wait()

class FourierTransform(ThreeDScene):
        def construct(self):

            axes = ThreeDAxes(x_range=[-1, 1, 1], y_range=[0, 10 * 10 ** -6, 2 * 10 ** -6],
                              z_range=[-1, 1, 1], x_length=10, y_length=14, z_length=10)

            numberplane = NumberPlane(x_range=[-1.5, 1.5, 0.25], y_range=[-1.5, 1.5, 0.25], x_length=9, y_length=9,
                                      background_line_style={
                                          "stroke_color": BLUE,
                                          "stroke_width": 0.7,
                                          "stroke_opacity": 1, }).rotate(90 * DEGREES, RIGHT).move_to(axes.get_origin())
            # ___________________________________________________________________
            self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.1)  # 3d view
            # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
            # axes.y_axis.rotate(90*DEGREES,[0,1,0])
            # axes.z_axis.rotate(-90*DEGREES,[0,0,1])
            # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000,
            #                             zoom=0.7)  # xz plane
            # axes.x_axis.rotate(90 * DEGREES, [1, 0, 0])
            # ___________________________________________________________________

            # 0.7*np.exp(1j * (2 * np.pi *0.5 * t+0.4)

            tvalue = ValueTracker(1)
            head_tracker = ValueTracker(0.1*10**-6)
            amp_tracker = ValueTracker(1)

            xm, ym, zm = TheSiGuy_lib.csv_to_xyz('csv/out_fdomain_mag.csv')
            xp, yp, zp = TheSiGuy_lib.csv_to_xyz('csv/out_fdomain_phase.csv')
            mag_res = axes.plot_line_graph(xm, ym, zm, add_vertex_dots=False, line_color=RED)
            phs_res = axes.plot_line_graph(xp, yp, zp, add_vertex_dots=False, line_color=TEAL_E)

            step = TheSiGuy_lib.three_d_graph_from_csv(axes, 'csv/out_tdomain.csv', color=LIGHT_PINK,
                                                       stroke_width=3)

            xp, yp, zp = TheSiGuy_lib.csv_to_xyz('csv/out_fdomain_phase.csv')
            freq = []
            amp = []
            phs = []


            ces=VGroup()
            dots=VGroup()

            for i in np.arange(0, 990, 200):
                freq.append(xm[i])
            for i in np.arange(0, 990, 200):
                amp.append(zm[i])
            for i in np.arange(0, 990, 200):
                phs.append(zp[i])

            dot = Dot3D(axes.get_origin(), color=RED)
            ces=VGroup()
            dots=VGroup()

            for i,f in enumerate(freq):

                ce=axes.plot_parametric_curve(lambda t: [np.real(amp[i]*np.exp(1j * (2 * np.pi *freq[i] * t+phs[i]))  ) +axes.p2c(dot.get_center())[0] , t, np.imag(amp[i]*np.exp(1j * (2 * np.pi *freq[i] * t+phs[i])) ) +axes.p2c(dot.get_center())[2] ], stroke_width=2, color=BLUE,t_range=np.array([0, 0.1, 0.1*10**-6])).add_updater(lambda m,dt: m.become(axes.plot_parametric_curve(lambda t: [np.real(amp[i]*np.exp(1j * (2 * np.pi *freq[i] * t+phs[i]))  ) +axes.p2c(dot.get_center())[0] , t, np.imag(amp[i]*np.exp(1j * (2 * np.pi *freq[i] * t+phs[i])) ) +axes.p2c(dot.get_center())[2] ], stroke_width=2, color=BLUE,t_range=np.array([0, dt, 0.1*10**-6]))))
                dot=Dot3D(color=RED).add_updater(lambda m: m.move_to(ce.get_end()))


                ces.add(ce)
                dots.add(dot)

            # comps = [ always_redraw(lambda: axes.plot_parametric_curve(lambda t: [np.real(a*np.exp(1j * (2 * np.pi *f * t+p))  ), t, np.imag(a*np.exp(1j * (2 * np.pi *f * t+p)) )], stroke_width=2, color=BLUE,t_range=np.array([0, head_tracker.get_value(), 0.1*10**-6])))   for f, a, p in zip(freq, amp, phs)]
            # dots= [always_redraw(lambda: Dot3D(comp.get_end(), color=RED)) for comp in comps]

            # head_tracker.set_value(10 * 10 ** -6)
            self.add(axes,ces[10])
            # self.play(head_tracker.animate.set_value(10*10**-6), run_time=3)
            self.wait(3)







    #_______________________________ just try but not working _______________________________________________

    # comp=lambda t:0
    # compp=[]
    # comps=[axes.plot_parametric_curve(lambda t: np.array([f, t, a*np.cos(2*np.pi*f*t+ph)]), stroke_width=2.2,color=YELLOW, t_range=[0, 10*10**-6, 10**-9]) for f,a,ph in zip(freq,amp,phs)]
    # for i in np.arange(0,len(comps),1):
    #     for j in np.arange(i,-1,-1):
    #         comp= comp+amp[j]*np.cos(2*np.pi*freq[j]*t+phs[j])
    #
    #     compp.append(comp)


# def two_d_graph_from_csv(ax, csvFile, stroke_width=1.5, color=YELLOW):
#     x = []
#     y = []
#     df = pd.read_csv(csvFile, names=['x', 'y'])
#     for ind, row in df.iterrows():
#         x.append(row.x)
#         y.append(row.y)
#
#     graph = ax.plot_line_graph(x, y, stroke_width=stroke_width, line_color=color, add_vertex_dots=False)
#
#     return graph
class A(ThreeDScene):

    def construct(self):
        # self.set_camera_orientation(phi=56 * DEGREES, theta=24 * DEGREES, focal_distance=1000, zoom=0.4)  # 3d view

        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.6)  # 3d view

        # dot=Dot([0,2,0])
        # a=always_rotate(  Dot([0,2,0]))
        # self.add(dot)
        # self.wait(5)
        # self.play(Rotating(dot,OUT,10,[0,0,0]))
        # self.wait()

        # axes = ThreeDAxes(x_range=[-1, 1, 1], y_range=[0, 10 * 10 ** -6, 2 * 10 ** -6],
        #                   z_range=[-1, 1, 1], x_length=10, y_length=14, z_length=10)
        #
        # t=Text(str(axes.get_origin())).scale(0.5)

        axes = ThreeDAxes(x_range=[-1, 1, 1], y_range=[0, 10 * 10 ** -6, 2 * 10 ** -6],
                          z_range=[-1, 1, 1], x_length=10, y_length=14, z_length=10)

        numberplane = NumberPlane(x_range=[-1.5, 1.5, 0.25], y_range=[-1.5, 1.5, 0.25], x_length=9, y_length=9,
                                  background_line_style={
                                      "stroke_color": BLUE,
                                      "stroke_width": 0.7,
                                      "stroke_opacity": 1, }).rotate(90 * DEGREES, RIGHT).move_to(axes.get_origin())




        self.add(axes)




class B(Scene):

    def construct(self):
        c=Circle()
        l=Line(c.get_center(),c.get_end())
        self.add(c,l)





class Pii(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.6)  # 3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        # axes.y_axis.rotate(90*DEGREES,[0,1,0])
        # axes.z_axis.rotate(-90*DEGREES,[0,0,1])
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000,
        #                             zoom=0.7)  # xz plane
        # axes.x_axis.rotate(90 * DEGREES, [1, 0, 0])

        # self.set_camera_orientation(phi=-90 * DEGREES, theta=0 * DEGREES, focal_distance=1000,gamma=90*DEGREES, zoom=0.4)  # 3d view

        # ___________________________________________________________________

        axes = ThreeDAxes(x_range=[-3, 3, 3], y_range=[0, 10 , 2 ],
                          z_range=[-3, 3, 3], x_length=10, y_length=14, z_length=10)

        numberplane = NumberPlane(x_range=[-1.5, 1.5, 0.25], y_range=[-1.5, 1.5, 0.25], x_length=9, y_length=9,
                                  background_line_style={
                                      "stroke_color": BLUE,
                                      "stroke_width": 0.7,
                                      "stroke_opacity": 1, }).rotate(90 * DEGREES, RIGHT).move_to(axes.get_origin())
        # ___________________________________________________________________


        # x,y,z=TheSiGuy_lib.csv_to_xyz('fourier_components/comp30.csv')
        #
        #
        # shape=axes.plot_line_graph(x,y,z,add_vertex_dots=False)
        # self.add(axes,shape)

        # x,y, z = TheSiGuy_lib.csv_to_xyz('fourier_components/comp30.csv')
        # y = [0 for y in x]
        #
        # shape = axes.plot_line_graph(x,y, z, add_vertex_dots=False)
        # self.add(axes,shape)

        # x, y, z = TheSiGuy_lib.csv_to_xyz('fourier_components/comp30.csv')
        # y = [0 for y in x]
        # xx = []
        # yy = []
        # zz = []
        # for i in range(0, len(x) + 1, 100):
        #     xn = x[i]
        #     yn = y[i]
        #     zn = z[i]
        #     xx.append(xn)
        #     yy.append(yn)
        #     zz.append(zn)
        #
        # shape = axes.plot_line_graph(xx, yy, zz, add_vertex_dots=False)
        #
        # self.add(axes, shape)

        circle = axes.plot_parametric_curve(lambda t: [2 * np.cos(t), 0, 2 * np.sin(t)], t_range=[0, 2 * PI],
                                            stroke_color=YELLOW,
                                            stroke_width=2,
                                            stroke_opacity=1)

        self.add(axes,circle)


class C(Scene):
    def construct(self):
        axes=Axes(x_range=[-10,10,5],y_range=[-10,10,5],x_length=7,y_length=7)



        c_color=RED
        c_width=1
        c_opacity=1
        v_color=RED
        v_width=1
        v_opacity=1
        Circle


        


class Circuits(Scene):
    def construct(self):
        svg=SVGMobject('svg/rc_circuit.svg').scale(0.2)
        # self.play(Write(svg))
        # self.wait()
        self.add(svg)



class MagPhsPots(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes(x_range=[0, 1 * 10 ** 6, 0.2 * 1000000], y_range=[0, 10 * 10 ** -6, 2 * 10 ** -6],z_range=[-1, 2, 0.5], x_length=15, y_length=14, z_length=6).shift([0, 0, -3])
        # self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.5)  # 3d view
        # axes.x_axis.animate().rotate(90 * DEGREES, [1, 0, 0])
        self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.6)     #yz plane
        axes.y_axis.rotate(90*DEGREES,[0,1,0])
        axes.z_axis.rotate(90*DEGREES,[0,0,1])
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.6) #xz plane
        # axes = ThreeDAxes(x_range=[0, 1*10**6, 0.2*1000000], y_range=[0, 10*10**-6, 2*10**-6], z_range=[-0.5, 2, 0.5], x_length=15, y_length=14,z_length=6).shift([0,0,-3])

        yz_plane = TheSiGuy_lib.yz_plane(axes)
        # xz_plane = TheSiGuy_lib.xz_plane(axes,GREEN)
        # ___________for yz plane______________
        # axes.z_axis.rotate(90*DEGREES,[0,0,1])
        # axes.y_axis.rotate(90*DEGREES,[0,1,0])
        #______________________________________
        #____________for xz plane______________
        # axes.x_axis.rotate(90*DEGREES,[1,0,0])


        xm,ym,zm=TheSiGuy_lib.csv_to_xyz('csv/in_fdomain_mag.csv')
        xp,yp,zp=TheSiGuy_lib.csv_to_xyz('csv/in_fdomain_phase.csv')
        mag_res=axes.plot_line_graph(xm,ym,zm,add_vertex_dots=False,line_color=RED)
        phs_res=axes.plot_line_graph(xp,yp,zp,add_vertex_dots=False,line_color=TEAL_E)

        step=TheSiGuy_lib.three_d_graph_from_csv(axes,'csv/in_tdomain.csv',color=LIGHT_PINK,stroke_width=3)



        xp,yp,zp=TheSiGuy_lib.csv_to_xyz('csv/in_fdomain_phase.csv')
        freq=[]
        amp=[]
        phs=[]


        for i in np.arange(0,990,10):
            freq.append(xm[i])
        for i in np.arange(0,990,10):
            amp.append(zm[i])
        for i in np.arange(0,990,10):
            phs.append(zp[i])





        comps=[axes.plot_parametric_curve(lambda t: np.array([f, t, a * np.cos(2 * np.pi*f * t + p)]), stroke_width=2,color=GOLD, t_range=[0, 10*10**-6, 10**-9]) for f,a,p in zip(freq,amp,phs)]

        comps_acc = ["csv/step_comps/comp%i.csv" % num for num in range(1, 100)]
        graphs_acc = [TheSiGuy_lib.three_d_graph_from_csv(ax=axes, csvFile=file,color=YELLOW,stroke_width=3) for file in comps_acc]
        mags=[axes.plot_line_graph(xm[:(i+1)*10],ym[:(i+1)*10],zm[:(i+1)*10],add_vertex_dots=False,line_color=RED,stroke_width=3) for i,curve in enumerate(comps)]

        transforms=[ReplacementTransform(c,graphs_acc[-1]) for c in comps]
        # self.add(axes, graphs_acc[0])
        #___________________________________
        # self.play(Create(axes))
        # self.wait(0.2)
        # self.play(FadeIn(yz_plane),run_time=1)
        # self.wait()
        # self.play(Create(step),run_time=1)
        # self.wait()
        #__________________________________



        ###################### ploting the components on time freq axis one by one #############################
        # self.add(axes, graphs_acc[0],step)
        self.add(axes)

        # dot1=Dot3D(axes.c2p(freq[31],0,amp[31]),color=GREEN).scale(0.8)
        # dot2=Dot3D(axes.c2p(freq[13],0,amp[13]),color=RED).scale(0.8)
        # # dot2=Dot3D(mags[16].get_end())
        # vl1=axes.get_line_from_axis_to_point(index=0,point=dot1.get_center(),color=GREEN)
        # vl2=axes.get_line_from_axis_to_point(index=0,point=dot2.get_center(),color=RED)
        # hl1=axes.get_line_from_axis_to_point(index=2,point=dot1.get_center(),color=GREEN)
        # hl2=axes.get_line_from_axis_to_point(index=2,point=dot2.get_center(),color=RED)
        # comps[13].set_color(RED)
        # comps[31].set_color(GREEN)
        #
        # # self.add(mags[22],dot1,dot2, comps[22],comps[13],vl1,vl2,hl1,hl2)
        # self.add(dot1,dot2,vl1,vl2,hl1,hl2)


        # self.play(Create(comps[13]))
        # self.play(Create(comps[31]))
        # self.wait()
        # self.move_camera(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.6, run_time=2)
        # self.wait(0.5)
        # self.play(FadeIn(dot1),FadeIn(dot2),FadeOut(comps[13]),FadeOut(comps[31]))
        # self.play(Create(vl1),Create(hl1))
        # self.play(Create(vl2),Create(hl2))
        # self.wait()
        # self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.5,added_anims=[axes.x_axis.animate().rotate(90*DEGREES,[1,0,0])])
        # self.play(FadeOut(dot1),FadeOut(dot2),FadeOut(vl1),FadeOut(vl2),FadeOut(hl1),FadeOut(hl2))
        # self.wait()
        # self.play(FadeIn(comps[13].set_color(RED)),FadeIn(comps[28].set_color(GREEN)))
        # self.wait()





        # for i,curve in enumerate(comps):
        #     mag=axes.plot_line_graph(xm[:(i+1)*10],ym[:(i+1)*10],zm[:(i+1)*10],add_vertex_dots=False,line_color=RED,stroke_width=3)
        #     # phs=axes.plot_line_graph(xp[:(i+1)*10],yp[:(i+1)*10],zp[:(i+1)*10],add_vertex_dots=False,line_color=GOLD_E)
        #     # self.play(Transform(propagating_wave_curves[0],i))
        #     # self.remove(propagating_wave_curves[i-1])
        #     comps[i-1].set_stroke([BLUE,GREEN],0.8)
        #     self.remove(graphs_acc[i-1])
        #     self.add(comps[i])
        #     self.add(mags[i])
        #     # self.add(phs)
        #     # self.add(graphs_acc[i])
        #     self.wait(0.14)
        #     self.remove(comps[0])
        # self.wait()





#_____________________________________________________
        for i in comps:
            i.set_stroke([BLUE,GREEN],0.8)

        # g = VGroup(*comps)

        # self.add(axes,*comps,mags[-1])
        # self.play(FadeIn(yz_plane))
        # self.wait(0.5)
        # self.move_camera(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.6,added_anims=[axes.x_axis.animate().rotate(-90 * DEGREES, [1, 0, 0]),axes.y_axis.animate.rotate(90*DEGREES,[0,1,0]),axes.z_axis.animate.rotate(90*DEGREES,[0,0,1])])
        # self.wait()
        # self.play(*transforms)
        # self.wait()
#________________________________________________________

        self.add(yz_plane,*comps,mags[-1])
        self.play(*transforms)
        self.wait()


        # self.play(FadeIn(comps_acc[-1],run_time=2),FadeOut(g))
        # self.wait()

        # self.play(Transform(comps[13].copy(),comps_acc[70]))
        # self.wait()
        # self.play(Transform(g[3],g[-1]))
        # self.wait()

class MagPhsPots2(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes(x_range=[0, 1 * 10 ** 6, 0.2 * 1000000], y_range=[0, 10 * 10 ** -6, 2 * 10 ** -6],z_range=[-0.5, 1, 0.25], x_length=15, y_length=14, z_length=6).shift([0, 0, -3])
        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.5)  # 3d view
        axes.x_axis.animate().rotate(90 * DEGREES, [1, 0, 0])
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.6)     #yz plane
        # axes.y_axis.rotate(90*DEGREES,[0,1,0])
        # axes.z_axis.rotate(90*DEGREES,[0,0,1])
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.6) #xz plane
        # axes = ThreeDAxes(x_range=[0, 1*10**6, 0.2*1000000], y_range=[0, 10*10**-6, 2*10**-6], z_range=[-0.5, 2, 0.5], x_length=15, y_length=14,z_length=6).shift([0,0,-3])

        yz_plane = TheSiGuy_lib.yz_plane(axes)
        # xz_plane = TheSiGuy_lib.xz_plane(axes,GREEN)
        # ___________for yz plane______________
        # axes.z_axis.rotate(90*DEGREES,[0,0,1])
        # axes.y_axis.rotate(90*DEGREES,[0,1,0])
        #______________________________________
        #____________for xz plane______________
        # axes.x_axis.rotate(90*DEGREES,[1,0,0])


        xm,ym,zm=TheSiGuy_lib.csv_to_xyz('csv/in_fdomain_mag.csv')
        xp,yp,zp=TheSiGuy_lib.csv_to_xyz('csv/in_fdomain_phase.csv')
        mag_res=axes.plot_line_graph(xm,ym,zm,add_vertex_dots=False,line_color=RED)
        phs_res=axes.plot_line_graph(xp,yp,zp,add_vertex_dots=False,line_color=TEAL_E)

        step=TheSiGuy_lib.three_d_graph_from_csv(axes,'csv/in_tdomain.csv',color=LIGHT_PINK,stroke_width=3)



        xp,yp,zp=TheSiGuy_lib.csv_to_xyz('csv/in_fdomain_phase.csv')
        freq=[]
        amp=[]
        phs=[]


        for i in np.arange(0,990,10):
            freq.append(xm[i])
        for i in np.arange(0,990,10):
            amp.append(zm[i])
        for i in np.arange(0,990,10):
            phs.append(zp[i])





        comps=[axes.plot_parametric_curve(lambda t: np.array([f, t, a * np.cos(2 * np.pi*f * t + p)]), stroke_width=2,color=GOLD, t_range=[0, 10*10**-6, 10**-9]) for f,a,p in zip(freq,amp,phs)]

        comps_acc = ["csv/step_comps/comp%i.csv" % num for num in range(1, 100)]
        graphs_acc = [TheSiGuy_lib.three_d_graph_from_csv(ax=axes, csvFile=file,color=YELLOW,stroke_width=3) for file in comps_acc]
        mags=[axes.plot_line_graph(xm[:(i+1)*10],ym[:(i+1)*10],zm[:(i+1)*10],add_vertex_dots=False,line_color=RED,stroke_width=3) for i,curve in enumerate(comps)]

        # transforms=[ReplacementTransform(c,graphs_acc[-1]) for c in comps]
        # self.add(axes, graphs_acc[0])
        #___________________________________
        # self.play(Create(axes))
        # self.wait(0.2)
        # self.play(FadeIn(yz_plane),run_time=1)
        # self.wait()
        # self.play(Create(step),run_time=1)
        # self.wait()
        #__________________________________



        ###################### ploting the components on time freq axis one by one #############################
        # self.add(axes, graphs_acc[0],step)
        self.add(axes)

        dot1=Dot3D(axes.c2p(freq[31],0,amp[31]),color=GREEN).scale(0.8)
        # dot2=Dot3D(axes.c2p(freq[13],0,amp[13]),color=RED).scale(0.8)
        # # dot2=Dot3D(mags[16].get_end())
        vl1=axes.get_line_from_axis_to_point(index=0,point=dot1.get_center(),color=GREEN)
        # vl2=axes.get_line_from_axis_to_point(index=0,point=dot2.get_center(),color=RED)
        hl1=axes.get_line_from_axis_to_point(index=2,point=dot1.get_center(),color=GREEN).reverse_points()
        # hl2=axes.get_line_from_axis_to_point(index=2,point=dot2.get_center(),color=RED)
        # comps[13].set_color(RED)
        comps[31].set_color(GREEN)
        #
        # # self.add(mags[22],dot1,dot2, comps[22],comps[13],vl1,vl2,hl1,hl2)
        # self.add(dot1,dot2,vl1,vl2,hl1,hl2)

        # self.add(axes,dot1,hl1,vl1,comps[31])
        self.add(axes)
        self.play(Create(comps[31]))
        self.wait()
        self.play(FadeIn(dot1))
        self.play(Create(vl1))
        self.play(Create(hl1))
        self.wait()


        # self.play(Create(comps[13]))
        # self.play(Create(comps[31]))
        # self.wait()
        # self.move_camera(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.6, run_time=2)
        # self.wait(0.5)
        # self.play(FadeIn(dot1),FadeIn(dot2),FadeOut(comps[13]),FadeOut(comps[31]))
        # self.play(Create(vl1),Create(hl1))
        # self.play(Create(vl2),Create(hl2))
        # self.wait()
        # self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.5,added_anims=[axes.x_axis.animate().rotate(90*DEGREES,[1,0,0])])
        # self.play(FadeOut(dot1),FadeOut(dot2),FadeOut(vl1),FadeOut(vl2),FadeOut(hl1),FadeOut(hl2))
        # self.wait()
        # self.play(FadeIn(comps[13].set_color(RED)),FadeIn(comps[28].set_color(GREEN)))
        # self.wait()





        # for i,curve in enumerate(comps):
        #     mag=axes.plot_line_graph(xm[:(i+1)*10],ym[:(i+1)*10],zm[:(i+1)*10],add_vertex_dots=False,line_color=RED,stroke_width=3)
        #     # phs=axes.plot_line_graph(xp[:(i+1)*10],yp[:(i+1)*10],zp[:(i+1)*10],add_vertex_dots=False,line_color=GOLD_E)
        #     # self.play(Transform(propagating_wave_curves[0],i))
        #     # self.remove(propagating_wave_curves[i-1])
        #     comps[i-1].set_stroke([BLUE,GREEN],0.8)
        #     self.remove(graphs_acc[i-1])
        #     self.add(comps[i])
        #     self.add(mags[i])
        #     # self.add(phs)
        #     # self.add(graphs_acc[i])
        #     self.wait(0.14)
        #     self.remove(comps[0])
        # self.wait()





#_____________________________________________________
        # for i in comps:
        #     i.set_stroke([BLUE,GREEN],0.8)

        # g = VGroup(*comps)

        # self.add(axes,*comps,mags[-1])
        # self.play(FadeIn(yz_plane))
        # self.wait(0.5)
        # self.move_camera(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.6,added_anims=[axes.x_axis.animate().rotate(-90 * DEGREES, [1, 0, 0]),axes.y_axis.animate.rotate(90*DEGREES,[0,1,0]),axes.z_axis.animate.rotate(90*DEGREES,[0,0,1])])
        # self.wait()
        # self.play(*transforms)
        # self.wait()
#________________________________________________________

        # self.add(yz_plane,*comps,mags[-1])
        # # self.play(*transforms)
        # # self.wait()
        #
        # for i,c in enumerate(comps):
        #     self.remove(comps[i],graphs_acc[i-1])
        #     self.add(graphs_acc[i])
        #     self.wait(0.1)
        #
        # self.wait()


        # self.play(FadeIn(comps_acc[-1],run_time=2),FadeOut(g))
        # self.wait()

        # self.play(Transform(comps[13].copy(),comps_acc[70]))
        # self.wait()
        # self.play(Transform(g[3],g[-1]))
        # self.wait()










class PhasePlots3(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000,
                                    zoom=0.8)  # xz plane
        axes = ThreeDAxes(x_range=[0, 1 * 10 ** 6, 0.2 * 1000000], y_range=[0, 10 * 10 ** -6, 2 * 10 ** -6],
                            z_range=[-3.50, 1.05, 1.05], x_length=15, y_length=14, z_length=6,
                            axis_config={"stroke_width": 1.5, "include_ticks": True, "include_tip": False}).shift(
            [0, 0, 0.5])
        ax = Axes(x_range=[0, 1 * 10 ** 6, 0.2 * 1000000], y_range=[-3.50, 0.5, 1.05],
                    axis_config={"stroke_width": 1.5, "include_ticks": True, "include_tip": False}, y_length=4)
        numberplane = NumberPlane(x_range=[0, 1 * 10 ** 6, 1000000], y_range=[-4, 0.5, 0.5], x_length=15,
                                    y_length=6, background_line_style={"stroke_width": 1, "stroke_opacity": 0.5, },
                                    axis_config={"stroke_width": 1.5, "include_ticks": True, "include_tip": False})
        xp1, yp1, zp1 = TheSiGuy_lib.csv_to_xyz('csv/in_fdomain_phase.csv')
        axes.x_axis.rotate(90 * DEGREES, [1, 0, 0])

        xp=[]
        yp=[]
        zp=[]
        for i in np.arange(0,990,10):
            xp.append(xp1[i])
        for i in np.arange(0,990,10):
            yp.append(yp1[i])
        for i in np.arange(0,990,10):
            zp.append(zp1[i])


        # phs_plt = axes.plot_line_graph(xp, yp, zp, add_vertex_dots=False,line_color=ORANGE, stroke_width=2)

        # self.play(Create(axes))
        # self.wait(0.2)
        # self.wait(1)
        # self.wait()
        # self.wait(1)
        # self.wait()

        self.add(axes)

        dot1=Dot3D(axes.c2p(xp[31],zp[31]),color=GREEN).scale(0.8)
        dot2=Dot3D(axes.c2p(xp[13],zp[13]),color=RED).scale(0.8)
        # dot2=Dot3D(mags[16].get_end())
        vl1=axes.get_line_from_axis_to_point(index=0,point=dot1.get_center(),color=GREEN)
        vl2=axes.get_line_from_axis_to_point(index=0,point=dot2.get_center(),color=RED)
        hl1=axes.get_line_from_axis_to_point(index=2,point=dot1.get_center(),color=GREEN)
        hl2=axes.get_line_from_axis_to_point(index=2,point=dot2.get_center(),color=RED)

        #
        # # self.add(mags[22],dot1,dot2, comps[22],comps[13],vl1,vl2,hl1,hl2)
        self.add(dot1,dot2,vl1,vl2,hl1,hl2)

        # self.play(Create(comps[13]))
        # self.play(Create(comps[31]))
        # self.wait()
        # self.move_camera(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.6, run_time=2)
        # self.wait(0.5)


        # self.play(FadeIn(dot1),FadeIn(dot2))
        # self.play(Create(vl1),Create(hl1))
        # self.play(Create(vl2),Create(hl2))
        # self.wait()


        # self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.5,added_anims=[axes.x_axis.animate().rotate(90*DEGREES,[1,0,0])])
        # self.play(FadeOut(dot1),FadeOut(dot2),FadeOut(vl1),FadeOut(vl2),FadeOut(hl1),FadeOut(hl2))
        # self.wait()
        # self.play(FadeIn(comps[13].set_color(RED)),FadeIn(comps[28].set_color(GREEN)))
        # self.wait()

        ###################### ploting the components on time freq axis one by one #############################

        # for i in range(0, 990, 10):
        #     # mag = axes.plot_line_graph(xm[:(i + 1) * 10], ym[:(i + 1) * 10], zm[:(i + 1) * 10], add_vertex_dots=False,
        #     #                            line_color=RED)
        #     phs1 = axes.plot_line_graph(xp1[:(i + 1)], yp1[:(i + 1)], zp1[:(i + 1)], add_vertex_dots=False,
        #                                     line_color=ORANGE, stroke_width=2)
        #     # self.play(Transform(propagating_wave_curves[0],i))
        #     # self.remove(propagating_wave_curves[i-1])
        #     # comps[i - 1].set_stroke([BLUE, GREEN], 0.8)
        #     # self.remove(graphs_acc[i - 1])
        #     # self.add(comps[i])
        #     # self.add(mag)
        #     self.add(phs1)
        #     # self.add(graphs_acc[i])
        #     self.wait(0.14)
        #     # self.remove(comps[0])
        # self.wait()




class PhasePlots4(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000,
                                    zoom=0.8)  # xz plane
        axes = ThreeDAxes(x_range=[0, 1 * 10 ** 6, 0.2 * 1000000], y_range=[0, 10 * 10 ** -6, 2 * 10 ** -6],
                            z_range=[-3.50, 1.05, 1.05], x_length=15, y_length=14, z_length=6,
                            axis_config={"stroke_width": 1.5, "include_ticks": True, "include_tip": False}).shift(
            [0, 0, 0.5])
        ax = Axes(x_range=[0, 1 * 10 ** 6, 0.2 * 1000000], y_range=[-3.50, 0.5, 1.05],
                    axis_config={"stroke_width": 1.5, "include_ticks": True, "include_tip": False}, y_length=4)
        numberplane = NumberPlane(x_range=[0, 1 * 10 ** 6, 1000000], y_range=[-4, 0.5, 0.5], x_length=15,
                                    y_length=6, background_line_style={"stroke_width": 1, "stroke_opacity": 0.5, },
                                    axis_config={"stroke_width": 1.5, "include_ticks": True, "include_tip": False})
        xp1, yp1, zp1 = TheSiGuy_lib.csv_to_xyz('csv/out_fdomain_phase.csv')
        axes.x_axis.rotate(90 * DEGREES, [1, 0, 0])

        # self.play(Create(axes))
        # self.wait(0.2)
        # self.wait(1)
        # self.wait()
        # self.wait(1)
        # self.wait()
        x=[]
        y=[]
        z=[]

        ###################### ploting the components on time freq axis one by one #############################

        for i in range(0, 990, 10):
            # mag = axes.plot_line_graph(xm[:(i + 1) * 10], ym[:(i + 1) * 10], zm[:(i + 1) * 10], add_vertex_dots=False,
            #                            line_color=RED)
            phs1 = axes.plot_line_graph(xp1[:(i + 1)], yp1[:(i + 1)], zp1[:(i + 1)], add_vertex_dots=False,
                                            line_color=ORANGE, stroke_width=3)

            x.append(xp1[i])
            y.append(yp1[i])
            z.append(zp1[i])
            # self.play(Transform(propagating_wave_curves[0],i))
            # self.remove(propagating_wave_curves[i-1])
            # comps[i - 1].set_stroke([BLUE, GREEN], 0.8)
            # self.remove(graphs_acc[i - 1])
            # self.add(comps[i])
            # self.add(mag)
            # self.add(phs1)
            # self.add(graphs_acc[i])
            # self.wait(0.14)
            # self.remove(comps[0])
        # self.wait()

        dot1 = Dot3D(axes.c2p(x[31],0, z[31]), color=GREEN).scale(0.8)
        dot2 = Dot3D(axes.c2p(x[13],0, z[13]), color=RED).scale(0.8)
        vl1 = axes.get_line_from_axis_to_point(index=0, point=dot1.get_center(), color=GREEN)
        vl2 = axes.get_line_from_axis_to_point(index=0, point=dot2.get_center(), color=RED)
        hl1 = axes.get_line_from_axis_to_point(index=2, point=dot1.get_center(), color=GREEN)
        hl2 = axes.get_line_from_axis_to_point(index=2, point=dot2.get_center(), color=RED)

        #
        # # self.add(mags[22],dot1,dot2, comps[22],comps[13],vl1,vl2,hl1,hl2)
        # self.add(axes,dot1, dot2, vl1, vl2, hl1, hl2)

        self.add(axes)
        self.wait(2)
        self.play(FadeIn(dot1))
        self.play(Create(vl1))
        self.play(Create(hl1))
        self.wait()

        # self.play(Create(comps[13]))
        # self.play(Create(comps[31]))
        # self.wait()
        # self.move_camera(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.6, run_time=2)
        # self.wait(0.5)
        # self.play(FadeIn(dot1),FadeIn(dot2),FadeOut(comps[13]),FadeOut(comps[31]))
        # self.play(Create(vl1),Create(hl1))
        # self.play(Create(vl2),Create(hl2))
        # self.wait()
        # self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.5,added_anims=[axes.x_axis.animate().rotate(90*DEGREES,[1,0,0])])
        # self.play(FadeOut(dot1),FadeOut(dot2),FadeOut(vl1),FadeOut(vl2),FadeOut(hl1),FadeOut(hl2))
        # self.wait()

        # self.wait(5.5)
        # self.play(FadeIn(dot1), FadeIn(dot2))
        # self.play(Create(vl1), Create(hl1))
        # self.play(Create(vl2),Create(hl2))
        # self.wait(2)
        # self.play(FadeOut(dot1), FadeOut(dot2), FadeOut(vl1), FadeOut(vl2), FadeOut(hl1), FadeOut(hl2))
        # self.wait()





class D(ThreeDScene):
    def construct(self):


#____________phase  _______________________________________________________________________________________________________

        #
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000,
        #                             zoom=0.8)  # xz plane
        # axes = ThreeDAxes(x_range=[0, 1 * 10 ** 6, 0.2 * 1000000], y_range=[0, 10 * 10 ** -6, 2 * 10 ** -6],
        #                     z_range=[-3.50, 1.05, 1.05], x_length=15, y_length=14, z_length=6,
        #                     axis_config={"stroke_width": 1.5, "include_ticks": True, "include_tip": False}).shift(
        #     [0, 0, 0.5])
        # ax = Axes(x_range=[0, 1 * 10 ** 6, 0.2 * 1000000], y_range=[-3.50, 0.5, 1.05],
        #             axis_config={"stroke_width": 1.5, "include_ticks": True, "include_tip": False}, y_length=4)
        # numberplane = NumberPlane(x_range=[0, 1 * 10 ** 6, 1000000], y_range=[-4, 0.5, 0.5], x_length=15,
        #                             y_length=6, background_line_style={"stroke_width": 1, "stroke_opacity": 0.5, },
        #                             axis_config={"stroke_width": 1.5, "include_ticks": True, "include_tip": False})
        # xp1, yp1, zp1 = TheSiGuy_lib.csv_to_xyz('csv/out_fdomain_phase.csv')
        # axes.x_axis.rotate(90 * DEGREES, [1, 0, 0])



#_______________ Mag  _________________________________________________________________________________
        #
        axes = ThreeDAxes(x_range=[0, 1 * 10 ** 6, 0.2 * 1000000], y_range=[0, 10 * 10 ** -6, 2 * 10 ** -6],
                          z_range=[-0.5, 1, 0.25], x_length=15, y_length=14, z_length=6).shift([0, 0, -3])
        # self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.5)  # 3d view
        # axes.x_axis.rotate(90 * DEGREES, [1, 0, 0])
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.6)     #yz plane
        # axes.y_axis.rotate(90*DEGREES,[0,1,0])
        # axes.z_axis.rotate(90*DEGREES,[0,0,1])
        self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.6) #xz plane
        # axes = ThreeDAxes(x_range=[0, 1*10**6, 0.2*1000000], y_range=[0, 10*10**-6, 2*10**-6], z_range=[-0.5, 2, 0.5], x_length=15, y_length=14,z_length=6).shift([0,0,-3])

        yz_plane = TheSiGuy_lib.yz_plane(axes)
        axes.x_axis.rotate(90 * DEGREES, [1, 0, 0])


        self.play(Create(axes))
        self.wait()
        self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.5,added_anims=[axes.x_axis.animate().rotate(90 * DEGREES, [1, 0, 0])])
        self.wait()
        # self.add(a)


        #
        # self.play(Create(axes))
        # self.wait()




class Equations8(Scene):
    def construct(self):
        # eq1=MathTex(r'v_{1}=V_m \cos (\omega t)',color=RED)
        # eq2=MathTex(r'v_{2}=V_m \cos (\omega t+\phi)',color=YELLOW).shift(DOWN)

        # cos = MathTex(r'V_m \cos (\omega t+\phi)', color=YELLOW)
        # sin = MathTex(r'V_m \sin (\omega t+\phi)', color=YELLOW).shift(DOWN)

        # phi=MathTex(r'\phi ',color=RED).scale(3)
        c=MathTex(r'C ',color=RED).scale(3)

        # self.play(Write(sin))
        # self.wait()


        self.add(c)





class Res(ThreeDScene):
    def construct(self):
        self.camera.background_color = "#101010"

        axes = ThreeDAxes(x_range=[-1.5, 1.5, 0.25], y_range=[0, 10.3, 2], z_range=[-1.5, 1.5, 0.25], x_length=9, z_length=9, y_length=15)
        numberplane = NumberPlane(x_range=[-1.5, 1.5, 0.25], y_range=[-1.5, 1.5, 0.25], x_length=9, y_length=9,
                                  background_line_style={
                                      "stroke_color": BLUE,
                                      "stroke_width": 0.7,
                                      "stroke_opacity": 1,}).rotate(90 * DEGREES, RIGHT).move_to(axes.get_origin())
        #___________________________________________________________________
        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.58)  # 3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        # axes.y_axis.rotate(90*DEGREES,[0,1,0])
        # axes.z_axis.rotate(-90*DEGREES,[0,0,1])
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7)  # xz plane
        # axes.x_axis.rotate(90 * DEGREES, [1, 0, 0])
        self.set_camera_orientation(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.6)  #yx
        #___________________________________________________________________

        xy_plane = TheSiGuy_lib.xy_plane(axes)




        tvalue = ValueTracker(1)
        head_tracker = ValueTracker(10)
        amp_tracker=ValueTracker(1)
        ce1=always_redraw(lambda : axes.plot_parametric_curve(lambda t: [0.6*np.real(  np.exp(1j * (2 * np.pi * 0.3 * t+0.7 ))),t,0.6*np.imag(np.exp(1j * (2 * np.pi * 0.3 * t+0.7 )))], stroke_width=2, color=RED, t_range=np.array([0, head_tracker.get_value(), 0.01])))
        phs_tracker = ValueTracker(0.8)
        ce2=always_redraw(lambda : axes.plot_parametric_curve(lambda t: [np.real(  np.exp(1j * (2 * np.pi * 0.3 * t +0.7))),t,np.imag(np.exp(1j * (2 * np.pi * 0.3 * t +0.7)))], stroke_width=2, color=YELLOW, t_range=np.array([0, head_tracker.get_value(), 0.01])))
        dot1 = always_redraw(lambda: Dot3D(ce1.get_end(),color=RED).scale(1.5))
        dot2 = always_redraw(lambda: Dot3D(ce2.get_end(),color=YELLOW).scale(1.5))
        expTheta = MathTex(r'c \hspace{0.6 mm}', r'e^{j ', r'(wt+\phi) }').scale(1.2).rotate(90 * DEGREES, RIGHT).move_to(axes.c2p(1, 0, 1))
        theta = MathTex(r'\theta ', color=RED).rotate(90 * DEGREES, RIGHT).move_to(axes.c2p(0.25, 0, 0.1))
        expasfunoftime = MathTex(r'c \hspace{0.6 mm} e^{j(wt+\phi)}').rotate(90 * DEGREES, RIGHT).move_to(axes.c2p(1, 0, 1))
        expasfunoftimemoving = always_redraw(lambda: MathTex(r'c \hspace{0.6 mm} e^{j(w *  %0.1f +\phi)}' % tvalue.get_value()).rotate(90 * DEGREES, RIGHT).move_to(axes.c2p(1, 0, 1)))
        euler_formula = MathTex(r'e^{j \omega  t} = cos(\omega  t)+j \hspace{0.7 mm} sin(\omega  t)')

        # vect = always_redraw(lambda: Arrow3D(axes.get_origin(), ce.get_points()[500], stroke_width=0.5, color=RED))
        vect1 = always_redraw(lambda: Arrow3D(axes.get_origin(), dot1.get_center(), stroke_width=0.5, color=PINK))
        vect2 = always_redraw(lambda: Arrow3D(axes.get_origin(), dot2.get_center(), stroke_width=0.5, color=PINK))
        dot_start1=always_redraw(lambda : Dot3D(ce1.get_start(),color=RED))
        dot_start2=always_redraw(lambda : Dot3D(ce2.get_start(),color=YELLOW))
        vect_start1 = always_redraw(lambda: Arrow3D(axes.get_origin(), dot_start1.get_center(), stroke_width=0.5, color=RED))
        vect_start2 = always_redraw(lambda: Arrow3D(axes.get_origin(), dot_start2.get_center(), stroke_width=0.5, color=YELLOW))



#___________________________________________________________________________________________
        # ce1 = always_redraw(lambda: axes.plot_parametric_curve(lambda t: [np.real(np.exp(1j * (2 * np.pi * 0.3 * t))), t, np.imag(np.exp(1j * (2 * np.pi * 0.3 * t)))],stroke_width=2, color=RED, t_range=np.array([0, head_tracker.get_value(), 0.01])))
        # ce2 = always_redraw(lambda: axes.plot_parametric_curve(lambda t: [np.real(np.exp(1j * (2 * np.pi * 0.3 * t + phs_tracker.get_value()))), t,np.imag(np.exp(1j * (2 * np.pi * 0.3 * t + phs_tracker.get_value())))], stroke_width=2,color=YELLOW, t_range=np.array([0, head_tracker.get_value(), 0.01])))
#___________________________________________________________________________________________







        # self.add(numberplane, axes, ce1, ce2, dot1, dot2)
        # self.wait()
        # self.play(head_tracker.animate.set_value(10), run_time=20, rate_func=rate_functions.linear)
        # self.wait()

        # self.add(numberplane, axes)
        # self.play(FadeIn(dot_start2,vect_start2))
        # self.wait()
        # self.play(FadeIn(ce2,dot2))
        # self.wait()
        # self.play(head_tracker.animate.set_value(10), run_time=10, rate_func=rate_functions.linear)
        # self.wait()

        # self.add(numberplane, axes, dot_start2, vect_start2, ce2, dot2)
        # self.play(FadeOut(dot2))
        # self.wait()

        # self.add(numberplane, axes, ce1,ce2, vect_start2, dot_start2,dot_start1,vect_start1)
        # vect_start1.set_stroke(opacity=0.2).scale(5)
        # vect_start2.set_stroke(opacity=0.2).scale(5)

        self.add(numberplane,axes,xy_plane)
        self.play(Create(ce1))
        self.wait()
        self.play(Create(ce2))
        self.wait()
        self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.58,run_time=2)
        # self.wait(vect_start1.animate().set_stroke(opacity=1).scale(0.2))
        # self.wait(vect_start2.animate().set_stroke(opacity=1).scale(0.2))
        self.play(FadeIn(vect_start1))
        self.play(FadeIn(vect_start2))
        self.wait()








        # self.wait()
        # self.play(amp_tracker.animate.set_value(1.5))
        # self.play(amp_tracker.animate.set_value(1))
        # self.wait()
        #
        # self.play(phs_tracker.animate.set_value(2))
        # self.play(phs_tracker.animate.set_value(0.8))
        # self.wait()




        # self.add(axes,ce,dot)

        # self.play(Create(numberplane))
        # self.play(Create(axes))
        # self.wait()
        # self.play(Write(expTheta))
        # self.play(FadeIn(dot))
        # self.wait()
        # self.play(ReplacementTransform(expTheta[0].copy(),vect),ReplacementTransform(expTheta[2].copy(),theta))
        # self.wait()
        # self.play(ReplacementTransform(theta,expTheta[2]))
        # self.wait()

        # self.add(numberplane, axes, expTheta, vect, dot)
        # self.wait()
        # self.play(FadeOut(expTheta,vect),FadeIn(ce))
        # self.remove(dot)
        # self.add(dot)
        # self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.58, added_anims=[axes.x_axis.animate.rotate(90*DEGREES,[1,0,0])],run_time=2)
        # self.wait()

        # self.add(numberplane,axes,expTheta,vect,ce,dot)
        # self.wait()
        # self.play(FadeOut(vect))
        # self.play(head_tracker.animate.set_value(10), run_time=25,rate_func=rate_functions.linear)
        # self.wait()

        # self.add(numberplane, axes,ce, dot)
        # self.play(FadeOut(dot))
        # self.play(FadeIn(dot_start),FadeIn(vect_start))
        # self.play(phs_tracker.animate.set_value(6.28),run_time=4)
        # self.wait()
        # self.play(phs_tracker.animate.set_value(0.5), run_time=4)
        # self.wait()




class Res2(ThreeDScene):
    def construct(self):
        self.camera.background_color = "#101010"

        axes = ThreeDAxes(x_range=[-1.5, 1.5, 0.25], y_range=[0, 10.3, 2], z_range=[-1.5, 1.5, 0.25], x_length=9,
                          z_length=9, y_length=15)
        numberplane = NumberPlane(x_range=[-1.5, 1.5, 0.25], y_range=[-1.5, 1.5, 0.25], x_length=9, y_length=9,
                                  background_line_style={
                                      "stroke_color": BLUE,
                                      "stroke_width": 0.7,
                                      "stroke_opacity": 1, }).rotate(90 * DEGREES, RIGHT).move_to(axes.get_origin())
        # ___________________________________________________________________
        # self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.58)  # 3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        # axes.y_axis.rotate(90*DEGREES,[0,1,0])
        # axes.z_axis.rotate(-90*DEGREES,[0,0,1])
        self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7)  # xz plane
        axes.x_axis.rotate(90 * DEGREES, [1, 0, 0])
        # self.set_camera_orientation(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.6)  # yx
        # ___________________________________________________________________

        xy_plane = TheSiGuy_lib.xy_plane(axes)

        tvalue = ValueTracker(1)
        head_tracker = ValueTracker(10)
        amp_tracker = ValueTracker(1)
        ce1 = always_redraw(lambda: axes.plot_parametric_curve(
            lambda t: [0.6 * np.real(np.exp(1j * (2 * np.pi * 0.3 * t + 0.7))), t,
                       0.6 * np.imag(np.exp(1j * (2 * np.pi * 0.3 * t + 0.7)))], stroke_width=2, color=RED,
            t_range=np.array([0, head_tracker.get_value(), 0.01])))
        phs_tracker = ValueTracker(0.8)
        ce2 = always_redraw(lambda: axes.plot_parametric_curve(
            lambda t: [np.real(np.exp(1j * (2 * np.pi * 0.3 * t + 0.7))), t,
                       np.imag(np.exp(1j * (2 * np.pi * 0.3 * t + 0.7)))], stroke_width=2, color=YELLOW,
            t_range=np.array([0, head_tracker.get_value(), 0.01])))
        dot1 = always_redraw(lambda: Dot3D(ce1.get_end(), color=RED).scale(1.5))
        dot2 = always_redraw(lambda: Dot3D(ce2.get_end(), color=YELLOW).scale(1.5))
        expTheta = MathTex(r'c \hspace{0.6 mm}', r'e^{j ', r'(wt+\phi) }').scale(1.2).rotate(90 * DEGREES,
                                                                                             RIGHT).move_to(
            axes.c2p(1, 0, 1))
        theta = MathTex(r'\theta ', color=RED).rotate(90 * DEGREES, RIGHT).move_to(axes.c2p(0.25, 0, 0.1))
        expasfunoftime = MathTex(r'c \hspace{0.6 mm} e^{j(wt+\phi)}').rotate(90 * DEGREES, RIGHT).move_to(
            axes.c2p(1, 0, 1))
        expasfunoftimemoving = always_redraw(
            lambda: MathTex(r'c \hspace{0.6 mm} e^{j(w *  %0.1f +\phi)}' % tvalue.get_value()).rotate(90 * DEGREES,
                                                                                                      RIGHT).move_to(
                axes.c2p(1, 0, 1)))
        euler_formula = MathTex(r'e^{j \omega  t} = cos(\omega  t)+j \hspace{0.7 mm} sin(\omega  t)')

        # vect = always_redraw(lambda: Arrow3D(axes.get_origin(), ce.get_points()[500], stroke_width=0.5, color=RED))
        vect1 = always_redraw(lambda: Arrow3D(axes.get_origin(), dot1.get_center(), stroke_width=0.5, color=PINK))
        vect2 = always_redraw(lambda: Arrow3D(axes.get_origin(), dot2.get_center(), stroke_width=0.5, color=PINK))
        dot_start1 = always_redraw(lambda: Dot3D(ce1.get_start(), color=RED))
        dot_start2 = always_redraw(lambda: Dot3D(ce2.get_start(), color=YELLOW))
        vect_start1 = always_redraw(
            lambda: Arrow3D(axes.get_origin(), dot_start1.get_center(), stroke_width=0.5, color=RED))
        vect_start2 = always_redraw(
            lambda: Arrow3D(axes.get_origin(), dot_start2.get_center(), stroke_width=0.5, color=YELLOW))

        # ___________________________________________________________________________________________
        # ce1 = always_redraw(lambda: axes.plot_parametric_curve(lambda t: [np.real(np.exp(1j * (2 * np.pi * 0.3 * t))), t, np.imag(np.exp(1j * (2 * np.pi * 0.3 * t)))],stroke_width=2, color=RED, t_range=np.array([0, head_tracker.get_value(), 0.01])))
        # ce2 = always_redraw(lambda: axes.plot_parametric_curve(lambda t: [np.real(np.exp(1j * (2 * np.pi * 0.3 * t + phs_tracker.get_value()))), t,np.imag(np.exp(1j * (2 * np.pi * 0.3 * t + phs_tracker.get_value())))], stroke_width=2,color=YELLOW, t_range=np.array([0, head_tracker.get_value(), 0.01])))
        # ___________________________________________________________________________________________

        # self.add(numberplane, axes, ce1, ce2, dot1, dot2)
        # self.wait()
        # self.play(head_tracker.animate.set_value(10), run_time=20, rate_func=rate_functions.linear)
        # self.wait()

        # self.add(numberplane, axes)
        # self.play(FadeIn(dot_start2,vect_start2))
        # self.wait()
        # self.play(FadeIn(ce2,dot2))
        # self.wait()
        # self.play(head_tracker.animate.set_value(10), run_time=10, rate_func=rate_functions.linear)
        # self.wait()

        # self.add(numberplane, axes, dot_start2, vect_start2, ce2, dot2)
        # self.play(FadeOut(dot2))
        # self.wait()

        # self.add(numberplane, axes, ce1,ce2, vect_start2, dot_start2,dot_start1,vect_start1)
        # vect_start1.set_stroke(opacity=0.2).scale(5)
        # vect_start2.set_stroke(opacity=0.2).scale(5)

        self.add(numberplane, axes, xy_plane)
        self.play(Create(ce1),FadeIn(dot_start1))
        self.wait()
        self.play(Create(ce2),FadeIn(dot_start2))
        self.wait()
        # self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.58, run_time=2)
        # self.wait(vect_start1.animate().set_stroke(opacity=1).scale(0.2))
        # self.wait(vect_start2.animate().set_stroke(opacity=1).scale(0.2))
        self.play(FadeIn(vect_start1))
        self.play(FadeIn(vect_start2))
        self.wait()

        # self.wait()
        # self.play(amp_tracker.animate.set_value(1.5))
        # self.play(amp_tracker.animate.set_value(1))
        # self.wait()
        #
        # self.play(phs_tracker.animate.set_value(2))
        # self.play(phs_tracker.animate.set_value(0.8))
        # self.wait()

        # self.add(axes,ce,dot)

        # self.play(Create(numberplane))
        # self.play(Create(axes))
        # self.wait()
        # self.play(Write(expTheta))
        # self.play(FadeIn(dot))
        # self.wait()
        # self.play(ReplacementTransform(expTheta[0].copy(),vect),ReplacementTransform(expTheta[2].copy(),theta))
        # self.wait()
        # self.play(ReplacementTransform(theta,expTheta[2]))
        # self.wait()

        # self.add(numberplane, axes, expTheta, vect, dot)
        # self.wait()
        # self.play(FadeOut(expTheta,vect),FadeIn(ce))
        # self.remove(dot)
        # self.add(dot)
        # self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.58, added_anims=[axes.x_axis.animate.rotate(90*DEGREES,[1,0,0])],run_time=2)
        # self.wait()

        # self.add(numberplane,axes,expTheta,vect,ce,dot)
        # self.wait()
        # self.play(FadeOut(vect))
        # self.play(head_tracker.animate.set_value(10), run_time=25,rate_func=rate_functions.linear)
        # self.wait()

        # self.add(numberplane, axes,ce, dot)
        # self.play(FadeOut(dot))
        # self.play(FadeIn(dot_start),FadeIn(vect_start))
        # self.play(phs_tracker.animate.set_value(6.28),run_time=4)
        # self.wait()
        # self.play(phs_tracker.animate.set_value(0.5), run_time=4)
        # self.wait()




class Ind(ThreeDScene):
    def construct(self):
        self.camera.background_color = "#101010"

        axes = ThreeDAxes(x_range=[-1.5, 1.5, 0.25], y_range=[0, 10.3, 2], z_range=[-1.5, 1.5, 0.25], x_length=9, z_length=9, y_length=15)
        numberplane = NumberPlane(x_range=[-1.5, 1.5, 0.25], y_range=[-1.5, 1.5, 0.25], x_length=9, y_length=9,
                                  background_line_style={
                                      "stroke_color": BLUE,
                                      "stroke_width": 0.7,
                                      "stroke_opacity": 1,}).rotate(90 * DEGREES, RIGHT).move_to(axes.get_origin())
        #___________________________________________________________________
        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.58)  # 3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        # axes.y_axis.rotate(90*DEGREES,[0,1,0])
        # axes.z_axis.rotate(-90*DEGREES,[0,0,1])
        self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7)  # xz plane
        axes.x_axis.rotate(90 * DEGREES, [1, 0, 0])
        # self.set_camera_orientation(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.6)  #yx
        #___________________________________________________________________

        xy_plane = TheSiGuy_lib.xy_plane(axes)




        tvalue = ValueTracker(1)
        head_tracker = ValueTracker(0.001)
        amp_tracker=ValueTracker(1)
        ce1=always_redraw(lambda : axes.plot_parametric_curve(lambda t: [0.6*np.real(  np.exp(1j * (2 * np.pi * 0.3 * t+0.7 ))),t,0.6*np.imag(np.exp(1j * (2 * np.pi * 0.3 * t+0.7 )))], stroke_width=2, color=RED, t_range=np.array([0, head_tracker.get_value(), 0.01])))
        phs_tracker = ValueTracker(0.8)
        ce2=always_redraw(lambda : axes.plot_parametric_curve(lambda t: [np.real(  np.exp(1j * (2 * np.pi * 0.3 * t +2.27))),t,np.imag(np.exp(1j * (2 * np.pi * 0.3 * t +2.27)))], stroke_width=2, color=YELLOW, t_range=np.array([0, head_tracker.get_value(), 0.01])))
        dot1 = always_redraw(lambda: Dot3D(ce1.get_end(),color=RED).scale(1.5))
        dot2 = always_redraw(lambda: Dot3D(ce2.get_end(),color=YELLOW).scale(1.5))
        expTheta = MathTex(r'c \hspace{0.6 mm}', r'e^{j ', r'(wt+\phi) }').scale(1.2).rotate(90 * DEGREES, RIGHT).move_to(axes.c2p(1, 0, 1))
        theta = MathTex(r'\theta ', color=RED).rotate(90 * DEGREES, RIGHT).move_to(axes.c2p(0.25, 0, 0.1))
        expasfunoftime = MathTex(r'c \hspace{0.6 mm} e^{j(wt+\phi)}').rotate(90 * DEGREES, RIGHT).move_to(axes.c2p(1, 0, 1))
        expasfunoftimemoving = always_redraw(lambda: MathTex(r'c \hspace{0.6 mm} e^{j(w *  %0.1f +\phi)}' % tvalue.get_value()).rotate(90 * DEGREES, RIGHT).move_to(axes.c2p(1, 0, 1)))
        euler_formula = MathTex(r'e^{j \omega  t} = cos(\omega  t)+j \hspace{0.7 mm} sin(\omega  t)')

        # vect = always_redraw(lambda: Arrow3D(axes.get_origin(), ce.get_points()[500], stroke_width=0.5, color=RED))
        vect1 = always_redraw(lambda: Arrow3D(axes.get_origin(), dot1.get_center(), stroke_width=0.5, color=PINK))
        vect2 = always_redraw(lambda: Arrow3D(axes.get_origin(), dot2.get_center(), stroke_width=0.5, color=PINK))
        dot_start1=always_redraw(lambda : Dot3D(ce1.get_start(),color=RED))
        dot_start2=always_redraw(lambda : Dot3D(ce2.get_start(),color=YELLOW))
        vect_start1 = always_redraw(lambda: Arrow3D(axes.get_origin(), dot_start1.get_center(), stroke_width=0.5, color=RED))
        vect_start2 = always_redraw(lambda: Arrow3D(axes.get_origin(), dot_start2.get_center(), stroke_width=0.5, color=YELLOW))



#___________________________________________________________________________________________
        # ce1 = always_redraw(lambda: axes.plot_parametric_curve(lambda t: [np.real(np.exp(1j * (2 * np.pi * 0.3 * t))), t, np.imag(np.exp(1j * (2 * np.pi * 0.3 * t)))],stroke_width=2, color=RED, t_range=np.array([0, head_tracker.get_value(), 0.01])))
        # ce2 = always_redraw(lambda: axes.plot_parametric_curve(lambda t: [np.real(np.exp(1j * (2 * np.pi * 0.3 * t + phs_tracker.get_value()))), t,np.imag(np.exp(1j * (2 * np.pi * 0.3 * t + phs_tracker.get_value())))], stroke_width=2,color=YELLOW, t_range=np.array([0, head_tracker.get_value(), 0.01])))
#___________________________________________________________________________________________







        # self.add(numberplane, axes, ce1, ce2, dot1, dot2)
        # self.wait()
        # self.play(head_tracker.animate.set_value(10), run_time=20, rate_func=rate_functions.linear)
        # self.wait()

        # self.add(numberplane, axes)
        # self.play(FadeIn(dot_start2,vect_start2))
        # self.wait()
        # self.play(FadeIn(ce2,dot2))
        # self.wait()
        # self.play(head_tracker.animate.set_value(10), run_time=10, rate_func=rate_functions.linear)
        # self.wait()

        # self.add(numberplane, axes, dot_start2, vect_start2, ce2, dot2)
        # self.play(FadeOut(dot2))
        # self.wait()

        # self.add(numberplane, axes, ce1,ce2, vect_start2, dot_start2,dot_start1,vect_start1)
        # vect_start1.set_stroke(opacity=0.2).scale(5)
        # vect_start2.set_stroke(opacity=0.2).scale(5)

        self.add(numberplane,axes,xy_plane)
        self.play(FadeIn(dot_start1,ce1,vect_start1))
        self.play(FadeIn(dot_start2,ce2,vect_start2))
        self.wait(0.5)
        self.play(head_tracker.animate.set_value(10), run_time=10, rate_func=rate_functions.linear)
        self.wait()
        # self.play(Create(ce1))
        # self.wait()
        # self.play(Create(ce2))
        # self.wait()
        # self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.58,run_time=2)
        # # self.wait(vect_start1.animate().set_stroke(opacity=1).scale(0.2))
        # # self.wait(vect_start2.animate().set_stroke(opacity=1).scale(0.2))
        # self.play(FadeIn(vect_start1))
        # self.play(FadeIn(vect_start2))
        # self.wait()








        # self.wait()
        # self.play(amp_tracker.animate.set_value(1.5))
        # self.play(amp_tracker.animate.set_value(1))
        # self.wait()
        #
        # self.play(phs_tracker.animate.set_value(2))
        # self.play(phs_tracker.animate.set_value(0.8))
        # self.wait()




        # self.add(axes,ce,dot)

        # self.play(Create(numberplane))
        # self.play(Create(axes))
        # self.wait()
        # self.play(Write(expTheta))
        # self.play(FadeIn(dot))
        # self.wait()
        # self.play(ReplacementTransform(expTheta[0].copy(),vect),ReplacementTransform(expTheta[2].copy(),theta))
        # self.wait()
        # self.play(ReplacementTransform(theta,expTheta[2]))
        # self.wait()

        # self.add(numberplane, axes, expTheta, vect, dot)
        # self.wait()
        # self.play(FadeOut(expTheta,vect),FadeIn(ce))
        # self.remove(dot)
        # self.add(dot)
        # self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.58, added_anims=[axes.x_axis.animate.rotate(90*DEGREES,[1,0,0])],run_time=2)
        # self.wait()

        # self.add(numberplane,axes,expTheta,vect,ce,dot)
        # self.wait()
        # self.play(FadeOut(vect))
        # self.play(head_tracker.animate.set_value(10), run_time=25,rate_func=rate_functions.linear)
        # self.wait()

        # self.add(numberplane, axes,ce, dot)
        # self.play(FadeOut(dot))
        # self.play(FadeIn(dot_start),FadeIn(vect_start))
        # self.play(phs_tracker.animate.set_value(6.28),run_time=4)
        # self.wait()
        # self.play(phs_tracker.animate.set_value(0.5), run_time=4)
        # self.wait()






class Ind2(ThreeDScene):
    def construct(self):
        self.camera.background_color = "#101010"

        axes = ThreeDAxes(x_range=[-1.5, 1.5, 0.25], y_range=[0, 10.3, 2], z_range=[-1.5, 1.5, 0.25], x_length=9, z_length=9, y_length=15)
        numberplane = NumberPlane(x_range=[-1.5, 1.5, 0.25], y_range=[-1.5, 1.5, 0.25], x_length=9, y_length=9,
                                  background_line_style={
                                      "stroke_color": BLUE,
                                      "stroke_width": 0.7,
                                      "stroke_opacity": 1,}).rotate(90 * DEGREES, RIGHT).move_to(axes.get_origin())
        #___________________________________________________________________
        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.58)  # 3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        # axes.y_axis.rotate(90*DEGREES,[0,1,0])
        # axes.z_axis.rotate(-90*DEGREES,[0,0,1])
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7)  # xz plane
        # axes.x_axis.rotate(90 * DEGREES, [1, 0, 0])
        # self.set_camera_orientation(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.6)  #yx
        #___________________________________________________________________

        xy_plane = TheSiGuy_lib.xy_plane(axes)




        tvalue = ValueTracker(1)
        head_tracker = ValueTracker(0.001)
        amp_tracker=ValueTracker(1)
        ce1=always_redraw(lambda : axes.plot_parametric_curve(lambda t: [0.6*np.real(  np.exp(1j * (2 * np.pi * 0.3 * t+0.7 ))),t,0.6*np.imag(np.exp(1j * (2 * np.pi * 0.3 * t+0.7 )))], stroke_width=2, color=RED, t_range=np.array([0, head_tracker.get_value(), 0.01])))
        phs_tracker = ValueTracker(0.8)
        ce2=always_redraw(lambda : axes.plot_parametric_curve(lambda t: [np.real(  np.exp(1j * (2 * np.pi * 0.3 * t +2.27))),t,np.imag(np.exp(1j * (2 * np.pi * 0.3 * t +2.27)))], stroke_width=2, color=YELLOW, t_range=np.array([0, head_tracker.get_value(), 0.01])))
        dot1 = always_redraw(lambda: Dot3D(ce1.get_end(),color=RED).scale(1.5))
        dot2 = always_redraw(lambda: Dot3D(ce2.get_end(),color=YELLOW).scale(1.5))
        expTheta = MathTex(r'c \hspace{0.6 mm}', r'e^{j ', r'(wt+\phi) }').scale(1.2).rotate(90 * DEGREES, RIGHT).move_to(axes.c2p(1, 0, 1))
        theta = MathTex(r'\theta ', color=RED).rotate(90 * DEGREES, RIGHT).move_to(axes.c2p(0.25, 0, 0.1))
        expasfunoftime = MathTex(r'c \hspace{0.6 mm} e^{j(wt+\phi)}').rotate(90 * DEGREES, RIGHT).move_to(axes.c2p(1, 0, 1))
        expasfunoftimemoving = always_redraw(lambda: MathTex(r'c \hspace{0.6 mm} e^{j(w *  %0.1f +\phi)}' % tvalue.get_value()).rotate(90 * DEGREES, RIGHT).move_to(axes.c2p(1, 0, 1)))
        euler_formula = MathTex(r'e^{j \omega  t} = cos(\omega  t)+j \hspace{0.7 mm} sin(\omega  t)')

        # vect = always_redraw(lambda: Arrow3D(axes.get_origin(), ce.get_points()[500], stroke_width=0.5, color=RED))
        vect1 = always_redraw(lambda: Arrow3D(axes.get_origin(), dot1.get_center(), stroke_width=0.5, color=PINK))
        vect2 = always_redraw(lambda: Arrow3D(axes.get_origin(), dot2.get_center(), stroke_width=0.5, color=PINK))
        dot_start1=always_redraw(lambda : Dot3D(ce1.get_start(),color=RED))
        dot_start2=always_redraw(lambda : Dot3D(ce2.get_start(),color=YELLOW))
        vect_start1 = always_redraw(lambda: Arrow3D(axes.get_origin(), dot_start1.get_center(), stroke_width=0.5, color=RED))
        vect_start2 = always_redraw(lambda: Arrow3D(axes.get_origin(), dot_start2.get_center(), stroke_width=0.5, color=YELLOW))



#___________________________________________________________________________________________
        # ce1 = always_redraw(lambda: axes.plot_parametric_curve(lambda t: [np.real(np.exp(1j * (2 * np.pi * 0.3 * t))), t, np.imag(np.exp(1j * (2 * np.pi * 0.3 * t)))],stroke_width=2, color=RED, t_range=np.array([0, head_tracker.get_value(), 0.01])))
        # ce2 = always_redraw(lambda: axes.plot_parametric_curve(lambda t: [np.real(np.exp(1j * (2 * np.pi * 0.3 * t + phs_tracker.get_value()))), t,np.imag(np.exp(1j * (2 * np.pi * 0.3 * t + phs_tracker.get_value())))], stroke_width=2,color=YELLOW, t_range=np.array([0, head_tracker.get_value(), 0.01])))
#___________________________________________________________________________________________







        # self.add(numberplane, axes, ce1, ce2, dot1, dot2)
        # self.wait()
        # self.play(head_tracker.animate.set_value(10), run_time=20, rate_func=rate_functions.linear)
        # self.wait()

        # self.add(numberplane, axes)
        # self.play(FadeIn(dot_start2,vect_start2))
        # self.wait()
        # self.play(FadeIn(ce2,dot2))
        # self.wait()
        # self.play(head_tracker.animate.set_value(10), run_time=10, rate_func=rate_functions.linear)
        # self.wait()

        # self.add(numberplane, axes, dot_start2, vect_start2, ce2, dot2)
        # self.play(FadeOut(dot2))
        # self.wait()

        # self.add(numberplane, axes, ce1,ce2, vect_start2, dot_start2,dot_start1,vect_start1)
        # vect_start1.set_stroke(opacity=0.2).scale(5)
        # vect_start2.set_stroke(opacity=0.2).scale(5)

        self.add(numberplane,axes,xy_plane)
        self.play(FadeIn(dot_start1,ce1,vect_start1))
        self.play(FadeIn(dot_start2,ce2,vect_start2))
        self.wait(0.5)
        self.play(head_tracker.animate.set_value(10), run_time=10, rate_func=rate_functions.linear)
        self.wait()
        # self.play(Create(ce1))
        # self.wait()
        # self.play(Create(ce2))
        # self.wait()
        # self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.58,run_time=2)
        # # self.wait(vect_start1.animate().set_stroke(opacity=1).scale(0.2))
        # # self.wait(vect_start2.animate().set_stroke(opacity=1).scale(0.2))
        # self.play(FadeIn(vect_start1))
        # self.play(FadeIn(vect_start2))
        # self.wait()








        # self.wait()
        # self.play(amp_tracker.animate.set_value(1.5))
        # self.play(amp_tracker.animate.set_value(1))
        # self.wait()
        #
        # self.play(phs_tracker.animate.set_value(2))
        # self.play(phs_tracker.animate.set_value(0.8))
        # self.wait()




        # self.add(axes,ce,dot)

        # self.play(Create(numberplane))
        # self.play(Create(axes))
        # self.wait()
        # self.play(Write(expTheta))
        # self.play(FadeIn(dot))
        # self.wait()
        # self.play(ReplacementTransform(expTheta[0].copy(),vect),ReplacementTransform(expTheta[2].copy(),theta))
        # self.wait()
        # self.play(ReplacementTransform(theta,expTheta[2]))
        # self.wait()

        # self.add(numberplane, axes, expTheta, vect, dot)
        # self.wait()
        # self.play(FadeOut(expTheta,vect),FadeIn(ce))
        # self.remove(dot)
        # self.add(dot)
        # self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.58, added_anims=[axes.x_axis.animate.rotate(90*DEGREES,[1,0,0])],run_time=2)
        # self.wait()

        # self.add(numberplane,axes,expTheta,vect,ce,dot)
        # self.wait()
        # self.play(FadeOut(vect))
        # self.play(head_tracker.animate.set_value(10), run_time=25,rate_func=rate_functions.linear)
        # self.wait()

        # self.add(numberplane, axes,ce, dot)
        # self.play(FadeOut(dot))
        # self.play(FadeIn(dot_start),FadeIn(vect_start))
        # self.play(phs_tracker.animate.set_value(6.28),run_time=4)
        # self.wait()
        # self.play(phs_tracker.animate.set_value(0.5), run_time=4)
        # self.wait()






class Cap1(ThreeDScene):
    def construct(self):
        self.camera.background_color = "#101010"

        axes = ThreeDAxes(x_range=[-1.5, 1.5, 0.25], y_range=[0, 10.3, 2], z_range=[-1.5, 1.5, 0.25], x_length=9, z_length=9, y_length=15)
        numberplane = NumberPlane(x_range=[-1.5, 1.5, 0.25], y_range=[-1.5, 1.5, 0.25], x_length=9, y_length=9,
                                  background_line_style={
                                      "stroke_color": BLUE,
                                      "stroke_width": 0.7,
                                      "stroke_opacity": 1,}).rotate(90 * DEGREES, RIGHT).move_to(axes.get_origin())
        #___________________________________________________________________
        # self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.58)  # 3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        # axes.y_axis.rotate(90*DEGREES,[0,1,0])
        # axes.z_axis.rotate(-90*DEGREES,[0,0,1])
        self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7)  # xz plane
        axes.x_axis.rotate(90 * DEGREES, [1, 0, 0])
        # self.set_camera_orientation(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.6)  #yx
        #___________________________________________________________________

        xy_plane = TheSiGuy_lib.xy_plane(axes)




        tvalue = ValueTracker(1)
        head_tracker = ValueTracker(0.001)
        amp_tracker=ValueTracker(1)
        ce1=always_redraw(lambda : axes.plot_parametric_curve(lambda t: [np.real(  np.exp(1j * (2 * np.pi * 0.3 * t+2.27 ))),t,np.imag(np.exp(1j * (2 * np.pi * 0.3 * t +2.27)))], stroke_width=2, color=RED, t_range=np.array([0, head_tracker.get_value(), 0.01])))
        phs_tracker = ValueTracker(0.8)
        ce2=always_redraw(lambda : axes.plot_parametric_curve(lambda t: [0.6*np.real(  np.exp(1j * (2 * np.pi * 0.3 * t +0.7))),t,0.6*np.imag(np.exp(1j * (2 * np.pi * 0.3 * t +0.7)))], stroke_width=2, color=YELLOW, t_range=np.array([0, head_tracker.get_value(), 0.01])))
        dot1 = always_redraw(lambda: Dot3D(ce1.get_end(),color=RED).scale(1.5))
        dot2 = always_redraw(lambda: Dot3D(ce2.get_end(),color=YELLOW).scale(1.5))
        expTheta = MathTex(r'c \hspace{0.6 mm}', r'e^{j ', r'(wt+\phi) }').scale(1.2).rotate(90 * DEGREES, RIGHT).move_to(axes.c2p(1, 0, 1))
        theta = MathTex(r'\theta ', color=RED).rotate(90 * DEGREES, RIGHT).move_to(axes.c2p(0.25, 0, 0.1))
        expasfunoftime = MathTex(r'c \hspace{0.6 mm} e^{j(wt+\phi)}').rotate(90 * DEGREES, RIGHT).move_to(axes.c2p(1, 0, 1))
        expasfunoftimemoving = always_redraw(lambda: MathTex(r'c \hspace{0.6 mm} e^{j(w *  %0.1f +\phi)}' % tvalue.get_value()).rotate(90 * DEGREES, RIGHT).move_to(axes.c2p(1, 0, 1)))
        euler_formula = MathTex(r'e^{j \omega  t} = cos(\omega  t)+j \hspace{0.7 mm} sin(\omega  t)')

        # vect = always_redraw(lambda: Arrow3D(axes.get_origin(), ce.get_points()[500], stroke_width=0.5, color=RED))
        vect1 = always_redraw(lambda: Arrow3D(axes.get_origin(), dot1.get_center(), stroke_width=0.5, color=PINK))
        vect2 = always_redraw(lambda: Arrow3D(axes.get_origin(), dot2.get_center(), stroke_width=0.5, color=PINK))
        dot_start1=always_redraw(lambda : Dot3D(ce1.get_start(),color=RED))
        dot_start2=always_redraw(lambda : Dot3D(ce2.get_start(),color=YELLOW))
        vect_start1 = always_redraw(lambda: Arrow3D(axes.get_origin(), dot_start1.get_center(), stroke_width=0.5, color=RED))
        vect_start2 = always_redraw(lambda: Arrow3D(axes.get_origin(), dot_start2.get_center(), stroke_width=0.5, color=YELLOW))



#___________________________________________________________________________________________
        # ce1 = always_redraw(lambda: axes.plot_parametric_curve(lambda t: [np.real(np.exp(1j * (2 * np.pi * 0.3 * t))), t, np.imag(np.exp(1j * (2 * np.pi * 0.3 * t)))],stroke_width=2, color=RED, t_range=np.array([0, head_tracker.get_value(), 0.01])))
        # ce2 = always_redraw(lambda: axes.plot_parametric_curve(lambda t: [np.real(np.exp(1j * (2 * np.pi * 0.3 * t + phs_tracker.get_value()))), t,np.imag(np.exp(1j * (2 * np.pi * 0.3 * t + phs_tracker.get_value())))], stroke_width=2,color=YELLOW, t_range=np.array([0, head_tracker.get_value(), 0.01])))
#___________________________________________________________________________________________







        # self.add(numberplane, axes, ce1, ce2, dot1, dot2)
        # self.wait()
        # self.play(head_tracker.animate.set_value(10), run_time=20, rate_func=rate_functions.linear)
        # self.wait()

        # self.add(numberplane, axes)
        # self.play(FadeIn(dot_start2,vect_start2))
        # self.wait()
        # self.play(FadeIn(ce2,dot2))
        # self.wait()
        # self.play(head_tracker.animate.set_value(10), run_time=10, rate_func=rate_functions.linear)
        # self.wait()

        # self.add(numberplane, axes, dot_start2, vect_start2, ce2, dot2)
        # self.play(FadeOut(dot2))
        # self.wait()

        # self.add(numberplane, axes, ce1,ce2, vect_start2, dot_start2,dot_start1,vect_start1)
        # vect_start1.set_stroke(opacity=0.2).scale(5)
        # vect_start2.set_stroke(opacity=0.2).scale(5)

        self.add(numberplane,axes,xy_plane)
        self.play(FadeIn(dot_start1,ce1,vect_start1))
        self.play(FadeIn(dot_start2,ce2,vect_start2))
        self.wait(0.5)
        self.play(head_tracker.animate.set_value(10), run_time=10, rate_func=rate_functions.linear)
        self.wait()
        # self.play(Create(ce1))
        # self.wait()
        # self.play(Create(ce2))
        # self.wait()
        # self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.58,run_time=2)
        # # self.wait(vect_start1.animate().set_stroke(opacity=1).scale(0.2))
        # # self.wait(vect_start2.animate().set_stroke(opacity=1).scale(0.2))
        # self.play(FadeIn(vect_start1))
        # self.play(FadeIn(vect_start2))
        # self.wait()








        # self.wait()
        # self.play(amp_tracker.animate.set_value(1.5))
        # self.play(amp_tracker.animate.set_value(1))
        # self.wait()
        #
        # self.play(phs_tracker.animate.set_value(2))
        # self.play(phs_tracker.animate.set_value(0.8))
        # self.wait()




        # self.add(axes,ce,dot)

        # self.play(Create(numberplane))
        # self.play(Create(axes))
        # self.wait()
        # self.play(Write(expTheta))
        # self.play(FadeIn(dot))
        # self.wait()
        # self.play(ReplacementTransform(expTheta[0].copy(),vect),ReplacementTransform(expTheta[2].copy(),theta))
        # self.wait()
        # self.play(ReplacementTransform(theta,expTheta[2]))
        # self.wait()

        # self.add(numberplane, axes, expTheta, vect, dot)
        # self.wait()
        # self.play(FadeOut(expTheta,vect),FadeIn(ce))
        # self.remove(dot)
        # self.add(dot)
        # self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.58, added_anims=[axes.x_axis.animate.rotate(90*DEGREES,[1,0,0])],run_time=2)
        # self.wait()

        # self.add(numberplane,axes,expTheta,vect,ce,dot)
        # self.wait()
        # self.play(FadeOut(vect))
        # self.play(head_tracker.animate.set_value(10), run_time=25,rate_func=rate_functions.linear)
        # self.wait()

        # self.add(numberplane, axes,ce, dot)
        # self.play(FadeOut(dot))
        # self.play(FadeIn(dot_start),FadeIn(vect_start))
        # self.play(phs_tracker.animate.set_value(6.28),run_time=4)
        # self.wait()
        # self.play(phs_tracker.animate.set_value(0.5), run_time=4)
        # self.wait()






class Cap2(ThreeDScene):
    def construct(self):
        self.camera.background_color = "#101010"

        axes = ThreeDAxes(x_range=[-1.5, 1.5, 0.25], y_range=[0, 10.3, 2], z_range=[-1.5, 1.5, 0.25], x_length=9, z_length=9, y_length=15)
        numberplane = NumberPlane(x_range=[-1.5, 1.5, 0.25], y_range=[-1.5, 1.5, 0.25], x_length=9, y_length=9,
                                  background_line_style={
                                      "stroke_color": BLUE,
                                      "stroke_width": 0.7,
                                      "stroke_opacity": 1,}).rotate(90 * DEGREES, RIGHT).move_to(axes.get_origin())
        #___________________________________________________________________
        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.58)  # 3d view
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.7)     #yz plane
        # axes.y_axis.rotate(90*DEGREES,[0,1,0])
        # axes.z_axis.rotate(-90*DEGREES,[0,0,1])
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, focal_distance=1000, zoom=0.7)  # xz plane
        # axes.x_axis.rotate(90 * DEGREES, [1, 0, 0])
        # self.set_camera_orientation(phi=180 * DEGREES, theta=0 * DEGREES, focal_distance=1000, zoom=0.6)  #yx
        #___________________________________________________________________

        xy_plane = TheSiGuy_lib.xy_plane(axes)




        tvalue = ValueTracker(1)
        head_tracker = ValueTracker(0.001)
        amp_tracker=ValueTracker(1)
        ce1 = always_redraw(lambda: axes.plot_parametric_curve(
            lambda t: [np.real(np.exp(1j * (2 * np.pi * 0.3 * t + 2.27))), t,
                       np.imag(np.exp(1j * (2 * np.pi * 0.3 * t + 2.27)))], stroke_width=2, color=RED,
            t_range=np.array([0, head_tracker.get_value(), 0.01])))
        phs_tracker = ValueTracker(0.8)
        ce2 = always_redraw(lambda: axes.plot_parametric_curve(
            lambda t: [0.6 * np.real(np.exp(1j * (2 * np.pi * 0.3 * t + 0.7))), t,
                       0.6 * np.imag(np.exp(1j * (2 * np.pi * 0.3 * t + 0.7)))], stroke_width=2, color=YELLOW,
            t_range=np.array([0, head_tracker.get_value(), 0.01])))
        dot1 = always_redraw(lambda: Dot3D(ce1.get_end(),color=RED).scale(1.5))
        dot2 = always_redraw(lambda: Dot3D(ce2.get_end(),color=YELLOW).scale(1.5))
        expTheta = MathTex(r'c \hspace{0.6 mm}', r'e^{j ', r'(wt+\phi) }').scale(1.2).rotate(90 * DEGREES, RIGHT).move_to(axes.c2p(1, 0, 1))
        theta = MathTex(r'\theta ', color=RED).rotate(90 * DEGREES, RIGHT).move_to(axes.c2p(0.25, 0, 0.1))
        expasfunoftime = MathTex(r'c \hspace{0.6 mm} e^{j(wt+\phi)}').rotate(90 * DEGREES, RIGHT).move_to(axes.c2p(1, 0, 1))
        expasfunoftimemoving = always_redraw(lambda: MathTex(r'c \hspace{0.6 mm} e^{j(w *  %0.1f +\phi)}' % tvalue.get_value()).rotate(90 * DEGREES, RIGHT).move_to(axes.c2p(1, 0, 1)))
        euler_formula = MathTex(r'e^{j \omega  t} = cos(\omega  t)+j \hspace{0.7 mm} sin(\omega  t)')

        # vect = always_redraw(lambda: Arrow3D(axes.get_origin(), ce.get_points()[500], stroke_width=0.5, color=RED))
        vect1 = always_redraw(lambda: Arrow3D(axes.get_origin(), dot1.get_center(), stroke_width=0.5, color=PINK))
        vect2 = always_redraw(lambda: Arrow3D(axes.get_origin(), dot2.get_center(), stroke_width=0.5, color=PINK))
        dot_start1=always_redraw(lambda : Dot3D(ce1.get_start(),color=RED))
        dot_start2=always_redraw(lambda : Dot3D(ce2.get_start(),color=YELLOW))
        vect_start1 = always_redraw(lambda: Arrow3D(axes.get_origin(), dot_start1.get_center(), stroke_width=0.5, color=RED))
        vect_start2 = always_redraw(lambda: Arrow3D(axes.get_origin(), dot_start2.get_center(), stroke_width=0.5, color=YELLOW))



#___________________________________________________________________________________________
        # ce1 = always_redraw(lambda: axes.plot_parametric_curve(lambda t: [np.real(np.exp(1j * (2 * np.pi * 0.3 * t))), t, np.imag(np.exp(1j * (2 * np.pi * 0.3 * t)))],stroke_width=2, color=RED, t_range=np.array([0, head_tracker.get_value(), 0.01])))
        # ce2 = always_redraw(lambda: axes.plot_parametric_curve(lambda t: [np.real(np.exp(1j * (2 * np.pi * 0.3 * t + phs_tracker.get_value()))), t,np.imag(np.exp(1j * (2 * np.pi * 0.3 * t + phs_tracker.get_value())))], stroke_width=2,color=YELLOW, t_range=np.array([0, head_tracker.get_value(), 0.01])))
#___________________________________________________________________________________________







        # self.add(numberplane, axes, ce1, ce2, dot1, dot2)
        # self.wait()
        # self.play(head_tracker.animate.set_value(10), run_time=20, rate_func=rate_functions.linear)
        # self.wait()

        # self.add(numberplane, axes)
        # self.play(FadeIn(dot_start2,vect_start2))
        # self.wait()
        # self.play(FadeIn(ce2,dot2))
        # self.wait()
        # self.play(head_tracker.animate.set_value(10), run_time=10, rate_func=rate_functions.linear)
        # self.wait()

        # self.add(numberplane, axes, dot_start2, vect_start2, ce2, dot2)
        # self.play(FadeOut(dot2))
        # self.wait()

        # self.add(numberplane, axes, ce1,ce2, vect_start2, dot_start2,dot_start1,vect_start1)
        # vect_start1.set_stroke(opacity=0.2).scale(5)
        # vect_start2.set_stroke(opacity=0.2).scale(5)

        self.add(numberplane,axes,xy_plane)
        self.play(FadeIn(dot_start1,ce1,vect_start1))
        self.play(FadeIn(dot_start2,ce2,vect_start2))
        self.wait(0.5)
        self.play(head_tracker.animate.set_value(10), run_time=10, rate_func=rate_functions.linear)
        self.wait()
        # self.play(Create(ce1))
        # self.wait()
        # self.play(Create(ce2))
        # self.wait()
        # self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.58,run_time=2)
        # # self.wait(vect_start1.animate().set_stroke(opacity=1).scale(0.2))
        # # self.wait(vect_start2.animate().set_stroke(opacity=1).scale(0.2))
        # self.play(FadeIn(vect_start1))
        # self.play(FadeIn(vect_start2))
        # self.wait()








        # self.wait()
        # self.play(amp_tracker.animate.set_value(1.5))
        # self.play(amp_tracker.animate.set_value(1))
        # self.wait()
        #
        # self.play(phs_tracker.animate.set_value(2))
        # self.play(phs_tracker.animate.set_value(0.8))
        # self.wait()




        # self.add(axes,ce,dot)

        # self.play(Create(numberplane))
        # self.play(Create(axes))
        # self.wait()
        # self.play(Write(expTheta))
        # self.play(FadeIn(dot))
        # self.wait()
        # self.play(ReplacementTransform(expTheta[0].copy(),vect),ReplacementTransform(expTheta[2].copy(),theta))
        # self.wait()
        # self.play(ReplacementTransform(theta,expTheta[2]))
        # self.wait()

        # self.add(numberplane, axes, expTheta, vect, dot)
        # self.wait()
        # self.play(FadeOut(expTheta,vect),FadeIn(ce))
        # self.remove(dot)
        # self.add(dot)
        # self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES, focal_distance=1000, zoom=0.58, added_anims=[axes.x_axis.animate.rotate(90*DEGREES,[1,0,0])],run_time=2)
        # self.wait()

        # self.add(numberplane,axes,expTheta,vect,ce,dot)
        # self.wait()
        # self.play(FadeOut(vect))
        # self.play(head_tracker.animate.set_value(10), run_time=25,rate_func=rate_functions.linear)
        # self.wait()

        # self.add(numberplane, axes,ce, dot)
        # self.play(FadeOut(dot))
        # self.play(FadeIn(dot_start),FadeIn(vect_start))
        # self.play(phs_tracker.animate.set_value(6.28),run_time=4)
        # self.wait()
        # self.play(phs_tracker.animate.set_value(0.5), run_time=4)
        # self.wait()


class equations9(Scene):
    def construct(self):
        self.camera.background_color = "#101010"
        # phasor = MathTex(r'C \hspace{0.4 mm} \angle \phi')
        # self.play(Write(phasor))
        # self.wait()
        # phasors=Tex('TheSiGuy')
        # discur=MathTex(r'\frac{\partial \mathbf{D}}{\partial t}')
        in_cos=MathTex(r'A_i \cos (\omega t+\phi_i)')
        in_cos[0][0:2].set_color(RED)
        in_cos[0][-3:-1].set_color(BLUE)
        out_cos=MathTex(r'A_o \cos (\omega t+\phi_o)')
        out_cos[0][0:2].set_color(RED)
        out_cos[0][-3:-1].set_color(BLUE)
        # self.play(Write(discur))
        # self.wait()
        # self.add(in_cos,out_cos)

        # self.play(Write(in_cos))
        # self.play(Write(out_cos))
        self.play(Write(in_cos))
        self.wait()


class Sin(Scene):
    def construct(self):
        self.camera.background_color = "#101010"
        ax=Axes(x_length=10,y_length=3)
        sin=ax.plot(lambda t:2*np.sin(2*t),color=RED)
        self.play(Create(sin),run_time=2)
        self.wait()
