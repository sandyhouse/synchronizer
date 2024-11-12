from abc import ABC
from datetime import datetime
import os
from typing import Optional


class Synchronizer(ABC):
    def __init__(
            self,
            rank: int=None,
            world_size: int=None):
        self.rank = rank
        self.world_size = world_size
        self._check()

    def _check(self):
        rank = int(os.getenv("RANK", "0"))
        world_size = int(os.getenv("WORLD_SIZE", "1"))

        self.rank = self.rank if self.rank else rank
        self.world_size = self.world_size if self.world_size else world_size

        assert self.rank < self.world_size, (
            f"The rank ({self.rank}) should be less than "
            f"the number of processes ({self.world_size})."
        )

    def barrier(self):
        raise RuntimeError(
            "Do not call the interface class directly. Use one of its subclass."
        )
