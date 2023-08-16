import math


def _is_number(n):
    return isinstance(n, (int, float)) and math.isfinite(n)


def _edge_intersects_edge(a1, a2, b1, b2):
    ua_t = (b2[0] - b1[0]) * (a1[1] - b1[1]) - (b2[1] - b1[1]) * (a1[0] - b1[0])
    ub_t = (a2[0] - a1[0]) * (a1[1] - b1[1]) - (a2[1] - a1[1]) * (a1[0] - b1[0])
    u_b = (b2[1] - b1[1]) * (a2[0] - a1[0]) - (b2[0] - b1[0]) * (a2[1] - a1[1])

    if u_b != 0:
        ua = ua_t / u_b
        ub = ub_t / u_b

        if 0 <= ua <= 1 and 0 <= ub <= 1:
            return True

    return False


def _coordinates_contain_coordinates(outer, inner):
    intersects = _array_intersects_array(outer, inner)
    contains = _coordinates_contain_point(outer, inner[0])
    if not intersects and contains:
        return True
    return False


def _arrays_intersect_arrays(a, b):
    if _is_number(a[0][0]):
        if _is_number(b[0][0]):
            for i in range(len(a) - 1):
                for j in range(len(b) - 1):
                    if _edge_intersects_edge(a[i], a[i + 1], b[j], b[j + 1]):
                        return True
        else:
            for k in range(len(b)):
                if _arrays_intersect_arrays(a, b[k]):
                    return True
    else:
        for l in range(len(a)):
            if _arrays_intersect_arrays(a[l], b):
                return True

    return False


def _coordinates_contain_point(coordinates, point):
    contains = False
    for i in range(-1, len(coordinates) - 1):
        if ((coordinates[i][1] <= point[1] < coordinates[i + 1][1]) or
            (coordinates[i + 1][1] <= point[1] < coordinates[i][1])) and \
                (point[0] < (coordinates[i + 1][0] - coordinates[i][0]) * (point[1] - coordinates[i][1]) /
                 (coordinates[i + 1][1] - coordinates[i][1]) + coordinates[i][0]):
            contains = not contains
    return contains


def _points_equal(a, b):
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True


def _array_intersects_array(a, b):
    for i in range(len(a) - 1):
        for j in range(len(b) - 1):
            if _edge_intersects_edge(a[i], a[i + 1], b[j], b[j + 1]):
                return True
    return False


def _close_ring(coordinates):
    if not _points_equal(coordinates[0], coordinates[-1]):
        coordinates.append(coordinates[0])
    return coordinates


def _ring_is_clockwise(ring_to_test):
    total = 0
    pt1 = ring_to_test[0]
    for i in range(len(ring_to_test) - 1):
        pt2 = ring_to_test[i + 1]
        total += (pt2[0] - pt1[0]) * (pt2[1] + pt1[1])
        pt1 = pt2
    return total >= 0


def _orient_rings(poly):
    output = []
    polygon = poly[:]
    outer_ring = _close_ring(polygon.pop(0)[:])
    if len(outer_ring) >= 4:
        if not _ring_is_clockwise(outer_ring):
            outer_ring.reverse()
        output.append(outer_ring)
        for i in range(len(polygon)):
            hole = _close_ring(polygon[i][:])
            if len(hole) >= 4:
                if _ring_is_clockwise(hole):
                    hole.reverse()
                output.append(hole)
    return output


def _flatten_multi_polygon_rings(rings):
    output = []
    for i in range(len(rings)):
        polygon = _orient_rings(rings[i])
        for x in range(len(polygon) - 1, -1, -1):
            ring = polygon[x][:]
            output.append(ring)
    return output


def _shallow_clone(obj):
    target = {}
    for key, value in obj.items():
        target[key] = value
    return target

