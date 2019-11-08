import re 

original_filename = 'collection.bib'
output_filename = 'collection_updated.bib'
label = 'title'

with open(original_filename) as f:
    lines = f.readlines()

file  = open(output_filename, "w")
for line in lines:
	if re.search("^\stitle*", line):
		line = re.sub("^\stitle\s*=\s*{", "\ttitle={{", line)
		line = re.sub("},\s*\n", "}},\n", line)
		print(line)
	file.write(line)