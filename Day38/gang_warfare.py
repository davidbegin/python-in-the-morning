print("\033c")

# What happens if the condition fails:
#   * Return a default value
#   * Raise an Error
#   * Call some other function to do some work


# Dumb Simple Version
# LBYL
def lbyl():
    cool_stuff = {"weapon": "knife"}

    if "weapon" in cool_stuff:
        return cool_stuff["weapon"]

def eafp():
    # EAFP
    try:
        return cool_stuff["weapon"]
    except KeyError:
        return None

def rougues():
    # Python Rouges
    return cool_stuff.get("weapon", None)


# ========================================================================================

# With a Default Value

cool_stuff = {"weapon": "knife"}

def lbyl():
    if "weapon" in cool_stuff:
        return cool_stuff["weapon"]
    else:
        return "club"

def eafp():
    try:
        return cool_stuff["weapon"]
    except KeyError:
        return "club"

def rougues():
    return cool_stuff.get("weapon", "club")


# ========================================================================================

# Raise an Error
cool_stuff = {"weapon": "knife"}

def lbyl():
    if "weapon" in cool_stuff:
        return cool_stuff["weapon"]
    else:
        raise KeyError

def eafp():
    cool_stuff["weapon"]

def rougues():
    cool_stuff["weapon"]


# ========================================================================================


def other_func():
    print("Time to Func")

# Call Some othe Func
cool_stuff = {"weapon": "knife"}

def lbyl():
    if "weapon" in cool_stuff:
        return cool_stuff["weapon"]
    else:
        other_func()

def eafp():
    try:
        cool_stuff["weapon"]
    except:
        other_func()

def rougues():
    return cool_stuff.get("weapon", other_func)
    # return cool_stuff.get("weapon", other_func())



print(rougues())
