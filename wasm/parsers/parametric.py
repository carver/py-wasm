import io

from wasm.instructions import (
    Drop,
    Instruction,
    Select,
)
from wasm.opcodes import (
    BinaryOpcode,
)


def parse_parametric_instruction(opcode: BinaryOpcode,
                                 stream: io.BytesIO) -> Instruction:
    if opcode is BinaryOpcode.DROP:
        return Drop()
    elif opcode is BinaryOpcode.SELECT:
        return Select()
    else:
        raise Exception(f"Invariant: got unknown opcode {opcode}")
