// Cubic UFO

/*
Problem link:
https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard/00000000000079cc
*/

// my solution
#include <iostream>
#include <algorithm>    // std::sort
#include <vector>
#include <cmath>
double TOLERANCE = 0.00000001;

double get_area(double angle) {
    return sqrt(2) * cos(angle) + sin(angle);
}

// binary search
double find_xangle(double area) {
    double min = 0.0, max = 0.615479709;
    double mid, new_area, diff;

    while (true) {
        mid = (min + max) / 2.0;
        new_area = get_area(mid);
        if (fabs(new_area - area) <= TOLERANCE) {
            return mid;
        } else if (new_area > area) {
            max = mid;
        } else {
            min = mid;
        }
    }

    return 0;
}

std::vector<double> rotate_x(std::vector<double> v, double angle) {
    std::vector<double> new_v(3, 0);

    new_v[0] = v[0];
    new_v[1] = v[1] * cos(angle) - v[2] * sin(angle);
    new_v[2] = v[1] * sin(angle) + v[2] * cos(angle);

    return new_v;
}

int main()
{
    int T, n;
    T = 1;
    
    std::cin >> n;

    while (T <= n)
    {
        double A; // Area
        std::cin >> A;
        
        if (A <= 1.41421356237) {
            double angle;
            double sin_val, cos_val;
            
            angle = acos(A/sqrt(2)) + 0.78539816339;
            sin_val = sin(angle)/2;
            cos_val = cos(angle)/2;
            
            std::cout << "Case #" << std::to_string(T) << ":\n";
            printf("%.8f %.8f %.8f\n", cos_val, sin_val, 0.0);
            printf("%.8f %.8f %.8f\n", -sin_val, cos_val, 0.0);
            printf("%.8f %.8f %.8f\n", 0.0, 0.0, 0.5);

        } else {
            std::vector<double> vx = {0.3535533905932738, 0.3535533905932738, 0.0};
            std::vector<double> vy = {-0.3535533905932738, 0.3535533905932738, 0.0};
            std::vector<double> vz = {0.0, 0.0, 0.5};

            double angle = find_xangle(A);
            
            std::vector<double> vx_new, vy_new, vz_new;
            vx_new = rotate_x(vx, angle);
            vy_new = rotate_x(vy, angle);
            vz_new = rotate_x(vz, angle);

            std::cout << "Case #" << std::to_string(T) << ":\n";
            printf("%.8f %.8f %.8f\n", vx_new[0], vx_new[1], vx_new[2]);
            printf("%.8f %.8f %.8f\n", vy_new[0], vy_new[1], vy_new[2]);
            printf("%.8f %.8f %.8f\n", vz_new[0], vz_new[1], vz_new[2]);
        }
        
        T++;
    }
    
    return 0;
}