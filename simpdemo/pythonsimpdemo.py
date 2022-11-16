challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]

e= challenge[2][1]
g= challenge[2][0]
n= challenge[3]

print(f"My {e}! The {g} do {n}!")

trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

e= trial[2]["goggles"]
g= trial[2]["eyes"]
n= trial[3]

print(f"My {e}! The {g} do {n}!")

nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

e= nightmare[0]["user"]["name"]["first"]
g= nightmare[0]["kumquat"]
n= nightmare[0]["d"]

print(f"My {e}! The {g} do {n}!")
