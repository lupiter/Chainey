
import argparse
import re
from lark import Lark, Transformer, v_args

def get_args():
	parser = argparse.ArgumentParser(description='Convert text crochet instructions to a diagram.')
	parser.add_argument('instructions', metavar='file.txt', type=str, required=True,
	                    help='the source instructions')
	parser.add_argument('diagram', metavar='file.svg', type=str, required=True,
	                    help='the destination diagram')
	parser.add_argument('--uk', type=bool, help='instructions use uk terminology')
	return parser.parse_args()

parser = Lark(json_grammar, parser='earley', transformer=TreeToDiagram())

class TreeToDiagram(Transformer):
    def string(self, s):
        return s[1:-1].replace('\\"', '"')

    def pattern(self, children):
    	return Pattern()

    array = list
    pair = tuple
    object = dict
    number = v_args(inline=True)(int)


class CrochetParser(object):
	"""docstring for CrochetParser"""
	def __init__(self, text):
		super(CrochetParser, self).__init__()
		self.text = text

	def parse(self):
		self.__split_rows()
		self.__parse_rows()
		self.__identify_stitches()
		self.__attach_stitches()

	def __split_rows(self):
		self.rows = re.split('([Rr][Oo][Ww] [1-9]+:)', self.text)
		self.rows = [Row(row) for row in x.split("turn") for x in self.rows]

	def __parse_rows(self):
		for row in self.rows:
			row.parse()


if __name__ == "__main__"
	args = get_args()
	text = None
	with open(args.instructions) as f:
		text = f.read()
	parser = CrochetParser(text)
	parser.parse()
	if len(parser.errors) > 0:
		print(parser.errors)
	else:
		with open(args.diagram, 'w') as f:
			f.write(parser.diagram)
		print("done!")