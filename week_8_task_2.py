# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.

from collections import Counter
from collections import namedtuple
import heapq

word = input('введите строку из трех слов: ')
print(Counter(word))

class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, add):
        self.left.walk(code, add + '0')
        self.right.walk(code, add + '1')

class Leaf(namedtuple('Leaf', ['char'])):
    def walk(self, code, add):
        code[self.char] = add or '0'

def huffman_encode(word):
    h = []
    for chrt, freq in Counter(word).items():
        h.append((freq, len(h), Leaf(chrt)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}

    if h:
        [(_freq, _count, root)] = h
        root.walk(code, '')
    return code

def main():
    code = huffman_encode(word)
    encoded = ' '.join(code[chrt] for chrt in word)
    print(len(code), len(encoded)) 

    for chrt in sorted(code):
        print('{}: {}'.format(chrt, code[chrt]))
    print(encoded)

if __name__ == '__main__':
    main()