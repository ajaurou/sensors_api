import datetime

from fake_data_app.store import StoreSensor

def create_app() -> dict:
    """
    Create the available stores in our API
    5 stores, with each 8 sensors
    Each stores has a different number of people coming to it
    As well as different break and malfunction percentages
    (Not realistic, but we keep things simple)
    """

    store_name = ["Lille", "Paris", "Lyon", "Toulouse", "Marseille"]
    store_avg_visit = [3000, 8000, 6000, 2000, 1700]
    store_std_visit = [500, 800, 500, 400, 100]
    perc_malfunction = [0.05, 0.1, 0.08, 0.05, 0.05]
    perc_break = [0.05, 0.08, 0.05, 0.02, 0]

    stores = {}

    for i in range(len(store_name)):
        stores[ store_name[i] ] = StoreSensor(
            name=store_name[i],
            avg_visit=store_avg_visit[i],
            std_visit=store_std_visit[i],
            perc_break=perc_break[i],
            perc_malfunction=perc_malfunction[i]
        )

    return stores
