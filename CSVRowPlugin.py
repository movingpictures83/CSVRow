class CSVRowPlugin:
    def input(self, inputfile):
        self.infile = open(inputfile, 'r')
    def run(self):
        pass
    def output(self,outputfile):
        outfile = open(outputfile, 'w')
        self.infile.readline()
        for line in self.infile:
            contents = line.strip().split(',')
            outfile.write(contents[0][1:len(contents[0])-1]+"\n")
