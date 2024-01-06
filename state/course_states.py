from aiogram.dispatcher.filters.state import State, StatesGroup


class Steps(StatesGroup):
    authority1 = State()
    authority2 = State()
    profile = State()
    profile1 = State()
    profile2 = State()
    profile3 = State()
    end_and_buy = State()
    end_and_buy1 = State()
    end_and_buy2 = State()
    end_and_buy_finish = State()