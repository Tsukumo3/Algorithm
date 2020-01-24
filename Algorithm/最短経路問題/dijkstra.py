class Dijkstra():
    ''' ダイクストラ法

    重み付きグラフにおける単一始点最短路アルゴリズム

    * 使用条件
        - 負のコストがないこと
        - 有向グラフ、無向グラフともにOK

    * 計算量はO(E*log(V))

    * ベルマンフォード法より高速なので、負のコストがないならばこちらを使うとよい
    '''
    class Edge():
        ''' 重み付き有向辺 '''

        def __init__(self, _to, _cost):
            self.to = _to
            self.cost = _cost


    def __init__(self,_Vertexes):
        ''' 重み付き有向辺
        無向辺を表現したいときは、_fromと_toを逆にした有向辺を加えればよい

        Args:
            Vertex(int): 頂点の数
        '''

        #隣接リスト := 頂点Uのi個目のリスト
        self.Graph = [ [] for i in range(_Vertexes)]
        #辺の数
        self.Edges = 0
        #頂点の数
        self.Vertexes = _Vertexes

    @property
    def edges(self):
        ''' 辺数
        無向グラフのときは、辺数は有向グラフの倍になる
        '''
        return self._Edges

    @edges.setter
    def edges(self, input):
        self.Edges = input

    @property
    def vertexes(self):
        ''' 頂点数 '''
        return self._Vertexes

    @vertexes.setter
    def vertexes(self, input):
        self.vertexes = input

    def add(self, _from, _to, _cost):
        ''' 2頂点と、辺のコストを追加する
        '''
        #Graphの[_from]番目の配列にEdge(to,cost)を入れていく
        self.Graph[_from].append(self.Edge(_to, _cost))
        #Graphを追加したので、辺数を追加する
        self._Edges += 1

    def add_list(self, _list):
        """ 2頂点と、辺のコストをまとめてリストで追加する
        _from = item[0]
        _to = item[1]
        _cost = item[2]
        """
        for item in _list:
            _from = item[0]
            _to = item[1]
            _cost = item[2]

            self.Graph[_from].append(self.Edge(_to, _cost))
            self.Edges += 1

    def directed_graph(self,_list):
        ''' 有向グラフ '''
        self.add_list(_list)

    def undirected_graph(self,_list):
        ''' 無向グラフ '''
        new_list = []
        for item in _list:
            go = [item[0], item[1], item[2]]
            back = [item[1], item[0], item[2]]
            new_list.append(go)
            new_list.append(back)
        self.add_list(new_list)

    def shortest_path(self, start):
        """ 始点sから頂点iまでの最短路を格納したリストを返す
        Args:
            s(int): 始点s 0始まり
        Returns:
            d(list): d[i] := 始点sから頂点iまでの最短コストを格納したリスト。
                     到達不可の場合、値は10000
        """

        import heapq
        que = []  # プライオリティキュー（ヒープ木）
        #import sys
        #d = [sys.maxsize] * self.Vertexes

        # d[v] := 始点 s から頂点 v への最短経路長
        d = [10000] * self.Vertexes

        d[start] = 0

        heapq.heappush(que, (0, start))  # 始点の(最短距離, 頂点番号)をヒープに追加する

        while len(que) != 0:
            cost, aVertex = heapq.heappop(que)

            # キューに格納されている最短経路の候補がdの距離よりも大きければ、他の経路で最短経路が存在するので、処理をスキップ
            if d[aVertex] < cost:
                continue

            for i in range(len(self.Graph[aVertex])):
                # 頂点vに隣接する各頂点に関して、頂点vを経由した場合の距離を計算し、今までの距離(d)よりも小さければ更新する
                aEdge = self.Graph[aVertex][i]  # vのi個目の隣接辺e

                if d[aEdge.to] > d[aVertex] + aEdge.cost:
                    d[aEdge.to] = d[aVertex] + aEdge.cost  # dの更新
                    heapq.heappush(que, (d[aEdge.to], aEdge.to))  # キューに新たな最短経路の候補(最短距離, 頂点番号)の情報をpush

        return d

    def shortest_route(self,start):
        """ 始点sから頂点iまでの最短路を通る道の数え上げリストを返す
        Args:
            s(int): 始点s 0始まり
        Returns:
            d(list): d[i] := 始点sから頂点iまでの最短コストの道の数のリスト。
                     到達不可の場合、値は10000
        """

        import heapq
        que = []  # プライオリティキュー（ヒープ木）

        #import sys
        #d = [sys.maxsize] * self.Vertexes

        # d[v] := 始点 s から頂点 v への最短経路長
        d = [10000] * self.Vertexes
        # num[v] := 始点 s から頂点 v への最短経路数
        num = [1] * self.Vertexes

        mod = 10**9+7

        d[start] = 0

        heapq.heappush(que, (0, start))  # 始点の(最短距離, 頂点番号)をヒープに追加する

        while len(que) != 0:
            cost, aVertex = heapq.heappop(que)

            # キューに格納されている最短経路の候補がdの距離よりも大きければ、他の経路で最短経路が存在するので、処理をスキップ
            if d[aVertex] < cost:
                continue

            for i in range(len(self.Graph[aVertex])):
                # 頂点vに隣接する各頂点に関して、頂点vを経由した場合の距離を計算し、今までの距離(d)よりも小さければ更新する
                aEdge = self.Graph[aVertex][i]  # vのi個目の隣接辺e

                if d[aEdge.to] > d[aVertex] + aEdge.cost:
                    d[aEdge.to] = d[aVertex] + aEdge.cost  # dの更新
                    heapq.heappush(que, (d[aEdge.to], aEdge.to))  # キューに新たな最短経路の候補(最短距離, 頂点番号)の情報をpush

                elif d[aEdge.to] == d[aVertex] + aEdge.cost:
                    num[aEdge.to] += num[aVertex];
                    num[aEdge.to] %= mod;

        return num



if __name__ == '__main__':
    #sample　コピペ用
    '''
8 10
0 1 1
0 2 7
0 3 2
1 4 2
1 5 4
2 5 2
2 6 3
3 6 5
5 7 6
6 7 2


    0	1	2	3	4   5   6   7
0	0	1	7	2	-	-	-	-
1	1	0	-	-	2	4	-	-
2	7	-	0	-	-	2	3	-
3	2	-	-	0	-	-	5	-
4	-	2	-	-	0	1	-	-
5	-	4	2	-	1	0	-	6
6	-	-	3	5	-	-	0	2
7	-	-	-	-	-	6	2	0
    '''


    N,K = map(int,input().split())
    A = [list(map(int,input().split())) for i in range(K)]

    djk = Dijkstra(N)
    djk.undirected_graph(A)
    print("各ノードまでの最小コスト")
    print(djk.shortest_path(0))
    print("各ノードまでの最小コストでいける道の数")
    print(djk.shortest_route(0))
