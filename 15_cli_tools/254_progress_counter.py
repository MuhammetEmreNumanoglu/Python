import time
import sys

def progress_bar(current, total, width=40):
    filled = int(width * current / total)
    bar = "#" * filled + "-" * (width - filled)
    percent = current / total * 100
    sys.stdout.write(f"\r[{bar}] {percent:.1f}% ({current}/{total})")
    sys.stdout.flush()

total = 20
for i in range(1, total + 1):
    time.sleep(0.05)
    progress_bar(i, total)

print("\nDone!")

def counting_progress(items):
    total = len(items)
    for i, item in enumerate(items, 1):
        yield item
        percent = i / total * 100
        sys.stdout.write(f"\r  Processing... {percent:.0f}% ({i}/{total})")
        sys.stdout.flush()
    print()

items = list(range(30))
results = []
for item in counting_progress(items):
    time.sleep(0.02)
    results.append(item * 2)

print("Processed", len(results), "items")
