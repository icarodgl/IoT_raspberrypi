from peewee import *

class BancoConfig:
    @staticmethod
    def banco():
        db = SqliteDatabase('../../src/banco.db', pragmas=(
            ('journal_mode', 'wal'),  # WAL-mode.
            ('cache_size', -64 * 1000),  # 64MB cache.
            ('synchronous', 0)))  # Let the OS manage syncing.
        return db