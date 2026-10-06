# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    },
    "Arcturus": {
        "RA": "14h 15m 40s",
        "Dec": "+19° 10' 57″",
        "Magnitude": -0.05,
        "Spectral Type": "K1.5III"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
# 4) Look up another target, add all the necessary information to the targets list. 
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
# 6) What is your favorite constellation?

def name(targets):
    for i in targets:
        print(i)
name(targets)

def name2(targets):
    for i in targets:
        spectral_type = targets[i]["Spectral Type"]
        print(f"{i}:{spectral_type}")
name2(targets)

def name3(targets):
    for i in targets:
        mag = targets[i]["Magnitude"]
        if mag >=0.1:
            print(f"{i}")
name3(targets)

def brightest_near_20(targets):
    ideal_star = None
    min_dec_diff = float("inf")
    brightest_mag = float("inf")
    for star, info in targets.items():
        dec_str = info["Dec"]
        deg = int(dec_str.split("°")[0].replace("+", ""))
        dec_diff = abs(deg - 20)
        mag = info["Magnitude"]
        if dec_diff < min_dec_diff or (dec_diff == min_dec_diff and mag < brightest_mag):
            min_dec_diff = dec_diff
            brightest_mag = mag
            ideal_star = star

    return ideal_star

print(brightest_near_20(targets))

# My favorite constellation is Ursa Minor