from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class DecodedDataDTO:
    current_pc: int
    addr_mode: str
    cycles: int
    mnemonic: str
    length: int
    prg_bytes: List[int]  # Pass in the relevant bytes

    @property
    def operands(self) -> List[int]:
        count = self.operand_byte_count
        return self.prg_bytes[:count] if count > 0 else []
    
    @property
    def operand_byte_count(self) -> int:
        return self.length - 1