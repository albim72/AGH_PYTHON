from collections import deque

#odwracanie wartości str z użyciem stosu

def reverse(s):
    stack = deque(s)
    return ''.join(stack.pop() for _ in range(len(s)))

if __name__ == '__main__':
    s = "odracanie znaków w ciągu stringowym"
    s = reverse(s)
    print(s)
