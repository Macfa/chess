# neural network Game by chy

## To use
* modules:
	* os
	* numpy
	* chess
	* torch

## feature
1. en passan:
	* 3, 6 rank or None
2. kingside castling:
	* R,K Castling
3. queenside castling:
	* R,Q Castling

## scenario
* comm'n soon

## files
* parsing.py:
	* load a file about data in game
	* push a moves to game board 
	* save a file with board

* state.py:
	* inialize a board
	* define a Method to use
	* convert piece to vector
	* return vector

* play.py:
	* define a network
	* load a file that defined in parsing.py
	* define a loss function
	* input's data to network
	* play ( WEB framework )

## Helpful
* ThanksTo
	* Link : [chess databases](http://www.kingbase-chess.net)
	* Link : [geohot-twitchchess](https://github.com/geohot/twitchchess)
	* Link : [learn Math](https://ko.khanacademy.org)
	* Link : [learn deeplearning](https://www.edwith.org)
