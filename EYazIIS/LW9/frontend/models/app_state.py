from dataclasses import dataclass, field
from typing import Optional, Callable, Any

@dataclass
class AppState:
    current_text: str = ""
    current_language: str = "russian"
    abstract_type: str = "classic"
    result_data: Optional[Any] = None
    file_path: Optional[str] = None
    last_classic_abstract: Optional[Any] = None
    last_keyword_abstract: Optional[Any] = None

    on_state_change: list[Callable] = field(default_factory=list)

    def update_state(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self._notify_listeners()

    def add_listener(self, callback: Callable):
        self.on_state_change.append(callback)

    def _notify_listeners(self):
        for callback in self.on_state_change:
            callback()