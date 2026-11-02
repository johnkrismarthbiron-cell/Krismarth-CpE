"""Sorting algorithms and animation frames for the portfolio visualizer."""

from typing import Literal, TypedDict

Algorithm = Literal['bubble', 'selection', 'insertion']


class SortStep(TypedDict):
    data: list[float]
    compared: list[int]


def sort_with_steps(values: list[float], algorithm: Algorithm) -> list[SortStep]:
    """Sort values in ascending order and return snapshots for visualization."""
    data = list(values)
    steps: list[SortStep] = [{'data': data.copy(), 'compared': []}]

    def record(compared: list[int]) -> None:
        steps.append({'data': data.copy(), 'compared': compared})

    if algorithm == 'bubble':
        for end in range(len(data) - 1, 0, -1):
            swapped = False
            for index in range(end):
                record([index, index + 1])
                if data[index] > data[index + 1]:
                    data[index], data[index + 1] = data[index + 1], data[index]
                    swapped = True
                    record([index, index + 1])
            if not swapped:
                break
    elif algorithm == 'selection':
        for start in range(len(data)):
            minimum = start
            for index in range(start + 1, len(data)):
                record([minimum, index])
                if data[index] < data[minimum]:
                    minimum = index
            if minimum != start:
                data[start], data[minimum] = data[minimum], data[start]
                record([start, minimum])
    elif algorithm == 'insertion':
        for index in range(1, len(data)):
            value = data[index]
            cursor = index - 1
            while cursor >= 0:
                record([cursor, cursor + 1])
                if data[cursor] <= value:
                    break
                data[cursor + 1] = data[cursor]
                record([cursor, cursor + 1])
                cursor -= 1
            data[cursor + 1] = value
            if cursor + 1 != index:
                record([cursor + 1, index])
    else:
        raise ValueError(f'Unsupported sorting algorithm: {algorithm}')

    steps.append({'data': data.copy(), 'compared': []})
    return steps
