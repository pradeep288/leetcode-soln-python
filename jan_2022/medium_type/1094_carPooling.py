class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        location = {}
        # Create a dictionary with location as key and required seats at that location as value
        for trip in trips:
            if trip[1] in location.keys():
                location[trip[1]] += trip[0]
            else:
                location[trip[1]] = trip[0]

            if trip[2] in location.keys():
                location[trip[2]] -= trip[0]
            else:
                location[trip[2]] = -trip[0]

        # Check occupied_seats is more than capacity at a given location
        occupied_seats = 0
        for k in sorted(location.keys()):
            occupied_seats += location[k]
            if occupied_seats > capacity:
                return False

        return True
