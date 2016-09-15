import argparse, re
from text_iterator import TextIterator


class SourceFile:
	pass

def parse_source(source_text):
	"""Return a dictionary with the defined variables in."""
	it = TextIterator(source_text)
	return_dict = {}
	while not it.done:		
		it.ignore_regex(re.compile(r"\s*"))
		it.accept_regex(re.compile(r"[A-Z_]+"))
		name = it.accepted	
		it.ignore_regex(re.compile(r"\s*"))
		it.accept_string("{\n")
		text = ""
		while not it.accept_string("\n}\n") and not it.done:
			text += it.char
			it.step()
		return_dict[name] = text
	source = SourceFile()
	source.__dict__ = return_dict
	return source

def replace(text, src):
	for name in src.__dict__:
		string = "${" + name + "}"
		text = text.replace(string, src.__dict__[name])
	return text	

def produce(source):
	base_file = open("base/" + source.__BASE__, "r")
	base_text = base_file.read()
	base_file.close()
	out_text = replace(base_text, source)

	out_file = open("../" + source.__OUTPUT__, "w")
	out_file.write(out_text)
	out_file.close()

def get_sources(filenames):
	sources = []
	for filename in filenames:
		src_file = open(filename, "r")
		src = parse_source(src_file.read())
		sources.append(src)
		src_file.close()
	current = 0
	for src in sources:
		src.BEFORETABS = "\n\t".join(["<li><a href=\"" + src_before.__OUTPUT__ + "\">" + src_before.TABNAME + "</a></li>" for src_before in sources[:current]])
		src.AFTERTABS =  "\n\t".join(["<li><a href=\"" + src_before.__OUTPUT__ + "\">" + src_before.TABNAME + "</a></li>" for src_before in sources[current+1:]]) if current < len(sources) - 1 else ""
		current += 1
	return sources

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Compile text files into a website with tabs.")
	parser.add_argument("files", type=str, nargs="+", help=".txt files to be built as tabs of the website.")
	args = parser.parse_args()

	sources = get_sources(args.files)
	for src in sources:
		produce(src)

