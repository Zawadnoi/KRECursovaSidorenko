default:
	make build
	make install
	make run
	make clean

build:
	python -m compileall .

run:
	python -m compileall .
	python 1.py
	python 2.py
	python 3-1.py
	python 3-2.py
	python 4.py
	python 5.py
	python 6.py
	python 7-1.py
	python 7-2.py
	python 8.py
	python 9.py
	python 10.py

clean:
	rd /q /s __pycache__

install:
	mkdir \path
	copy 1.py \path
	copy 2.py \path
	copy 3-1.py \path
	copy 3-2.py \path
	copy 4.py \path
	copy 5.py \path
	copy 6.py \path
	copy 7-1.py \path
	copy 7-2.py \path
	copy 8.py \path
	copy 9.py \path
	copy 10.py \path
	copy library.py \path