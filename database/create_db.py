from nba_db_presets import *


"""
Create table of stats
season_string is in the format of '2017-18'

Args:
    the_season_type (str): Pre Season, Regular Season, All Star, or Playoffs
    db_table_name (str): Name of the sqlite database table
"""
def createPlayerBoxScores(the_season_type, db_table_name):

    for year in range(start_year, end_year + 1):
        season_string = formatSeasonString(year)
        stats = getDataFrame(season_string, the_season_type)

        if len(stats) != 0:
            stats.to_sql(db_table_name, conn, if_exists='append')
            print("Completed the {} {}".format(season_string, the_season_type))


"""
Check if database table exists

Args:
    db_connection (connection): SQLite database connection object
    db_table_name (str): Name of the sqlite database table
    
Return:
    True or False
"""
def tableExists(db_connection, db_table_name):
    cur = db_connection.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='{}'".format(db_table_name))

    if cur.fetchone() is not None:
        print("{} table already exists in the database, update by running update_db.py".format(db_table_name))
        cur.close()
        return True

    cur.close()
    return False


# Database file that will be created
conn = sqlite3.connect(database_name)


# As defined in presets.py file
start_year = db_start_year
end_year = current_year


"""
Loop through dictionary defined in presets.py file
If table does not exist in the database, must be created
"""
for season_type, table_name in season_types.items():
    if not tableExists(conn, table_name):
        print("{} table will be created now".format(table_name))
        createPlayerBoxScores(season_type, table_name)

conn.close()
