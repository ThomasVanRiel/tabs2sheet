import argparse



class Generator(object):
	"""docstring for Genrator"""
	def __init__(self):
		super(Generator, self).__init__()
		self.title = None
		self.composer = None

	def add_data(self, data):
		for k,v in data.iteritems():
			setattr(self, k, v)

	def add_title(self, title):
		self.title = title
		
	def add_composer(self, composer):
		self.composer = composer


def main():
	parser = argparse.ArgumentParser(description='Generate music sheet.')
	parser.add_argument('-t', '--title', nargs=1, help='Add a title to the score.')
	parser.add_argument('-c', '--composer', nargs=1, help='Add a composer to the score.')

	args = parser.parse_args()
	arg_dict =dict(vars(args)) 

	g = Generator()
	g.add_data(arg_dict)
	
if __name__ == '__main__':
	main()

