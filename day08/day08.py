import numpy as np

# input
example = [
    (162,817,812),
    (57,618,57),
    (906,360,560),
    (592,479,940),
    (352,342,300),
    (466,668,158),
    (542,29,236),
    (431,825,988),
    (739,650,466),
    (52,470,668),
    (216,146,977),
    (819,987,18),
    (117,168,530),
    (805,96,715),
    (346,949,466),
    (970,615,88),
    (941,993,340),
    (862,61,35),
    (984,92,344),
    (425,690,689),
]
example = np.array(example)

full = [
    [int(i) for i in line.strip().split(',')]
    for line in open('input.txt', 'r').readlines()
]
full = np.array(full)


def distance(a, b):
    return np.sqrt(np.sum((b-a)**2))


def distance_matrix(points):
    D = np.zeros(shape=(len(points), len(points)))
    for i, a in enumerate(points):
        for j, b in enumerate(points):
            D[i, j] = distance(a, b)

    np.fill_diagonal(D, np.inf)
    return D


def pairup(input, n=10):
    D = distance_matrix(input)
    clusters = [[i] for i in range(len(input))]

    for _ in range(n):
        i, j = np.unravel_index(np.argmin(D), D.shape)
        # mask distance matrix
        D[i, j] = np.inf
        D[j, i] = np.inf
        
        # check if already in same cluster
        for current in clusters:
            if i in current and j in current:
                break
        else:
            # find clusters containing i, j pair
            left_cluster_id = None
            right_cluster_id = None
            for cluster_id, cluster in enumerate(clusters):
                if i in cluster:
                    left_cluster_id = cluster_id
                if j in cluster:
                    right_cluster_id = cluster_id
            
            # merge one into the other and leave one empty
            if left_cluster_id is not None and right_cluster_id is not None:
                clusters[left_cluster_id].extend(clusters[right_cluster_id])
                clusters[right_cluster_id] = []

    return [c for c in clusters if len(c) != 0]

# part 1 - cluster by nearest distance
clusters_ex_1 = pairup(example)
result = int(np.prod(sorted([len(c) for c in clusters_ex_1])[-3:]))
print('Top 3 product = ', result)

# part 1 full
clusters_full_1 = pairup(full, n=1000)
result = int(np.prod(sorted([len(c) for c in clusters_full_1])[-3:]))
print('Top 3 product = ', result)
