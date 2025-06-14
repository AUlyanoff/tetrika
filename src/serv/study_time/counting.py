# -*- coding: utf-8 -*-

def appearance(intervals: dict) -> int:
    """Подсчёт суммарного времени учителя и ученика"""

    result = 0
    for k, v in intervals.items():
        if k in ('pupil', 'tutor'):
            for i in range(0, len(v), 2):
                result += v[i+1] - v[i]

    return result
