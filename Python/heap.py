def pop(heap):
    popped = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    lq = len(heap)
    node = 0
    while node < lq:
        minimum = heap[node]
        nxt_node = node
        l_node = node*2+1
        r_node = node*2+2
        if l_node < lq and heap[l_node] < minimum:
            minimum = heap[l_node]
            nxt_node = l_node
        if r_node < lq and heap[r_node] < minimum:
            minimum = heap[r_node]
            nxt_node = r_node
        if node != nxt_node:
            heap[node], heap[nxt_node] = heap[nxt_node], heap[node]
            node = nxt_node
        else:
            node = lq
    return popped


def push(heap, item):
    heap.append(item)
    lq = len(heap)
    node = lq-1
    while node > 0:
        nxt_node = (node-1)//2
        if heap[nxt_node] > heap[node]:
            heap[node], heap[nxt_node] = heap[nxt_node], heap[node]
            node = nxt_node
        else:
            node = 0
