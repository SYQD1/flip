# Generates Flip's app icon (filee.ico, filee.png, filee-menubar.png) with the standard library only:
# a violet-to-cyan rounded square with two white opposing arrows. Run: python build/make-flip-icon.py
import os
import struct
import zlib

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "src", "Filee.App", "Assets", "Icons")
C1 = (124, 58, 237)   # violet
C2 = (6, 182, 212)    # cyan
SS = 4                # supersamples per axis


def in_rounded(x, y, m=0.04, r=0.22):
    lo, hi = m, 1 - m
    if x < lo or x > hi or y < lo or y > hi:
        return False
    cx = min(max(x, lo + r), hi - r)
    cy = min(max(y, lo + r), hi - r)
    return (x - cx) ** 2 + (y - cy) ** 2 <= r * r


def in_arrow(x, y, sx0, sx1, cy, half, base, tip, head_half):
    if sx0 <= x <= sx1 and abs(y - cy) <= half:
        return True
    lo, hi = (base, tip) if tip > base else (tip, base)
    if lo <= x <= hi:
        return abs(y - cy) <= head_half * abs(tip - x) / abs(tip - base)
    return False


def in_symbol(x, y):
    return (in_arrow(x, y, 0.24, 0.60, 0.38, 0.045, 0.58, 0.78, 0.13)
            or in_arrow(x, y, 0.40, 0.76, 0.62, 0.045, 0.42, 0.22, 0.13))


def render(size, template=False):
    rows = []
    for py in range(size):
        row = bytearray([0])
        for px in range(size):
            bg = sym = 0
            for sy in range(SS):
                for sx in range(SS):
                    x = (px + (sx + 0.5) / SS) / size
                    y = (py + (sy + 0.5) / SS) / size
                    if template:
                        sym += in_symbol(x, y)
                    elif in_rounded(x, y):
                        bg += 1
                        sym += in_symbol(x, y)
            n = SS * SS
            if template:
                row += bytes((0, 0, 0, round(255 * sym / n)))
                continue
            t = ((px + py) / 2) / size
            base = [C1[i] + (C2[i] - C1[i]) * t for i in range(3)]
            a = bg / n
            w = sym / bg if bg else 0
            rgb = [round(base[i] * (1 - w) + 255 * w) for i in range(3)]
            row += bytes((*rgb, round(255 * a)))
        rows.append(bytes(row))
    raw = b"".join(rows)

    def chunk(kind, data):
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)

    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", size, size, 8, 6, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b""))


def write_ico(path, sizes):
    images = [render(s) for s in sizes]
    header = struct.pack("<HHH", 0, 1, len(images))
    offset = 6 + 16 * len(images)
    entries = b""
    for s, img in zip(sizes, images):
        entries += struct.pack("<BBBBHHII", s % 256, s % 256, 0, 0, 1, 32, len(img), offset)
        offset += len(img)
    with open(path, "wb") as f:
        f.write(header + entries + b"".join(images))


if __name__ == "__main__":
    write_ico(os.path.join(OUT, "filee.ico"), [256, 128, 64, 48, 32, 24, 16])
    with open(os.path.join(OUT, "filee.png"), "wb") as f:
        f.write(render(512))
    with open(os.path.join(OUT, "filee-menubar.png"), "wb") as f:
        f.write(render(64, template=True))
    print("Flip icons written to", os.path.normpath(OUT))
