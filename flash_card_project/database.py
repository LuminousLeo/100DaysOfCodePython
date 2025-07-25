import sqlite3
import pandas

# use pandas.read_csv() to get the columns of within
# the csv file
# NOTE:  got this csv from this reddit post https://www.reddit.com/r/LearnJapanese/comments/rft2oe/first_3000_words_most_commonly_used_in_japanese/
JP_DATAFRAME = pandas.read_csv('./data/Copy of 3000 common JP words.csv')
TABLE_NAME = 'JP_WORDS'
COLUMN_NAMES = [col for col in JP_DATAFRAME.columns]


def database_creation():
    """database_creation() is a method that creates a sql database from
    the csv file that contain all the necessary data for it"""

    # access (or create if it does not exist)
    # the database that contains all the most used japanese
    # words, their pronunciation and translation
    conn = sqlite3.connect('data/japanese.db')
    cursor = conn.cursor()

    # get a list of column names from JP_CSV dataframe
    # cool oneliner that I saw online :P
    column_names = ', '.join([f'"{col}"' for col in COLUMN_NAMES])
    # creation query
    create_table_query  = f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ({column_names}, known BOOLEAN);'
    # create the table with the necessary columns
    cursor.execute(create_table_query)

    # get everything inside the JP_WORDS table
    table_check_query = f'SELECT count(*) FROM {TABLE_NAME}'
    table_check = cursor.execute(table_check_query)
    num_words = table_check.fetchall()

    # check if table is empty
    if num_words[0][0] == 0:
        # iterate through every row in the dataframe to get each row
        # and then insert that said row into the sql database
        for index, row in JP_DATAFRAME.iterrows():
            values = ', '.join([f'"{row_item}"' for row_item in row])
            insert_sql = f'INSERT INTO {TABLE_NAME} ({', '.join(JP_DATAFRAME.columns)}) VALUES ({values})'
            cursor.execute(insert_sql)

        conn.commit()
        conn.close()


def rand_words():
    """rand_words() is a method that selects 10 different japanese
    words (and it's pronounciation and translation) from the database and returns them
    as a list of tuples. ex: [(jap, pronounce, translation), ...]"""

    # get the database
    conn = sqlite3.connect('data/japanese.db')
    cursor = conn.cursor()

    # get 10 random jap words (and it's pronounciaton and translation) from the database
    word_selection_query1 = f'SELECT {', '.join([f'{col}' for col in COLUMN_NAMES])} FROM {TABLE_NAME} WHERE known IS TRUE ORDER BY RANDOM() LIMIT 3'
    word_selection_exec1 = cursor.execute(word_selection_query1)
    word_list = word_selection_exec1.fetchall()
    if len(word_list) == 0:
        word_selection_query2 = f'SELECT {', '.join([f'{col}' for col in COLUMN_NAMES])} FROM {TABLE_NAME} WHERE known IS NULL OR known IS FALSE ORDER BY RANDOM() LIMIT 10'
    elif len(word_list) == 1:
        word_selection_query2 = f'SELECT {', '.join([f'{col}' for col in COLUMN_NAMES])} FROM {TABLE_NAME} WHERE known IS NULL OR known IS FALSE ORDER BY RANDOM() LIMIT 9'
    elif len(word_list) == 2:
        word_selection_query2 = f'SELECT {', '.join([f'{col}' for col in COLUMN_NAMES])} FROM {TABLE_NAME} WHERE known IS NULL OR known IS FALSE ORDER BY RANDOM() LIMIT 8'
    elif len(word_list) == 3:
        word_selection_query2 = f'SELECT {', '.join([f'{col}' for col in COLUMN_NAMES])} FROM {TABLE_NAME} WHERE known IS NULL OR known IS FALSE ORDER BY RANDOM() LIMIT 7'
    word_selection_exec2 = cursor.execute(word_selection_query2)
    word_list.extend(word_selection_exec2.fetchall())
    conn.commit()
    conn.close()

    # return those words (and it's pronounciaton and translation) as a list of tuples
    return word_list


def save_word_db(word):
    """save_word_db(word) is a method from the database module that
    updates the 'known' column to TRUE of a given word"""

    # connect to the database
    conn = sqlite3.connect('data/japanese.db')
    cursor = conn.cursor()

    # update the 'known' column of the given word to TRUE
    word_insert_query = f'UPDATE {TABLE_NAME} SET known = TRUE WHERE japanese = "{word}"'
    cursor.execute(word_insert_query)

    conn.commit()
    conn.close()