from peewee import *
import os
class BancoConfig:
    @staticmethod
    def banco():
        db1 = SqliteDatabase('banco.db', pragmas=(
            ('journal_mode', 'wal'),  # WAL-mode.
            ('cache_size', -64 * 1000),  # 64MB cache.
            ('synchronous', 0)))  # Let the OS manage syncing.

        db2 = PostgresqlDatabase(
            'wfbhsspy',  # Required by Peewee.
            user='wfbhsspy',  # Will be passed directly to psycopg2.
            password=os.environ.get("DB_PASS"),  # Ditto.
            host='raja.db.elephantsql.com')  # Ditto.

        # os.environ.get('BD_RPGMESA')

        return db2