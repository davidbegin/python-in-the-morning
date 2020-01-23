print("\033c")


# If we build a Twitch Chatbot

class CoolClass:
    def another_method(self):
        print("Im cool class")

class ContextMatters():
    def another_method(self):
        print("I can do more work!!")

    def __enter__(self):
        print("A long time ago")
        return CoolClass()

    def __exit__(self, a,b,c):
        print("And then they woke up from the dream")

with ContextMatters():
# with ContextMatters() as cm:
    # cm.another_method()
    print("Meat of a Sandwhich")


