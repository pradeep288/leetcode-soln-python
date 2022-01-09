import enum


class Direction(enum.Enum):
    north = 1
    south = 2
    east = 3
    west = 4


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        cur_x, cur_y, count = 0, 0, 0
        cur_dir = Direction.north
        while count < 4:
            for instruction in instructions:
                if instruction == "G":
                    if cur_dir == Direction.north:
                        cur_y += 1
                    elif cur_dir == Direction.south:
                        cur_y -= 1
                    elif cur_dir == Direction.east:
                        cur_x += 1
                    elif cur_dir == Direction.west:
                        cur_x -= 1
                elif instruction == "L":
                    if cur_dir == Direction.north:
                        cur_dir = Direction.west
                    elif cur_dir == Direction.west:
                        cur_dir = Direction.south
                    elif cur_dir == Direction.south:
                        cur_dir = Direction.east
                    elif cur_dir == Direction.east:
                        cur_dir = Direction.north
                elif instruction == "R":
                    if cur_dir == Direction.north:
                        cur_dir = Direction.east
                    elif cur_dir == Direction.east:
                        cur_dir = Direction.south
                    elif cur_dir == Direction.south:
                        cur_dir = Direction.west
                    elif cur_dir == Direction.west:
                        cur_dir = Direction.north
            count += 1

        return cur_x == 0 and cur_y == 0
