#coding=utf-8
import sys
import os
import csv
from pathlib import Path

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

read_file = open("answersheet.csv", "r", encoding="utf-8")
write_file = open("answersheet_new.csv", "w", encoding="utf-8")
reader = csv.reader(read_file)
writer = csv.writer(write_file)

lines = read_file.readlines()
lines = [line[:-1].split(",") for line in lines]
# print(lines[1])
# exit()
writer.writerow(lines[0])

cnt = 0
for line in lines[1:]:
	# print(line)
	file = line[1]
	# print(file)
	if is_ascii(file):
		# print(line)
		writer.writerow(line)
	else:
		# print(file)
		ori = file
		# ori = ori.encode("utf-8").decode('utf-8')
		# ori = Path(ori)
		# print(ori, os.path.exists(ori))
		# continue

		new_fname = "./images/IM-"+str(cnt).zfill(4)+".jpg"
		cnt += 1
		os.rename(ori, new_fname)
		print(f"rename {ori} to {new_fname}")
		new_line = [line[i] if i != 1 else new_fname for i in range(len(line))]
		print(f"new row: {new_line}")
		writer.writerow(new_line)

read_file.close()
write_file.close()