class SemanticError(Exception):
    def __init__(self, message, line=None, column=None):
        self.message = message
        self.line = line
        self.column = column
        super().__init__(self.format_message())

    def format_message(self):
        if self.line is not None and self.column is not None:
            return f"[{self.line}:{self.column}]: {self.message}"
        return self.message

