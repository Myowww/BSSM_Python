import time
import random

WORD_LIST = [
    "The quick brown fox jumps over the lazy dog.",
    "Jack eagerly explored the mysterious cave.",
    "The sun sets behind the mountains, casting a warm glow.",
    "Vivid colors painted the sky during the breathtaking sunset.",
    "A gentle breeze rustled the leaves in the tranquil forest.",
    "The adventurous hiker reached the summit of the towering peak.",
    "Waves crashed against the rocky shore in a rhythmic dance.",
    "Graceful swans glided across the serene lake.",
    "The old bookstore was filled with the scent of aged paper.",
    "A chorus of crickets serenaded the night under the full moon.",
]

random.shuffle(WORD_LIST)

for i in WORD_LIST:
    시작 = time.time()
    입력 = input(i + "\n").strip()
    Speed = time.time() - 시작

    정확도 = 0
    for c, a in zip(입력, i):
        if c == a:
            정확도 += 1

    Len = len(i)
    c = 정확도 / Len * 100
    e = (Len - 정확도) / Len * 100
    speed = float(Speed) * 60

    print(f"타수: {speed:0.2f} 정확도: {c:0.2f}% 오타: {e:0.2f}%")
