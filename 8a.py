import sys

lines = [line.rstrip() for line in sys.stdin]

w, h = 25, 6
layer_size = w * h
layers = [lines[0][i-layer_size:i] for i in range(layer_size, len(lines[0]), layer_size)]

min_zeros = layer_size + 1
min_layer = ''
for layer in layers:
    zero_count = layer.count('0')
    if zero_count < min_zeros:
        min_zeros = zero_count
        min_layer = layer

print(min_layer.count('1') * min_layer.count('2'))
