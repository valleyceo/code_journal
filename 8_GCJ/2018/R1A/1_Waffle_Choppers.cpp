// Waffle Choppers

/*
Problem link:
https://codejam.withgoogle.com/2018/challenges/0000000000007883/dashboard
*/

// my solution
#include <iostream>
#include <string>
#include <vector>

void print_waffle(std::vector<std::string> waffle) {
	std::cout << "PRINTING WAFFLE..." << std::endl;
	for (int i = 0; i < waffle.size(); i++) {
		std::cout << waffle[i] << std::endl;
	}
}

void print_vector(std::vector<int> v) {
	std::cout << "PRINTING VECTOR..." << std::endl;
	for (int i = 0; i < v.size(); i++) {
		std::cout << v[i] << " ";
	}
	std::cout << std::endl;
}

int getChipsCount(std::vector<std::string> waffle, int rbegin, int cbegin, int rend, int cend) {
	int tot = 0;

	for (int i = rbegin; i < rend; i++) {
		for (int j = cbegin; j < cend; j++) {
			if (waffle[i][j] == '@')
				tot += 1;
		}
	}

	return tot;
}

int main()
{
	int T, n;
	T = 1;
	
	std::cin >> n;

	while (T <= n)
	{
		int R, C, H, V; // row, column, #horizontal cuts, # vertical cuts

        std::cin >> R >> C >> H >> V;
		
		std::vector<std::string> waffle(R);

		// get waffle board
		for (int i = 0; i < R; i++) {
			std::cin >> waffle[i];
		}

		std::vector<int> r_view(R, 0), c_view(C, 0);
		int total_chips = 0;

		// horizontal and vertial view of waffle
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (waffle[i][j] == '@'){
					r_view[i] += 1;
					c_view[j] += 1;
					total_chips += 1;
				}
			}
		}

		// check if cookies can be divided
		if (total_chips % (H+1) != 0 || total_chips % (V+1) != 0) {
			std::cout << "Case #" << std::to_string(T) << ": " << "IMPOSSIBLE" << '\n';
			T++;
			continue;
		}

		// check if slices can be evenly divided from both horizontal and vertical
		int h_size = total_chips/(H+1);
		int v_size = total_chips/(V+1);

		// std::cout <<"cuts: "<< h_size << " " << v_size << std::endl;
		bool is_evencut = true;

		int h_count = 0;
		int v_count = 0;

		std::vector<int> h_cuts;
		std::vector<int> v_cuts;

		v_cuts.push_back(0);
		h_cuts.push_back(0);

		for (int i = 0; i < R; i++) {
			h_count += r_view[i];

			if (h_count == h_size) {
				h_count = 0;
				h_cuts.push_back(i+1);
			} else if (h_count > h_size) {
				is_evencut = false;
				break;
			}
		}

		for (int i = 0; i < C; i++) {
			v_count += c_view[i];

			if (v_count == v_size) {
				v_count = 0;
				v_cuts.push_back(i+1);
			} else if (v_count > v_size) {
				is_evencut = false;
				break;
			}
		}

		// validate all slices are actually even (case [0 1][1 0])
		int v_idx = 0, h_idx = 0;
		int slice_chips = -1;

		for (int i = 1; i < h_cuts.size(); i++) {
			for (int j = 1; j < v_cuts.size(); j++) {
				// init
				if (slice_chips < 0) {
					slice_chips = getChipsCount(waffle, h_cuts[i-1], v_cuts[j-1], h_cuts[i], v_cuts[j]);
					//std::cout << "init slice: " << slice_chips << std::endl;
					//std::cout << "init slice: " << slice_chips << std::endl;
				} else {
					if (slice_chips != getChipsCount(waffle, h_cuts[i-1], v_cuts[j-1], h_cuts[i], v_cuts[j])) {
						is_evencut = false;
						//std::cout <<  getChipsCount(waffle, h_cuts[i-1], v_cuts[j-1], h_cuts[i], v_cuts[j]) << std::endl;
						//std::cout << "HERE!!" << std::endl;
						break;
					}
				}
			}

			if (!is_evencut) {
				break;
			}
		}

		if (is_evencut && h_count == 0 && v_count == 0) {
			std::cout << "Case #" << std::to_string(T) << ": " << "POSSIBLE" << '\n';
		} else {
			std::cout << "Case #" << std::to_string(T) << ": " << "IMPOSSIBLE" << '\n';
		}
		
		T++;
	}
	
	return 0;
}