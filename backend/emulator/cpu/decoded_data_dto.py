from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class DecodedDataDTO:
    current_pc: int
    addr_mode: str
    cycles: int
    mnemonic: str
    length: int
    type: str

    @property
    def operand_byte_count(self) -> int:
        return self.length - 1