import threading
from threading import Lock


class SafeAccount:
    def __init__(self, balance):
        self.balance = balance
        self.lock = Lock()

    def withdraw(self, amount):
        with self.lock:  # ← Lock acquired here
            if self.balance >= amount:
                import time

                time.sleep(0.001)
                self.balance -= amount
                print(f"Withdrew {amount} from account. New balance: {self.balance}")
                return True
        return False


account = SafeAccount(100)


def worker(account, amount):
    for _ in range(10):
        account.withdraw(amount)


t1 = threading.Thread(target=worker, args=(account, 10))
t2 = threading.Thread(target=worker, args=(account, 10))

t1.start()
t2.start()
t1.join()
t2.join()

print(f"Final balance: {account.balance}")
