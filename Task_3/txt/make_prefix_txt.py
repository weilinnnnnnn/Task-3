prefix = b"Hello, I am file A."

# Pad with PDF comment bytes ('%' lines are comments in PDF)
# until we hit exactly 64 bytes
while len(prefix) % 64 != 0:
    prefix += b'%'

print(f"Prefix length: {len(prefix)} bytes")
with open("prefix.pdf", "wb") as f:
    f.write(prefix)