figura.pdf: plot.py datos.dat datos1.dat
	python plot.py
datos.dat: a.out
	./a.out
a.out: Laboratorio.cpp
	g++ Laboratorio.cpp
datos1.dat: a.out
	./a.out
a.out: Laboratorio.cpp
	g++ Laboratorio.cpp
