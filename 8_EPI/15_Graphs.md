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