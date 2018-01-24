from nba_db_presets import *

"""
Check for an existing SQLite database

Args:
    db_file (str): database file path
    
Return:
    Connection object
"""
def check_connection(db_file):
    try:
        dburi = 'file:{}?mode=rw'.format(pathname2url(db_file))
        conn = sqlite3.connect(dburi, uri=True)
        return conn
    except sqlite3.OperationalError:
        print("{} file does not exist, run create_db.py".format(db_file))
        raise SystemExit(0)

def getRecentSeasonInDatabase(database_table):
    cur.execute("SELECT MAX(SEASON_ID) FROM {}".format(database_table))
    most_recent_season_in_db = cur.fetchone()[0][-4:]
    return most_recent_season_in_db


def getNumberOfRowsInDatabaseTable(database_table, database_recent_season):
    cur.execute("SELECT COUNT(*) FROM {} WHERE SEASON_ID LIKE '%{}'".format(database_table, database_recent_season))
    number_of_rows_in_db = int(cur.fetchone()[0])
    return number_of_rows_in_db


conn = check_connection(database_name)
cur = conn.cursor()
end_year = current_year


for season_type, table_name in season_types.items():
    recent_season_in_db = getRecentSeasonInDatabase(table_name)

    for year in range(int(recent_season_in_db), end_year + 1):
        number_of_db_rows = getNumberOfRowsInDatabaseTable(table_name, year)
        season_string = formatSeasonString(year)
        stats = getDataFrame(season_string, season_type)
        number_of_data_frame_rows = len(stats)

        stats = dropNullValues(stats, season_string, season_type)

        if number_of_data_frame_rows == number_of_db_rows:
            print("No new entries found for {} {}".format(season_string, season_type))
        else:
            amount_of_new_data = len(stats) - number_of_db_rows
            stats = stats.sort_values(by=['GAME_DATE'])

            new_data = stats.tail(amount_of_new_data)

            new_data.to_sql(table_name, conn, if_exists='append')
            print("{} new entries added for {} {}".format(str(amount_of_new_data), season_string, season_type))
