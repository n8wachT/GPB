import sqlite3
from os.path import exists

schema_text ='''
create table bot (
    token       text primary key,
    username    text,
    nickname    text,
    bot_id      bigint,
    owner_id    bigint
);
create table plugins (
    plugin      text,
    variable    text,
    value       text
);
create table groups (
    group_id    text,
    manager     bigint default 0,
    type        text not null
);
create table ignored (
    gid         text,
    uid         bigint not null
);
create table mods (
    gid         text,
    uid         bigint not null
);
'''

db_filename = 'store.db'
def build_schema():
    conn = sqlite3.connect(db_filename)
    conn.executescript(schema_text)
    print 'Schema created.'
    conn.close()

if(not exists(db_filename)):
    print 'Creating file and schema.'
    build_schema()
else:
    print 'Database found.'

def get_cursor():
    conn = sqlite3.connect(db_filename)
    return conn.cursor()

def get_dbconn():
    return sqlite3.connect(db_filename)
