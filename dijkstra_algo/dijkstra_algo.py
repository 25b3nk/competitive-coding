"""
Dijkstra's algorithm
"""

from typing import List
import sys
import json


class Dijkstra(object):
    def __init__(self):
        self.__dist_graph: List[List[int]] = [[]]
        self.__buffer: dict = {}
        self.__spt: dict = {}

    def set_dist_graph(self, graph: List[List[int]]) -> bool:
        self.__buffer: dict = {}
        self.__spt: dict = {}
        num_of_rows = len(graph)
        for row in graph:
            if not (len(row) == num_of_rows):
                print("Graph is not square matrix")
                return False
        self.__dist_graph = graph
        return True

    def __add_to_output(self,
                        json_data: dict,
                        curr_ind: int,
                        prev_ind: int,
                        cost: int):
        json_data[curr_ind] = {
            "prev_ind": prev_ind,
            "cost": cost
        }

    def find_shortest_path(self, starting_index: int = 0):
        self.__buffer: dict = {}
        self.__spt: dict = {}
        self.__add_to_output(self.__spt, starting_index, prev_ind=-1, cost=0)
        current_ind = starting_index
        current_cost = 0
        while True:
            current_cost = self.__spt[current_ind]["cost"]
            # print("Current ind: {} Current cost: {}".format(current_ind, current_cost))
            for ind, val in enumerate(self.__dist_graph[current_ind]):
                if (val <= 0) or (ind in self.__spt):
                    continue
                if (ind not in self.__buffer) or (ind in self.__buffer and self.__buffer[ind]["cost"] > (current_cost + val)):
                    self.__add_to_output(self.__buffer, curr_ind=ind, prev_ind=current_ind, cost=(current_cost + val))
            min_val = sys.maxsize
            for key in self.__buffer:
                if self.__buffer[key]["cost"] < min_val:
                    min_val = self.__buffer[key]["cost"]
                    current_ind = key
            if current_ind in self.__spt:
                print("Error :: We are updating key already in spt")
            self.__add_to_output(self.__spt, current_ind, prev_ind=self.__buffer[current_ind]["prev_ind"], cost=self.__buffer[current_ind]["cost"])

            del self.__buffer[current_ind]

            if len(self.__spt) == len(self.__dist_graph):
                break
        return self.__spt

    def find_shortest_path_in_steps(self, current_ind, prev_ind, current_cost):
        if current_cost == 0:
            self.__add_to_output(self.__spt, current_ind, prev_ind=prev_ind, cost=current_cost)
        current_cost = self.__spt[current_ind]["cost"]
        # print("Current ind: {} Current cost: {}".format(current_ind, current_cost))
        for ind, val in enumerate(self.__dist_graph[current_ind]):
            if (val <= 0) or (ind in self.__spt):
                continue
            if (ind not in self.__buffer) or (ind in self.__buffer and self.__buffer[ind]["cost"] > (current_cost + val)):
                self.__add_to_output(self.__buffer, curr_ind=ind, prev_ind=current_ind, cost=(current_cost + val))
        min_val = sys.maxsize
        for key in self.__buffer:
            if self.__buffer[key]["cost"] < min_val:
                min_val = self.__buffer[key]["cost"]
                current_ind = key
        if current_ind in self.__spt:
            print("Error :: We are updating key already in spt")
        self.__add_to_output(self.__spt, current_ind, prev_ind=self.__buffer[current_ind]["prev_ind"], cost=self.__buffer[current_ind]["cost"])
        prev_ind = self.__buffer[current_ind]["prev_ind"]
        current_cost = self.__buffer[current_ind]["cost"]
        del self.__buffer[current_ind]

        next_step = True
        if len(self.__spt) == len(self.__dist_graph):
            next_step = False
        return next_step, current_ind, prev_ind, current_cost, self.__buffer, self.__spt


if __name__ == "__main__":
    '''
         0  1  2  3  4  5  6  7  8
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0,11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9,14, 0, 0, 0],
        [0, 0, 0, 9, 0,10, 0, 0, 0],
        [0, 0, 4,14,10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8,11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
    '''
    graph = [
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

    dij = Dijkstra()
    dij.set_dist_graph(graph=graph)
    output = dij.find_shortest_path()
    print(json.dumps(output, indent=4))
