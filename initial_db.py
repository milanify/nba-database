from nba_py.league import GameLog
import sqlite3

conn = sqlite3.connect('nba.db')

'''
THIS IS THE CURRENT SEASON START YEAR. 
Example: As of right now, we are in the 2017-18 NBA season (officially known as the 2018 NBA season)
This means the season start year is 2017!
'''
current_season_start = 2017

# Season stats start with the 1996-1997 season
start_year = 1996
end_year = current_season_start

'''
Loops through all seasons
season_string is in the format of 2017-18
'''
for years in range(start_year, end_year + 1):
    next_year = (years + 1)
    string_next_year = str(next_year)
    season_string = "{}-{}".format(years, string_next_year[-2:])
    stats = GameLog(season=season_string, season_type='Regular Season', player_or_team='P').overall()
    stats.to_sql('player_game_stats', conn, if_exists='append')


conn.close()
