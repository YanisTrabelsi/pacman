import time


class Chrono():

    def __init__(self):

        self.start_time: float | None = None
        self.time_paused: float | None = None
        self.total_paused: float = 0.0

    def start(self):

        self.start_time = time.monotonic()
        self.time_paused = None
        self.total_paused = 0.0

    def pause(self):

        if self.start_time is not None and self.time_paused is None:
            self.time_paused = time.monotonic()

    def resume(self):

        if self.time_paused is not None:
            self.total_paused += time.monotonic() - self.time_paused
            self.time_paused = None

    def elapsed(self) -> float:

        if self.start_time is None:
            return 0.0

        if self.time_paused is not None:
            return self.time_paused - self.start_time - self.total_paused

        return time.monotonic() - self.start_time - self.total_paused

    def reset(self):

        self.start_time = None
        self.time_paused = None
        self.total_paused = 0.0
