#include <stdio.h>
#include <gmp.h>
#include <sys/time.h>

#include "src/ec.h"
#include "src/fp.h"
#include "src/sm.h"
#include "src/naf.h"
#include "src/utils.h"


int main(void) {

    int max_bits = 256;
    int max_str = 80;
    char *p = "115792089237316195423570985008687907853269984665640564039457584007908834671663";
    char *n = "115792089237316195423570985008687907852837564279074904382605163141518161494337";
    char *a = "0";
    char *b = "7";

    ecc_curve secp256k1;
    ecc_init_curve(&secp256k1, p, a, max_bits, max_str);

    ecc_jcb_t JP, JG;
    ecc_init_jcb(&JP);
    //ecc_print_jcb(&JP);
    ecc_init_setstr_jcb(&JG, "55066263022277343669578718895168534326250603453777594175500187360389116729240", "32670510020758816978083085130507043184471273380659243275938904335757337482424", "1");

    ecc_afn_t G, R;
    ecc_init_setstr_afn(&G, "55066263022277343669578718895168534326250603453777594175500187360389116729240", "32670510020758816978083085130507043184471273380659243275938904335757337482424");
    ecc_init_afn(&R);
    //ecc_print_afn(&G);

    mpz_t k; mpz_init(k);
    mpz_set_str(k, "0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364140", 0);

    //rtl(&JP, &JG, k, &secp256k1);
    ltr(&JP, &G, k, &secp256k1);

    ecc_print_jcb(&JP);

    ecc_jcb_to_afn(&R, &JP, &secp256k1);
    ecc_print_afn(&R);
    mpz_clear(k);
    ecc_clear_jcb(&JP);
    ecc_clear_jcb(&JG);
    ecc_clear_afn(&G);
    ecc_clear_afn(&R);
    return 0;
}
