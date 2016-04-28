import sqlite3
from os.path import exists

schema_text ='''
create table bot (
    token       text primary key,
    username    text,
    nickname    text,
    bot_id      bigint
);
create table apikeys (
    name        text primary key,
    token       text not null
);
create table groups (
    id          bigint primary key not null,
    admin       bigint default 0,
    type        text not null
);
create table ignored (
    gid         bigint primary key not null,
    uid         bigint not null
);
create table mods (
    gid         bigint primary key not null,
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
    print 'Database loaded.'
    

def main(args):
    pass

def load_db():
    pass

    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

