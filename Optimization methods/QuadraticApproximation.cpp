#include <iostream>
#include <cmath>
#include <cstdlib>

double f(double x) {
    return pow(x, 4) + pow(x, 2) + x + 1;
}

int main() {
    double a = -1, b = 0;
    double eps = 0.0001;

    double x1 = a + static_cast<double>(rand()) / (static_cast<double>(RAND_MAX / (b - a)));
    double x2 = 0;
    double x3 = 0;
    double fmin = 0;
    double xmin = 0;
    double f2;
    double f1;
    double f3;
    bool skip = false;

    while (true) {
        if (!skip) {
            x2 = x1 + eps;
            double f1 = f(x1);
            double f2 = f(x2);

            if (f1 > f2) {
                x3 = x1 + 2 * eps;
            } else {
                x3 = x1 - eps;
            }

            double f3 = f(x3);

            if (f1 <= f2 && f1 <= f3) {
                fmin = f1;
                xmin = x1;
            } else if (f2 <= f1 && f2 <= f3) {
                fmin = f2;
                xmin = x2;
            } else {
                fmin = f3;
                xmin = x3;
            }
        }

        double numerator = ((x2 * x2 - x3 * x3) * f(x1) + (x3 * x3 - x1 * x1) * f(x2) + (x1 * x1 - x2 * x2) * f(x3));
        double denominator = ((x2 - x3) * f(x1) + (x3 - x1) * f(x2) + (x1 - x2) * f(x3));

        if (denominator == 0) {
            x1 = xmin;
            continue;
        }

        double maybe_x = 0.5 * (numerator / denominator);
        double f_maybe_x = f(maybe_x);

        if (fabs((fmin - f_maybe_x) / f_maybe_x) < eps && fabs((xmin - maybe_x) / maybe_x) < eps) {
            std::cout << "Minimum found at x = " << maybe_x << std::endl;
            break;
        } else if (maybe_x >= x1 && maybe_x <= x3) {
            f2 = f_maybe_x;
            x2 = maybe_x;

            if (maybe_x <= x2) {
                f3 = f2;
                x3 = x2;
            } else {
                f1 = f2;
                x1 = x2;
            }
            skip = true;
        } else {
            x1 = maybe_x;
            skip = false;
        }
    }

    std::cout << "End" << '\n';
}
