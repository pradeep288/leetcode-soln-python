import enum


class Direction(enum.Enum):
    North = 1
    South = 2
    East = 3
    West = 4


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        cur_x, cur_y = 0, 0

        cur_dir = Direction.North

        for instruction in instructions:
            if instruction == "G":
                if cur_dir == Direction.North:
                    cur_y += 1
                elif cur_dir == Direction.South:
                    cur_y -= 1
                elif cur_dir == Direction.East:
                    cur_x += 1
                else:
                    cur_x -= 1
            elif instruction == "L":
                if cur_dir == Direction.North:
                    cur_dir = Direction.West
                elif cur_dir == Direction.South:
                    cur_dir = Direction.East
                elif cur_dir == Direction.East:
                    cur_dir = Direction.North
                else:
                    cur_dir = Direction.South
            else:
                if cur_dir == Direction.North:
                    cur_dir = Direction.East
                elif cur_dir == Direction.South:
                    cur_dir = Direction.West
                elif cur_dir == Direction.East:
                    cur_dir = Direction.South
                else:
                    cur_dir = Direction.North

        return (cur_x == 0 and cur_y == 0) or cur_dir!=Direction.North
