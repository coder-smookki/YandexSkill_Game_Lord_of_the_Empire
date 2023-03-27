from threading import Thread
from core.utils.globalStorage import globalStorage


def doFuncAsAsync(func, args=[]):
    def async_func(func, args):
        with globalStorage['app'].app_context():
            func(*args)

    Thread(target=async_func, args=([func, args]), daemon=True).start()
