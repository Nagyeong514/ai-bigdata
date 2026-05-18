class Recoding:
    def __str__(self, date, category, amount):
            self.date = date
            self.category = category
            self.amount = amount
            
        def get_info(self):
            print("===== 지출 내역 =====")
            print(f"{date} | {category} | {amount}")
            print("====================")