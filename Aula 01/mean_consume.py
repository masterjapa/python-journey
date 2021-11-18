class MeanConsume:
    def __init__(self):
        self.initial_mark = 0
        self.final_mark = 0
        self.total_refuelled = 0

    def main(self):
        self.get_travel_info()
        mean_consume = self.calculate_mean(
            self.initial_mark, self.final_mark, self.total_refuelled)
        self.print_mean_consume(mean_consume)

    def get_travel_info(self):
        self.initial_mark = input(
            "Insira a kilometragem inicial do percurso: ")
        self.final_mark = input(
            "Insira a kilometragem final do percurso: ")
        self.total_refuelled = input(
            "Insira a quantidade de litros abastecidos no percurso: ")

    def calculate_mean(self, initial_mark, final_mark, total_refuelled):
        mean = (int(final_mark) - int(initial_mark)) / int(total_refuelled)
        return f"{mean:.2f}"

    def print_mean_consume(self, mean):
        print(f"O consumo médio nesta viagem foi de {mean}km/l")


if __name__ == '__main__':
    MeanConsume().main()
