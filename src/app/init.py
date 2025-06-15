# -*- coding: utf-8 -*-
import logging

tetrika = "'Онлайн-школa Тетрика' test task started"

logger = logging.getLogger(__name__)
logging.basicConfig(force=True, level=logging.DEBUG, datefmt='%H:%M:%S',
                    format='%(asctime)s %(levelname).1s: %(filename)s/%(funcName)s/%(lineno)d: %(message)s')
