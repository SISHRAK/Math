#include <iostream>
#include <cmath>
#include <functional>
#include <vector>

bool isMonotonic(const std::function<double(double)>& func, double a, double b) {
    double prev_y = func(a);
    bool increasing = prev_y < func(a + 0.01);
    for (double x = a + 0.01; x <= b; x += 0.01) {
        double y = func(x);
        if ((increasing && y < prev_y) || (!increasing && y > prev_y)) return false;
        prev_y = y;
    }
    return true;
}

bool rootExists(const std::function<double(double)>& func, double a0, double b0) {
    if (func(a0) * func(b0) > 0) {
        std::cout << "No roots or multiple roots on the interval\n";
        return false;
    }
    if (!isMonotonic(func, a0, b0)) {
        std::cout << "More than one root in the interval\n";
        return false;
    }
    return true;
}

double diff(const std::function<double(double)>& f, double x0) {
    const double h = 1e-6;
    return (f(x0 + h) - f(x0 - h)) / (2 * h);
}

double newton(const std::function<double(double)>& func, double a0, double b0, double eps) {
    double x = (a0 + b0) / 2; // Start at midpoint for better chances of convergence
    double diffVal;
    int cnt = 0;
    do {
        diffVal = diff(func, x);
        if (diffVal == 0) {
            std::cout << "Derivative is zero, stopping\n";
            return x;
        }
        double prev_x = x;
        x = prev_x - func(prev_x) / diffVal;
        cnt++;
    } while (std::abs(func(x)) > eps && cnt < 1000);

    std::cout << "Root: " << x << " after " << cnt << " iterations\n";
    return x;
}

int main() {
    auto func = [](double x) { return x * x * x - x + 4; }; // Example function

    double a0 = -5, b0 = 5, eps = 1e-6;

    if (rootExists(func, a0, b0)) {
        double root = newton(func, a0, b0, eps);
        std::cout << "Root found: " << root << std::endl;
    }

    return 0;
}
