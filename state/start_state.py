from aiogram.dispatcher.filters.state import State, StatesGroup


class Start(StatesGroup):
    name = State()
    new_or_old_data = State()
    sphere = State()
    born_date = State()
    born_time = State()
    born_city = State()
