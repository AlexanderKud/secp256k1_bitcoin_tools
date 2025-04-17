default:
	g++ -O3 -c sha256/sha256.c -o sha256.o
	g++ -O3 -c base58/base58.c -o base58.o
	g++ -O3 -c rmd160/rmd160.c -o rmd160.o
	g++ -O3 -c bech32/segwit_addr.c -o segwit_addr.o
	g++ -O3 -c -Wno-write-strings secp256k1/secp256k1.cpp -o secp256k1.o
	g++ -O3 -c util/util.c -o util.o
	g++ -O3 -c -Wno-unused-result -Wno-write-strings  bloom/bloom.c -o bloom.o
	g++ -O3 -c -Wno-unused-result main.cpp -o main.o
	g++ -o main main.o bloom.o secp256k1.o util.o base58.o sha256.o rmd160.o segwit_addr.o -lgmpxx -lgmp -lm
	#rm *.o
clean:
	#rm -r *.o
