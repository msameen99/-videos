from imports import *
class First(Scene):
    def construct(self):
        self.camera.background_color = "#101010"

        # ax=Axes(x_range=[0,1e-10],y_range=[0,10e-3])
        # # g=TheSiGuy_lib.two_d_graph_from_acsii(ax,"csv_files/cap_current.txt")
        # g=TheSiGuy_lib.two_d_graph_from_csv(ax,"csv_files/current1.csv")
        # self.add(ax,g)

        # loverc = MathTex(r'Z_{o}=\sqrt{\frac{L}{C}}=\frac{0.05  \hspace{1 mm} nH}{0.02  \hspace{1 mm} pF}=50  \hspace{1 mm} \Omega ',stroke_width=3,color=RED)
        # self.add(loverc)
        # self.play(Write(loverc))


        # reflection_coefficient=MathTex(r'\Gamma=\frac{V^{-}}{V^{+}}=\frac{Z_L-Z_o}{Z_L+Z_o}')
        # rect=SurroundingRectangle(reflection_coefficient,buff=MED_SMALL_BUFF,stroke_width=1.5)

        # self.play(Write(reflection_coefficient))
        # self.play(Create(rect))
        # self.wait()

        # voltage = MathTex(
        #     r'v(l, t)=v^{+} \hspace{0.5 mm} e^{-\alpha l}  e^{j (\omega t-\beta l)}+{{v^{-} \hspace{0.5 mm} e^{\alpha l}  e^{j (\omega t+\beta l)}}}')
        # current = MathTex(
        #     r'I(l, t)=I^{+} \hspace{0.5 mm} e^{-\alpha l}  e^{j (\omega t-\beta l)}+{{I^{-} \hspace{0.5 mm} e^{\alpha l}  e^{j (\omega t+\beta l)}}}').shift(1.25*DOWN)

        # self.play(Write(voltage),Write(current))
        # self.wait()
        # self.add(voltage[1],current[1])
        # g=Group(voltage[1],current[1])
        # rect=SurroundingRectangle(g,stroke_width=1.3)
        # self.add(voltage,current,rect)

        # self.play(Write(voltage),Write(current))
        # self.play(Create(rect))
        # self.wait()
        #
        # i_in_v_div_circuit=MathTex(r'I=\frac{1v}{200\Omega + 50\Omega }=4 mA')
        # self.play(Write(i_in_v_div_circuit))
        # self.wait()
        # I_into_line=MathTex(r'I=\frac{V}{Z_{o}}')
        # self.play(Write(I_into_line))
        # self.wait()

        # v_at_the_load=MathTex(r'V2=IR_{l}')
        # self.play(Write(v_at_the_load))
        # self.wait()

        # rl=MathTex(r'R_{l}')
        # self.add(rl)

        tau=MathTex(r'\tau = z_{o}.c1= 1  \hspace{1 mm} psec')
        self.play(Write(tau))
        self.wait()

