# Graphs


<details>
<summary> Concept overview </summary>

---
- Graph = vertices (V) + edges (E)
- Edge: e(u, v), where u-source and v-sink
- Directed acyclic graph(DAC) - directed graph that is not circular
- Two vertices can be 'connected' or 'disconnected' via edge
- Types:
	- Weakly connected: there is a 'undirected' path between every pair  
	- Strongly connected: there is 'directed' path between every pair  
	- Complete: there is an edge between every pair  

- Search Complexity
	- both BFS, DFS has complexity of O(|V| + |E|)

---

</details>


<details>
<summary> Graphs Basics (DFS) </summary>

---
- Given list of winning and losing pair
- Greate a graph s.t. node follows winners->losers edge

---

```cpp
struct MatchResult {
	string winning_team, losing_team;
};

// main function
bool CanTeamABeatTeamB(const vector<MatchResult>& matches, const string& team_a, const string& team_b) {
	return IsReachableDfs(BuildGraph(matches), team_a, team_b, make_unique<unordered_set<string>>().get());
}

// creating graph
unordered_map<string, unordered_set<string>> BuildGraph (const vector<MatchResult>& matches) {

	unordered_map<string, unordered_set<string>> graph;
	
	for (const MatchResult& match : matches) {
		graph[match.winning_team].emplace(match.losing_team);
	}

	return graph;
}

// dfs search
bool IsReachableDfs(const unordered_map<string, unordered_set<string>>& graph, 
					const string& curr, const string& dest, unordered_set<string>* visited_ptr) {
	unordered_Set<string>& visited = *visited_ptr;

	if (curr == dest) {
		return true;
	} else if (visited.count(curr) || !graph.count(curr)) {
		return false;
	}

	visited.emplace(curr);

	const unordered_set<string>& tream_list = graph.at(curr);
	return any_of(Begin(tream_list), end(tream_list), [&](const string& team) {
		return IsReachableDfs(graph, team, dest, visited_ptr);
	});
}
```

---
- Time complexity: O(E)

---
</details>


<details>
<summary> Search a Maze (DFS) </summary>

---
- Given a 2D array grid representing a maze with designated entry and exit points
- Find path for entrance to exit, if one exists
---

```cpp
typedef enum {kWhite, kBlack} Color;

struct Coordinate {
	bool operator==(const Coordinate& that) const { // const after () indicates this method does not mutate (change members of this class)
		return x == that.x && y == that.y;
	}
	int x, y;
};

vector<Coordinate> SearchMaze(vector<vector<Color>> maze, const Coordinate& s, const Coordinate& e) {
	vector<Coordinate> path;
	SearchMazeHelper(s, e, &maze, &path);
	return path;
}

bool SearchMazeHelper(const Coordinate& cur, const Coordinate& e, 
					  vector<vector<Color>>* maze_ptr, vector<Coordinate>* path_ptr) {
	auto& maze = *maze_ptr;

	if (cur.x < 0 || cur.x >= size(maze) || cur.y < 0 || cur.y >= size(maze[cur.x]) || maze[cur.x][cur.y] != kWhite) {
		return false;
	}

	auto& path = *path_ptr;
	path.emplace_back(cur);
	maze[cur.x][cur.y] = kBlack;

	if (cur == e) {
		return true;
	}

	for (const Coordinate& next_move : {Coordinate{cur.x, cur.y+1}, Coordinate{cur.x, cur.y-1},
										Coordinate{cur.x+1, cur.y}, Coordinate{cur.x-1, cur.y}}) {
		if (SearchMazeHelper(next_move, e, maze_ptr, path_ptr)) {
			return true;
		}
	}

	path.pop_back();
	return false;
}

```

---
- Time complexity: O(|V| + |E|)

---
</details>


<details>
<summary> Paint a Boolean Matrix (Flip Color region, BFS) </summary>

---
- Given a 2D array with black or white cell and a coordinate
- Change all neighbor of same color to opposite

---

```cpp
void FlipColor(int x, int y, vector<deque<bool>>* image_ptr) {
	vector<deque<bool>>& image = *image_ptr;
	const bool color = image[x][y];

	queue<pair<int, int>> q;
	image[x][y] = !color;

	while (!empty(q)) {
		cont auto [x, y] = q.front();
		q.pop();

		for (const auto& [next_x, next_y] : initializer_list<pair<int, int>>{{x, y+1}, {x, y-1}, {x+1, y}, {x-1, y}}) {
			if (next_x >= 0 && next_x < size(image) && next_y >= 0 && next_y < size(image[next_x]) && image[next_x][next_y] == color) {
				image[next_x][next_y] = !color;
				q.emplace(next_x, next_y);
			}
		}
	}
}
```

---
- Time complexity: O(mn), BFS

---
</details>


<details>
<summary> Paint a Boolean Matrix (Flip Color region, DFS) </summary>

```cpp
void FlipColor(int x, int y, vector<deque<bool>>* image_ptr) {
	vector<deque<bool>>& image = *image_ptr;
	const bool color = image[x][y];

	image[x][y] = !color; // flip
	for (const auto& [next_x, next_y] : initializer_list<pair<int, int>>{{x, y+1}, {x, y-1}, {x+1, y}, {x-1, y}}) {
		if (next_x >= 0 && next_x < size(image) && next_y >= 0 && next_y < size(image[next_x]) && image[next_x][next_y] == color) {
			FlipColor(next_x, next_y, &image)
		}
	}
}
```

---
- Time complexity: O(mn), DFS

---
</details>


<details>
<summary> Compute Enclosed Regions </summary>

---
- Given a 2D array of either W or B entry
- Replace all Ws that cannot reach the boundary to B (i.e. all W's that is surrounded by B)

---

```cpp
void FillSurroundedRegions(vector<vector<char>>* board_ptr) {
	vector<vector<char>>& board = *board_ptr;

	for (int i = 0; i < size(board); ++i) {
		MarkBoundaryRegion(i, 0, board_ptr); // top edge
		MarkBoundaryRegion(i, size(board[i])-1, board_ptr);
	}

	for (int j = 0; j < size(board.front()); ++j) {
		MarkBoundaryRegion(0, j, board_ptr);
		MarkBoundaryRegion(size(board)-1, j, board_ptr);
	}

	for (vector<char>& row : board) {
		for (char& c : row) {
			c = c != 'T' ? 'B' : 'W';
		}
	}
}

void MarkBoundaryRegion(int i, int j, vector<vector<char>>* board_ptr) {
	queue<pair<int, int>> q(deque<pair<int, int>>(1, {i, j}));
	vector<vector<char>>& board = *board_ptr;

	while (!empty(q)) {
		const auto [x, y] = q.front();
		q.pop();

		if (x >= 0 && x < size(board) && y >= 0 && y < size(board[x]) && board[x][y] == 'W') {
			board[x][y] = 'T';
			q.emplace(x-1, y);
			q.emplace(x+1, y);
			q.emplace(x, y+1);
			q.emplace(x, y-1);
		}
	}
}
```

---
- Time complexity: O(mn), BFS

- Explanation:  
	1. Start from all edge points, BFS if they are 'W' and convert to 'T'  
	2. Scan the whole grid, convert all 'T' to 'W' and rest to 'B'

---
</details>


<details>
<summary> Deadlock Detection (need to review) </summary>

---
- Given a directed graph
- Check if the graph contains a cycle (has a deadlock)

- Deadlock: A situation in which two or more competing actions are each waiting for the other to finish
- Circular graph is sufficient for deadlock but not necessary (depends on OS)
- Node markings: white (never discovered), gray (first discovered), black (finished processing) 
---

```cpp
struct GraphVertex {
	enum Color { kWhite, kGray, kBlack } color = kWhite;
	vector<GraphVertex*> edges;
}

bool IsDeadlocked(vector<GraphVertex>* graph) {
	return any_of(begin(*graph), end(*graph), [](GraphVertex& vertex) {
		return vertex.color == GraphVertex::kWhite && HasCycle(&vertex);
	});
}

bool HasCycle(GraphVertex* cur) {
	if (cur->color == GraphVertex::kGray) {
		return true;
	}

	cur->color = GraphVertex::kGray;

	for (GraphVertex*& next : cur->edges) {
		if (next->color != GraphVertex::kBlack && HasCycle(next)) {
			return true;
		}
	}

	cur->color = GraphVertex::kBlack;
	return false;
}
```

---
- Time complexity: O(|V| + |E|), DFS

---
</details>


<details>
<summary> Clone a Graph (need to review) </summary>

---
- Given a directed graph and a reference vertex u
- Create a copy of graph that is reachable from u

---

```cpp
struct GraphVertex {
	int label;
	vector<GraphVertex*> edges;
};

GraphVertex* CloneGraph(GraphVertex* graph) {
	if (!graph) {
		return nullptr;
	}

	unordered_map<GraphVertex*, GraphVertex*> vertex_map;
	queue<GraphVertex*> q(deque<GraphVertex*>(1, graph));
	vertex_map.emplace(graph, new GraphVertex({graph->lable}));

	while (!empty(q)) {
		auto v = q.front();
		q.pop();

		for (GraphVertex* e : v->edges) {
			if (!vertex_map.count(e)) {
				vertex_map.emplace(e, new GraphVertex({e->label}));
				q.emplace(e);
			}

			vertex_map[v]->edges.emplace_back(vertex_map[e]);
		}
	}

	return vertex_map[graph];
}
```

---
- Time complexity: O(|V|+|E|), BFS queue  
- Space complexity: O(|V|)

---
</details>


<details>
<summary> Compute Enclosed Regions (need to review) </summary>

---
- Given a set of pins and wires connecting pairs of pins (either left or right)
- Determine if it is possible to place the pins such that their immediate neighbor is always the opposite
- Return such division if one exists

---

```cpp
struct GraphVertex {
	int d = -1;
	vector<GraphVertex*> edges;
};

bool IsAnyPlacementFeasible(vector<GraphVertex>* graph) {
	return all_of(begin(*graph), end(*graph), [](GraphVertex& v) {return v.d != -1 || Bfs(&v); });
}

bool Bfs(GraphVertex* s) {
	s->d = 0;
	queue<GraphVertex*> q;
	q.emplace(s);

	while (!empty(q)) {
		for (GraphVertex*& t : q.front()->edges) {
			if (t->d == -1) {
				t->d = q.front()->d + 1;
				q.emplace(t);
			} else if (t->d == q.front()->d) {
				return false;
			}
		}
		q.pop();
	}

	return true;
}
```

---
- Time complexity: O(p + w), p: path, w: number of wires, BFS
- Space complexity: O(p)

- Other term for this problem: bipartite graphs, 2-colorable

---
</details>


<details>
<summary> Transform One String to Another (need to review, no idea) </summary>

---
- Given a dictionary D and two strings s and t
- Determine if s produces t

---

```cpp
int TransformString(unordered_set<string> D, const string& s, const string& t) {
	struct StringWithDistance {
		string candidate_string;
		int distance;
	};

	queue<StringWithDistance> q;
	D.erase(s);
	q.emplace(StringWithDistance{s, 0});

	while (!empty(q)) {
		StringWithDistance f(q.front());

		if (f.candidate_string == t) {
			return f.distance;
		}

		string str = f.candidate_string;
		for (int i = 0; i < size(str); ++i) {
			for(int c = 0; c < 26; ++c) {
				str[i] = 'a' + c;
				if (auto it = D.find(str); it != end(D)) {
					D.erase(it);
					q.emplace(StringWithDistance{str, f.distance + 1});
				}
			}
			str[i] = f.candidate_string[i];
		}
		q.pop();
	}

	return -1;
}

```

---
- Time complexity: BFS - O(n^2), where n is the number of words in dictionary

---
</details>


<details>
<summary> Team Photo Day 2 (need to review) </summary>

---
- Given the same team photo problem
- Determine the largest number of teams that can be photographed simultaneously

---

```cpp
struct GraphVertex {
	vector<GraphVertex*> edges;
	int max_distance = 0;
};

int FindLargestNumberTeams(vector<GraphVertex>* graph ) {
	int max_level = 0;
	for (GraphVertex& g : *graph) {
		if (g.max_distance == 0) {
			max_level = max(max_level, Dfs(&g));
		}
	}
	return max_level;
}

int Dfs(GraphVertex* curr) {
	curr->max_distance = 1;
	for (GraphVertex* vertex : curr->edges) {
		curr->max_distance = max(curr->max_distance, (vertex->max_distance ?
								 vertex->max_distance : Dfs(vertex)) + 1);
	}
	return curr->max_distance;
}
```

---
- Time computation: O(|V| + |E|)

---
</details>