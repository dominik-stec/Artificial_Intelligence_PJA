"""
author: Dominik Stec,
index:  s12623,
email:  s12623@pja.edu.pl
To run module type:
 >> python calc_hearth_attack_risk.py
as Python interpreter command
random, numpy, copy, scikit-learn, pandas, json modules installation is need
algorithm write 2 json files and calculate risk of hearth attack for woman and man
"""

import random as r
import numpy as np
import copy
from sklearn import svm
from sklearn.model_selection import train_test_split
import pandas as pd
import json


class calc_hearth_attack_risk():
    """
    This class generate data about factors of hearth attack risk for woman and man.
    This data are write into two json files.
    This data are retrieve for use by support vector machine algorithm from scikit-learn module to train and test
    As result fitted SVC algorithm return classification woman or man into one of group:
    - high risk of hearth attack,
    - low risk of hearth attack
    Generated data come from internet resources statistics. Links are given.
    Factor specifications come from web site:
    https://wylecz.to/uklad-krazenia/czynniki-ryzyka-zawalu-serca/
    """

    #  public raw data from generate
    heart_attack_stat_data_man = list()
    heart_attack_stat_data_woman = list()


    def get_binary_randoms(self, peoples, random_start=10, random_stop=990):
        """This method generate list of tuples, consist two binary values: 0 or 1,
            with given by generate, random, split line proportion between binary tuples

        Args:
            peoples (list): Peoples with given factors about hearth attack
            random start (int): start value for random method generated split line proportion for binary tuples,
                                default value is 10
            random stop (int): maximum value for random method generated split line proportion for binary tuples,
                                default value is 990

        Returns:
            list: list of factors with high and low risk of hearth attack
        """
        #  list healthy people params
        disease_people = list()
        #  list disease people params
        health_people = list()
        #   to return
        all_classified_people = list()
        #  data classification
        mark_disease = 1
        mark_healthy = 0

        #  wrong value
        if random_start >= random_stop or random_stop > 990:
            return None
        #  split peoples to healthy and disease random sized groups
        #  low value == more disease peoples
        #  high value == more healthy people
        peoples_split_line = r.randrange(random_start, random_stop)

        #  for disease group
        for diseases in range(0, peoples_split_line):
            #  i have this
            disease_rand_val = 1
            #  add to disease group
            disease_people.append([disease_rand_val, mark_disease])
        #  for healthy group
        for healthy in range(peoples_split_line, peoples):
            #  i dont have this
            healthy_rand_val = 0
            #  add to health group
            health_people.append([healthy_rand_val, mark_healthy])

        #  join disease and health groups
        disease_people.extend(health_people)
        all_classified_people = copy.deepcopy(disease_people)

        #  return joined groups
        return all_classified_people


    def get_max_normative_randoms(self, normative, maximum, peoples):
        """This method generate list of tuples, consist generated risk factor value and
            its classification into group with high or low disease risk.

            Args:
                normative (int): Value of risk factor norm. If factor is greater than norm than risk is high else is low
                maximum (int): Maximum value of factor value generated for people from group of risk
                peoples (list): Peoples with given factors about hearth attack

            Returns:
                list: list of factors with high and low risk of hearth attack
        """
        #  list healthy people params
        disease_people = list()
        #  list disease people params
        health_people = list()
        #  data classification
        mark_disease = 1
        mark_healthy = 0

        #  split peoples to healthy and disease random sized groups
        peoples_split_line = r.randrange(10, peoples - 10)

        #  for disease group
        for diseases in range(0, peoples_split_line):
            #  value > norm == disease
            disease_rand_val = r.randrange(normative + 1, maximum)
            #  add to disease group
            disease_people.append([disease_rand_val, mark_disease])
        #  for healthy group
        for healthy in range(peoples_split_line, peoples):
            #  value == normative == health
            healthy_rand_val = normative
            #  add to health group
            health_people.append([healthy_rand_val, mark_healthy])

        #  join disease and health groups
        disease_people.extend(health_people)
        all_classified_people = copy.deepcopy(disease_people)

        #  return joined groups
        return all_classified_people


    def get_normative_randoms_range(self, normative, minimum, maximum, direction, peoples):
        """This method generate list of tuples, consist generated risk factor value and
             its classification into group with high or low disease risk.

             Args:
                 normative (int): Value of risk factor norm. Depend of given :param direction:
                                    if factor is greater than norm than risk is high else is low or vice versa
                 minimum (int): Minimum value of factor value generated for people from group of risk
                                or vice versa depends on given :param direction:
                 maximum (int): Maximum value of factor value generated for people from group of risk
                                or vice versa depends on given :param direction:
                 direction (str): if direction is set to 'min_is_health' than factors lowest than :param normative:
                                are classify to health and rest factors are classify to group of risk
                                and if  direction is set to 'max_is_health' than vice versa
                peoples (list): Peoples with given factors about hearth attack

             Returns:
                 list: list of factors with high and low risk of hearth attack
        """
        #  list healthy people params
        disease_people = list()
        #  list disease people params
        health_people = list()
        #  data classification
        mark_disease = 1
        mark_healthy = 0

        #  split peoples to healthy and disease random sized groups
        peoples_split_line = r.randrange(10, peoples - 10)

        #  if min value mean more healthy
        if direction == 'min_is_health':
            #  for disease group
            for diseases in range(0, peoples_split_line):
                #  value > norm == disease
                disease_rand_val = r.randrange(normative, maximum)
                #  add to disease group
                disease_people.append([disease_rand_val, mark_disease])
            #  for healthy group
            for healthy in range(peoples_split_line, peoples):
                #  value <= norm == health
                healthy_rand_val = r.randrange(minimum, normative)
                #  add to health group
                health_people.append([healthy_rand_val, mark_healthy])
        #  if max value mean more healthy
        elif direction == 'max_is_health':
            for diseases in range(0, peoples_split_line):
                #  value < norm == disease
                disease_rand_val = r.randrange(minimum, normative)
                disease_people.append([disease_rand_val, mark_disease])
            for healthy in range(peoples_split_line, peoples):
                #  velue >= norm == health
                healthy_rand_val = r.randrange(normative, maximum)
                health_people.append([healthy_rand_val, mark_healthy])

        #  join disease and health groups
        disease_people.extend(health_people)
        all_classified_people = copy.deepcopy(disease_people)

        #  return joined groups
        return all_classified_people


    def calc_heart_attack_factors(self):
        """This method generate lists of different factors with its group risk or health classification.
            Given, generated classification params come from internet statistics.
        """
        #  cholesterol
        #  https://www.allecco.pl/artykuly/cholesterol-normy-rodzaje-dobry-i-zly-cholesterol-hdl-i-ldl.html
        woman_HDL = self.get_normative_randoms_range(50, 1, 300, 'max_is_health', 1000)
        man_HDL = self.get_normative_randoms_range(40, 1, 300, 'max_is_health', 1000)
        woman_LDL = self.get_normative_randoms_range(100, 20, 300, 'min_is_health', 1000)
        man_LDL = self.get_normative_randoms_range(100, 20, 300, 'min_is_health', 1000)

        #  nadciśnienie tętnicze skurczowe
        #  disease if: value > 140
        #  https://wylecz.to/uklad-krazenia/czynniki-ryzyka-zawalu-serca/
        systolic_arterial_hypertension = self.get_max_normative_randoms(140, 240, 1000)

        #  nadciśnienie tętnicze rozkurczowe
        #  disease if: value > 90
        #  https://wylecz.to/uklad-krazenia/czynniki-ryzyka-zawalu-serca/
        diastolic_hypertension = self.get_max_normative_randoms(90, 120, 1000)

        #  20 % smoke
        #  https://cbos.pl/SPISKOM.POL/2019/K_104_19.PDF
        smoking = self.get_binary_randoms(1000, 199, 201)

        #  11 % diabetes
        #  https://pacjent.gov.pl/artykul/cukrzyca-w-liczbach
        diabetes = self.get_binary_randoms(1000, 109, 112)

        #  https://www.medonet.pl/narodowy-test-zdrowia-polakow/raport-2020,narodowy-test-zdrowia-polakow-2020--problem-otylosci-jest-coraz-grozniejszy,film,61552230.html
        #  man 28 % corpulence (otyłość)
        man_corpulance = self.get_binary_randoms(1000, 279, 281)

        #  woman 21 % corpulence (otyłość)
        woman_corpulance = self.get_binary_randoms(1000, 209, 211)

        #  age
        #  https://podyplomie.pl/kardiologia/09999,zawal-miesnia-sercowego-u-osob-mlodych
        age = self.get_normative_randoms_range(60, 45, 100, 'min_is_health', 1000)

        #  man have often heart attack than woman
        male = self.get_binary_randoms(1000, 300, 700)
        female = self.get_binary_randoms(1000, 100, 200)

        #  statistics empty
        make_sport_excersises = self.get_binary_randoms(1000, 650, 850)

        #  make man hearth attack factors list
        self.heart_attack_stat_data_man.append(man_HDL)
        self.heart_attack_stat_data_man.append(man_LDL)
        self.heart_attack_stat_data_man.append(systolic_arterial_hypertension)
        self.heart_attack_stat_data_man.append(diastolic_hypertension)
        self.heart_attack_stat_data_man.append(smoking)
        self.heart_attack_stat_data_man.append(diabetes)
        self.heart_attack_stat_data_man.append(man_corpulance)
        self.heart_attack_stat_data_man.append(age)
        self.heart_attack_stat_data_man.append(male)
        self.heart_attack_stat_data_man.append(make_sport_excersises)

        #  make woman hearth attack factors list
        self.heart_attack_stat_data_woman.append(woman_HDL)
        self.heart_attack_stat_data_woman.append(woman_LDL)
        self.heart_attack_stat_data_woman.append(systolic_arterial_hypertension)
        self.heart_attack_stat_data_woman.append(diastolic_hypertension)
        self.heart_attack_stat_data_woman.append(smoking)
        self.heart_attack_stat_data_woman.append(diabetes)
        self.heart_attack_stat_data_woman.append(woman_corpulance)
        self.heart_attack_stat_data_woman.append(age)
        self.heart_attack_stat_data_woman.append(female)
        self.heart_attack_stat_data_woman.append(make_sport_excersises)


    def get_X_y_fit_data_to_preprecessing(self, heart_attack_factors_data):
        """This method generate list of data with X and y value for SVC algorithm. X value is train data array
            and y value is raw data with hearth attack group classification for next retrieve.

             Args:
                 hearth_attack_factors_data (list): Data with given groups of classified peoples
                                                     into healthy or high risk about hearth attack,
                                                     depends on given risk factors

             Returns:
                 list: list of ready train data and raw classification data for next retrieve
        """
        # map raw list data to numpy module
        np_data = np.zeros(shape=(10, 1000, 2))
        for i in range(0, len(heart_attack_factors_data)):
            np_data[i] = heart_attack_factors_data[i]

        #  reshape raw data
        np_t_data = np_data.T
        #  make X data for fit
        X = np.array(np_t_data[0])

        #  make y raw data not for fit
        health_state_preprocess = np.array(np_t_data[1])

        ret = [X, health_state_preprocess]
        return ret

    def get_y_classification(self, health_state):
        """This method retrieve raw data with classification of hearth attack risk
            into shape ready to use in SVC algorithm.

             Args:
                 health_state (list): Data with given groups of classified peoples
                                      into healthy or high risk about hearth attack,
                                      depends on given risk factors

             Returns:
                 list: list of ready train, classification data
        """
        #  counters for calc disease risk
        yes = 0.
        no = 0.
        #  to return
        state_classifier = np.zeros(1000)
        #  for loop
        idx = 0
        classifier = 0
        #  get single human hearth attack risk factors marks
        for state in health_state:
            for i in range(0, len(state)):
                #  if no risk
                if state[i] == 0.:
                    no = no + 1.
                #  if risk
                elif state[i] == 1.:
                    yes = yes + 1.
                #  if yes have more
                if yes > no:
                    classifier = 1
                #  if no have more
                elif no >= yes:
                    classifier = 0
            #  sign classifier for human
            state_classifier[idx] = classifier
            idx = idx + 1
            #  reset
            yes = 0.
            no = 0.
        return state_classifier

    def generate_json_data(self):
        """This method generate two JSON format files about woman and man with factors about hearth attack risk.
            JSON data are write into files.
        """
        #  map from numpy to pandas
        df_woman = pd.DataFrame(self.heart_attack_stat_data_woman)
        df_man = pd.DataFrame(self.heart_attack_stat_data_man)

        #  format json shape
        df_json_woman = df_woman.to_json(orient='split')
        df_json_man = df_man.to_json(orient='split')

        #  map from pandas to json module
        json_woman = json.loads(df_json_woman)
        json_man = json.loads(df_json_man)

        #  write json to file with indent, vertical format
        with open('woman_json.txt', 'w') as outfile:
            json.dump(json_woman, outfile, indent=1)
        print('\ngenerated json data to file:  woman_json.txt')

        # for man
        with open('man_json.txt', 'w') as outfile:
            json.dump(json_man, outfile, indent=1)
        print('generated json data to file:  man_json.txt')


risk = calc_hearth_attack_risk()

#  calc raw data from based statistics generator
risk.calc_heart_attack_factors()

#  generate json data to file from raw data
risk.generate_json_data()

#  get X data and y preprocess data for fit SVC
health_state_woman_preprocess = risk.get_X_y_fit_data_to_preprecessing(risk.heart_attack_stat_data_woman)
health_state_man_preprocess = risk.get_X_y_fit_data_to_preprecessing(risk.heart_attack_stat_data_man)

#  get y data for fit SVC
y_woman = risk.get_y_classification(health_state_woman_preprocess[1])
X_woman = health_state_woman_preprocess[0]
y_man = risk.get_y_classification(health_state_man_preprocess[1])
X_man = health_state_man_preprocess[0]

print()

#  SVC logic for woman data
X_train, X_test, y_train, y_test = train_test_split(X_woman, y_woman, test_size=0.20)
svc = svm.SVC(kernel='linear', gamma=100).fit(X_train, y_train)
score = svc.score(X_test, y_test)
print('woman acc', score)
print('woman healthy', svc.predict(np.array([[180, 60, 120, 110, 0, 1, 0, 40, 0, 1]])))
print('woman disease', svc.predict(np.array([[30, 270, 140, 70, 1, 1, 1, 60, 1, 0]])))

print()

#  SVC logic for man data
X_train, X_test, y_train, y_test = train_test_split(X_man, y_man, test_size=0.20)
svc = svm.SVC(kernel='linear', gamma=100).fit(X_train, y_train)
score = svc.score(X_test, y_test)
print('man acc', score)
print('man healthy', svc.predict(np.array([[200, 40, 140, 90, 0, 0, 1, 30, 1, 1]])))
print('man disease', svc.predict(np.array([[1, 300, 120, 60, 1, 1, 1, 75, 1, 0]])))


