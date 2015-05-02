# coding: utf-8

class UF:
  def __init__(self, N):
    self.nodes = range(N+1)
    self.N = N

  def connect(self, u, v):
    for i in range(1, self.N+1):
      if i == u: continue
      if self.nodes[i] == self.nodes[u]:
        self.nodes[i] = self.nodes[v]
    self.nodes[u] = self.nodes[v]

  def is_connected(self, u, v):
    return self.nodes[u] == self.nodes[v]

  def get_graph_ids(self):
    return list(set(self.nodes))

def main():
  N, M = map(int, raw_input().split(' '))
  uf = UF(N)
  non_tree_keys = []
  for i in range(M):
    u, v = map(int, raw_input().split(' '))
    if uf.is_connected(u, v): non_tree_keys.append(u)
    else: uf.connect(u, v)
  ids = uf.get_graph_ids()
  for k in non_tree_keys:
    if uf.nodes[k] in ids:
      ids.remove(uf.nodes[k])
  print len(ids) - 1

if __name__ == '__main__':
  main()
