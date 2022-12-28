
from typing import Callable

from pyrogram import Client
from pyrogram.types import Message

from .. import SUDO_USERS



def sudo_commands(func: Callable) -> Callable:
    """
    Restricts user's from executing certain sudo user's' related commands
    """

    async def decorator(client: Client, message: Message):
        uid = message.from_user.id
        if uid in SUDO_USERS:
            return await func(client, message)
        elif uid in OWNER_ID:
            return await func(client, message)

    return decorator

