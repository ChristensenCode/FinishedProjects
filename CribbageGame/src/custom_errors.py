class DiscardError(Exception):
    def __init__(self, message="Two cards must be discarded!") -> None:
        self.message = message
        super().__init__(self.message)
