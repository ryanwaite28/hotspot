import psycopg2
from chamber import DATABASE_URL

sql_file = 'schema.sql'
drop_sql_file = 'drop-tables.sql'

def init_tables(drop_tables = False):
    try:
        DB = psycopg2.connect(DATABASE_URL)
        cursor = DB.cursor()

        if drop_tables == True:
            delete_commands_list = ''
            with open(drop_sql_file) as dfp:
                delete_commands_list = dfp.read().split(';')[:-1]
            
            for command in delete_commands_list:
                try:
                    cursor.execute(command)
                    DB.commit()
                except Exception as e:
                    print('command failed...')
                    print(command)
                    raise e
                print('tables dropped successfully')

        commands_list = ''
        with open(sql_file) as fp:
            commands_list = fp.read().split(';')[:-1]

        for command in commands_list:
            try:
                cursor.execute(command)
                DB.commit()
            except Exception as e:
                print('command failed...')
                print(command)
                raise e

        print('tables created successfully')
        cursor.close()

    except Exception as e:
        print('error: could not create tables...')
        print(e)