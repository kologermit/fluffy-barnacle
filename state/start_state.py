from aiogram.dispatcher.filters.state import State, StatesGroup


class Start(StatesGroup):
    name = State()
    sphere = State()
    born_date = State()
    born_time = State()
    born_city = State()
