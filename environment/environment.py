# -*- coding: utf-8 -*-
"""
    Alaa El Jawad
    ~~~~~~~~~~~~~
    Environment describes where the model will wander and allows us
    to calculate everything linked to the relation between the model
    and the environment
"""


class Environment(object):
    def __init__(self, width=400, height=400, wind_force=2, wind_dir=0):
        self.width = width
        self.height = height
        self.conditions = {'wind_direction': wind_dir,
                           'wind_force': wind_force}
