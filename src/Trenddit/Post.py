class Post:
	def __init__(self, id, subreddit, title):
		self.id = id
		self.subreddit = subreddit
		self.title = title
		self.link = "reddit.com/" + id

	def toString(self):
		string = self.subreddit + "\n" + self.title + "\n" + self.link
		return string

	def getId(self):
		return self.id