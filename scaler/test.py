class Test:

    def __init__(self, data_path) -> None:

        self.data_path = data_path

    def show_data(self, ):
        
        self.content = open(self.data_path, 'r', encoding='UTF-8')
        self.df = self.content.readlines()
        self.content.close()

        for i in range(0, len(self.df)):
            # print(self.df[i])
            print(self.df[i].split())

        return