from manim import *
from dijkstra_algo import Dijkstra
import networkx as nx

dist_graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0,11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9,14, 0, 0, 0],
    [0, 0, 0, 9, 0,10, 0, 0, 0],
    [0, 0, 4,14,10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8,11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]
start_ind = 0
end_ind = 4


class DijkstraAnimation(Scene):
    def construct(self):
        global dist_graph, start_ind, end_ind
        dij = Dijkstra()
        dij.set_dist_graph(graph=dist_graph)
        vertices = list(range(len(dist_graph)))
        labels = {}
        for v in vertices:
            labels[v] = str(v)
        edges = []
        edge_cost = {}
        for row_ind, row in enumerate(dist_graph):
            for col_ind in range(row_ind, len(dist_graph)):
                val = row[col_ind]
                if val > 0:
                    edges.append((row_ind, col_ind))
                    edge_cost[(row_ind, col_ind)] = val
        g = Graph(vertices=vertices, edges=edges, layout="spring", labels=False).scale(1.65)
        # self.add(g)
        self.play(Create(g), run_time=5)

        self.play(g[0].animate.move_to([-6, 0, 0]),
                  g[1].animate.move_to([-3, 2, 0]),
                  g[2].animate.move_to([0, 2, 0]),
                  g[3].animate.move_to([3, 2, 0]),
                  g[4].animate.move_to([6, 0, 0]),
                  g[5].animate.move_to([3, -2, 0]),
                  g[6].animate.move_to([0, -2, 0]),
                  g[7].animate.move_to([-3, -2, 0]),
                  g[8].animate.move_to([-1, 0, 0]))

        vertex_text_alignment = {
            0: LEFT,
            1: UP,
            2: UP,
            3: UP,
            4: RIGHT,
            5: DOWN,
            6: DOWN,
            7: DOWN,
            8: RIGHT
        }

        for ind, v in enumerate(vertices):
            t = Text(str(v), color=YELLOW).scale(1).next_to(g[ind].get_bottom(), vertex_text_alignment[ind])
            self.add(t)

        for ind, edge in enumerate(edges):
            offset = np.array((0.0, 0.0, 0.0))
            if (vertex_text_alignment[edge[0]] == LEFT).all():
                offset = LEFT + UP
            elif (vertex_text_alignment[edge[0]] == UP).all():
                offset = UP
            elif (vertex_text_alignment[edge[0]] == RIGHT).all():
                offset = DOWN
            elif (vertex_text_alignment[edge[0]] == DOWN).all():
                offset = DOWN
            t = Text(str(edge_cost[edge]), color=ORANGE).scale(0.75).next_to(g.edges[edge].get_edge_center(ORIGIN), ORIGIN + offset)
            self.add(t)

        output_dict = dij.find_shortest_path(0)
        shortest_path = []
        end_ind_ = end_ind
        while True:
            prev_ind = output_dict[end_ind_]["prev_ind"]
            shortest_path.insert(0, (prev_ind, end_ind_))
            end_ind_ = prev_ind
            if prev_ind == start_ind:
                break
        vertex_config = g.default_vertex_config
        for edge in shortest_path:
            vertex_config["fill_color"] = RED
            g[0].vertex_config = Dot(**vertex_config)
            self.wait(1)
            g.add_edges(*[edge],
                        edge_config= {
                            edge: {"stroke_color": GREEN}
                        })
        # self.add(g)
        self.wait()


class DijkstraAnimation2(Scene):
    def construct(self):
        global dist_graph, start_ind, end_ind
        dij = Dijkstra()
        dij.set_dist_graph(graph=dist_graph)
        vertices = list(range(len(dist_graph)))
        edges = []
        edge_cost = {}
        for row_ind, row in enumerate(dist_graph):
            for col_ind in range(row_ind, len(dist_graph)):
                val = row[col_ind]
                if val > 0:
                    edges.append((row_ind, col_ind))
                    edge_cost[(row_ind, col_ind)] = val

        # Graph
        g = Graph(vertices=vertices, edges=edges, layout="spring", labels=False).scale(1.65)
        # self.add(g)
        self.play(Create(g), run_time=5)

        # Moving the nodes to fixed places
        self.play(g[0].animate.move_to([-6, 0, 0]),
                  g[1].animate.move_to([-3, 2, 0]),
                  g[2].animate.move_to([0, 2, 0]),
                  g[3].animate.move_to([3, 2, 0]),
                  g[4].animate.move_to([6, 0, 0]),
                  g[5].animate.move_to([3, -2, 0]),
                  g[6].animate.move_to([0, -2, 0]),
                  g[7].animate.move_to([-3, -2, 0]),
                  g[8].animate.move_to([0, 0, 0]))

        vertex_text_alignment = {
            0: LEFT,
            1: UP,
            2: UP,
            3: UP,
            4: RIGHT,
            5: DOWN,
            6: DOWN,
            7: DOWN,
            8: RIGHT
        }

        # Vertex label
        for ind, v in enumerate(vertices):
            t = Text(str(v), color=YELLOW).scale(1).next_to(g[ind].get_bottom(), vertex_text_alignment[ind])
            self.add(t)

        # Edge cost
        for ind, edge in enumerate(edges):
            offset = np.array((0.0, 0.0, 0.0))
            if (vertex_text_alignment[edge[0]] == LEFT).all():
                offset = LEFT + UP
            elif (vertex_text_alignment[edge[0]] == UP).all():
                offset = UP
            elif (vertex_text_alignment[edge[0]] == RIGHT).all():
                offset = DOWN
            elif (vertex_text_alignment[edge[0]] == DOWN).all():
                offset = DOWN
            t = Text(str(edge_cost[edge]), color=ORANGE).scale(0.75).next_to(g.edges[edge].get_edge_center(ORIGIN), ORIGIN + offset)
            self.add(t)

        self.wait(3)

        current_ind, prev_ind, current_cost = start_ind, -1, 0
        next_step = True
        spt = {}

        while next_step:
            next_step, current_ind, prev_ind, current_cost, buffer, spt = dij.find_shortest_path_in_steps(current_ind, prev_ind, current_cost)
            for edge in edges:
                g.add_edges(*[edge],
                        edge_config= {
                            edge: {"stroke_color": WHITE}
                        })
            for key in buffer:
                g[key].set_color(RED)
                edge = (buffer[key]["prev_ind"], key)
                g.add_edges(*[edge],
                        edge_config= {
                            edge: {"stroke_color": RED}
                        })
            for key in spt:
                g[key].set_color(GREEN)
                if spt[key]["prev_ind"] == -1:
                    continue
                g[spt[key]["prev_ind"]].set_color(GREEN)
                edge = (spt[key]["prev_ind"], key)
                g.add_edges(*[edge],
                        edge_config= {
                            edge: {"stroke_color": GREEN}
                        })
            self.wait(2)
        shortest_path = []
        end_ind_ = end_ind
        while True:
            prev_ind = spt[end_ind_]["prev_ind"]
            shortest_path.insert(0, (prev_ind, end_ind_))
            end_ind_ = prev_ind
            if prev_ind == start_ind:
                break
        for v in vertices:
            g[v].set_color(WHITE)
        for edge in edges:
            g.add_edges(*[edge],
                    edge_config= {
                        edge: {"stroke_color": WHITE}
                    })
        self.wait(3)
        for edge in shortest_path:
            self.wait(1)
            g[edge[0]].set_color(GREEN)
            g[edge[1]].set_color(GREEN)
            g.add_edges(*[edge],
                        edge_config= {
                            edge: {"stroke_color": GREEN}
                        })
        self.wait()


class MovingVertices(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4]
        edges = [(1, 2), (2, 3), (3, 4), (1, 3), (1, 4), (2, 1)]
        g = Graph(vertices, edges)
        self.play(Create(g))
        self.wait()
        self.play(g[1].animate.move_to([1, 1, 0]),
                  g[2].animate.move_to([-1, 1, 0]),
                  g[3].animate.move_to([1, -1, 0]),
                  g[4].animate.move_to([-1, -1, 0]))
        self.wait()
