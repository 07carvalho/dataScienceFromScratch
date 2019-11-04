from matplotlib import pyplot as plt

def main():
    years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
    gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

    # grafico de linha, years no eixo x e gdp no eixo y 
    plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

    plt.title("GDP Nominal")

    plt.ylabel("Bilhoes de $")
    plt.show()

if __name__ == "__main__":
    main()