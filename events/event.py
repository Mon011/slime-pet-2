import threading
from exceptions import CoinAmountException
from entities import slime
from components import singleton, GameState

def on_threaded_event(function) -> threading.Thread:
    def wrapper(*args, **kwargs) -> threading.Thread:
        thread = threading.Thread(target = function, args = args, kwargs = kwargs) 
        thread.start()
        return thread
    return wrapper

class Event:

    @on_threaded_event
    def on_trigger(self) -> threading.Thread:
        pass 

class OnCoinIncreaseEvent(Event):
    coin_amount: int

    def __init__(self, coin_amount):
        self.coin_amount = coin_amount
        super().__init__() 

    @on_threaded_event
    def on_trigger(self) -> threading.Thread:
        slime.coins += self.coin_amount 

class OnCoinDecreaseEvent(Event):
    coin_amount: int

    def __init__(self, coin_amount):
        self.coin_amount = coin_amount
        super().__init__()

    @on_threaded_event
    def on_trigger(self) -> threading.Thread:
        if slime.coins < self.coin_amount:
            raise CoinAmountException()
        else:
            slime.coins -= self.coin_amount    


class OnHungerDecreaseEvent(Event):
    decrease_hunger_amount: int

    def __init__(self, decrease_hunger_amount):
        self.decrease_hunger_amount = decrease_hunger_amount
        super().__init__()

    @on_threaded_event
    def on_trigger(self) -> threading.Thread:
        slime.hunger += self.decrease_hunger_amount

class OnGameOverEvent(Event):
    @on_threaded_event
    def on_trigger(self) -> threading.Thread:
        singleton.state = GameState.GAME_OVER


def on_event(event: Event):
    event.on_trigger().join()