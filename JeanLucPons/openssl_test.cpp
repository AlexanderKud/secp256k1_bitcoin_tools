#include <climits> 
#include <openssl/bn.h>
#include <stdio.h>

int main() {
 BN_CTX *ctx = BN_CTX_new(); // контекст для вычислений
 BIGNUM *mybignum = nullptr;   // число, которое будем умножать
 BIGNUM *mul = BN_new();     // результат умножения

 BN_dec2bn(&mybignum, "18446744073709551615"); // 2^64-1
 BN_mul(mul, mybignum, mybignum, ctx);

 // распечатаем результат
 char *dec = BN_bn2dec(mul);
 if (dec) {
  printf("%s\n", dec);
  OPENSSL_free(dec);
 }

 // освободим выделенную память
 BN_free(mybignum);
 BN_free(mul);
}
