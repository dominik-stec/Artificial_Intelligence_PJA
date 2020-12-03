"""
author: Dominik Stec,
index:  s12623,
email:  s12623@pja.edu.pl

To run visualization type:
 >> python traffic_simulation.py
as Python interpreter command

pygame and scikit-fuzzy modules installation is need
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


class FuzzyLogic:
    """
    class compute if traffic lights should be green or red depends on how big is traffic, average speed of cars
    and how many people go across street
    """
    __traffic_right = None
    __people_right = None
    __speed_right = None
    __intensity_right = None

    __traffic_left = None
    __people_left = None
    __speed_left = None
    __intensity_left = None

    __traffic_up = None
    __people_up = None
    __speed_up = None
    __intensity_up = None

    __traffic_down = None
    __people_down = None
    __speed_down = None
    __intensity_down = None

    __intensity_left_ctrl = None
    __intensity_left_c = None
    __intensity_right_ctrl = None
    __intensity_right_c = None
    __intensity_up_ctrl = None
    __intensity_up_c = None
    __intensity_down_ctrl = None
    __intensity_down_c = None

    __left_right_intensity = None
    __right_left_intensity = None
    __up_down_intensity = None
    __down_up_intensity = None

    __light_horizontal = None

    __light_horizontal_ctrl = None
    __light_horizontal_c = None

    # define number of cars, cars speed and people
    def __init__(self, traffic=40, people=50, speed=70):

        self.traffic_right = ctrl.Antecedent(np.arange(0, traffic+1, 1), 'traffic')
        self.people_right = ctrl.Antecedent(np.arange(0, people+1, 1), 'people')
        self.speed_right = ctrl.Antecedent(np.arange(0, speed+1, 1), 'speed')
        self.intensity_right = ctrl.Consequent(np.arange(0, 101, 1), 'intensity')

        self.traffic_left = ctrl.Antecedent(np.arange(0, traffic+1, 1), 'traffic')
        self.people_left = ctrl.Antecedent(np.arange(0, people+1, 1), 'people')
        self.speed_left = ctrl.Antecedent(np.arange(0, speed+1, 1), 'speed')
        self.intensity_left = ctrl.Consequent(np.arange(0, 101, 1), 'intensity')

        self.traffic_up = ctrl.Antecedent(np.arange(0, traffic+1, 1), 'traffic')
        self.people_up = ctrl.Antecedent(np.arange(0, people+1, 1), 'people')
        self.speed_up = ctrl.Antecedent(np.arange(0, speed+1, 1), 'speed')
        self.intensity_up = ctrl.Consequent(np.arange(0, 101, 1), 'intensity')

        self.traffic_down = ctrl.Antecedent(np.arange(0, traffic+1, 1), 'traffic')
        self.people_down = ctrl.Antecedent(np.arange(0, people+1, 1), 'people')
        self.speed_down = ctrl.Antecedent(np.arange(0, speed+1, 1), 'speed')
        self.intensity_down = ctrl.Consequent(np.arange(0, 101, 1), 'intensity')

        self.left_right_intensity = ctrl.Antecedent(np.arange(0, 101, 1), 'left-to-right')
        self.right_left_intensity = ctrl.Antecedent(np.arange(0, 101, 1), 'right-to-left')
        self.up_down_intensity = ctrl.Antecedent(np.arange(0, 101, 1), 'up-to-down')
        self.down_up_intensity = ctrl.Antecedent(np.arange(0, 101, 1), 'down-to-up')

        self.light_horizontal = ctrl.Consequent(np.arange(0, 3, 1), 'light')

    def __define_auto_membership_functions_of_part_directions(self):

        self.traffic_right.automf(3)
        self.people_right.automf(3)
        self.speed_right.automf(3)
        self.intensity_right.automf(3)

        self.traffic_left.automf(3)
        self.people_left.automf(3)
        self.speed_left.automf(3)
        self.intensity_left.automf(3)

        self.traffic_up.automf(3)
        self.people_up.automf(3)
        self.speed_up.automf(3)
        self.intensity_up.automf(3)

        self.traffic_down.automf(3)
        self.people_down.automf(3)
        self.speed_down.automf(3)
        self.intensity_down.automf(3)

    def __define_left_site_rules(self):
        # all rule are the same
        rule_left_1 = ctrl.Rule(self.traffic_left['poor'] & self.speed_left['poor'] & self.people_left['poor'],
                                self.intensity_left['poor'])
        rule_left_2 = ctrl.Rule(self.traffic_left['average'] & self.speed_left['average'] & self.people_left['average'],
                                self.intensity_left['average'])
        rule_left_3 = ctrl.Rule(self.traffic_left['good'] & self.speed_left['good'] & self.people_left['good'], self.intensity_left['good'])

        # one rule is good rest are poor
        rule_left_4 = ctrl.Rule(self.traffic_left['good'] & self.speed_left['poor'] & self.people_left['poor'],
                                self.intensity_left['average'])
        rule_left_5 = ctrl.Rule(self.traffic_left['poor'] & self.speed_left['good'] & self.people_left['poor'],
                                self.intensity_left['average'])
        rule_left_6 = ctrl.Rule(self.traffic_left['poor'] & self.speed_left['poor'] & self.people_left['good'],
                                self.intensity_left['average'])

        # one rule is good rest are average
        rule_left_7 = ctrl.Rule(self.traffic_left['good'] & self.speed_left['average'] & self.people_left['average'],
                                self.intensity_left['good'])
        rule_left_8 = ctrl.Rule(self.traffic_left['average'] & self.speed_left['good'] & self.people_left['average'],
                                self.intensity_left['good'])
        rule_left_9 = ctrl.Rule(self.traffic_left['average'] & self.speed_left['average'] & self.people_left['good'],
                                self.intensity_left['good'])

        # one rule is average rest are poor
        rule_left_10 = ctrl.Rule(self.traffic_left['average'] & self.speed_left['poor'] & self.people_left['poor'],
                                 self.intensity_left['poor'])
        rule_left_11 = ctrl.Rule(self.traffic_left['poor'] & self.speed_left['average'] & self.people_left['poor'],
                                 self.intensity_left['poor'])
        rule_left_12 = ctrl.Rule(self.traffic_left['poor'] & self.speed_left['poor'] & self.people_left['average'],
                                 self.intensity_left['poor'])

        rule_left_no_exception = ctrl.Rule(self.traffic_left['poor'] | self.speed_left['poor'] | self.people_left['poor'] |
                                           self.traffic_left['average'] | self.speed_left['average'] | self.people_left['average'] |
                                           self.traffic_left['good'] | self.speed_left['good'] | self.people_left['good'],
                                self.intensity_left['poor'])

        self.intensity_left_ctrl = ctrl.ControlSystem([rule_left_1, rule_left_2, rule_left_3,
                                                  rule_left_4, rule_left_5, rule_left_6,
                                                  rule_left_7, rule_left_8, rule_left_9,
                                                  rule_left_10, rule_left_11, rule_left_12,
                                                       rule_left_no_exception])

        self.intensity_left_c = ctrl.ControlSystemSimulation(self.intensity_left_ctrl)


    def __set_left_site_traffic_input(self, traffic):
        self.intensity_left_c.input['traffic'] = traffic

    def __set_left_site_people_input(self, people):
        self.intensity_left_c.input['people'] = people

    def __set_left_site_speed_input(self, speed):
        self.intensity_left_c.input['speed'] = speed

    def set_left_site_inputs(self, traffic, people, speed):
        """This method compute fuzzy logic int output value for traffic, people, speed defines as input values
           for left site intersection

        Args:
            traffic (int): How many cars is on left site street intersection
            people (int): How many people is on left site street intersection
            speed (int): What is average cars speed for left site intersection
        """
        self.__set_left_site_traffic_input(traffic)
        self.__set_left_site_people_input(people)
        self.__set_left_site_speed_input(speed)
        self.intensity_left_c.compute()

    def __define_right_site_rules(self):
        # all rule are the same
        rule_right_1 = ctrl.Rule(self.traffic_right['poor'] & self.speed_right['poor'] & self.people_right['poor'],
                                 self.intensity_right['poor'])
        rule_right_2 = ctrl.Rule(self.traffic_right['average'] & self.speed_right['average'] & self.people_right['average'],
                                 self.intensity_right['average'])
        rule_right_3 = ctrl.Rule(self.traffic_right['good'] & self.speed_right['good'] & self.people_right['good'],
                                 self.intensity_right['good'])

        # one rule is good rest are poor
        rule_right_4 = ctrl.Rule(self.traffic_right['good'] & self.speed_right['poor'] & self.people_right['poor'],
                                 self.intensity_right['average'])
        rule_right_5 = ctrl.Rule(self.traffic_right['poor'] & self.speed_right['good'] & self.people_right['poor'],
                                 self.intensity_right['average'])
        rule_right_6 = ctrl.Rule(self.traffic_right['poor'] & self.speed_right['poor'] & self.people_right['good'],
                                 self.intensity_right['average'])

        # one rule is good rest are average
        rule_right_7 = ctrl.Rule(self.traffic_right['good'] & self.speed_right['average'] & self.people_right['average'],
                                 self.intensity_right['good'])
        rule_right_8 = ctrl.Rule(self.traffic_right['average'] & self.speed_right['good'] & self.people_right['average'],
                                 self.intensity_right['good'])
        rule_right_9 = ctrl.Rule(self.traffic_right['average'] & self.speed_right['average'] & self.people_right['good'],
                                 self.intensity_right['good'])

        # one rule is average rest are poor
        rule_right_10 = ctrl.Rule(self.traffic_right['average'] & self.speed_right['poor'] & self.people_right['poor'],
                                  self.intensity_right['poor'])
        rule_right_11 = ctrl.Rule(self.traffic_right['poor'] & self.speed_right['average'] & self.people_right['poor'],
                                  self.intensity_right['poor'])
        rule_right_12 = ctrl.Rule(self.traffic_right['poor'] & self.speed_right['poor'] & self.people_right['average'],
                                  self.intensity_right['poor'])

        rule_right_no_exception = ctrl.Rule(self.traffic_right['poor'] | self.speed_right['poor'] | self.people_right['poor'] |
                                           self.traffic_right['average'] | self.speed_right['average'] | self.people_right['average'] |
                                           self.traffic_right['good'] | self.speed_right['good'] | self.people_right['good'],
                                self.intensity_right['poor'])

        self.intensity_right_ctrl = ctrl.ControlSystem([rule_right_1, rule_right_2, rule_right_3,
                                                   rule_right_4, rule_right_5, rule_right_6,
                                                   rule_right_7, rule_right_8, rule_right_9,
                                                   rule_right_10, rule_right_11, rule_right_12,
                                                        rule_right_no_exception])

        self.intensity_right_c = ctrl.ControlSystemSimulation(self.intensity_right_ctrl)

    def __set_right_site_traffic_input(self, traffic):
        self.intensity_right_c.input['traffic'] = traffic

    def __set_right_site_people_input(self, people):
        self.intensity_right_c.input['people'] = people

    def __set_right_site_speed_input(self, speed):
        self.intensity_right_c.input['speed'] = speed

    def set_right_site_inputs(self, traffic, people, speed):
        """This method compute fuzzy logic int output value for traffic, people, speed defines as input values
           for right site intersection

        Args:
            traffic (int): How many cars is on right site street intersection
            people (int): How many people is on right site street intersection
            speed (int): What is average cars speed for right site intersection
        """
        self.__set_right_site_traffic_input(traffic)
        self.__set_right_site_people_input(people)
        self.__set_right_site_speed_input(speed)
        self.intensity_right_c.compute()

    def __define_up_site_rules(self):
        # all rule are the same
        rule_up_1 = ctrl.Rule(self.traffic_up['poor'] & self.speed_up['poor'] & self.people_up['poor'],
                              self.intensity_up['poor'])
        rule_up_2 = ctrl.Rule(self.traffic_up['average'] & self.speed_up['average'] & self.people_up['average'],
                              self.intensity_up['average'])
        rule_up_3 = ctrl.Rule(self.traffic_up['good'] & self.speed_up['good'] & self.people_up['good'], self.intensity_up['good'])

        # one rule is good rest are poor
        rule_up_4 = ctrl.Rule(self.traffic_up['good'] & self.speed_up['poor'] & self.people_up['poor'],
                              self.intensity_up['average'])
        rule_up_5 = ctrl.Rule(self.traffic_up['poor'] & self.speed_up['good'] & self.people_up['poor'],
                              self.intensity_up['average'])
        rule_up_6 = ctrl.Rule(self.traffic_up['poor'] & self.speed_up['poor'] & self.people_up['good'], self.intensity_up['average'])

        # one rule is good rest are average
        rule_up_7 = ctrl.Rule(self.traffic_up['good'] & self.speed_up['average'] & self.people_up['average'],
                              self.intensity_up['good'])
        rule_up_8 = ctrl.Rule(self.traffic_up['average'] & self.speed_up['good'] & self.people_up['average'],
                              self.intensity_up['good'])
        rule_up_9 = ctrl.Rule(self.traffic_up['average'] & self.speed_up['average'] & self.people_up['good'],
                              self.intensity_up['good'])

        # one rule is average rest are poor
        rule_up_10 = ctrl.Rule(self.traffic_up['average'] & self.speed_up['poor'] & self.people_up['poor'],
                               self.intensity_up['poor'])
        rule_up_11 = ctrl.Rule(self.traffic_up['poor'] & self.speed_up['average'] & self.people_up['poor'],
                               self.intensity_up['poor'])
        rule_up_12 = ctrl.Rule(self.traffic_up['poor'] & self.speed_up['poor'] & self.people_up['average'],
                               self.intensity_up['poor'])

        rule_up_no_exception = ctrl.Rule(self.traffic_up['poor'] | self.speed_up['poor'] | self.people_up['poor'] |
                                           self.traffic_up['average'] | self.speed_up['average'] | self.people_up['average'] |
                                           self.traffic_up['good'] | self.speed_up['good'] | self.people_up['good'],
                                self.intensity_up['poor'])


        self.intensity_up_ctrl = ctrl.ControlSystem([rule_up_1, rule_up_2, rule_up_3,
                                                rule_up_4, rule_up_5, rule_up_6,
                                                rule_up_7, rule_up_8, rule_up_9,
                                                rule_up_10, rule_up_11, rule_up_12,
                                                     rule_up_no_exception])

        self.intensity_up_c = ctrl.ControlSystemSimulation(self.intensity_up_ctrl)

    def __set_up_site_traffic_input(self, traffic):
        self.intensity_up_c.input['traffic'] = traffic

    def __set_up_site_people_input(self, people):
        self.intensity_up_c.input['people'] = people

    def __set_up_site_speed_input(self, speed):
        self.intensity_up_c.input['speed'] = speed

    def set_up_site_inputs(self, traffic, people, speed):
        """This method compute fuzzy logic int output value for traffic, people, speed defines as input values
           for up site intersection

        Args:
            traffic (int): How many cars is on up site street intersection
            people (int): How many people is on up site street intersection
            speed (int): What is average cars speed for up site intersection
        """
        self.__set_up_site_traffic_input(traffic)
        self.__set_up_site_people_input(people)
        self.__set_up_site_speed_input(speed)
        self.intensity_up_c.compute()

    def __define_down_site_rules(self):
        # all rule are the same
        rule_down_1 = ctrl.Rule(self.traffic_down['poor'] & self.speed_down['poor'] & self.people_down['poor'],
                                self.intensity_down['poor'])
        rule_down_2 = ctrl.Rule(self.traffic_down['average'] & self.speed_down['average'] & self.people_down['average'],
                                self.intensity_down['average'])
        rule_down_3 = ctrl.Rule(self.traffic_down['good'] & self.speed_down['good'] & self.people_down['good'], self.intensity_down['good'])

        # one rule is good rest are poor
        rule_down_4 = ctrl.Rule(self.traffic_down['good'] & self.speed_down['poor'] & self.people_down['poor'],
                                self.intensity_down['average'])
        rule_down_5 = ctrl.Rule(self.traffic_down['poor'] & self.speed_down['good'] & self.people_down['poor'],
                                self.intensity_down['average'])
        rule_down_6 = ctrl.Rule(self.traffic_down['poor'] & self.speed_down['poor'] & self.people_down['good'],
                                self.intensity_down['average'])

        # one rule is good rest are average
        rule_down_7 = ctrl.Rule(self.traffic_down['good'] & self.speed_down['average'] & self.people_down['average'],
                                self.intensity_down['good'])
        rule_down_8 = ctrl.Rule(self.traffic_down['average'] & self.speed_down['good'] & self.people_down['average'],
                                self.intensity_down['good'])
        rule_down_9 = ctrl.Rule(self.traffic_down['average'] & self.speed_down['average'] & self.people_down['good'],
                                self.intensity_down['good'])

        # one rule is average rest are poor
        rule_down_10 = ctrl.Rule(self.traffic_down['average'] & self.speed_down['poor'] & self.people_down['poor'],
                                 self.intensity_down['poor'])
        rule_down_11 = ctrl.Rule(self.traffic_down['poor'] & self.speed_down['average'] & self.people_down['poor'],
                                 self.intensity_down['poor'])
        rule_down_12 = ctrl.Rule(self.traffic_down['poor'] & self.speed_down['poor'] & self.people_down['average'],
                                 self.intensity_down['poor'])

        rule_down_no_exception = ctrl.Rule(self.traffic_down['poor'] | self.speed_down['poor'] | self.people_down['poor'] |
                                           self.traffic_down['average'] | self.speed_down['average'] | self.people_down['average'] |
                                           self.traffic_down['good'] | self.speed_down['good'] | self.people_down['good'],
                                self.intensity_down['poor'])


        self.intensity_down_ctrl = ctrl.ControlSystem([rule_down_1, rule_down_2, rule_down_3,
                                                  rule_down_4, rule_down_5, rule_down_6,
                                                  rule_down_7, rule_down_8, rule_down_9,
                                                  rule_down_10, rule_down_11, rule_down_12,
                                                       rule_down_no_exception])

        self.intensity_down_c = ctrl.ControlSystemSimulation(self.intensity_down_ctrl)

    def __set_down_site_traffic_input(self, traffic):
        self.intensity_down_c.input['traffic'] = traffic

    def __set_down_site_people_input(self, people):
        self.intensity_down_c.input['people'] = people

    def __set_down_site_speed_input(self, speed):
        self.intensity_down_c.input['speed'] = speed

    def set_down_site_inputs(self, traffic, people, speed):
        """This method compute fuzzy logic int output value for traffic, people, speed defines as input values
           for down site intersection

        Args:
            traffic (int): How many cars is on down site street intersection
            people (int): How many people is on down site street intersection
            speed (int): What is average cars speed for down site intersection
        """
        self.__set_down_site_traffic_input(traffic)
        self.__set_down_site_people_input(people)
        self.__set_down_site_speed_input(speed)
        self.intensity_down_c.compute()

    def __define_membership_functions_of_all_directions(self):
        self.left_right_intensity['red'] = fuzz.trimf(self.left_right_intensity.universe, [0, 20, 40])
        self.left_right_intensity['no_change_light'] = fuzz.trimf(self.left_right_intensity.universe, [40, 50, 60])
        self.left_right_intensity['green'] = fuzz.trimf(self.left_right_intensity.universe, [60, 80, 100])
        self.right_left_intensity['red'] = fuzz.trimf(self.right_left_intensity.universe, [0, 20, 40])
        self.right_left_intensity['no_change_light'] = fuzz.trimf(self.right_left_intensity.universe, [40, 50, 60])
        self.right_left_intensity['green'] = fuzz.trimf(self.right_left_intensity.universe, [60, 80, 100])
        self.up_down_intensity['red'] = fuzz.trimf(self.up_down_intensity.universe, [0, 20, 40])
        self.up_down_intensity['no_change_light'] = fuzz.trimf(self.up_down_intensity.universe, [40, 50, 60])
        self.up_down_intensity['green'] = fuzz.trimf(self.up_down_intensity.universe, [60, 80, 100])
        self.down_up_intensity['red'] = fuzz.trimf(self.down_up_intensity.universe, [0, 20, 40])
        self.down_up_intensity['no_change_light'] = fuzz.trimf(self.down_up_intensity.universe, [40, 50, 60])
        self.down_up_intensity['green'] = fuzz.trimf(self.down_up_intensity.universe, [60, 80, 100])

        self.light_horizontal['red'] = fuzz.trimf(self.light_horizontal.universe, [0, 1, 1])
        self.light_horizontal['green'] = fuzz.trimf(self.light_horizontal.universe, [1, 1, 2])

    def __define_all_sites_rules(self):
        rule_light_1 = ctrl.Rule(
            self.left_right_intensity['red'] & self.right_left_intensity['red'] & self.up_down_intensity['red'] & self.down_up_intensity['green'],
            self.light_horizontal['red'])
        rule_light_2 = ctrl.Rule(
            self.left_right_intensity['red'] & self.right_left_intensity['red'] & self.up_down_intensity['green'] & self.down_up_intensity['red'],
            self.light_horizontal['red'])
        rule_light_3 = ctrl.Rule(
            self.left_right_intensity['red'] & self.right_left_intensity['red'] & self.up_down_intensity['green'] & self.down_up_intensity['green'],
            self.light_horizontal['red'])
        rule_light_4 = ctrl.Rule(
            self.left_right_intensity['green'] & self.right_left_intensity['green'] & self.up_down_intensity['red'] & self.down_up_intensity['green'],
            self.light_horizontal['green'])
        rule_light_5 = ctrl.Rule(
            self.left_right_intensity['green'] & self.right_left_intensity['green'] & self.up_down_intensity['green'] & self.down_up_intensity['red'],
            self.light_horizontal['green'])
        rule_light_6 = ctrl.Rule(
            self.left_right_intensity['green'] & self.right_left_intensity['green'] & self.up_down_intensity['red'] & self.down_up_intensity['red'],
            self.light_horizontal['green'])
        rule_light_7 = ctrl.Rule(
            self.left_right_intensity['green'] & self.right_left_intensity['green'] & self.up_down_intensity['green'] & self.down_up_intensity['green'],
            self.light_horizontal['green'])
        rule_light_8 = ctrl.Rule(
            self.left_right_intensity['red'] & self.right_left_intensity['red'] & self.up_down_intensity['red'] & self.down_up_intensity['red'],
            self.light_horizontal['red'])
        rule_light_9 = ctrl.Rule(
            self.left_right_intensity['red'] & self.right_left_intensity['green'] & self.up_down_intensity['red'] & self.down_up_intensity['red'],
            self.light_horizontal['green'])
        rule_light_10 = ctrl.Rule(
            self.left_right_intensity['red'] & self.right_left_intensity['green'] & self.up_down_intensity['green'] & self.down_up_intensity['green'],
            self.light_horizontal['red'])
        rule_light_11 = ctrl.Rule(
            self.left_right_intensity['red'] & self.right_left_intensity['green'] & self.up_down_intensity['red'] & self.down_up_intensity['green'],
            self.light_horizontal['red'])
        rule_light_12 = ctrl.Rule(
            self.left_right_intensity['red'] & self.right_left_intensity['green'] & self.up_down_intensity['green'] & self.down_up_intensity['red'],
            self.light_horizontal['red'])
        rule_light_13 = ctrl.Rule(
            self.left_right_intensity['green'] & self.right_left_intensity['red'] & self.up_down_intensity['red'] & self.down_up_intensity['red'],
            self.light_horizontal['green'])
        rule_light_14 = ctrl.Rule(
            self.left_right_intensity['green'] & self.right_left_intensity['red'] & self.up_down_intensity['green'] & self.down_up_intensity['green'],
            self.light_horizontal['red'])
        rule_light_15 = ctrl.Rule(
            self.left_right_intensity['green'] & self.right_left_intensity['red'] & self.up_down_intensity['green'] & self.down_up_intensity['red'],
            self.light_horizontal['red'])
        rule_light_16 = ctrl.Rule(
            self.left_right_intensity['green'] & self.right_left_intensity['red'] & self.up_down_intensity['red'] & self.down_up_intensity['green'],
            self.light_horizontal['red'])

        rule_light_17 = ctrl.Rule(
            (self.left_right_intensity['no_change_light'] | self.right_left_intensity['no_change_light'] | self.up_down_intensity['no_change_light']) & self.down_up_intensity['red'],
            self.light_horizontal['red'])
        rule_light_18 = ctrl.Rule(
            (self.left_right_intensity['no_change_light'] | self.right_left_intensity['no_change_light'] | self.up_down_intensity['no_change_light']) & self.down_up_intensity['green'],
            self.light_horizontal['green'])
        rule_light_19 = ctrl.Rule(
            (self.left_right_intensity['no_change_light'] | self.right_left_intensity['no_change_light'] | self.down_up_intensity['no_change_light']) & self.up_down_intensity['red'],
            self.light_horizontal['red'])
        rule_light_20 = ctrl.Rule(
            (self.left_right_intensity['no_change_light'] | self.right_left_intensity['no_change_light'] | self.down_up_intensity['no_change_light']) & self.up_down_intensity['green'],
            self.light_horizontal['green'])
        rule_light_21 = ctrl.Rule(
            (self.left_right_intensity['no_change_light'] | self.down_up_intensity['no_change_light'] | self.up_down_intensity['no_change_light']) & self.right_left_intensity['red'],
            self.light_horizontal['red'])
        rule_light_22 = ctrl.Rule(
            (self.left_right_intensity['no_change_light'] | self.down_up_intensity['no_change_light'] | self.up_down_intensity['no_change_light']) & self.right_left_intensity['green'],
            self.light_horizontal['green'])
        rule_light_23 = ctrl.Rule(
            (self.down_up_intensity['no_change_light'] | self.right_left_intensity['no_change_light'] | self.up_down_intensity['no_change_light']) & self.left_right_intensity['red'],
            self.light_horizontal['red'])
        rule_light_24 = ctrl.Rule(
            (self.down_up_intensity['no_change_light'] | self.right_left_intensity['no_change_light'] | self.up_down_intensity['no_change_light']) & self.left_right_intensity['green'],
            self.light_horizontal['green'])

        rule_light_no_exception = ctrl.Rule(
            (self.down_up_intensity['red'] | self.down_up_intensity['no_change_light'] | self.down_up_intensity['green']) |
            self.up_down_intensity['red'] | self.up_down_intensity['no_change_light'] | self.up_down_intensity['green'] |
            self.left_right_intensity['red'] | self.left_right_intensity['no_change_light'] | self.left_right_intensity['green'] |
            self.right_left_intensity['red'] | self.right_left_intensity['no_change_light'] | self.right_left_intensity['green'],
            self.light_horizontal['red'])

        self.light_horizontal_ctrl = ctrl.ControlSystem([rule_light_1, rule_light_2, rule_light_3,
                                                    rule_light_4, rule_light_5, rule_light_6, rule_light_7, rule_light_8,
                                                    rule_light_9, rule_light_10, rule_light_11, rule_light_12, rule_light_13,
                                                    rule_light_14, rule_light_15, rule_light_16, rule_light_17, rule_light_18,
                                                    rule_light_19, rule_light_20, rule_light_21, rule_light_22, rule_light_23,
                                                    rule_light_24, rule_light_no_exception
                                                         ])

        self.light_horizontal_c = ctrl.ControlSystemSimulation(self.light_horizontal_ctrl)

    def initialize_fuzzy_logic(self):
        """This method initialize membership functions for fuzzy logic
            and read traffic, speed and people count input values
            next prepare input values for all sites intersection
        """
        self.__define_auto_membership_functions_of_part_directions()
        self.__define_left_site_rules()
        self.__define_right_site_rules()
        self.__define_up_site_rules()
        self.__define_down_site_rules()

        self.__define_membership_functions_of_all_directions()
        self.__define_all_sites_rules()

    def is_horizontal_light_green(self):
        """this method compute if light should be red or green in intersection area
            depends on input traffic, speed and people count values

        Returns:
            bool: A flag define color of light
        """
        self.light_horizontal_c.input['left-to-right'] = self.intensity_left_c.output['intensity']
        self.light_horizontal_c.input['right-to-left'] = self.intensity_right_c.output['intensity']
        self.light_horizontal_c.input['up-to-down'] = self.intensity_up_c.output['intensity']
        self.light_horizontal_c.input['down-to-up'] = self.intensity_down_c.output['intensity']

        self.light_horizontal_c.compute()

        if self.light_horizontal_c.output['light'] >= 1:
            return True
        return False
