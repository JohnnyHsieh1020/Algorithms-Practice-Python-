states_list = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

result = []

while states_list:
    appropriate_station = None
    covered_states = set()
    # Check which station can cover the most states.
    for station, states in stations.items():
        covered = states_list & states
        if len(covered) > len(covered_states):
            appropriate_station = station
            covered_states = covered
    # Eliminate
    states_list -= covered_states
    # Save appropriate station.
    result.append(appropriate_station)

print(result)
