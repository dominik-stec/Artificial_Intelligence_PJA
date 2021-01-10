"""
author: Dominik Stec,
index:  s12623,
email:  s12623@pja.edu.pl
To run visualization type:
 >> python movies_recommendation.py
as Python interpreter command
pandas, numpy, copy, math and scikit-learn modules installation is need
algorithm retrieve prepared data from needed Excel file
"""

import pandas as pd
import numpy as np
import copy
import math
from sklearn.cluster import KMeans

class MovieRecommendation():
    """
    This class read rating by users, movies data from Excel file
    and return recommended user name for given user with similar likes,
    in addition exist possibility to show 5 recommended and not recommended
    by user movies.
    """
    __df = None
    __np_df_map = None

    def read_data(self):
        """This method read prepared data from Excel file with extension *.xls
            and retrieve this data into DataFrame format with labels from Pandas library
        """

        #  read data from Excel to DataFrame
        excel_data_df = pd.read_excel('data.xls', header=None)

        col_label = list()
        single_row_col = dict()
        row = list()
        row_list = list()

        #  save columns label names from Excel
        for col in excel_data_df.index:
            col_label.append(excel_data_df.loc[col].at[0])

        #  iter numbers of rows from Excel
        for row_count in excel_data_df.index:
            #  iter numbers od columns with step=2 from Excel
            for col in range(1, excel_data_df.shape[1], 2):
                #  save movie title as key
                key = excel_data_df.loc[row_count].at[col]
                #  condition prevent index out of bound exception
                if excel_data_df.shape[1] == col+1:
                    break
                #  save movie rating as val
                val = excel_data_df.loc[row_count].at[col+1]
                #  save single entity
                single_row_col[key] = val
                #  save list of single entities into one row
                row.append(single_row_col)
            #  copy complete row into list od rows
            row_list.append(copy.deepcopy(row))
            #  clear for next iter
            row.clear()
            single_row_col.clear()

        data = dict()
        #  make 'data' dictionary keys as columns names labels
        #  foreach key (column) assign rows (entities) in vertical direction
        for col in excel_data_df.index:
            data[col_label[col]] = row_list[col][0]

        #  make DataFrame with row and column labels from dictionary
        self.__df = pd.DataFrame.from_dict(data, orient="index")
        #  map DataFrame entities with rating to numpy array
        self.__np_df_map = self.__df.to_numpy()




    def get_movies(self, user, movies_rating):
        """This method return 5 best or 5 weak user movies depends on choose retrieve flag

        Args:
            user (str): User name for return rated by user movies
            movies_rating (str): For movies_rating named 'first' return 5 best user movies
                                    For movies_rating named 'last'return 5 weak user movies

        Returns:
            list: list of 5 best or 5 weak movies
        """
        #  get user row index in DataFrame
        idx = 0
        for idx_name in self.__df.index:
            if idx_name == user:
                break
            idx = idx + 1

        np_df_map_keys = list()
        #  copy of vector with user ratings values
        vect = self.__np_df_map[idx].copy()

        #  5 iter for choose 5 first or last movies, default select first
        #  depends on given flag find 5 maximum or 5 minimum rating values
        for i in range(0, 5):
            if movies_rating == 'first':
                min_or_max_val = np.nanmax(vect)
            elif movies_rating == 'last':
                min_or_max_val = np.nanmin(vect)
            else:
                min_or_max_val = np.nanmax(vect)

            #  find index of column for optimized rating of movie
            counter = 0
            for item in vect:
                if item == min_or_max_val:
                    break
                counter = counter + 1

            #  remember index into list
            np_df_map_keys.append(counter)
            #  exclude used rating from next iter and optimization search
            vect[counter] = None

        #  check user name index in row
        user_idx = 0
        for user_name in self.__df.index:
            if user_name == user:
                break
            user_idx = user_idx + 1

        movies = list()
        col_idx = 0
        i = 0

        #  sort columns positions ascending
        np_df_map_keys.sort()

        #  add chosen movies names into method return list
        #  use for this column indexes mapping to column (movies) name
        for col in self.__df.columns:
            if i == 5:
                break
            if col_idx == np_df_map_keys[i]:
                movies.append(col)
                i = i + 1
            col_idx = col_idx + 1

        return movies

    def euclidean_score(self, dataset, user1, user2):
        """This method compute the Euclidean distance score between user1 and user2

        Args:
            dataset (DataFrame): data use for calculate distance between user1 and user2
            user1 (str): first user name
            user2 (str): second user name

        Returns:
            float: distance calculation between user1 and user2 based on dataset
        """

        #  check if user name is valid
        if user1 not in dataset.index:
            raise TypeError('Cannot find ' + user1 + ' in the dataset')

        if user2 not in dataset.index:
            raise TypeError('Cannot find ' + user2 + ' in the dataset')

        #  Movies rated by both user1 and user2
        common_movies = {}

        #  mapping user name to indexed position
        idx = 0
        user_idx = dict()
        for user in dataset.index:
            user_idx[user] = idx
            idx = idx + 1

        #  convert user row with ratings from DataFrame to numpy
        np_data_user1 = dataset.loc[user1].to_numpy()
        np_data_user2 = dataset.loc[user2].to_numpy()
        #  number of movies
        length = len(np_data_user1)
        for i in range(0, length):
            #  if users choose the same movie
            if not math.isnan(np_data_user1[i]) and not math.isnan(np_data_user2[i]):
                #  remember title of movie
                item = dataset.columns.values[i]
                common_movies[item] = 1

        # If there are no common movies between the users,
        # then the score is 0
        if len(common_movies) == 0:
            return 0

        squared_diff = []

        #  number of movies
        for i in range(0, length):
            #  if users choose the same movie
            if not math.isnan(np_data_user1[i]) and not math.isnan(np_data_user2[i]):
                #  Euclidean distance calculation
                #  access to dataset by method iloc with integer indexes
                user1_rate = dataset.iloc[user_idx[user1], i]
                user2_rate = dataset.iloc[user_idx[user2], i]
                squared_diff.append(np.square(user1_rate - user2_rate))

        return 1 / (1 + np.sqrt(np.sum(squared_diff)))

    # Compute the Pearson correlation score between user1 and user2
    def pearson_score(self, dataset, user1, user2):
        """This method Compute the Pearson correlation score between user1 and user2

        Args:
            dataset (DataFrame): data use for calculate distance between user1 and user2
            user1 (str): first user name
            user2 (str): second user name

        Returns:
            float: distance calculation between user1 and user2 based on dataset
        """

        #  check if user name is valid
        if user1 not in dataset.index:
            raise TypeError('Cannot find ' + user1 + ' in the dataset')

        if user2 not in dataset.index:
            raise TypeError('Cannot find ' + user2 + ' in the dataset')

        # Movies rated by both user1 and user2
        common_movies = {}

        #  mapping user name to indexed position
        idx = 0
        user_idx = dict()
        for user in dataset.index:
            user_idx[user] = idx
            idx = idx + 1

        #  convert user row with ratings from DataFrame to numpy
        np_data_user1 = dataset.loc[user1].to_numpy()
        np_data_user2 = dataset.loc[user2].to_numpy()
        #  number of movies
        length = len(np_data_user1)
        for i in range(0, length):
            #  if users choose the same movie
            if not math.isnan(np_data_user1[i]) and not math.isnan(np_data_user2[i]):
                #  remember title of movie
                item = dataset.columns.values[i]
                common_movies[i] = item

        num_ratings = len(common_movies)

        # If there are no common movies between user1 and user2, then the score is 0
        if num_ratings == 0:
            return 0

        #  Calculate the sum of ratings of all the common movies
        #  access to dataset by method iloc with integer indexes
        user1_sum = np.sum([dataset.iloc[user_idx[user1], item] for item in common_movies])
        user2_sum = np.sum([dataset.iloc[user_idx[user2], item] for item in common_movies])

        # Calculate the sum of squares of ratings of all the common movies
        user1_squared_sum = np.sum(np.square([dataset.iloc[user_idx[user1], item] for item in common_movies]))
        user2_squared_sum = np.sum(np.square([dataset.iloc[user_idx[user2], item] for item in common_movies]))

        # Calculate the sum of products of the ratings of the common movies
        sum_of_products = np.sum([dataset.iloc[user_idx[user1], item] * dataset.iloc[user_idx[user2], item] for item in common_movies])

        # Calculate the Pearson correlation score
        Sxy = sum_of_products - (user1_sum * user2_sum / num_ratings)
        Sxx = user1_squared_sum - np.square(user1_sum) / num_ratings
        Syy = user2_squared_sum - np.square(user2_sum) / num_ratings

        if Sxx * Syy == 0:
            return 0

        return Sxy / np.sqrt(Sxx * Syy)

    def get_user_recommendation(self, user):
        """This method choose mostly similar user in movies rating preferences

        Args:
            user (str): name of user for fit rating movies preferences

        Returns:
            str: name of user with mostly similar preferences with given user
        """

        #  list of users without chosen user
        usr = np.array([usr for usr in self.__df.index.values if not usr==user])
        order = 0
        user_order = dict()
        metric_list = list()
        #  for single user
        for u in usr:
            #  calculate Pearson metric
            metric = self.pearson_score(self.__df, user, u)
            #  change negative metric to positive metric
            if metric < 0:
                metric = np.abs(metric)
            #  map index of user position to user name
            user_order[order] = u
            order = order + 1
            #  save metric value as list nested in list
            metric_list.append([metric])
        #  append neighborhood for metric as list value=1
        #  create two dimensional point for KMeans algorithm
        for i in metric_list:
            i.append(1)
        #  convert metric points to numpy array
        X = np.array(metric_list)

        #  artificial intelligence
        kmeans = KMeans(init='k-means++', n_clusters=3, n_init=20)
        kmeans.fit(X)
        result = kmeans.predict(X)

        #  get user name from index
        #  find maximum value index as result AI algorithm
        idx = None
        max = np.nanmax(result)
        for i in range(0, len(result)):
            if result[i] == max:
                idx = i
        ret = user_order[idx]

        return ret


mov_recom = MovieRecommendation()
mov_recom.read_data()
print()
print('list of recommended movies:')
print(mov_recom.get_movies('Dominik Stec', 'first'))
print()
print('list of not recommended movies:')
print(mov_recom.get_movies('Dominik Stec', 'last'))
print()
print('user with similar movies ratings:')
print(mov_recom.get_user_recommendation('Dominik Stec'))
