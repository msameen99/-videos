from imports import *
import pandas as pd


class SmoothGraphFromSetPoints(VMobject):
    def __init__(self, set_of_points, **kwargs):
        super().__init__(**kwargs)
        self.set_points_smoothly(set_of_points)


def list_c2p(list,ax=Axes()):
    pts=[ax.coords_to_point(*pt) for pt in list ]
    return pts

def vmobj_from_list(list):
    vmobj=VMobject().set_points_as_corners(list)
    return vmobj

def xy_plane(axis,color=BLUE):
    ax=axis
    xy_plane = Polygram([[ax.x_axis.get_start()[0], ax.y_axis.get_start()[1], ax.get_origin()[2]],
                         [ax.x_axis.get_start()[0], ax.y_axis.get_end()[1], ax.get_origin()[2]],
                         [ax.x_axis.get_end()[0], ax.y_axis.get_end()[1], ax.get_origin()[2]],
                         [ax.x_axis.get_end()[0], ax.y_axis.get_start()[1], ax.get_origin()[2]]], stroke_width=0,
                        fill_color=color, fill_opacity=0.1)
    return xy_plane



def xz_plane(axis,color=BLUE):
    ax=axis
    xz_plane = Polygram([[ax.x_axis.get_start()[0], ax.get_origin()[1], ax.z_axis.get_start()[2]],
                         [ax.x_axis.get_start()[0], ax.get_origin()[1], ax.z_axis.get_end()[2]],
                         [ax.x_axis.get_end()[0], ax.get_origin()[1], ax.z_axis.get_end()[2]],
                         [ax.x_axis.get_end()[0], ax.get_origin()[1], ax.z_axis.get_start()[2]]], stroke_width=0,
                        fill_color=color, fill_opacity=0.1)
    return xz_plane


def yz_plane(axis,color=BLUE):
    ax=axis
    yz_plane = Polygram([[ax.get_origin()[0], ax.y_axis.get_end()[1], ax.z_axis.get_start()[2]],
                         [ax.get_origin()[0], ax.y_axis.get_end()[1], ax.z_axis.get_end()[2]],
                         [ax.get_origin()[0], ax.y_axis.get_start()[1], ax.z_axis.get_end()[2]],
                         [ax.get_origin()[0], ax.y_axis.get_start()[1], ax.z_axis.get_start()[2]]], stroke_width=0,
                        fill_color=color, fill_opacity=0.05)

    return yz_plane


def three_graphs_from_csv(ax, ax1, ax2,csvFile,stroke_width=1):
    d3 = []
    d21 = []
    d22 = []
    d = []
    df = pd.read_csv(csvFile, names=['x', 'y', 'z'])
    for ind, row in df.iterrows():
        d3List = [row.x, row.y, row.z]
        d21List = [row.z, row.x]
        d22List = [row.z, row.y]

        d3.append(d3List)
        d21.append(d21List)
        d22.append(d22List)

    pts3d = [ax.coords_to_point(*pt) for pt in d3]
    ptsd21 = [ax1.coords_to_point(*pt) for pt in d21]
    ptsd22 = [ax2.coords_to_point(*pt) for pt in d22]

    graph = VMobject(color=YELLOW, stroke_width=stroke_width).set_points_as_corners(pts3d)
    g1 = VMobject(color=YELLOW, stroke_width=stroke_width).set_points_as_corners(ptsd21)
    g2 = VMobject(color=YELLOW, stroke_width=stroke_width).set_points_as_corners(ptsd22)

    dot = Dot3D(graph.get_start()).scale(0.6)
    dot1 = Dot(g1.get_start()).scale(0.6)
    dot2 = Dot(g2.get_start()).scale(0.6)

    return graph, g1, g2, dot, dot1, dot2


def three_d_graph_from_csv(ax,csvFile,stroke_width=1,color=YELLOW):
    d3 = []
    x = []
    y = []
    z = []

    df = pd.read_csv(csvFile, names=['x', 'y', 'z'])
    for ind, row in df.iterrows():
        d3List = [row.x, row.y, row.z]

        for ind, row in df.iterrows():
            x.append(row.x)
            y.append(row.y)
            z.append(row.z)

        graph=ax.plot_line_graph(x,y,z,add_vertex_dots=False,stroke_width=stroke_width,line_color=color)
        return graph


    #     d3.append(d3List)
    #
    #
    # pts3d = [ax.coords_to_point(*pt) for pt in d3]
    # pts2d1 = [ax.coords_to_point(pt[0],pt[1],0) for pt in d3]
    #
    #
    # graph = VMobject(color=YELLOW, stroke_width=stroke_width).set_points_as_corners(pts3d)
    # g1 = VMobject(color=YELLOW, stroke_width=stroke_width).set_points_as_corners(pts2d1)
    #
    #
    # dot = Dot3D(graph.get_start()).scale(0.6)
    #
    #
    # return graph,g1, dot

def two_d_graph_from_csv(ax,csvFile,stroke_width=1.5,color=YELLOW):

    x = []
    y = []
    df = pd.read_csv(csvFile, names=['x', 'y'])
    for ind, row in df.iterrows():
        x.append(row.x)
        y.append(row.y)

    #     dList = [row.x, row.y]
    #
    #     d.append(dList)
    #
    #
    # pts = [ax.coords_to_point(*pt) for pt in d]




    # graph = VMobject(color=YELLOW, stroke_width=stroke_width).set_points_as_corners(pts)
    graph= ax.plot_line_graph(x,y,stroke_width=stroke_width,line_color=color,add_vertex_dots=False)




    # dot = Dot(graph.get_start()).scale(0.6)

    return graph





def two_d_graph_reversed_from_csv(ax,csvFile,stroke_width=1.5):

    x = []
    y = []
    df = pd.read_csv(csvFile, names=['x', 'y'])
    for ind, row in df.iterrows():
        x.append(row.x)
        y.append(row.y)

    #     dList = [row.x, row.y]
    #
    #     d.append(dList)
    #
    #
    # pts = [ax.coords_to_point(*pt) for pt in d]




    # graph = VMobject(color=YELLOW, stroke_width=stroke_width).set_points_as_corners(pts)
    x.reverse()
    y.reverse()
    graph= ax.plot_line_graph(x,y,stroke_width=stroke_width)



    # dot = Dot(graph.get_start()).scale(0.6)

    return graph



def csv_to_xy(csvFile):
    x = []
    y = []
    df = pd.read_csv(csvFile, names=['x', 'y'])
    for ind, row in df.iterrows():
        x.append(row.x)
        y.append(row.y)

    return x,y


def csv_to_xyz(csvFile):
    x = []
    y = []
    z = []
    df = pd.read_csv(csvFile, names=['x', 'y','z'])
    for ind, row in df.iterrows():
        x.append(row.x)
        y.append(row.y)
        z.append(row.z)

    return x, y, z


def area_graph_of_points(ax,x_min,x_max,mobject,opacity=0.3,color=[BLUE, GREEN]):
    points = (
            [ax.c2p(0,x_min,0)]
            + [p for p in mobject.points if x_min <= ax.p2c(p)[1] <= x_max]
            + [ax.c2p(0,x_max,0)]
    )
    return Polygon(*points,).set_opacity(opacity).set_color(color)



def area_2d_parametric_function(x_min,x_max,mobject,opacity=0.3,color=[BLUE, GREEN]):
    points = (
            [[0,x_min,0]]
            + [p for p in mobject.points if x_min <= p[1] <= x_max]
            + [[0,x_max,0]]
    )
    return Polygon(*points).set_opacity(opacity).set_color(color)


# def surface_from_3d_curves()


def create_dot_headed_path(path, tracker, color=YELLOW, stroke_width=2):
    created_path = always_redraw(lambda: VMobject(color=color, stroke_width=stroke_width).set_points_as_corners(
        path.points[:int(tracker.get_value())]))
    animated_dot = always_redraw(lambda: Dot3D(created_path.get_end()))
    return created_path, animated_dot





def two_d_graph_from_acsii(ax,csvFile,stroke_width=1.5,color=YELLOW):

    x = []
    y = []
    df = pd.read_csv(csvFile, sep=" ", names=['x', 'y'])
    for ind, row in df.iterrows():
        x.append(row.x)
        y.append(row.y)

    #     dList = [row.x, row.y]
    #
    #     d.append(dList)
    #
    #
    # pts = [ax.coords_to_point(*pt) for pt in d]




    # graph = VMobject(color=YELLOW, stroke_width=stroke_width).set_points_as_corners(pts)
    graph= ax.plot_line_graph(x,y,stroke_width=stroke_width,line_color=color, add_vertex_dots=False)




    # dot = Dot(graph.get_start()).scale(0.6)

    return graph



