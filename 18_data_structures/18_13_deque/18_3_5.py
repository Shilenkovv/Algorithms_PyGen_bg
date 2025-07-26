from collections import deque


class TapCounter:
    def __init__(self):
        self.taps: deque[int] = deque()

    def tap(self, ts: int):
        self.taps.append(ts)
        # удаляем устаревшие нажатия
        while self.taps and self.taps[0] < ts - 299:
            self.taps.popleft()

    def count(self, ts: int):
        # удаляем устаревшие нажатия
        while self.taps and self.taps[0] < ts - 299:
            self.taps.popleft()
        return len(self.taps)
