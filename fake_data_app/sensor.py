from datetime import date, timedelta
import sys
import numpy as np

class VisitSensor:
    """
    Simulate a sesnsor at the entrance of a mall
    """
    def __init__(self,
                 avg_visit: int,
                 std_visit: int,
                 perc_break: float = 0.015,
                 perc_malfunction: float = 0.035) -> None:
        """Initialize the sensor"""
        self.avg_visit = avg_visit
        self.std_visit = std_visit
        self.perc_break = perc_break
        self.perc_malfunction = perc_malfunction

    def simulate_visit(self, business_date: date) -> int:
        """ To complete"""

        # Ensure reproductibilty of measurements
        np.random.seed(seed=business_date.toordinal())

        # Get the day number of the week
        week_day = business_date.weekday()

        visit = np.random.normal(self.avg_visit, self.std_visit)

        # More traffic on Wednesday (2), Friday (4) and Saturday (5)
        if week_day == 2:
            visit *= 1.10
        elif week_day == 4:
            visit *= 1.25
        elif week_day == 5:
            visit *= 1.35

        elif week_day == 6:
            visit = -1

        return np.floor(visit)

    def get_visit_count(self, business_date:date) -> int:

        np.random.seed(seed=business_date.toordinal())

        prob_malfunction = np.random.random()

        if prob_malfunction < self.perc_break:
            print('break')
            visit = 0

        visit = self.simulate_visit(business_date)

        if prob_malfunction < self.perc_malfunction:
            visit *= 0.2

        return visit



if __name__ == '__main__':
    if len(sys.argv) > 1:
        year, month, day = [ int(v) for v in sys.argv[1].split('-') ]
    else:
        year, month, day = [2023, 10, 25]

    capteur = VisitSensor(1500, 150)

    init_date = date(2024,1,1)
    while init_date < date(2026,1,1):

        visit_count = capteur.get_visit_count(init_date)
        print(init_date, visit_count)
        init_date += timedelta(days=1)
