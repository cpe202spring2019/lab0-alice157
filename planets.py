def weight_on_planets():
    output_string = "\nOn Mars you would weigh {} pounds.\nOn Jupiter you would weigh {} pounds."
    earth_weight = int(input("What do you weigh on earth? "))
    mars_weight = earth_weight * 0.38
    jupiter_weight = earth_weight * 2.34
    print(output_string.format(mars_weight, jupiter_weight))

if __name__ == '__main__':
    weight_on_planets()
