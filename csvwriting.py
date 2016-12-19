import csv

csvfile = open("examplefile.csv", "w")

csvwriter = csv.writer(csvfile, delimiter=',')

csvwriter.writerow(["all", "my", "cells", "go", "in", "this", "list"])

csvfile.close()
