import heapq

heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
min_element = heapq.heappop(heap)
