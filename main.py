from nba_py.league import GameLog
import sqlite3

conn = sqlite3.connect('nba.db')

start_date = 1996
end_date = 2017

for date in range(start_date, end_date + 1):
    next_year = (date + 1)
    string_next_year = str(next_year)
    season_string = "{}-{}".format(date, string_next_year[-2:])
    stats = GameLog(season=season_string, season_type='Regular Season', player_or_team='P').overall()
    stats.to_sql('player_game_stats', conn, if_exists='append')



conn.close()
