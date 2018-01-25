# nba-database

Create and update your own database of *National Basketball Association (NBA)* player box score statistics

Or use this repository to download periodically updated database files (coming soon)


## Preview
> Creating

![alt tag](https://github.com/milan102/nba-database/blob/master/gifs/create.gif)

> Updating

![alt tag](https://github.com/milan102/nba-database/blob/master/gifs/update.gif)

> Querying

```SQL
SELECT * FROM player_reg_season
	WHERE season_id LIKE '%2017'
	AND player_name = 'Stephen Curry'
```

![alt tag](https://github.com/milan102/nba-database/blob/master/gifs/query.gif)


## Requirements/Dependencies
- [Download Python3](https://www.python.org/downloads/)
- [Make sure you have pip, run `pip --version` in a command line to verify](https://pip.pypa.io/en/stable/installing/)

Do the following in a command line:
```python
pip install requests
```

```
pip install pandas
```

```
pip install nba_py
```


## Instructions for Modifying Presets
The *nba_db_presets.py* file has two items that can be changed:
1. Database start year
2. Name of database file

I recommend you **do not** modify the start year because certain stats from before 1984 are missing and incomplete

```python
# Create database starting with the year Micheal Jordan got drafted, the 1984-85 season
db_start_year = 1984

# Query up to the current year
now = datetime.datetime.now()
current_year = now.year

# Name of database file
database_name = 'nba.db'
```


## Notes
@klane *Special thanks to https://klane.github.io/databall1/data/wrangling/ for being a great starting point and reference*

@seemethere *And of course to https://github.com/seemethere/nba_py for creating the python API*

*By default, the script downloads raw player stat boxscores. Using these boxscores, additional advanced stats and team stats can be calculated on your own*


## Donations
<p align="center">
<a href="https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=HL3P4UC2JKEAN&lc=US&item_name=Milan%27s%20Software&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donateCC_LG%2egif%3aNonHosted"><img src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" alt="Donate"/></a>
</p>
