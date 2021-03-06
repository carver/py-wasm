import io

from wasm.exceptions import (
    MalformedModule,
)


def parse_null_byte(stream: io.BytesIO) -> None:
    byte = stream.read(1)
    if byte == b'\x00':
        return
    elif byte:
        raise MalformedModule(f"TODO: expected 0x00 but got {hex(byte[0])}")
    else:
        raise Exception("Unexpected end of stream")
