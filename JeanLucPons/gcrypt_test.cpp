#include <gcrypt.h>
#include <cassert>

int main() {
 unsigned long long mybignum = 18446744073709551615ull; // 2^64-1
 gcry_mpi_t max_ul = gcry_mpi_new(64);                  // представление mybignum в формате gcrypt
 gcry_mpi_t mul = gcry_mpi_new(128);                    // результат умножения

 // переводим mybignum в формат gcrypt
 size_t scanned = 0;
 gcry_mpi_scan(&max_ul, GCRYMPI_FMT_USG, &mybignum, sizeof(unsigned long long), &scanned);
 assert(scanned==sizeof(unsigned long long) && "failed to scan the whole number");

 // умножаем
 gcry_mpi_mul(mul, max_ul, max_ul);
 // выводим на экран
 gcry_mpi_dump(mul);

 // освобождаем ресурсы
 gcry_mpi_release(mul);
 gcry_mpi_release(max_ul);
}
