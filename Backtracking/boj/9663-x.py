from typing import List


N = int(input())
cases = []


# 1. 가능한 모든 경우의 수 저장 ([0][0] ~ [n-1][n-1])
# 수정) 이 방식이 미친 짓인게 경우의 수가 너무 커짐. 여기서 가지치기 필요
def dfs(possible_positions, path=[]):
    """ 가능한 (x, y) 조합에서 뽑기
    Args:
        possible_positions: [(x1, y1), ...]
        path: 지금까지 놓은 퀸들 위치
    """
    if len(path) == N:
        cases.append(path)
        return

    if not path:
        dfs(possible_positions[1:], possible_positions[0])
    else:
        print('path', path)
        prev_x, prev_y = path[-1]
        _possible_positions = possible_positions[:]
        for pos in possible_positions:
            dx, dy = prev_x - pos[0], prev_y[1]
            if dx == 0 or dy == 0 or \
                    dx == dy or dx == -dy:
                _possible_positions.remove(pos)

            dfs(_possible_positions, [*path, pos])


def check_all(cases: List[List[int]]):
    """
    Args:
        cases: 가능한 좌표들의 모임의 집합
    Returns:
        count: 공격할 수 없는 경우
    """
    count = 0
    for positions in cases:
        is_all_valid = True
        for idx, position in enumerate(positions):
            x, y = position
            for other in positions[idx+1:]:
                if is_valid(x - other[0], y - other[1]):
                    is_all_valid = False
                    break

            if not is_all_valid:
                break

        if is_all_valid:
            count += 1

    return count


def is_valid(dx, dy):
    # 두 점의 차이(벡터)로 공격할 수 있는 위치인지 계산
    # 상하좌우, 대각선
    if dx == 0 or dy == 0 or \
            dx == dy or dx == -dy:
        return True

    return False


dfs(l(i, j) for i in range(N) for j in range(N)])
print(check_all(cases))
