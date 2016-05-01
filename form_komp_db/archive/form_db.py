import sqlite3

caches_table = []
name_db = 'out.sqlite'
db = sqlite3.connect(name_db)
db_new = sqlite3.connect('out_new.sqlite')


def take_name_table():
    cur = db.cursor()
    k = cur.execute('SELECT * FROM sqlite_master WHERE type = "table"')
    for j in k:
        if j[1] != 'sqlite_stat1' and j[1] != 'ОК' and j[1] != 'ОПК':
            caches_table.append(j[1])


def work_with_tables(tables):
    cur = db.cursor()
    cur_new = db_new.cursor()
    for j in tables:
        # kk = cur_new.execute('CREATE TABLE ' + j + ' (cod text, description text, eneter text)')
        print('\n\t' + '{' + str(j) + '}' + '\t\n')
        k = cur.execute('SELECT * FROM ' + j)
        for lines in k:
            line = []
            line.append(processing_word(lines[0]))
            line.append(processing_word(lines[1]))
            line.append(processing_word(lines[6]))
            # if line[0]!='' and line[1]!='' and line[2]!='':
                # kk = cur_new.execute('INSERT INTO ' + j + ' VALUES (?,?,?)', line)
            print(line)


def processing_word(word):
    m = str(word)
    m = m.strip()
    return(m)

take_name_table()
work_with_tables(caches_table)
