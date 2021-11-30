#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Collection, Iterator
from itertools import cycle


def split_chunks(orig_list: Collection, chunk_size: int) -> Iterator[list]:
    for i in range(0, len(orig_list), chunk_size):
        yield orig_list[i:i + chunk_size]


def encrypt(msg: str) -> str:
    encrypted = ''

    for char in msg:
        encrypted += char + '#'

    return encrypted


def decrypt(encrypted: str) -> str:
    msg = ''

    for char in split_chunks(encrypted, 2):
        msg += char[0]

    return msg


def binary_encode(data: str) -> str:
    binary = ''

    for char in data:
        unicode = ord(char)
        binary += format(unicode, '08b')

    return binary


def binary_decode(binary: str) -> str:
    data = ''

    for char_bin in split_chunks(binary, 8):
        unicode = int(char_bin, 2)
        char = chr(unicode)
        data += char

    return data


# https://en.wikipedia.org/wiki/MLT-3_encoding
def mlt3_line_encode(data: str) -> str:
    signal_levels = cycle(['-1', '0', '1', '0'])
    signal_level = '0'
    encoded = ''

    for bit in data:
        signal_level = next(signal_levels) if bit == '1' else signal_level
        encoded += ',' + signal_level

    return encoded[1:]


def mlt3_line_decode(signal_src: str) -> str:
    signal = signal_src.split(',')
    previous = '0' if signal[0] == '0' else '1'
    data = previous

    for signal_level in signal[1:]:
        bit = '0' if signal_level == previous else '1'
        data += bit
        previous = signal_level

    return data


def test_encodings():
    in_msg = 'O pé do Zé tem chulé.\n'
    print(f'In Message: {in_msg}\n')

    in_encrypted = encrypt(in_msg)
    print(f'In Encrypted: {in_encrypted}\n')

    in_binary = binary_encode(in_encrypted)
    print(f'In Binary: {in_binary}\n')

    signal = mlt3_line_encode(in_binary)
    print(f'Signal: {signal}\n')

    out_binary = mlt3_line_decode(signal)
    print(f'Out Binary: {out_binary}\n')

    out_encrypted = binary_decode(out_binary)
    print(f'Out Encrypted: {out_encrypted}\n')

    out_msg = decrypt(out_encrypted)
    print(f'Out Message: {out_msg}\n')

    assert in_msg == out_msg, 'In and out messages are different!'


if __name__ == '__main__':
    test_encodings()
