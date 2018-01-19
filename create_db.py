from nba_py.league import GameLog
import sqlite3

# Database file
conn = sqlite3.connect('nba.db')

"""
THIS IS THE CURRENT SEASON START YEAR. 

Example: At the time of writing, we are in the 2017-18 NBA season (officially known as the 2018 NBA season)
This means the season start year is 2017!
"""
current_season_start = 2017

# Create database starting with the year Micheal Jordan got drafted, the 1984-85 season
start_year = 1984
end_year = current_season_start


"""
Get individual player stats for every game

Args:
    seasonType (str): Pre Season, Regular Season, All Star, or Playoffs
    dbTableName (str): Name of the sqlite database table

season_string is in the format of '2017-18'
"""
def getPlayerBoxScores(seasonType, dbTableName):
    for year in range(start_year, end_year + 1):
        next_year = (year + 1)
        string_next_year = str(next_year)
        season_string = '{}-{}'.format(year, string_next_year[-2:])
        stats = GameLog(season=season_string, season_type=seasonType, player_or_team='P').overall()
        stats.to_sql(dbTableName, conn, if_exists='replace')
        conn.close()


getPlayerBoxScores('Regular Season', 'player_reg_season')
getPlayerBoxScores('All Star', 'player_all_star')
getPlayerBoxScores('Playoffs', 'player_playoffs')

