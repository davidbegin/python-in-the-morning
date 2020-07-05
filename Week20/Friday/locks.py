from threading import Lock


lock = Lock()

lock.acquire()

if lock.locked():
    print("Locked")

lock.release()

if not lock.locked():
    print("Unlocked")
# breakpoint()
# print()


# acquire
# lock
# release
