def slices(arr, slice_len):
    return [''.join(seq) for seq in zip(*[iter(arr)]*slice_len)]

line = input().rstrip()

w, h = 25, 6
img_size = w * h
layers = slices(line, img_size)

# Part 1
min_layer = min(layers, key=lambda layer: layer.count('0'))
print(min_layer.count('1') * min_layer.count('2'))

# Part 2
charmap = {'0': '.', '1': '#'}
# below next only gets the topmost non-transparent colour
img = ''.join((next(charmap[c] for c in col if c != '2') for col in zip(*layers)))

print()
print('\n'.join(slices(img, w)))
