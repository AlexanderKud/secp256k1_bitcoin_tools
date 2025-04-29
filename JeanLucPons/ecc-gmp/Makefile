default:
	gcc -O3 -c src/ec.c -o ec.o
	gcc -O3 -c src/fp.c -o fp.o
	gcc -O3 -c src/utils.c -o utils.o
	gcc -O3 -c src/naf.c -o naf.o
	gcc -O3 -c src/sm.c -o sm.o
	gcc -O3 -o ecc_test main.c ec.o fp.o utils.o naf.o sm.o -lgmp
	#gcc -O3 -o ecc_test main_1.c ec.o fp.o utils.o naf.o sm.o -lgmp

