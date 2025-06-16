# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger(__name__)


def appearance(intervals: dict) -> int:
    """Подсчёт суммарного времени учителя и ученика"""
    logger.debug(f"({appearance.__doc__}) started")

    result = 0
    for k, v in intervals.items():
        if k in ('pupil', 'tutor'):
            if len(v) & 1:
                logger.error(f"{k}: {len(v)} - odd number of timestamps")
                return -1
            for i in range(0, len(v), 2):
                result += v[i + 1] - v[i]

    logger.info(f"result = {result} sec., ended")
    return result
