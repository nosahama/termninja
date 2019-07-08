import datetime
from sqlalchemy import (insert,
                        select)
from .conn import conn
from .tables import rounds_table


async def add_round_played(friendly_name, username, score):
    query = insert(rounds_table)
    values = {
        'game_friendlyname': friendly_name,
        'user_username': username,
        'score': score,
        'played_at': datetime.datetime.now()
    }
    await conn.execute(query=query, values=values)