from typing import List


def solution(n: int, lost: List[int], reserve: List[int]) -> int:
    lost_map = {n: 1 for n in sorted(lost)}
    reserve_map = {n: 1 for n in sorted(reserve)}

    # me first
    for key, is_valid in lost_map.items():
        if not is_valid:
            continue

        if key in reserve_map and reserve_map[key]:
            lost_map[key] = 0
            reserve_map[key] = 0

    # others next
    for key, is_valid in lost_map.items():
        if not is_valid:
            continue

        if key - 1 in reserve_map and reserve_map[key - 1]:
            lost_map[key] = 0
            reserve_map[key - 1] = 0
        elif key + 1 in reserve_map and reserve_map[key + 1]:
            lost_map[key] = 0
            reserve_map[key + 1] = 0

    lost_count = 0
    for v in lost_map.values():
        if v == 1:
            lost_count += 1

    return n - lost_count
