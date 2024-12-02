class FinanceCalculator:
    def __init__(self):
        self.expenses = []
        self.savings = 0
        self.investment = 0

    def add_expense(self, amount):
        """Menambahkan pengeluaran ke daftar pengeluaran."""
        if amount < 0:
            print("Jumlah pengeluaran tidak boleh negatif.")
            return
        self.expenses.append(amount)
        print(f"Pengeluaran sebesar {amount} telah ditambahkan.")

    def calculate_total_expenses(self):
        """Menghitung total pengeluaran bulanan."""
        total = sum(self.expenses)
        print(f"Total pengeluaran bulanan: {total}")
        return total

    def set_savings(self, amount):
        """Mengatur jumlah tabungan bulanan."""
        if amount < 0:
            print("Jumlah tabungan tidak boleh negatif.")
            return
        self.savings = amount
        print(f"Tabungan bulanan diatur sebesar {self.savings}.")

    def calculate_remaining_after_savings_and_investment(self):
        """Menghitung sisa uang setelah tabungan dan investasi."""
        total_expenses = self.calculate_total_expenses()
        remaining = self.savings + self.investment - total_expenses
        print(f"Sisa uang setelah tabungan dan investasi: {remaining}")
        return remaining

    def set_investment(self, amount):
        """Mengatur jumlah investasi."""
        if amount < 0:
            print("Jumlah investasi tidak boleh negatif.")
            return
        self.investment = amount
        print(f"Jumlah investasi diatur sebesar {self.investment}.")

    def calculate_total_investment(self):
        """Menghitung total investasi."""
        total_investment = self.investment
        print(f"Total investasi: {total_investment}")
        return total_investment


def main():
    calculator = FinanceCalculator()

    while True:
        print("\nMenu:")
        print("1. Set Tabungan Bulanan")
        print("2. Set Investasi")
        print("3. Tambah Pengeluaran")
        print("4. Hitung Total Investasi")
        print("5. Hitung Sisa Uang Setelah Tabungan dan Investasi")
        print("6. Hitung Total Pengeluaran")
        print("7. Keluar")

        choice = input("Pilih opsi (1-7): ")

        if choice == '1':
            try:
                amount = float(input("Masukkan jumlah tabungan bulanan: "))
                calculator.set_savings(amount)
            except ValueError:
                print("Input tidak valid. Silakan masukkan angka.")
        elif choice == '2':
            try:
                amount = float(input("Masukkan jumlah investasi: "))
                calculator.set_investment(amount)
            except ValueError:
                print("Input tidak valid. Silakan masukkan angka.")
        elif choice == '3':
            try:
                amount = float(input("Masukkan jumlah pengeluaran: "))
                calculator.add_expense(amount)
            except ValueError:
                print("Input tidak valid. Silakan masukkan angka.")
        elif choice == '4':
            calculator.calculate_total_investment()
        elif choice == '5':
            calculator.calculate_remaining_after_savings_and_investment()
        elif choice == '6':
            calculator.calculate_total_expenses()
        elif choice == '7':
            print("Terima kasih telah menggunakan Kalkulator Keuangan Sederhana!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()