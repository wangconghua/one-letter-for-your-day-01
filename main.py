"""One Letter for Your Day: the letter C.

C stands for chaos: the whole day was pure chaos, nothing went to plan,
and that is the honest report. One character, nothing else.
Writes exactly "C" (no trailing newline) to /output/entry.txt.
"""
import os

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write("C")
