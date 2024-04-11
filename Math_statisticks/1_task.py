import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

num_samples = 20000
sample_size = 1000
mu, sigma = 0, 1

sample_means = np.zeros(num_samples)
sample_variances = np.zeros(num_samples)
sample_medians = np.zeros(num_samples)
u1_values = np.zeros(num_samples)
u2_values = np.zeros(num_samples)

for i in range(num_samples):
    sample = np.random.normal(mu, sigma, sample_size)
    sample_means[i] = np.mean(sample)
    sample_variances[i] = np.var(sample, ddof=3)
    sample_medians[i] = np.quantile(sample, 0.5)
    sorted_sample = np.sort(sample)
    u1_values[i] = sample_size * stats.norm.cdf(sorted_sample[1], mu, sigma)
    u2_values[i] = sample_size * (1 - stats.norm.cdf(sorted_sample[-1], mu, sigma))


def plot_histogram_and_density(data, density_function, title, bins=30, **kwargs):
    plt.hist(data, bins=bins, density=True, alpha=0.6, color='g', label='Гистограмма')
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = density_function(x, **kwargs)
    plt.plot(x, p, 'k', linewidth=2, label='Теоретическая плотность')
    plt.title(title)
    plt.legend()
    plt.grid(True)


p = stats.norm.pdf(sample_means)

plt.figure(figsize=(18, 10))

plt.subplot(2, 3, 1)
plot_histogram_and_density(sample_means, stats.norm.pdf, "Выборочное среднее", loc=mu,
                           scale=sigma / np.sqrt(sample_size))

plt.subplot(2, 3, 2)
plot_histogram_and_density(sample_variances, stats.chi2.pdf, "Выборочная дисперсия", df=sample_size - 1,
                           scale=sigma ** 2 / (sample_size - 1))

plt.subplot(2, 3, 3)
plt.subplot(2, 3, 1)
# plot_histogram_and_density(sample_medians, stats.median.pdf, "Выборочное среднее", loc=mu,
#                            scale=sigma / np.sqrt(sample_size))
plt.hist(sample_medians, bins=30, density=True, alpha=0.6, color='b')
plt.title("Выборочная квантиль 0.5")
plt.grid(True)

plt.subplot(2, 3, 4)
plot_histogram_and_density(u1_values, stats.gamma.pdf, "$nF(X_{(2)})$", a=2, scale=1)

plt.subplot(2, 3, 5)
plot_histogram_and_density(u2_values, stats.expon.pdf, "$n(1 - F(X_{(n)}))$", scale=1)

plt.tight_layout()
plt.show()

stats_data = {
    "Выборочное среднее": (sample_means.mean(), sample_means.var(), np.median(sample_means)),
    "Выборочная дисперсия": (sample_variances.mean(), sample_variances.var(), np.median(sample_variances)),
    "Выборочная квантиль 0.5": (sample_medians.mean(), sample_medians.var(), np.median(sample_medians)),
    "nF(X_(2))": (u1_values.mean(), u1_values.var(), np.median(u1_values)),
    "n(1 - F(X_n))": (u2_values.mean(), u2_values.var(), np.median(u2_values))
}

for stat, values in stats_data.items():
    print(f"{stat}: Среднее = {values[0]:.4f}, Дисперсия = {values[1]:.4f}, Медиана = {values[2]:.4f}")
