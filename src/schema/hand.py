from __future__ import annotations

from collections import Counter
from typing import Optional

from pydantic import BaseModel

from src.enum.common import CallType
from src.schema.call import Call
from src.schema.tile import Tile


class Hand(BaseModel):
    concealed_tiles: list[Tile]
    calls: list[Call]
    last_tile: Optional[Tile]

    @property
    def is_opened(self) -> bool:
        return any(call.type != CallType.CONCEALED_KAN for call in self.calls)

    @property
    def tiles(self) -> list[Tile]:
        ret = self.concealed_tiles[:]

        for call in self.calls:
            ret.extend(call.tiles)

        if self.last_tile is not None:
            ret.append(self.last_tile)

        return ret

    @property
    def counts(self) -> dict[Tile, int]:
        return Counter(self.tiles)

    @property
    def concealed_counts(self) -> dict[Tile, int]:
        ret = self.concealed_tiles[:]

        if self.last_tile is not None:
            ret.append(self.last_tile)

        return Counter(self.concealed_tiles)
