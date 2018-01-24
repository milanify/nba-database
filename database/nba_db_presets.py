import datetime
import sqlite3
import pandas as pd
from sqlite3 import Error
from nba_py.league import GameLog
from urllib.request import pathname2url

# Create database starting with the year Micheal Jordan got drafted, the 1984-85 season
db_start_year = 1984

# Query up to the current year
now = datetime.datetime.now()
current_year = now.year

# Name of database file
database_name = 'nba.db'


"""
Dictionary of types of season data to download
Keys: Pre Season, Regular Season, All Star, and Playoffs
Values: Database table name

Format:
    season_type: sqlite_table_name
"""
season_types = {'Regular Season': 'player_reg_season',
                'All Star': 'player_all_star',
                'Playoffs': 'player_playoffs'}


"""
Properly formats the season

Example:
    At the time of this comment, we are in the 2018 NBA season, known as 2017-18 season
    If 2017 is passed into this function, "2017-18" will be returned

Args:
    season_start_year (str or int): beginning year of season

Return:
    String object in YYYY-YY format
"""
def formatSeasonString(season_start_year):
    next_year = int(season_start_year) + 1
    string_next_year = str(next_year)
    formatted_season_string = '{}-{}'.format(season_start_year, string_next_year[-2:])
    return formatted_season_string

"""
Retrieves player stats using nba_py API

Args:
    the_season_string (str): season in YYYY-YY format
    the_season_type (str): Pre Season, Regular Season, All Star, or Playoffs

Return:
    Pandas DataFrame object
"""
def getDataFrame(the_season_string, the_season_type):
    data_frame = GameLog(season=the_season_string, season_type=the_season_type, player_or_team='P').overall()
    return data_frame


"""
Ignores games in progress, where the Win/Loss column is NULL

Args:
    stats_data_frame (DataFrame): stats retrieved from api
    the_season_string (str): season in YYYY-YY format
    the_season_type (str): Pre Season, Regular Season, All Star, or Playoffs 

Return:
    Pandas DataFrame object without null values in the W/L column
"""
def dropNullValues(stats_data_frame, the_season_string, the_season_type):
    dataframe_rows_before_dropping = len(stats_data_frame)
    stats_dataframe = stats_data_frame.dropna(subset=['WL'])
    dataframe_rows_after_dropping = len(stats_dataframe)

    amount_of_rows_dropped = dataframe_rows_before_dropping - dataframe_rows_after_dropping
    if amount_of_rows_dropped > 0:
        print("{} entries for {} {} are for games currently in progress. Update again later to get them.".format(
            amount_of_rows_dropped, the_season_string, the_season_type))

    return stats_dataframe
