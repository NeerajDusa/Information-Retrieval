from os import listdir, getcwd, path
from os.path import isfile, join
from nltk.stem import PorterStemmer


class listpost:
    def __init__(self, txtfile, wordcount):
        self.txtfile = txtfile.split(".")[0]
        self.wordcount = wordcount

    def __str__(self):
        return f"({self.txtfile},{self.wordcount})"

class invIndex:
    
    def __init__(self):
        self.posting = dict()

    def process_word(self, chars):

        if "‘" in chars:
            chars = chars.replace("‘", "")
        
        if "’" in chars:
            chars = chars.replace("’", "")
 
        if "(" in chars:
            chars = chars.replace("(", "")

        if ")" in chars:
            chars = chars.replace(")", "")
                  
        if "\n" in chars:
            chars = chars.replace("\n", "")

        if "," in chars:
            chars = chars.split(",")[0]
        
        if "&" in chars:
            chars = chars.replace("&", "") 
        
        if "." in chars:
            chars = chars.replace(".", "")

        if "-" in chars:
            chars = chars.replace("-", " ")
        
        if "“" in chars:
            chars = chars.replace("“", "")

        if "”" in chars:
            chars = chars.replace("”", "")
        
        stemmer = PorterStemmer()
        return stemmer.stem(chars)

    def file_processor(self, file_name, cont):
        eachterm_map = dict()
        words = cont.split(" ")

        for chars in words:
            chars = self.process_word(chars)

            if chars in eachterm_map.keys():
                eachterm_map[chars] += 1
            else:
                eachterm_map[chars] = 1
        
        for wdata in eachterm_map.items():
            wordval, wordcount = wdata
            listitem = listpost(file_name, wordcount)
            if wordval in self.posting.keys():
                self.posting[wordval].append(listitem)
            else:
                self.posting[wordval] = list([listitem])

    def index_of_directory(self, path_of_dir):
        
        filenames = [ f for f in listdir(path_of_dir) if isfile(join(path_of_dir, f))]
        
        for f in filenames:
            cont = open(join(path_of_dir, f), encoding='utf-8')
            self.file_processor(f, cont.read())
    
    def to_export_index(self, output_file_name="InvIndexing-output"):
        for wdata in list(self.posting.items()):
            wval, wkey  = wdata
            output_string = f"{wval} => "
            posting_list = "".join([f"{str(posting_item.txtfile)}," for posting_item in wkey])
            output_string += f"( {len(wkey)} , [{posting_list}])\n" 
            with open(f"{output_file_name}.txt", 'a', encoding="utf-8") as f:
                f.write(output_string)



if __name__ == "__main__":
    
    FilePath =  path.abspath(getcwd()) + r"/Sample-Dataset"

    inverter = invIndex()
    inverter.index_of_directory(path_of_dir=FilePath)

    inverter.to_export_index()
   