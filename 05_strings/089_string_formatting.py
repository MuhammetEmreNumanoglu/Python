name = "Alice"
score = 95.678

print("Hello, %s!" % name)
print("Score: %.2f" % score)

print("Hello, {}! Score: {:.2f}".format(name, score))
print("{0} and {0} again, {1}".format(name, score))
print("{name} scored {score}".format(name=name, score=score))

print(f"Hello, {name}!")
print(f"Score: {score:.2f}")
print(f"Pi is approximately {3.14159:.4f}")

number = 1234567
print(f"{number:,}")
print(f"{number:>15}")
print(f"{'left':<15}|")
print(f"{'center':^15}|")
