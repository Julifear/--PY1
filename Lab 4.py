from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Функция, просчитывающая количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """

    table = [[1 for _ in range(n)] for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            table[i][j] = table[i - 1][j] + table[i - 1][j - 1] + table[i][j - 1]
    return table

if __name__ == '__main__':
    paths = car_paths(4, 2)
    print(paths[-1][-1])  # 7