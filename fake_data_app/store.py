import numpy as np

from datetime import date
from sensor import VisitSensor


class StoreSensor:
    def __init__(self,
                 name:str,
                 avg_visit:int,
                 std_visit:int,
                 perc_break:float = 0,
                 perc_malfunction:float = 0
                 ):
        """
        :param name:
        :param avg_visit:
        :param std_visit:
        :param perc_break:
        :param perc_malfunction:

        Initialize a store
        """
        self.name = name
        self.sensors = list()

        # To always get the same result when asking for the same store
        seed = np.sum(list(self.name.encode("ascii")))
        np.random.seed(seed=seed)

        # 80/20: most people take the main entrance, and so on ;)
        traffic_percentage = [0.48, 0.30, 0.05, 0.03, 0.01, 0.02, 0.10, 0.01]

        # Initialisation of the store's sensors
        # To keep things simple, we assume each store has eight sensors
        # Otherwise we would need to dynamically create traffic_percentages that sum to 1
        for i in range(len(traffic_percentage)):
            sensor = VisitSensor(
                traffic_percentage[i] * avg_visit,
                traffic_percentage[i] * std_visit,
                perc_break=perc_break,
                perc_malfunction=perc_malfunction
            )

            self.sensors.append(sensor)

    def get_sensor_traffic(self, sensor_id: int, business_date:date) -> int:
        """Return the traffic sensor at the given sensor_id at a date"""
        return self.sensors[sensor_id].get_visit_count(business_date)

    def get_all_traffic(self, business_date:date) -> int:
        """Return the traffic for one store"""
        return sum([ sensor.get_visit_count(business_date) for sensor in self.sensors ])
