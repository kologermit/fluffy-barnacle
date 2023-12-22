import logging
from aiogram import types

def message_logger(m: types.Message, state: str):
   print("Type: Message, Id: {id}, Name: {name}, State: {state}, Text: |{text}|".format(
        id=m.from_user.id,
        state=state,
        name=m.from_user.full_name,
        text=m.text))
   
def callback_logger(c: types.CallbackQuery, state: str):
   print("Type: Callback, Id: {id}, Name: {name}, State: {state}".format(
      id=c.from_user.id,
      name=c.from_user.full_name,
      state=state
   ))