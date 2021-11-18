class Converter:
    def __init__(self):
        self.donation = 0.00
        self.dolar = 5.51

    def main(self):
        self.get_donation()
        converted_donation = self.convert_donation(self.donation)
        self.print_donation(converted_donation)

    def convert_donation(self, donation):
        return self.dolar * float(donation)

    def get_donation(self):
        self.donation = input("Digite o valor da doação: ")

    def print_donation(self, donation):
        print(f"Valor doado em reais R${donation}")


if __name__ == '__main__':
    Converter().main()
