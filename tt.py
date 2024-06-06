class Transaction:
    def __init__(self, parent=None):
        self.store = {}
        self.parent = parent

class KeyValueStore:
    def __init__(self):
        self.transactions = [Transaction()]

    def current_transaction(self):
        return self.transactions[-1]

    def get(self, key):
        for transaction in reversed(self.transactions):
            if key in transaction.store:
                if transaction.store[key] is None:
                    raise KeyError(f'Key {key} not found')
                else:
                    return transaction.store[key]
        raise KeyError(f'Key {key} not found')

    def set(self, key, value):
        self.current_transaction().store[key] = value

    def delete(self, key):
        if key in self.current_transaction().store:
            del self.current_transaction().store[key]
        else:
            raise KeyError(f'Key {key} not found')

    def begin(self):
        self.transactions.append(Transaction(self.current_transaction()))

    def commit(self):
        if len(self.transactions) == 1:
            raise ValueError('No transaction')
        top_transaction = self.transactions.pop()
        for key, value in top_transaction.store.items():
            self.current_transaction().store[key] = value

    def rollback(self):
        if len(self.transactions) == 1:
            raise ValueError('No transaction')
        self.transactions.pop()



# Initialize the KeyValueStore
store = KeyValueStore()

# Set and print a value in the store
store.set("hello", "world")
print(store.get("hello"))  # Prints "world"

# Start a transaction
store.begin()

# Set and print a value in the transaction
store.set("hello", "mars")
print(store.get("hello")) # Prints "mars"

# Rollback the transaction changes
store.rollback()
print(store.get("hello")) # Prints "world" again (rollback reverted the last change during the transaction)

# Start another transaction
store.begin()

# Set and print a value in the transaction
store.set("hello", "pluto")
print(store.get("hello")) # Prints "pluto"

# Commit the transaction changes
store.commit()
print(store.get("hello")) # Prints "pluto" (commit preserved the last change during the transaction)