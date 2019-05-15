figura.pdf: plot.py datos.dat
	python plot.py
datos.dat: a.out
	./a.out
a.out: Laboratorio.cpp
	g++ Laboratorio.cpp

