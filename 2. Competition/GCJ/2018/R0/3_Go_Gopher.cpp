// Go, Gopher!

/*
Problem link:
https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard/0000000000007a30
*/

// my solution
// run: g++ q3.cpp -std=c++14 -pthread -O3 -o q3.out
// python testing_tool.py ./q3.out

#include <iostream>
#include <string>
#include <vector>
    
bool is_over(int i, int j) {
    if (i == 0 && j == 0) {
        return true;
    }

    return false;
}

void print_map(std::vector< std::vector<char> > omap) {
    int r = omap.size();
    int c = omap[0].size();

    printf("printing map.. \n\n");

    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            std::cout << omap[i][j] << " ";
        }
        std::cout << std::endl;
    }

    return;
}

bool check_map(std::vector< std::vector<char> > omap, int height, int width) {

    for (int i = 3; i < 3 + height; i++) {
        for (int j = 3; j < 3 + width; j++) {
            if (omap[i][j] == 'O') {
                return false;
            }
        }
    }

    return true;
}

int main() {
    int num_test_cases;
    std::cin >> num_test_cases;
    bool is_completed;

    for (int i = 0; i < num_test_cases; ++i) {
        int a;
        std::cin >> a;
        is_completed = false;

        if (a == 20) {
            // short case
            std::vector< std::vector<char> > orchard(30, std::vector<char>(30, 'O'));
            int width = 4, height = 5;
            int width_begin = 3, height_begin = 3, w = width - 2, h = height - 2;
            int coord_i, coord_j;
            
            for (int i = height_begin; i < height_begin + h; i++) {
                for (int j = width_begin; j < width_begin + w; j++) {
                    // center case (just check center)
                    while (orchard[i][j] == 'O') {
                        std::cout << i << " " << j << std::endl;
                        std::cin >> coord_i >> coord_j;
                        if (is_over(coord_i, coord_j)) { is_completed = true; break; }

                        orchard[coord_i][coord_j] = 'X';
                    }

                    // begin case, make sure prev is all covered
                    if (i == height_begin) {
                        while (orchard[i-1][j] == 'O') {
                            std::cout << i << " " << j << std::endl;
                            std::cin >> coord_i >> coord_j;
                            if (is_over(coord_i, coord_j)) { is_completed = true; break; }

                            orchard[coord_i][coord_j] = 'X';
                        }
                    }

                    if (j == width_begin) {
                        while (orchard[i][j-1] == 'O') {
                            std::cout << i << " " << j << std::endl;
                            std::cin >> coord_i >> coord_j;
                            if (is_over(coord_i, coord_j)) { is_completed = true; break; }

                            orchard[coord_i][coord_j] = 'X';
                        }
                    }

                    // end case, make sure end is all covered
                    if (i == height_begin + h - 1) {
                        while (orchard[i+1][j] == 'O') {
                            std::cout << i << " " << j << std::endl;
                            std::cin >> coord_i >> coord_j;
                            if (is_over(coord_i, coord_j)) { is_completed = true; break; }

                            orchard[coord_i][coord_j] = 'X';
                        }
                    }

                    if (j == width_begin + w - 1) {
                        while (orchard[i][j+1] == 'O') {
                            std::cout << i << " " << j << std::endl;
                            std::cin >> coord_i >> coord_j;
                            if (is_over(coord_i, coord_j)) { is_completed = true; break; }

                            orchard[coord_i][coord_j] = 'X';
                        }
                    }

                    // 4 corner cases
                    if (i == height_begin && j == width_begin) {
                        while (orchard[i-1][j-1] == 'O') {
                            std::cout << i << " " << j << std::endl;
                            std::cin >> coord_i >> coord_j;
                            if (is_over(coord_i, coord_j)) { is_completed = true; break; }

                            orchard[coord_i][coord_j] = 'X';
                        }
                    }

                    if (i == height_begin && j == width_begin + w - 1) {
                        while (orchard[i-1][j+1] == 'O') {
                            std::cout << i << " " << j << std::endl;
                            std::cin >> coord_i >> coord_j;
                            if (is_over(coord_i, coord_j)) { is_completed = true; break; }

                            orchard[coord_i][coord_j] = 'X';
                        }
                    }

                    if (i == height_begin + h - 1 && j == width_begin) {
                        while (orchard[i+1][j-1] == 'O') {
                            std::cout << i << " " << j << std::endl;
                            std::cin >> coord_i >> coord_j;
                            if (is_over(coord_i, coord_j)) { is_completed = true; break; }

                            orchard[coord_i][coord_j] = 'X';
                        }
                    }

                    if (i == height_begin + h - 1 && j == width_begin + w - 1) {
                        while (orchard[i+1][j+1] == 'O') {
                            std::cout << i << " " << j << std::endl;
                            std::cin >> coord_i >> coord_j;
                            if (is_over(coord_i, coord_j)) { is_completed = true; break; }

                            orchard[coord_i][coord_j] = 'X';
                        }
                    }
                }

                if (is_completed) {
                    break;
                }
            }
        } else if (a == 200) {
            // long case
            std::vector< std::vector<char> > orchard(50, std::vector<char>(50, 'O'));
            int width = 20, height = 10;
            int width_begin = 3, height_begin = 3, w = width - 2, h = height - 2;
            int coord_i, coord_j;

            for (int i = height_begin; i < height_begin + h; i++) {
                for (int j = width_begin; j < width_begin + w; j++) {
                    // center case (just check center)
                    while (orchard[i][j] == 'O') {
                        std::cout << i << " " << j << std::endl;
                        std::cin >> coord_i >> coord_j;
                        if (is_over(coord_i, coord_j)) { is_completed = true; break; }

                        orchard[coord_i][coord_j] = 'X';
                    }

                    // begin case, make sure prev is all covered
                    if (i == height_begin) {
                        while (orchard[i-1][j] == 'O') {
                            std::cout << i << " " << j << std::endl;
                            std::cin >> coord_i >> coord_j;
                            if (is_over(coord_i, coord_j)) { is_completed = true; break; }

                            orchard[coord_i][coord_j] = 'X';
                        }
                    }

                    if (j == width_begin) {
                        while (orchard[i][j-1] == 'O') {
                            std::cout << i << " " << j << std::endl;
                            std::cin >> coord_i >> coord_j;
                            if (is_over(coord_i, coord_j)) { is_completed = true; break; }

                            orchard[coord_i][coord_j] = 'X';
                        }
                    }

                    // end case, make sure end is all covered
                    if (i == height_begin + h - 1) {
                        while (orchard[i+1][j] == 'O') {
                            std::cout << i << " " << j << std::endl;
                            std::cin >> coord_i >> coord_j;
                            if (is_over(coord_i, coord_j)) { is_completed = true; break; }

                            orchard[coord_i][coord_j] = 'X';
                        }
                    }

                    if (j == width_begin + w - 1) {
                        while (orchard[i][j+1] == 'O') {
                            std::cout << i << " " << j << std::endl;
                            std::cin >> coord_i >> coord_j;
                            if (is_over(coord_i, coord_j)) { is_completed = true; break; }

                            orchard[coord_i][coord_j] = 'X';
                        }
                    }

                    // 4 corner cases
                    if (i == height_begin && j == width_begin) {
                        while (orchard[i-1][j-1] == 'O') {
                            std::cout << i << " " << j << std::endl;
                            std::cin >> coord_i >> coord_j;
                            if (is_over(coord_i, coord_j)) { is_completed = true; break; }

                            orchard[coord_i][coord_j] = 'X';
                        }
                    }

                    if (i == height_begin && j == width_begin + w - 1) {
                        while (orchard[i-1][j+1] == 'O') {
                            std::cout << i << " " << j << std::endl;
                            std::cin >> coord_i >> coord_j;
                            if (is_over(coord_i, coord_j)) { is_completed = true; break; }

                            orchard[coord_i][coord_j] = 'X';
                        }
                    }

                    if (i == height_begin + h - 1 && j == width_begin) {
                        while (orchard[i+1][j-1] == 'O') {
                            std::cout << i << " " << j << std::endl;
                            std::cin >> coord_i >> coord_j;
                            if (is_over(coord_i, coord_j)) { is_completed = true; break; }

                            orchard[coord_i][coord_j] = 'X';
                        }
                    }

                    if (i == height_begin + h - 1 && j == width_begin + w - 1) {
                        while (orchard[i+1][j+1] == 'O') {
                            std::cout << i << " " << j << std::endl;
                            std::cin >> coord_i >> coord_j;
                            if (is_over(coord_i, coord_j)) { is_completed = true; break; }

                            orchard[coord_i][coord_j] = 'X';
                        }
                    }
                }

                if (is_completed) {
                    break;
                }
            }
        }
    }
    return 0;
}