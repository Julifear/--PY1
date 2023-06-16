from typing import Union
import networkx as nx


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Функция, рассчитывающая минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    return nx.dijkstra_path_length(graph, 0, graph.number_of_nodes() - 1)

def graph_creator(weights: tuple):
    """
    Функция, формирующая граф по стоимости ступеней.

    :param weights: Стоимость ступеней.
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    graph = nx.DiGraph()
    numbersteps = len(weights)
    for i in range(numbersteps - 1):
        graph.add_weighted_edges_from([(i, i + 1, weights[i]), (i, i + 2, weights[i + 1])])
        graph.add_weighted_edges_from([(numbersteps - 1, numbersteps, weights[numbersteps - 1])])
    return graph


if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    stairway_graph = graph_creator(stairway)
    length = len(stairway)
    print(stairway_path(stairway_graph))  # 72