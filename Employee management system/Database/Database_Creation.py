#######SQLitestuff######################


def create_connection(db_file):
"""Create a database connection to a SQLite database"""
    conn=None
    try:
    conn=sqlite3.connect(db_file)
    exceptErrorase:
    print(e)

    return conn

###Creates a new database called database when needed uncomment this section

#if__name__=='__main__':
#create_connection('DatabaseFiles\database.db')

###ends new database builder


def create_table(conn,create_table_sql):
    try:
        c=conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
            print(e)


def database_builder():
    database=r"databasefiles\database.db"

    sql_create_employees_table="""CREATE TABLE IF NOT EXISTS employees(
    id integer PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    employee_number integer,
    password TEXT,
    role TEXT,
    initials TEXT

    );"""

    sql_create_about_table="""CREATE TABLE IFNOT EXISTS products(
    id integer PRIMARY KEY AUTOINCREMENT,
    Education TEXT NOT NULL,
    EnvironmentSatisfaction TEXT NOT NULL,
    JobInvolvement TEXT,
    JobSatisfaction Text,
    PerformanceRating TEXT,
    RelationshipSatisfaction TEXT,
    WorkLifeBalance Text,
    );"""

#createadatabaseconnection
conn=create_connection(database)

#createtables
if conn is not None:
    #createprojectstable
    create_table(conn,sql_create_employees_table)

    #createtaskstable
    create_table(conn,sql_create_products_table)
else:
	Print('Error! Cannot create the database connection.")
