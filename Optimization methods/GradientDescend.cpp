#include <iostream>
#include <cmath>

double f(double x, double y) {
    return pow(x, 4) + pow(y, 4) - 2 * pow(x - y, 2);
}

double f_x_der(double x, double y) {
    return 4 * pow(x, 3) - 4 * x + 4 * y;
}

double f_y_der(double x, double y) {
    return 4 * pow(y, 3) + 4 * x - 4 * y;
}

double norm(double x, double y) {
    return sqrt(pow(x, 2) + pow(y, 2));
}

double grad_desc(double x, double y) {
    double prec = 0.0001;
    double step = 1;
    double new_x, new_y, grad_x, grad_y;

    while (true) {
        grad_x = f_x_der(x, y);
        grad_y = f_y_der(x, y);
        new_x = x - step * grad_x;
        new_y = y - step * grad_y;

        if (fabs(f(new_x, new_y) - f(x, y)) < prec) {
            x = new_x;
            y = new_y;
            break;
        }

        if (f(new_x, new_y) > f(x, y)) {
            step /= 10;
            continue;
        }

        x = new_x;
        y = new_y;
    }

    return f(x, y);
}

double steepest_desc(double x, double y) {
    double eps = 0.0001;
    double grad_x = f_x_der(x, y);
    double grad_y = f_y_der(x, y);
    double normed_grad = norm(grad_x, grad_y);

    while (norm(grad_x, grad_y) >= eps) {
        double s_k_x = grad_x / normed_grad;
        double s_k_y = grad_y / normed_grad;

        double l = -2.5, r = 2.5, x1, x2, left_eps, right_eps, x_m;

        while (r - l >= 2 * eps) {
            x1 = (l + r - eps) / 2;
            x2 = (l + r + eps) / 2;

            left_eps = f(x + x1 * s_k_x, y + x1 * s_k_y);
            right_eps = f(x + x2 * s_k_x, y + x2 * s_k_y);

            if (left_eps >= right_eps) {
                l = x1;
            } else {
                r = x2;
            }
        }

        x_m = (l + r) / 2;
        x += x_m * s_k_x;
        y += x_m * s_k_y;
        grad_x = f_x_der(x, y);
        grad_y = f_y_der(x, y);
        normed_grad = norm(grad_x, grad_y);
    }

    return f(x, y);
}

int main() {
    std::cout << "Gradient Descent Result: " << grad_desc(-0.2, 0.2) << std::endl;
    std::cout << "Steepest Descent Result: " << steepest_desc(-0.2, 0.2) << std::endl;
    return 0;
}
