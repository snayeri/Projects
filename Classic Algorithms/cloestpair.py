import math
import random
import numpy


def eulicd(pt0, pt1):
    return math.sqrt(sum(map(lambda x, y: (x - y) ** 2, pt0, pt1)))


def oneNorm(pt0, pt1):
    return sum(map(lambda x, y: abs(x - y), pt0, pt1))


def infNorm(pt0, pt1):
    return max(map(lambda x, y: abs(x - y), pt0, pt1))


def pNorm(pt0, pt1):
    return (sum(map(lambda x, y: (x - y) ** p, pt0, pt1))) ** (1. / p)


def distance(pt0, pt1):
    return infNorm(pt0, pt1)


def BruceForceCloestPair(ptlst):
    mindist = distance(ptlst[0], ptlst[1])
    pair = (ptlst[0], ptlst[1])
    for i in xrange(len(ptlst)):
        for j in xrange(i + 1, len(ptlst)):
            dist = distance(ptlst[i], ptlst[j])
            if dist < mindist:
                mindist = dist
                pair = (ptlst[i], ptlst[j])
    return mindist, pair


# TODO:
# update this func using select algo
def selectMin(ptlst, n, dim=0):
    return sorted(ptlst)[0:n]


def DivideConquer(ptlst):
    if len(ptlst) <= 4:
        return BruceForceCloestPair(ptlst)
    left, right = medianDivide(ptlst)
    min0, pair0 = DivideConquer(left)
    min1, pair1 = DivideConquer(right)
    (m, pair) = (min0, pair0) if min0 < min1 else (min1, pair1)
    right6 = selectMin(right, 6)
    for pt0 in left:
        for pt1 in right6:
            dist = distance(pt0, pt1)
            if dist < m:
                m = dist
                pair = (pt0, pt1)
    return m, pair


def medianDivide(ptlst, dim=0):
    ptlstdim = zip(*ptlst)[dim]
    median = numpy.median(ptlstdim)
    left, right = [], []
    for pt in ptlst:
        (left, right)[pt[dim] > median].append(pt)
    return left, right

# test code
def genRandomMatrix(m, n):
    return [[random.random() for j in xrange(n)] for i in xrange(m)]

if __name__ == "__main__":
    ptlst = genRandomMatrix(10, 2)
    print ptlst
    print DivideConquer(ptlst)
    print BruceForceCloestPair(ptlst)
