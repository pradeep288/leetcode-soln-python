class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()

        num_boats, i, j = 0, 0, len(people) - 1
        while i <= j:
            if people[i] + people[j] > limit:
                j -= 1
            else:
                i += 1
                j -= 1
            num_boats += 1

        return num_boats
