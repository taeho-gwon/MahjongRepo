from __future__ import annotations

from typing import Iterable, Optional

from pydantic import BaseModel

from src.enum.common import CallTypeEnum
from src.schema.call import Call
from src.schema.tile import Tile


class Hand(BaseModel):
    concealed_tiles: list[Tile]
    calls: list[Call]
    last_tile: Optional[Tile]

    @property
    def is_opened(self) -> bool:
        return any(call.type != CallTypeEnum.CONCEALED_KAN for call in self.calls)

    @property
    def iter_concealed_tiles(self) -> Iterable[Tile]:
        yield from self.concealed_tiles
        if self.last_tile:
            yield self.last_tile

    @property
    def iter_tiles(self) -> Iterable[Tile]:
        yield from self.concealed_tiles
        for call in self.calls:
            yield from call.tiles
        if self.last_tile:
            yield self.last_tile
