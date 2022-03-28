import numpy as np

import TheSiGuy_lib
from imports import *
class VectorSpace(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(65*DEGREES,35*DEGREES)
        ax=ThreeDAxes(x_range=[-2,10,2],y_range=[-2,10,2],z_range=[-2,10,2]).scale(0.61).move_to([0,0,0])

        xy_plane=TheSiGuy_lib.xy_plane(ax,color=YELLOW)
        xz_plane=TheSiGuy_lib.xz_plane(ax)
        yz_plane=TheSiGuy_lib.yz_plane(ax)

        xl=ax.get_x_axis_label("i")
        yl=ax.get_y_axis_label("j")
        zl=ax.get_z_axis_label("k",buff=MED_SMALL_BUFF,direction=UP).rotate(90,[0,0,1])

        x=ValueTracker(7)
        y=ValueTracker(3)
        z=ValueTracker(8)

        vector=always_redraw(lambda :  Arrow3D(ax.get_origin(),ax.c2p(x.get_value(),y.get_value(),z.get_value()),color=YELLOW))
        compx=always_redraw(lambda :  Arrow(ax.get_origin(),ax.c2p(x.get_value(),0,0),color=RED,buff=0,tip_length=0.3))
        compy=always_redraw(lambda :  Arrow(ax.get_origin(),ax.c2p(0,y.get_value(),0),color=RED,buff=0,tip_length=0.3))
        compz=always_redraw(lambda :  Arrow(ax.get_origin(),ax.c2p(0,0,z.get_value()),color=RED,buff=0,tip_length=0.3))
        ax.z_axis.rotate(90,[0,0,1])


        # self.add(ax,xy_plane,compx,compy,compz,vector,xl,yl,zl)
        self.play(Create(xy_plane), run_time=0.5)
        self.play(Create(ax),run_time=0.5)
        self.play(Write(xl),Write(yl),Write(zl),run_time=0.5)
        self.play(Create(vector),run_time=0.5)
        self.play(Create(compx),Create(compy),Create(compz),run_time=0.5)
        self.wait()
        self.play(x.animate.set_value(5),y.animate.set_value(7),z.animate.set_value(6),run_time=2)
        self.wait()
        self.play(x.animate.set_value(8),y.animate.set_value(5),run_time=2)
        self.wait()
        self.move_camera(phi=60*DEGREES,theta=10*DEGREES,run_time=1.5)
        self.wait()

class Equations(Scene):
    def construct(self):
        e4_4=MathTex(r"\vec{V}=v_{i}\vec{i}+v_{j}\vec{j}+v_{k}\vec{k}")
        e4_5=MathTex(r"\vec{i}\hspace{1 mm}.\hspace{1 mm}\vec{j}=\vec{i}\hspace{1 mm}.\hspace{1 mm}\vec{k}=\vec{k}\hspace{1 mm}.\hspace{1 mm}\vec{j} = 0",color=RED)
        e4_6=MathTex(r"\vec{i}\hspace{1 mm}.\hspace{1 mm}\vec{i}=\vec{j}\hspace{1 mm}.\hspace{1 mm}\vec{j}=\vec{k}\hspace{1 mm}.\hspace{1 mm}\vec{k}")
        e4_7i=MathTex(r"v_{i}=\frac{\vec{\hspace{0.5 mm}v\hspace{0.5 mm}}\hspace{1 mm}.\hspace{1 mm}\vec{i}}{\vec{i}\hspace{1 mm}.\hspace{1 mm}\vec{i}}=\frac{\left| \vec{V}\right|\left| \vec{\hspace{0.5 mm}i\hspace{0.5 mm}}\right|cos(\theta )}{\left| \vec{\hspace{0.5 mm}i\hspace{0.5 mm}}\right|\left| \vec{\hspace{0.5 mm}i\hspace{0.5 mm}}\right|}",color="#91EF81")
        e4_4j=MathTex(r"v_{j}=\frac{\vec{\hspace{0.5 mm}v\hspace{0.5 mm}}\hspace{1 mm}.\hspace{1 mm}\vec{j}}{\vec{j}\hspace{1 mm}.\hspace{1 mm}\vec{j}}=\frac{\left| \vec{V}\right|\left| \vec{\hspace{0.5 mm}j\hspace{0.5 mm}}\right|cos(\theta )}{\left| \vec{\hspace{0.5 mm}j\hspace{0.5 mm}}\right|\left| \vec{\hspace{0.5 mm}j\hspace{0.5 mm}}\right|}",color="#91EF81")
        e4_4k=MathTex(r"v_{k}=\frac{\vec{\hspace{0.5 mm}v\hspace{0.5 mm}}\hspace{1 mm}.\hspace{1 mm}\vec{k}}{\vec{k}\hspace{1 mm}.\hspace{1 mm}\vec{k}}=\frac{\left| \vec{V}\right|\left| \vec{\hspace{0.5 mm}k\hspace{0.5 mm}}\right|cos(\theta )}{\left| \vec{\hspace{0.5 mm}k\hspace{0.5 mm}}\right|\left| \vec{\hspace{0.5 mm}k\hspace{0.5 mm}}\right|}",color="#91EF81")
        vector_set = MathTex(r"\left\{ \vec{v_{1}},\vec{v_{2}},\vec{v_{3}},...,\vec{v_{n}}\right\}")
        vector_set_cond = MathTex(r"\vec{v_{i}}\hspace{1 mm}.\hspace{1 mm}\vec{v_{j}}=0\hspace{3 mm} for \hspace{1.5 mm} all \hspace{1.5 mm} i\neq j")

        setOfSignals=MathTex(r"\left\{ p_{1}(t),p_{2}(t),p_{3}(t),...,p_{n}(t) \right\}")
        e4_13=MathTex(r"x(t)= c_{1}p_{1}(t)+c_{2}p_{2}(t)+...+c_{n}p_{n}(t)",color='#FFD196')
        e4_14=MathTex(r"c_{n}=\frac{\int_{t_{1}}^{t_{2}}x(t)p_{n}^{\ast }(t)dt}{\int_{t_{1}}^{t_{2}}p_{n}(t)p_{n}^{\ast }(t)dt}",color='#8FFBFF')
        # e4_14=MathTex(r"")


        ijk_text=Text("where i,j and k are the three basis vectors along x,y and z respectively",font="Noto Sans",color="#91FFFB").scale(0.2)

        expSet=MathTex(r'\left\{e^{jn\omega _{o}t} \right\}',r'\hspace{1 mm} \hspace{1 mm} for \hspace{1 mm} -\infty < n< \infty ')
        expSet[0].set_color(RED)

        frep=MathTex(r'x(t)=\sum_{-\infty }^{\infty }c_{n}e^{jn\omega _{o}t}')


        expTheta=MathTex(r'e^{i \theta }')
        eq=MathTex(r'\vec{v}=c_{1}\vec{v_{1}}+c_{2}\vec{v_{2}}+...+c_{n}\vec{v_{n}}',color=RED)
        eq=MathTex(r'e^{jw_{o}t}')
        textt=Text('is a complete orthogonal set',font='Open_Sans')

        cn=MathTex(r"c_{n}=\frac{\int_{t_{1}}^{t_{2}}x(t).e^{-j\omega _{o}t}dt}{\int_{t_{1}}^{t_{2}}e^{jn\omega_{o}t}.e^{-jn\omega _{o}t}dt}").scale(2)
        cn2=MathTex(r"c_{n}= \frac{1}{T_{o}} \int_{t_{1}}^{t_{2}}x(t).e^{-j\omega _{o}t}dt").scale(2)
        norm1=MathTex(r"{\int_{\frac{-T_{o}}{2}}^{\frac{T_{0}}{2}}e^{jn\omega_{o}t}.e^{-jn\omega _{o}t}dt}").scale(2)
        norm2=MathTex(r"{\int_{\frac{-T_{o}}{2}}^{\frac{T_{o}}{2}}1\hspace{1 mm}dt}").scale(2)
        compact_trignometric=MathTex(r"x(t)=c_{0}+\sum_{n=1}^{\infty }c_{n}cos(n\omega _{o}t+\theta _{n})")
        to=MathTex(r"=T_{o}").scale(2)
        euler=MathTex(r'e^{i\omega t}=cos(\omega t)+i \hspace{0.5 mm} sin(\omega t)')
        generaltrifs=MathTex(r"x(t)=a_{0}+\sum_{n=1}^{\infty }a_{n}cos(n\omega _{o}t)+b_{n}sin(n\omega _{o}t)")

        self.play(Write(setOfSignals.scale(1.5),run_time=0.7))
        # self.add(cn)
        # self.wait()
        # self.play(Transform(cn,cn2))
        # self.play(Transform(norm1,norm2))
        self.wait()


class Vector_orthogonality(Scene):
    def construct(self):
        ax1=Axes(x_range=[-2,2,1],y_range=[-1.5,1.5,1],x_length=8,y_length=2,tips=False).shift(2.6*UP).shift(2.5*LEFT)
        ax2=Axes(x_range=[-2,2,1],y_range=[-1.5,1.5,1],x_length=8,y_length=2,tips=False).shift(2.5*LEFT)
        ax3=Axes(x_range=[-2,2,1],y_range=[-1.5,1.5,1],x_length=8,y_length=2,tips=False).shift(2.6*DOWN).shift(2.5*LEFT)

        g1=ax1.get_graph(lambda t:np.cos(2*np.pi*t),x_range=[-2,2],color=YELLOW )
        g2=ax2.get_graph(lambda t:np.cos(4*np.pi*t),x_range=[-2,2] ,color=YELLOW)
        g3=ax3.get_graph(lambda t:np.cos(2*np.pi*t)*np.cos(4*np.pi*t),x_range=[-2,2],color=RED )
        area= ax3.get_area(g3,[0,1])
        graph1_dots=VGroup()
        graph2_dots=VGroup()
        graph1_lines=VGroup()
        graph2_lines=VGroup()

        graph1_dots2=VGroup()
        graph2_dots2=VGroup()
        graph1_lines2=VGroup()
        graph2_lines2=VGroup()
        interval=ValueTracker(0.1)
        d=ValueTracker(0.5)
        for i in np.arange(-2,2,interval.get_value()):
            dot1=Dot(ax1.i2gp(i,g1)).scale(0.7)
            dot2=Dot(ax2.i2gp(i,g2)).scale(0.7)
            line1=DashedLine(ax1.c2p(i,0,0),dot1.get_center(),stroke_width=1)
            line2=DashedLine(ax2.c2p(i,0,0),dot2.get_center(),stroke_width=1)
            graph1_dots.add(dot1)
            graph2_dots.add(dot2)
            graph1_lines.add(line1)
            graph2_lines.add(line2)



        for i in np.arange(-2,2,0.02):
            dot1=Dot(ax1.i2gp(i,g1)).scale(0.7)
            dot2=Dot(ax2.i2gp(i,g2)).scale(0.7)
            line1=DashedLine(ax1.c2p(i,0,0),dot1.get_center(),stroke_width=1)
            line2=DashedLine(ax2.c2p(i,0,0),dot2.get_center(),stroke_width=1)
            graph1_dots2.add(dot1)
            graph2_dots2.add(dot2)
            graph1_lines2.add(line1)
            graph2_lines2.add(line2)

        equalSign=MathTex(r"=")
        vect1=MathTex(r"\begin{bmatrix}p(t_{1}) \\p(t_{2}) \\ \vdots \\p(t_{n}) \\ \end{bmatrix}").shift(2.5*DOWN+4*LEFT)
        vect2=MathTex(r"\begin{bmatrix}q(t_{1}) \\q(t_{2}) \\ \vdots \\q(t_{n}) \\ \end{bmatrix}").next_to(vect1,RIGHT).shift(RIGHT)
        equalSign = MathTex(r"=").next_to(vect2,RIGHT,buff=LARGE_BUFF)
        vecSum=MathTex(r"\sum p(t_{n})q(t_{n}) ").next_to(equalSign,buff=LARGE_BUFF)
        vecSumLim=MathTex(r"\displaystyle \lim_{interval \to 0} \sum p(t_{n})q(t_{n})").move_to(vecSum.get_center())
        vecInt=MathTex(r" \int  p(t)q(t)dt ").move_to(vecSum.get_center())
        veccomInt=MathTex(r"\int  p(t)q^{\ast }(t)dt ").align_to(vecInt,LEFT).move_to(vecSum.get_center())


        # self.add(ax1,ax2,g1,g2)
        # self.play(Create(ax1),Create(ax2))
        # self.play(Create(g1),Create(g2))
        # self.wait()
        # self.play(Create(graph1_dots),Create(graph2_dots),Create(graph1_lines),Create(graph2_lines))
        # self.add(vect1,vect2)


        # self.add(*graph1_lines)
        # self.add(*graph2_lines)
        # self.add(*graph1_dots)
        # self.add(*graph2_dots)
        # self.wait()
        # self.play(Transform(graph1_dots.copy(),vect1))
        # self.wait()
        # self.play(Transform(graph2_dots.copy(),vect2))
        # self.wait()
        # self.play(Write(equalSign),run_time=0.1)
        # self.play(Write(vecSum),run_time=0.7)
        # self.wait()
        # self.play(ReplacementTransform (vecSum,vecSumLim),Transform(graph1_dots,graph1_dots2),Transform(graph2_dots,graph2_dots2),Transform(graph1_lines,graph1_lines2),Transform(graph2_lines,graph2_lines2),run_time=2)
        # self.wait()
        # self.play(ReplacementTransform(vecSumLim,vecInt))
        # self.wait()
        # self.play(ReplacementTransform(vecInt,veccomInt))
        # self.wait()

        # self.wait()
        # self.play(d.animate.set_value(0.4),run_time=5,rate_func=linear)
        # self.wait()
        self.play(Create(ax1), Create(ax2))
        self.play(Create(g1),Create(g2))
        self.wait()

        self.play(Create(ax3))
        self.wait()
        self.play(Transform(g1.copy(),g3),Transform(g2.copy(),g3))
        self.wait()
        self.play(Create(area))
        self.wait()


class Complex_Exponential2(ThreeDScene):
    def construct(self):
        # self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, distance=1000)
        z_length = ValueTracker(0.1)
        ax = ThreeDAxes(x_range=[-1.5, 1.5, 0.25], y_range=[0, 27, 5], z_range=[-1.5, 1.5, 0.25], x_length=9,
                        z_length=9,y_length=12).scale(0.7)
        ax1 = Axes(x_range=[0, 30, 10], y_range=[-1.5, 1.5, 0.5], x_length=6, y_length=4).scale(0.8).shift(
            2 * DOWN + 3.5 * LEFT)
        ax2 = Axes(x_range=[0, 30, 10], y_range=[-1.5, 1.5, 0.5], x_length=6, y_length=4).scale(0.8).shift(
            2 * DOWN + 4 * RIGHT)

        xl = ax.get_x_axis_label("(x) real").scale(0.5)
        yl = ax.get_y_axis_label("(y) real").scale(0.5)
        zl = ax.get_z_axis_label("(z) real").scale(0.5)



        d3 = []
        d21 = []
        d22 = []
        df = pd.read_csv("complex_exp_pts", names=['x', 'y', 'z'])
        for ind, row in df.iterrows():
            d3List = [row.x, row.y, row.z]
            d21List = [row.y, row.x]
            d22List = [row.y, row.z]
            d3.append(d3List)
            d21.append(d21List)
            d22.append(d22List)

        pts3d = [ax.coords_to_point(*pt) for pt in d3]
        ptsd21 = [ax1.coords_to_point(*pt) for pt in d21]
        ptsd22 = [ax2.coords_to_point(*pt) for pt in d22]

        graph = always_redraw(lambda: VMobject(color=YELLOW, stroke_width=2).set_points_as_corners(pts3d))
        graph_part1=always_redraw(lambda : VMobject(color=YELLOW, stroke_width=2).set_points_as_corners(pts3d[:301]))
        graph_part2=always_redraw(lambda : VMobject(color=YELLOW, stroke_width=2).set_points_as_corners(pts3d[300:601]))
        graph_part3=always_redraw(lambda : VMobject(color=YELLOW, stroke_width=2).set_points_as_corners(pts3d[600:801]))
        graph_part4=always_redraw(lambda : VMobject(color=YELLOW, stroke_width=2).set_points_as_corners(pts3d[800:]))

        g1 = VMobject(color=RED, stroke_width=2).set_points_as_corners(ptsd21)
        g2 = VMobject(color=RED, stroke_width=2).set_points_as_corners(ptsd22)
        dot = Dot3D(graph.get_start()).scale(0.8)

        vect=always_redraw(lambda : Arrow3D(ax.get_origin(),graph.get_points()[70],stroke_width=0.5,color=RED))
        line1=Line(ax.get_origin(),dot.get_center())
        line2=Line(ax.get_origin(),ax.c2p(1,0,0))
        dot1 = Dot(g1.get_start()).scale(0.6)
        dot2 = Dot(g2.get_start()).scale(0.6)
        ax.y_axis.rotate(90*DEGREES, [0, 1, 0])
        ax.x_axis.rotate(90*DEGREES, [1, 0, 0])
        # ax.z_axis.rotate(90*DEGREES, [0, 0, 1])
        zl.rotate(90*DEGREES, [0, 0, 1])
        numberplane=NumberPlane(x_range=[-1.5,1.5,0.25],y_range=[-1.5,1.5,0.25],x_length=9,y_length=9,background_line_style = {
            "stroke_color": WHITE,
            "stroke_width": 1,
            "stroke_opacity": 0.4,
        }).scale(0.7).rotate(90*DEGREES,RIGHT).move_to(ax.get_origin())
        # angle=Angle(ax.x_axis,line1).rotate(90,RIGHT)
        expTheta = MathTex(r'1',r'e^{i ',r'\theta }').scale(1.2).rotate(90*DEGREES,RIGHT).move_to(ax.c2p(1,0,1))
        theta = MathTex(r'\theta ',color=RED).scale(0.5).rotate(90*DEGREES,RIGHT).move_to(ax.c2p(0.25,0,0.1))
        expasfunoftime=MathTex(r'e^{i \omega  t }').rotate(90*DEGREES,RIGHT).move_to(ax.c2p(1,0,1))
        tvalue=ValueTracker(0)
        expasfunoftimemoving= always_redraw(lambda :MathTex(r'e^{i \omega *  %0.1f }' % tvalue.get_value() ).rotate(90*DEGREES,RIGHT).move_to(ax.c2p(1,0,1)))
        euler_formula=MathTex(r'e^{j \omega  t} = cos(\omega  t)+j \hspace{0.7 mm} sin(\omega  t)')


        xy_plane=TheSiGuy_lib.xy_plane(color=BLUE,axis=ax)

        end_point1=ValueTracker(2)
        end_point2=ValueTracker(2)
        end_point3=ValueTracker(2)
        end_point4=ValueTracker(2)

        def create_dot_headed_path(path,tracker,color=YELLOW, stroke_width=2):
            created_path=always_redraw(lambda : VMobject(color=color,stroke_width=stroke_width).set_points_as_corners(path.points[:int(tracker.get_value())]))
            animated_dot=always_redraw(lambda : Dot3D(created_path.get_end()) )
            return created_path,animated_dot


        part1=create_dot_headed_path(graph_part1,end_point1)
        part2=create_dot_headed_path(graph_part2,end_point2)
        part3=create_dot_headed_path(graph_part3,end_point3)
        part4=create_dot_headed_path(graph_part4,end_point4)
#_________________________________________________________________
        graphh=VMobject(color=YELLOW, stroke_width=2).set_points_as_corners(pts3d)
        threeDGroup= VGroup(numberplane,ax,graphh).rotate(-90*DEGREES,RIGHT).scale(0.6).shift(1.8*UP)
        self.set_camera_orientation(phi=0*DEGREES ,theta=-90*DEGREES, distance=1000)
        self.add(threeDGroup)
        self.play(Create(ax1),Create(ax2))
        self.wait()
        self.play(Transform(graphh.copy(),g1),Transform(graphh.copy(),g2))
        self.play(FadeIn(dot.move_to(graph.get_start())),FadeIn(dot1),FadeIn(dot2),run_time=0.5)
        self.wait()
        self.play(MoveAlongPath(dot,graphh),MoveAlongPath(dot1,g1),MoveAlongPath(dot2,g2),run_time=10,rate_func=rate_functions.linear)
        self.wait()
#___________________________________________________________
        # self.add(ax1,g1,ax2,g2)



        # self.add(numberplane,ax, dot.move_to(graph.get_points()[70]),vect,expTheta,theta,graph)
        # self.add(numberplane,ax,dot,expasfunoftimemoving,graph_half2)
        # self.wait()
        # self.play(MoveAlongPath(dot,graph),tvalue.animate.set_value(25),run_time=15,rate_func=linear)
        # self.wait()
        # self.play(LaggedStart())

        # self.play(Create(numberplane))
        # self.play(Create(ax))
        # self.wait()
        # self.play(Write(expTheta),run_time=0.4)
        # self.wait()
        # self.play(ReplacementTransform(expTheta[0].copy(),vect),ReplacementTransform(expTheta[2].copy(),theta))
        # self.play(FadeIn(dot.move_to(graph.get_points()[70])))
        # self.wait()
        # self.play(FadeOut(vect),FadeOut(dot),FadeOut(theta))
        # self.wait()

        # ax.x_axis.rotate(90*DEGREES,[1,0,0])
        # ax.y_axis.rotate(90*DEGREES,[0,1,0])
        # ax.y_axis.rotate(90*DEGREES,[0,1,0])
        # ax.z_axis.rotate(90*DEGREES,[0,0,1])




        # self.play(end_point1.animate.set_value(len(graph_part1.get_points()+1)),run_time=2,rate_func=rate_functions.linear)
        # self.remove(part1[1])
        # self.add(*part2)
        # self.play(end_point2.animate.set_value(len(graph_part2.get_points() + 1)), run_time=2,rate_func=rate_functions.linear)
        # self.wait()
#____________________________________________________________________

        # self.add(numberplane, ax, expTheta)
        # self.wait()
        # self.play(ReplacementTransform(expTheta,expasfunoftime))
        # self.wait()
        # self.play(ReplacementTransform(expasfunoftime,expasfunoftimemoving),FadeIn(*part1))
        # self.remove(expTheta)
        # self.add(expasfunoftimemoving)
        # self.wait()
        # self.play(end_point1.animate().set_value(len(graph_part1.get_points()+1)),tvalue.animate().set_value(7.5),run_time=18,rate_func=rate_functions.linear)
        # self.remove(part1[1])
        # self.add(*part2)
        # self.move_camera(phi=75  * DEGREES, theta=35 * DEGREES, distance=1000,run_time=4,added_anims=[FadeOut(expasfunoftimemoving,run_time=3),Create(xy_plane,run_time=3),end_point2.animate(run_time=18,rate_func=rate_functions.linear).set_value(len(graph_part2.get_points())+1)])
        # self.remove(part2[1])
        # self.add(*part3)
        # self.move_camera(phi=180 * DEGREES, theta=0  * DEGREES, distance=1000,run_time=3,added_anims=[end_point3.animate(run_time=12,rate_func=rate_functions.linear).set_value(len(graph_part3.get_points())+1),ax.y_axis.animate(run_time=3).rotate(90*DEGREES,[0,1,0]),ax.x_axis.animate(run_time=3).rotate(90*DEGREES,[1,0,0])])
        # self.remove(part3[1])
        # self.add(*part4)
        # self.move_camera(phi=90  * DEGREES, theta=0  * DEGREES, distance=1000,run_time=3,added_anims=[end_point4.animate(run_time=12,rate_func=rate_functions.linear).set_value(len(graph_part4.get_points())+1),ax.y_axis.animate(run_time=3).rotate(90*DEGREES,[0,1,0]),ax.z_axis.animate(run_time=3).rotate(90*DEGREES,[0,0,1])])
        # self.wait(2)
        # self.move_camera(phi=75  * DEGREES, theta=35 * DEGREES, distance=1000,run_time=2,added_anims=[ax.x_axis.animate(run_time=3).rotate(90 * DEGREES, [1, 0, 0]),ax.z_axis.animate(run_time=3).rotate(90 * DEGREES, [0, 0, 1])])
        # self.wait()
        # self.move_camera(phi=90*DEGREES,theta=-90*DEGREES,distance=1000,run_time=2)
        # self.remove(part1[0],part2[0],part3[0],*part4)
        # self.add(graph)


#_________________________________________________________________


        # self.remove(part1[0], part2[0], part3[0], *part4)
        # self.add(graph)

        # self.play(Create(numberplane),Create(ax))
        # self.play(GrowArrow(vect))
        # self.play(FadeIn(dot),run_time=0.4)
        # self.wait()
        # self.play(FadeOut(vect),FadeOut(dot),run_time=0.5)
        # self.wait()
        # self.play(MoveAlongPath(dot,graph),run_time=3,rate_func=linear)
        # self.wait()

        # self.wait()
        # self.move_camera(phi=90 * DEGREES, theta=-90 * DEGREES,run_time=3,distance=1000,added_anims=[ax.x_axis.animate(run_time=2).rotate(90,[1,0,0]),xl.animate(run_time=2).rotate(90,[1,0,0])])
        # self.wait()
        # self.move_camera(phi=90 * DEGREES, theta=0 * DEGREES,run_time=3,distance=1000,added_anims=[ax.z_axis.animate.rotate(90,[0,0,1]),ax.y_axis.animate.rotate(90,[0,1,0]),zl.animate.rotate(90,[0,0,1]),yl.animate.rotate(90,[0,1,0])])
        # self.wait()

        # self.wait()
        # self.move_camera(theta= 48.0775*DEGREES,phi=33.1377*DEGREES,distance=100,gamma=-90*DEGREES,run_time=3)
        # self.wait()

        # self.add(ax1,ax2,g1,g2)

        # self.wait()
        # self.play(MoveAlongPath(dot,graph),MoveAlongPath(dot1,g1),MoveAlongPath(dot2,g2),run_time=5,rate_func=linear)
        # self.wait()








class Complex_Exponential3(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, distance=1000)
        z_length = ValueTracker(0.1)
        ax = ThreeDAxes(x_range=[-1.5, 1.5, 0.25], y_range=[0, 27, 5], z_range=[-1.5, 1.5, 0.25], x_length=9,
                        z_length=9,y_length=12).scale(0.7)
        ax1 = Axes(x_range=[0, 30, 10], y_range=[-1.5, 1.5, 0.5], x_length=6, y_length=4).scale(0.8).shift(
            2 * DOWN + 3.5 * LEFT)
        ax2 = Axes(x_range=[0, 30, 10], y_range=[-1.5, 1.5, 0.5], x_length=6, y_length=4).scale(0.8).shift(
            2 * DOWN + 4 * RIGHT)

        xl = ax.get_x_axis_label("(x) real").scale(0.5)
        yl = ax.get_y_axis_label("(y) real").scale(0.5)
        zl = ax.get_z_axis_label("(z) real").scale(0.5)



        d3 = []
        d21 = []
        d22 = []
        df = pd.read_csv("complex_exp_pts", names=['x', 'y', 'z'])
        for ind, row in df.iterrows():
            d3List = [row.x, row.y, row.z]
            d21List = [row.y, row.x]
            d22List = [row.y, row.z]
            d3.append(d3List)
            d21.append(d21List)
            d22.append(d22List)

        pts3d = [ax.coords_to_point(*pt) for pt in d3]
        ptsd21 = [ax1.coords_to_point(*pt) for pt in d21]
        ptsd22 = [ax2.coords_to_point(*pt) for pt in d22]

        graph = always_redraw(lambda: VMobject(color=YELLOW, stroke_width=2).set_points_as_corners(pts3d))
        graph_part1=always_redraw(lambda : VMobject(color=YELLOW, stroke_width=2).set_points_as_corners(pts3d[:301]))
        graph_part2=always_redraw(lambda : VMobject(color=YELLOW, stroke_width=2).set_points_as_corners(pts3d[300:601]))
        graph_part3=always_redraw(lambda : VMobject(color=YELLOW, stroke_width=2).set_points_as_corners(pts3d[600:801]))
        graph_part4=always_redraw(lambda : VMobject(color=YELLOW, stroke_width=2).set_points_as_corners(pts3d[800:]))

        g1 = VMobject(color=RED, stroke_width=2).set_points_as_corners(ptsd21)
        g2 = VMobject(color=RED, stroke_width=2).set_points_as_corners(ptsd22)
        dot = Dot3D(graph.get_start())

        vect=always_redraw(lambda : Arrow3D(ax.get_origin(),graph.get_points()[70],stroke_width=0.5,color=RED))
        line1=Line(ax.get_origin(),dot.get_center())
        line2=Line(ax.get_origin(),ax.c2p(1,0,0))
        dot1 = Dot(g1.get_start()).scale(0.6)
        dot2 = Dot(g2.get_start()).scale(0.6)
        ax.y_axis.rotate(90*DEGREES, [0, 1, 0])
        ax.x_axis.rotate(90*DEGREES, [1, 0, 0])
        # ax.z_axis.rotate(90*DEGREES, [0, 0, 1])
        zl.rotate(90*DEGREES, [0, 0, 1])
        numberplane=NumberPlane(x_range=[-1.5,1.5,0.25],y_range=[-1.5,1.5,0.25],x_length=9,y_length=9,background_line_style = {
            "stroke_color": WHITE,
            "stroke_width": 1,
            "stroke_opacity": 0.4,
        }).scale(0.7).rotate(90*DEGREES,RIGHT).move_to(ax.get_origin())
        # angle=Angle(ax.x_axis,line1).rotate(90,RIGHT)
        expTheta = MathTex(r'1',r'e^{i ',r'\theta }').scale(1.2).rotate(90*DEGREES,RIGHT).move_to(ax.c2p(1,0,1))
        theta = MathTex(r'\theta ',color=RED).scale(0.5).rotate(90*DEGREES,RIGHT).move_to(ax.c2p(0.25,0,0.1))
        expasfunoftime=MathTex(r'e^{i \omega  t }').rotate(90*DEGREES,RIGHT).move_to(ax.c2p(1,0,1))
        tvalue=ValueTracker(0)
        expasfunoftimemoving= always_redraw(lambda :MathTex(r'e^{i \omega *  %0.1f }' % tvalue.get_value() ).rotate(90*DEGREES,RIGHT).move_to(ax.c2p(1,0,1)))
        euler_formula=MathTex(r'e^{j \omega  t} = cos(\omega  t)+j \hspace{0.7 mm} sin(\omega  t)')


        xy_plane=TheSiGuy_lib.xy_plane(color=BLUE,axis=ax)

        end_point1=ValueTracker(2)
        end_point2=ValueTracker(2)
        end_point3=ValueTracker(2)
        end_point4=ValueTracker(2)

        def create_dot_headed_path(path,tracker,color=YELLOW, stroke_width=2):
            created_path=always_redraw(lambda : VMobject(color=color,stroke_width=stroke_width).set_points_as_corners(path.get_points()[:int(tracker.get_value())]))
            animated_dot=always_redraw(lambda : Dot3D(created_path.get_end()) )
            return created_path,animated_dot


        part1=create_dot_headed_path(graph_part1,end_point1)
        part2=create_dot_headed_path(graph_part2,end_point2)
        part3=create_dot_headed_path(graph_part3,end_point3)
        part4=create_dot_headed_path(graph_part4,end_point4)
#_________________________________________________________________
        # graphh=VMobject(color=YELLOW, stroke_width=2).set_points_as_corners(pts3d)
        # threeDGroup= VGroup(numberplane,ax,graphh).rotate(-90*DEGREES,RIGHT).scale(0.6).shift(1.8*UP)
        # self.set_camera_orientation(phi=0*DEGREES ,theta=-90*DEGREES, distance=1000)
        # self.add(threeDGroup)
        # self.play(Create(ax1),Create(ax2))
        # self.wait()
        # self.play(Transform(graphh.copy(),g1),Transform(graphh.copy(),g2))
        # self.play(FadeIn(dot.move_to(graph.get_start().scale(0.7))),FadeIn(dot1),FadeIn(dot2),run_time=0.5)
        # self.wait()
        # self.play(MoveAlongPath(dot,graphh),MoveAlongPath(dot1,g1),MoveAlongPath(dot2,g2),run_time=10,rate_func=rate_functions.linear)
        # self.wait()
#___________________________________________________________
        # self.add(ax1,g1,ax2,g2)



        # self.add(numberplane,ax, dot.move_to(graph.get_points()[70]),vect,expTheta,theta,graph)
        # self.add(numberplane,ax,dot,expasfunoftimemoving,graph_half2)
        # self.wait()
        # self.play(MoveAlongPath(dot,graph),tvalue.animate.set_value(25),run_time=15,rate_func=linear)
        # self.wait()
        # self.play(LaggedStart())

        # self.play(Create(numberplane))
        # self.play(Create(ax))
        # self.wait()
        # self.play(Write(expTheta),run_time=0.4)
        # self.wait()
        # self.play(ReplacementTransform(expTheta[0].copy(),vect),ReplacementTransform(expTheta[2].copy(),theta))
        # self.play(FadeIn(dot.move_to(graph.get_points()[70])))
        # self.wait()
        # self.play(FadeOut(vect),FadeOut(dot),FadeOut(theta))
        # self.wait()

        # ax.x_axis.rotate(90*DEGREES,[1,0,0])
        # ax.y_axis.rotate(90*DEGREES,[0,1,0])
        # ax.y_axis.rotate(90*DEGREES,[0,1,0])
        # ax.z_axis.rotate(90*DEGREES,[0,0,1])




        # self.play(end_point1.animate.set_value(len(graph_part1.get_points()+1)),run_time=2,rate_func=rate_functions.linear)
        # self.remove(part1[1])
        # self.add(*part2)
        # self.play(end_point2.animate.set_value(len(graph_part2.get_points() + 1)), run_time=2,rate_func=rate_functions.linear)
        # self.wait()
#____________________________________________________________________

        self.add(numberplane, ax, expTheta)
        self.wait()
        self.play(ReplacementTransform(expTheta,expasfunoftime))
        self.wait()
        self.play(ReplacementTransform(expasfunoftime,expasfunoftimemoving),FadeIn(*part1))
        self.remove(expTheta)
        self.add(expasfunoftimemoving)
        self.wait()
        self.play(end_point1.animate().set_value(len(graph_part1.get_points()+1)),tvalue.animate().set_value(7.5),run_time=18,rate_func=rate_functions.linear)
        self.remove(part1[1])
        self.add(*part2)
        self.move_camera(phi=75  * DEGREES, theta=35 * DEGREES, distance=1000,run_time=4,added_anims=[FadeOut(expasfunoftimemoving,run_time=3),Create(xy_plane,run_time=3),end_point2.animate(run_time=18,rate_func=rate_functions.linear).set_value(len(graph_part2.get_points())+1)])
        self.remove(part2[1])
        self.add(*part3)
        self.move_camera(phi=180 * DEGREES, theta=0  * DEGREES, distance=1000,run_time=3,added_anims=[end_point3.animate(run_time=12,rate_func=rate_functions.linear).set_value(len(graph_part3.get_points())+1),ax.y_axis.animate(run_time=3).rotate(90*DEGREES,[0,1,0]),ax.x_axis.animate(run_time=3).rotate(90*DEGREES,[1,0,0])])
        self.remove(part3[1])
        self.add(*part4)
        self.move_camera(phi=90  * DEGREES, theta=0  * DEGREES, distance=1000,run_time=3,added_anims=[end_point4.animate(run_time=12,rate_func=rate_functions.linear).set_value(len(graph_part4.get_points())+1),ax.y_axis.animate(run_time=3).rotate(90*DEGREES,[0,1,0]),ax.z_axis.animate(run_time=3).rotate(90*DEGREES,[0,0,1])])
        self.wait(2)
        self.move_camera(phi=75  * DEGREES, theta=35 * DEGREES, distance=1000,run_time=2,added_anims=[ax.x_axis.animate(run_time=3).rotate(90 * DEGREES, [1, 0, 0]),ax.z_axis.animate(run_time=3).rotate(90 * DEGREES, [0, 0, 1])])
        self.wait()
        self.move_camera(phi=90*DEGREES,theta=-90*DEGREES,distance=1000,run_time=2)
        self.remove(part1[0],part2[0],part3[0],*part4)
        self.add(graph)
        self.wait()


#_________________________________________________________________


        # self.remove(part1[0], part2[0], part3[0], *part4)
        # self.add(graph)

        # self.play(Create(numberplane),Create(ax))
        # self.play(GrowArrow(vect))
        # self.play(FadeIn(dot),run_time=0.4)
        # self.wait()
        # self.play(FadeOut(vect),FadeOut(dot),run_time=0.5)
        # self.wait()
        # self.play(MoveAlongPath(dot,graph),run_time=3,rate_func=linear)
        # self.wait()

        # self.wait()
        # self.move_camera(phi=90 * DEGREES, theta=-90 * DEGREES,run_time=3,distance=1000,added_anims=[ax.x_axis.animate(run_time=2).rotate(90,[1,0,0]),xl.animate(run_time=2).rotate(90,[1,0,0])])
        # self.wait()
        # self.move_camera(phi=90 * DEGREES, theta=0 * DEGREES,run_time=3,distance=1000,added_anims=[ax.z_axis.animate.rotate(90,[0,0,1]),ax.y_axis.animate.rotate(90,[0,1,0]),zl.animate.rotate(90,[0,0,1]),yl.animate.rotate(90,[0,1,0])])
        # self.wait()

        # self.wait()
        # self.move_camera(theta= 48.0775*DEGREES,phi=33.1377*DEGREES,distance=100,gamma=-90*DEGREES,run_time=3)
        # self.wait()

        # self.add(ax1,ax2,g1,g2)

        # self.wait()
        # self.play(MoveAlongPath(dot,graph),MoveAlongPath(dot1,g1),MoveAlongPath(dot2,g2),run_time=5,rate_func=linear)
        # self.wait()










class CFSeries(ThreeDScene):
    def construct(self):
        rotation=ValueTracker(0)
        ax=ThreeDAxes(x_range=[-3,5,1],y_range=[-5,25,5],z_range=[-5,5,1]).scale(0.9)
        ax1 = Axes(x_range=[0, 20, 10], y_range=[1, 2.5, 20])
        ax2 = Axes(x_range=[0, 30, 10], y_range=[-60, 60, 20], x_length=6, y_length=4).scale(0.8).shift(2 * DOWN + 4 * RIGHT)
        self.set_camera_orientation(phi=60*DEGREES,theta=35*DEGREES,distance=1000,zoom=0.8)

        # numberplane = NumberPlane(x_range=[-3, 5, 1], y_range=[-5, 5, 1], x_length=ax.x_length, y_length=ax.z_length,
        #                           background_line_style={
        #                               "stroke_color": WHITE,
        #                               "stroke_width": 1,
        #                               "stroke_opacity": 0.4,
        #                           }).scale(0.9).rotate(90 * DEGREES, RIGHT).move_to(ax.get_origin())

        #________________________
        # self.set_camera_orientation(phi=90*DEGREES,theta=-90*DEGREES,distance=1000)
        # ax.x_axis.rotate(90*DEGREES,[1,0,0])
        #__________________________________________
        # self.set_camera_orientation(phi=180 * DEGREES, theta=0 * DEGREES, distance=1000,zoom=0.8)
        #___________________________________
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, distance=1000,zoom=0.8)
        # ax.y_axis.rotate(90*DEGREES,[0,1,0])
        # ax.z_axis.rotate(90*DEGREES,[0,0,1])
        #___________________________________

        xl = ax.get_x_axis_label("x")
        yl = ax.get_y_axis_label("y")
        zl = ax.get_z_axis_label("z")

        xy_plane = TheSiGuy_lib.xy_plane(axis=ax)
        xz_plane = TheSiGuy_lib.xz_plane(axis=ax)
        yz_plane = TheSiGuy_lib.yz_plane(axis=ax)
        comps=["fourier_components/comp%i.csv" %num for num in range(1,42)]
        graphs=[TheSiGuy_lib.ThreeGraphsFromCsv(ax=ax,ax1=ax1,ax2=ax2,csvFile=file) for file in comps]
        transforms=[Transform(graphs[0][0],graphs[ind][0]) for ind in range(1,41)]

        # [graph,g1,g2,dot,dot1,dot2] = TheSiGuy_lib.ThreeGraphsFromCsv(ax=ax,ax1=ax1,ax2=ax2)

        # ax.x_axis.rotate(90*DEGREES,RIGHT)

        self.add(xy_plane,ax,graphs[-1][0])
        self.begin_ambient_camera_rotation()
        self.wait(14)
        self.stop_ambient_camera_rotation()
        self.wait()
        self.move_camera(phi=180*DEGREES,theta=0*DEGREES,distance=1000,zoom=0.8,run_time=3)
        self.wait()
        # self.play(Create(xy_plane))
        # self.play(Create(ax))
        # self.wait(0.5)
        # self.play(Create(graphs[0][0]))
        # self.wait()
        # for i in transforms:
        #     self.play(i)
        #
        # self.wait(2)

        # self.wait()
        # self.move_camera(theta=-70*DEGREES,phi=80*DEGREES,distance=100,run_time=3,added_anims=[ax.x_axis.animate(run_time=2).rotate(90*DEGREES,RIGHT)])
        # self.play(Create(xy_plane))
        # self.move_camera(theta=-35*DEGREES,phi=65*DEGREES,distance=100,run_time=3)
        # self.wait()
        # self.move_camera(theta=0*DEGREES,phi=180*DEGREES,distance=100,run_time=3)
        # self.wait(2)
        # self.begin_ambient_camera_rotation(rate=0.1)
        # self.play(MoveAlongPath(dot,graph),run_time=15)
        # self.wait()
        # self.play(Create(ax.z_axis))
        # self.wait()
        # self.play(Create(yz_plane))
        # self.wait()
        # self.begin_ambient_camera_rotation(rate=0.1)
        # self.wait(5)
        # self.play(rotation.animate.set_value(90),run_time=5,rate_func=linear)
        # self.wait()
        # self.play(MoveAlongPath(dot,graph),MoveAlongPath(dot1,g1),MoveAlongPath(dot2,g2),run_time=5,rate_func=linear)
        # self.wait()





class CFSeries_single_coefficients(ThreeDScene):
    def construct(self):
        rotation=ValueTracker(0)
        ax=ThreeDAxes(x_range= [-3,5,1],y_range= [-5,27,5],z_range=[-6,6,1],z_length=20).scale(0.9)
        ax1 = Axes(x_range=[0, 20, 10], y_range=[1, 2.5, 20])
        ax2 = Axes(x_range=[0, 30, 10], y_range=[-60, 60, 20], x_length=6, y_length=4).scale(0.8).shift(2 * DOWN + 4 * RIGHT)
        self.set_camera_orientation(phi=90*DEGREES,theta=0*DEGREES,distance=1000,zoom=0.8)
        xy_plane = TheSiGuy_lib.xy_plane(axis=ax)
        xz_plane = TheSiGuy_lib.xz_plane(axis=ax, color=RED)
        yz_plane = TheSiGuy_lib.yz_plane(axis=ax, color=GREEN)
        group=VGroup(ax,xy_plane,xz_plane,yz_plane)
        group.rotate(-90*DEGREES,UP)
        group.rotate(90*DEGREES,[0,1,0])


        #________________________
        # self.set_camera_orientation(phi=90*DEGREES,theta=-90*DEGREES,distance=1000)
        # ax.x_axis.rotate(90*DEGREES,[1,0,0])
        #__________________________________________
        # self.set_camera_orientation(phi=180 * DEGREES, theta=0 * DEGREES, distance=1000,zoom=0.8)
        #___________________________________
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES, distance=1000,zoom=0.8)
        # ax.y_axis.rotate(90*DEGREES,[0,1,0])
        # ax.z_axis.rotate(90*DEGREES,[0,0,1])
        #___________________________________
        #approximated real (x) vs time (y)

        first_ax = ThreeDAxes(x_range=[-3, 5, 1], y_range=[-5, 25, 5], z_range=[-5, 5, 1]).scale(0.9)
        first_ax1 = Axes(x_range=[0, 20, 10], y_range=[1, 2.5, 20])
        first_ax2 = Axes(x_range=[0, 30, 10], y_range=[-60, 60, 20], x_length=6, y_length=4).scale(0.8).shift(
            2 * DOWN + 4 * RIGHT)
        self.set_camera_orientation(phi=180 * DEGREES, theta=0 * DEGREES, distance=1000, zoom=0.8)
        xy_plane1 = TheSiGuy_lib.xy_plane(axis=first_ax)
        comps1 = ["fourier_components/comp%i.csv" % num for num in range(1, 42)]
        graphs1 = [TheSiGuy_lib.ThreeGraphsFromCsv(ax=first_ax, ax1=first_ax1, ax2=first_ax2, csvFile=file) for file in comps1]


        #________________________________________________________________

        xl = ax.get_x_axis_label("x")
        yl = ax.get_y_axis_label("y")
        zl = ax.get_z_axis_label("z")



        line=Line(ax.get_origin(),ax.c2p(1.4286,0,0),stroke_width=2,color=YELLOW)
        group.add(line)
        comps=["single_fourier_components/comp%i.csv" %num for num in range(1,42)]
        graphs=[TheSiGuy_lib.ThreeGraphsFromCsv(ax=ax,ax1=ax1,ax2=ax2,csvFile=file)[0] for file in comps]
        sinusoidal_graphs=graphs[15:26]
        transforms=[Transform(graphs1[-1][0].copy(),gr) for gr in sinusoidal_graphs]

        compsm = ["single_fourier_components_mag/comp%i.csv" % num for num in range(1, 42)]
        graphs_mag = [TheSiGuy_lib.ThreeGraphsFromCsv(ax=ax, ax1=ax1, ax2=ax2, csvFile=file)[0] for file in compsm]
        sinusoidal_graphs_m = graphs_mag[15:26]
        sinusoidal_graphs_mag =[m.set_stroke(color=YELLOW,opacity=0) for m in sinusoidal_graphs_m]

        transforms_mag = [Transform(g1,g2,run_time=4) for g1,g2 in zip(sinusoidal_graphs,sinusoidal_graphs_mag)]
        group.add(*sinusoidal_graphs)
        group.add(*sinusoidal_graphs_mag)
        # fades=[FadeOut(m,run_time=0.001) for m in sinusoidal_graphs_mag]

        # transforms=[Transform(graphs[0][0],graphs[ind][0]) for ind in range(1,41)]

        # [graph,g1,g2,dot,dot1,dot2] = TheSiGuy_lib.ThreeGraphsFromCsv(ax=ax,ax1=ax1,ax2=ax2)

        # ax.x_axis.rotate(90*DEGREES,RIGHT)
        #__________________________________________________
        # self.add(xy_plane1, first_ax, graphs1[-1][0])
        # self.wait(2)
        # self.play(Transform(first_ax,ax),Transform(xy_plane1,xy_plane),*transforms,FadeOut(graphs1[-1][0],run_time=0.2),FadeIn(line))
        # self.wait(2)




        self.add(ax,xy_plane,*sinusoidal_graphs)
        self.remove(*sinusoidal_graphs_mag)
        group.remove(xy_plane,xz_plane,yz_plane)
        self.wait()
        self.play(FadeOut(xy_plane))
        self.wait()
        self.move_camera(phi=70*DEGREES,theta=30*DEGREES,distance=1000,zoom=0.76,added_anims=[ax.y_axis.animate(run_time=1).rotate(90*DEGREES,[0,1,0]),ax.z_axis.animate(run_time=1).rotate(90*DEGREES,[1,0,0]),group.animate(run_time=3).rotate(-90*DEGREES,[0,1,0])],run_time=3)
        self.play(ax.y_axis.animate.rotate(90*DEGREES,[0,1,0]),ax.z_axis.animate.rotate(90*DEGREES,[1,0,0]),ax.x_axis.animate.rotate(90*DEGREES,[0,0,1]),run_time=0.5)
        self.wait()
        self.begin_ambient_camera_rotation()
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.wait()
        new_sin_mag = [m.set_stroke(color=YELLOW,opacity=0) for m in sinusoidal_graphs_mag]
        self.remove(*new_sin_mag)
        transforms_mag = [Transform(g1, g2.set_stroke(opacity=1), run_time=2) for g1, g2 in zip(sinusoidal_graphs, new_sin_mag)]

        self.play(*transforms_mag)
        self.move_camera(phi=90 * DEGREES, theta=90 * DEGREES, distance=1000, zoom=0.7,gamma=90*DEGREES,added_anims=[*transforms_mag,FadeIn(line),FadeOut(*sinusoidal_graphs_mag,run_time=0.1),group.animate(run_time=4).rotate(-90*DEGREES,[0,1,0])],run_time=4)

        self.play(ax.z_axis.animate.rotate(90*DEGREES,[0,0,1]),run_time=0.5)
        self.wait(1)

        self.wait()



        # self.move_camera(phi=70*DEGREES,theta=30*DEGREES,distance=1000,zoom=0.8,run_time=4)
        # self.begin_ambient_camera_rotation(rate=0.1)
        # self.wait(3)
        # self.move_camera(phi=70*DEGREES,theta=35*DEGREES,distance=1000,zoom=0.8)
        #___________________________________________________________________________________
        # ax.x_axis.rotate(90*DEGREES,[1,0,0])
        # self.set_camera_orientation(phi=90*DEGREES,theta=90*DEGREES,distance=1000,zoom=0.7,gamma=-90*DEGREES)
        # self.add(*sinusoidal_graphs,ax,line)
        # self.wait()
        # self.play(*transforms_mag)
        # self.wait()


        # self.add(ax,xy_plane,*graphs[15:26])
        # self.add(xz_plane,yz_plane)

        # self.begin_ambient_camera_rotation(rate=0.5)
        # self.wait(5)

        # self.add(ax,graphs[0][0],xl,yl,zl,xy_plane)
        # self.wait()
        # for i in transforms:
        #     self.play(i,run_time=0.5)
        #
        # self.wait(2)

        # self.wait()
        # self.move_camera(theta=-70*DEGREES,phi=80*DEGREES,distance=100,run_time=3,added_anims=[ax.x_axis.animate(run_time=2).rotate(90*DEGREES,RIGHT)])
        # self.play(Create(xy_plane))
        # self.move_camera(theta=-35*DEGREES,phi=65*DEGREES,distance=100,run_time=3)
        # self.wait()
        # self.move_camera(theta=0*DEGREES,phi=180*DEGREES,distance=100,run_time=3)
        # self.wait(2)
        # self.begin_ambient_camera_rotation(rate=0.1)
        # self.play(MoveAlongPath(dot,graph),run_time=15)
        # self.wait()
        # self.play(Create(ax.z_axis))
        # self.wait()
        # self.play(Create(yz_plane))
        # self.wait()
        # self.begin_ambient_camera_rotation(rate=0.1)
        # self.wait(5)
        # self.play(rotation.animate.set_value(90),run_time=5,rate_func=linear)
        # self.wait()
        # self.play(MoveAlongPath(dot,graph),MoveAlongPath(dot1,g1),MoveAlongPath(dot2,g2),run_time=5,rate_func=linear)
        # self.wait()





class ExactFunction(Scene):
    def construct(self):
        ax=Axes(x_range=[-3,30,5],y_range=[-3,5,1],x_length=9,y_length=7.5)
        ax.x_axis.tip_length=0.2
        d=[]
        df = pd.read_csv("fourier_components\exact_func.csv", names=['x', 'y'])
        for ind, row in df.iterrows():
            d3List = [row.x, row.y]
            d.append(d3List)

        ptsd = [ax.coords_to_point(*pt) for pt in d]

        graph = VMobject(color=YELLOW, stroke_width=1).set_points_as_corners(ptsd)
        # self.add(ax,graph)
        area =TheSiGuy_lib.area_graph_of_points(ax,5,20,graph)
        self.play(Create(ax),run_time=0.5)

        self.play(Create(graph),run_time=1)
        self.wait()
        self.play(FadeIn(area))
        self.wait()












