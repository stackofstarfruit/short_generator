import csv
import qbreader

# Read from "short_generator.csv"
with open("short_generator.csv", 'r', newline="\n") as infile:
    reader = csv.reader(infile, delimiter=',')
    rows = [row for row in reader]

# Write to "short_generator_weighted.csv"
with open("short_generator_weighted.csv", 'w', newline="\n") as outfile:
    writer = csv.writer(outfile, delimiter=',')
    i = 0
    for row in rows:
      if i != 0:
        work = row[0]
        #authorNames = row[1].split(" ")
        #author = authorNames[len(authorNames) - 1]
        #res = qbreader.query(questionType="tossup",searchType="all",queryString=work)
        #hits = len(res["tossups"]["questionArray"])
        hits = int(row[3])
        for x in range(hits):
          writer.writerow(row)
      else:
        writer.writerow(row)
      i = i + 1