import csv

class ImgIterator:
    def __init__(self, name):
        self.csv_file = name + ".csv"
        self.file_exist = True
    
    def __iter__(self):
        try:
            file = open(self.csv_file, newline="")
            self.csvreader = csv.reader(file)
        except:
            self.file_exist = False
        
        return self
    
    def __next__(self):
        if not self.file_exist:
            raise StopIteration
        
        return self.csvreader.__next__()
            
    

if __name__ == "__main__":
    ii = ImgIterator("snake")
    for rp, ap in ii:
        print(rp, ap)