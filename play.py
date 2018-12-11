from train import Net
import torch
from state import State
from flask import Flask, Response, request

class calcurator():
	def __init__(self):
		self.model = Net()
		self.model.load_state_dict(torch.load("nets/value.pth"))
		self.model.eval()
		

	def __call__(self, s):
		ser = s.serialize()[None]
		ser = torch.tensor(ser).float()
		output = self.model(ser)
		# print(float(torch.Tensor.item(output[0][0][0][0])))
		return float(torch.Tensor.item(output[0][0]))
		# return output[]

def getting_moves(s, c):
	res = []
	for i in s.list():
		s.board.push(i)
		res.append([i, c(s)])
		s.board.pop()
	return res


if __name__ == "__main__":
	s = State()
	c = calcurator()
	# getting_moves(s,c)

	

app = Flask(__name__)

@app.route("/")
def hello():
  ret = open("index.html").read()
  return ret.replace('start', s.board.fen())


@app.route("/test")
def test():
  ret = '<html><head>'
  # self play
  while not s.board.is_game_over():
    move = getting_moves(s, c)
    print("===================\n\n")
    print(sorted(move, reverse=True))
    ret += '<img width=600 height=600 src="data:image/svg+xml;base64,%s"></img><br/>' % to_svg(s)
  	
app.run()
