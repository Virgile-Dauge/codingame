def init_x_lines(hexs, n_rows=8, n_cols=8):
    def next_x(i, j, n_rows=8, n_cols=8):
        return i+1, j + 1 if i % 2 == 0 else j
    n_rows = 8
    n_cols = 8

    xlines = []
    for r in range(n_rows-1, 0, -2):
        res = []
        i = r
        j = 0
        while i < n_rows and j < n_cols:
            label = to_label(i, j)
            hexs[label] = {'xl': len(xlines), 'xi': len(res)}
            res.append(label)
            i, j = next_x(i, j)
        xlines.append(res)

    for c in range(n_cols):
        res = []
        i = 0
        j = c
        while i < n_rows and j < n_cols:
            label = to_label(i, j)
            res.append(label)
            hexs[label] = {'xl': len(xlines), 'xi': len(res)}
            i, j = next_x(i, j)
        xlines.append(res)

    return xlines
def init_y_lines(hexs, n_rows=8, n_cols=8):
    def next_y(i, j, n_rows=8, n_cols=8):
        return i+1, j - 1 if i % 2 != 0 else j

    ylines = []

    for c in range(n_cols):
        res = []
        i = 0
        j = c
        while i < n_rows and j >= 0:
            label = to_label(i, j)
            res.append(label)
            hexs[label].update({'yl': len(ylines), 'yi': len(res)})
            i, j = next_y(i, j)
        ylines.append(res)

    for r in range(2, n_cols, 2):
        res = []
        i = r
        j = n_cols-1
        while i < n_rows and j >= 0:
            label = to_label(i, j)
            hexs[label].update({'yl': len(ylines), 'yi': len(res)})
            res.append(label)
            i, j = next_y(i, j)
        ylines.append(res)

    return ylines
def init_z_lines(hexs, n_rows=8, n_cols=8):
    def next_z(i, j, n_rows=8, n_cols=8):
        return i, j + 1

    zlines = []

    for r in range(n_rows):
        res = []
        i = r
        j = 0
        while i < n_rows and j < n_cols:
            label = to_label(i, j)
            res.append(label)
            hexs[label].update({'zl': len(zlines), 'zi': len(res)})
            i, j = next_z(i, j)
        zlines.append(res)

    return zlines
class HexaGrid:
    def __init__(self):
        self.hexs = {}
        self.xlines = init_x_lines(self.hexs)
        self.ylines = init_y_lines(self.hexs)
        self.zlines = init_z_lines(self.hexs)

hg = HexaGrid()
hg.hexs, hg.xlines
