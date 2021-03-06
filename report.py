from matplotlib import pyplot as plt

def plot_best_individual_by_generation(arr):
    plt.plot(arr)
    plt.ylabel('Fitness melhor indivíduo')
    plt.xlabel('Geração')
    plt.title("Melhor indivíduo por geração")
    plt.savefig("best_fitness_by_generation.png")
    plt.close()

def plot_best_individual_by_history(arr):
    plt.plot(arr)
    plt.ylabel('Fitness melhor indivíduo')
    plt.xlabel('Geração')
    plt.title("Melhor indivíduo da história")
    plt.savefig("best_fitness_by_history.png")
    plt.close()

def plot_estats_fitness_by_generation(std_fitness,variance_fitness):
    plt.plot(std_fitness,label="Desvio Padrão")
    plt.plot(variance_fitness,label="Variância")
    plt.legend()
    plt.xlabel('Geração')
    plt.title("Statisticas do fitness da população por geração")
    plt.savefig("stats_fitness_by_generation.png")
    plt.close()

def plot_stats_std(arr):
    plt.plot(arr)
    plt.ylabel('Fitness médio')
    plt.xlabel('Geração')
    plt.title("Desvio Padrão do Fitness da população por geração")
    plt.savefig("std_fitness_by_generation.png")
    plt.close()

def plot_fitness_mean_by_generation(arr):
    plt.plot(arr)
    plt.ylabel('Fitness médio')
    plt.xlabel('Geração')
    plt.title("Fitness médio da população por geração")
    plt.savefig("mean_fitness_by_generation.png")
    plt.close()

def plot_mean_best_fitness_by_generation(mean_fitness,melhor,melhor_geracao):
    plt.plot(mean_fitness,label="Média fitness")
    plt.plot(melhor_geracao,label="Melhor fitness geração")
    plt.plot(melhor,label="Melhor fitness histórico")
    plt.legend()
    plt.ylabel('Fitness')
    plt.xlabel('Geração')
    plt.title("Média da população vs Melhor indivíduo em fitness por geração e geral")
    plt.savefig("mean_best_fitness_by_generation.png")
    plt.close()

def separate_stats(arr):
    mean_fitness = []
    std_fitness = []
    variance_fitness = []
    for i,j,k in arr:
        mean_fitness.append(i)
        variance_fitness.append(j)
        std_fitness.append(k)
    return mean_fitness,std_fitness,variance_fitness

def plot_graphs(best_fitness_generation,best_fitness, stats_fitness):
    plot_best_individual_by_generation(best_fitness_generation)
    plot_best_individual_by_history(best_fitness)
    mean_fitness,std_fitness,variance_fitness = separate_stats(stats_fitness)
    plot_fitness_mean_by_generation(mean_fitness)
    plot_estats_fitness_by_generation(std_fitness,variance_fitness)
    plot_stats_std(std_fitness)
    plot_mean_best_fitness_by_generation(mean_fitness,best_fitness,best_fitness_generation)