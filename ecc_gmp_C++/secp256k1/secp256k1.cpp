#include <iostream>
#include <gmpxx.h>
#include <gmp.h>
#include <stdio.h>
#include <stdlib.h>
#include "secp256k1.h"
#include "../util/util.h"
#include "../base58/libbase58.h"
#include "../rmd160/rmd160.h"
#include "../sha256/sha256.h"
#include "../bech32/segwit_addr.h"


static char X_coord[65];
static char Y_coord[65];
static char upub[132];
static char cpub[68];
static unsigned char bin_privatekey[39];
static unsigned char bin_sha256[32];
static char privatekey[66];
static char wif[54];
static unsigned char bin_publickey[65];
static unsigned char bin_rmd160[20];
static char hash160[42];
static unsigned char bin_digest[60];
static char address[50];
static char bech32_output[128];
char tap_tweak[] = "TapTweak";
static char bin_sha256_ret[33];
static char publickey[66];
static char hex_mpz[66];
static unsigned char pub_bin[33];
static char taghash[33];
static char taghash_final[99];

Point::Point() {}

Point::Point(mpz_class cx, mpz_class cy) {
  x = cx;
  y = cy;
}

Point::Point(const Point &p) {
  x = p.x;
  y = p.y;
}

void Point::print_Point() {
    gmp_printf("X:%0.64Zx Y:%0.64Zx\n", this->x, this->y);
    return;
}

Elliptic_Curve::Elliptic_Curve() {}

Secp256k1::Secp256k1() {}

void Secp256k1::Context_Init() {
    EC.a = 0; EC.b = 7;
    EC.p = "115792089237316195423570985008687907853269984665640564039457584007908834671663";
    EC.n = "115792089237316195423570985008687907852837564279074904382605163141518161494337";
    G.x = "55066263022277343669578718895168534326250603453777594175500187360389116729240";
    G.y = "32670510020758816978083085130507043184471273380659243275938904335757337482424";
    Infinity.x = 0;
    Infinity.y = 0;
    return;
}

Point Secp256k1::PubKey_To_Point(std::string &pubkey) {
    Point A;
    if(startsWith("04", pubkey.c_str())) {
        substr(X_coord, const_cast<char*>(pubkey.c_str()), 3, 64);
        substr(Y_coord, const_cast<char*>(pubkey.c_str()), 67, 64);
        A.x = mpz_class(X_coord, 16);
        A.y = mpz_class(Y_coord, 16);
    }
    if(startsWith("02", pubkey.c_str())) {
        mpz_class ysquared, mpz_aux1, mpz_aux2, Y1, Y2;
        substr(X_coord, const_cast<char*>(pubkey.c_str()), 3, 64);
        A.x = mpz_class(X_coord, 16);
        mpz_pow_ui(mpz_aux1.get_mpz_t(), A.x.get_mpz_t(), 3);
        mpz_add(mpz_aux1.get_mpz_t(), mpz_aux1.get_mpz_t(), EC.b.get_mpz_t());
        mpz_mod(ysquared.get_mpz_t(), mpz_aux1.get_mpz_t(), EC.p.get_mpz_t());
        mpz_add_ui(mpz_aux2.get_mpz_t(), EC.p.get_mpz_t(), 1);
        mpz_fdiv_q_ui(mpz_aux2.get_mpz_t(), mpz_aux2.get_mpz_t(), 4);
        mpz_powm(Y1.get_mpz_t(), ysquared.get_mpz_t(), mpz_aux2.get_mpz_t(), EC.p.get_mpz_t());
        mpz_sub(Y2.get_mpz_t(), EC.p.get_mpz_t(), Y1.get_mpz_t());
        if(mpz_tstbit(Y1.get_mpz_t(), 0) == 0) {
            A.y = Y1;
        } else {
            A.y = Y2;
        }
    }
    if(startsWith("03", pubkey.c_str())) {
        mpz_class ysquared, mpz_aux1, mpz_aux2, Y1, Y2;
        substr(X_coord, const_cast<char*>(pubkey.c_str()), 3, 64);
        A.x = mpz_class(X_coord, 16);
        mpz_pow_ui(mpz_aux1.get_mpz_t(), A.x.get_mpz_t(), 3);
        mpz_add(mpz_aux1.get_mpz_t(), mpz_aux1.get_mpz_t(), EC.b.get_mpz_t());
        mpz_mod(ysquared.get_mpz_t(), mpz_aux1.get_mpz_t(), EC.p.get_mpz_t());
        mpz_add_ui(mpz_aux2.get_mpz_t(), EC.p.get_mpz_t(), 1);
        mpz_fdiv_q_ui(mpz_aux2.get_mpz_t(), mpz_aux2.get_mpz_t(), 4);
        mpz_powm(Y1.get_mpz_t(), ysquared.get_mpz_t(), mpz_aux2.get_mpz_t(), EC.p.get_mpz_t());
        mpz_sub(Y2.get_mpz_t(), EC.p.get_mpz_t(), Y1.get_mpz_t());
        if(mpz_tstbit(Y1.get_mpz_t(), 0) == 0) {
            A.y = Y2;
        } else {
            A.y = Y1;
        }
    }
    return A;
}

Point Secp256k1::Point_Doubling(Point &p) {
    Point A, ATemp;
    mpz_class temp, slope;
    ATemp.x = p.x; ATemp.y = p.y;
    mpz_mul_ui(temp.get_mpz_t(), p.y.get_mpz_t(), 2);
    mpz_invert(temp.get_mpz_t(), temp.get_mpz_t(), EC.p.get_mpz_t());
    mpz_mul(slope.get_mpz_t(), p.x.get_mpz_t(), p.x.get_mpz_t());
    mpz_mul_ui(slope.get_mpz_t(), slope.get_mpz_t(), 3);
    mpz_add(slope.get_mpz_t(), slope.get_mpz_t(), EC.a.get_mpz_t());
    mpz_mul(slope.get_mpz_t(), slope.get_mpz_t(), temp.get_mpz_t());
    mpz_mod(slope.get_mpz_t(), slope.get_mpz_t(), EC.p.get_mpz_t());
    mpz_mul(A.x.get_mpz_t(), slope.get_mpz_t(), slope.get_mpz_t());
    mpz_sub(A.x.get_mpz_t(), A.x.get_mpz_t(), ATemp.x.get_mpz_t());
    mpz_sub(A.x.get_mpz_t(), A.x.get_mpz_t(), ATemp.x.get_mpz_t());
    mpz_mod(A.x.get_mpz_t(), A.x.get_mpz_t(), EC.p.get_mpz_t());
    mpz_sub(temp.get_mpz_t(), ATemp.x.get_mpz_t(), A.x.get_mpz_t());
    mpz_mul(A.y.get_mpz_t(), slope.get_mpz_t(), temp.get_mpz_t());
    mpz_sub(A.y.get_mpz_t(), A.y.get_mpz_t(), ATemp.y.get_mpz_t());
    mpz_mod(A.y.get_mpz_t(), A.y.get_mpz_t(), EC.p.get_mpz_t());
    return A;
}

Point Secp256k1::Point_Addition(Point &a, Point &b) {
    Point A, A1Temp, A2Temp;
    mpz_class u, v, temp, slope;
    A1Temp.x = a.x; A1Temp.y = a.y;
    A2Temp.x = b.x; A2Temp.y = b.y;
    if(mpz_cmp_ui(a.x.get_mpz_t(), 0) == 0 && mpz_cmp_ui(a.y.get_mpz_t(), 0) == 0) {
        mpz_set(A.x.get_mpz_t(), b.x.get_mpz_t());
        mpz_set(A.y.get_mpz_t(), b.y.get_mpz_t());
        return A;
    }
    if(mpz_cmp_ui(b.x.get_mpz_t(), 0) == 0 && mpz_cmp_ui(b.y.get_mpz_t(), 0) == 0) {
        mpz_set(A.x.get_mpz_t(), a.x.get_mpz_t());
        mpz_set(A.y.get_mpz_t(), a.y.get_mpz_t());
        return A;
    }
    if(mpz_cmp(a.x.get_mpz_t(), b.x.get_mpz_t()) == 0 && mpz_cmp(a.y.get_mpz_t(), b.y.get_mpz_t()) != 0) {
        mpz_set_ui(A.x.get_mpz_t(), 0);
        mpz_set_ui(A.y.get_mpz_t(), 0);
        return A;
    }
    if(mpz_cmp(a.x.get_mpz_t(), b.x.get_mpz_t()) == 0 && mpz_cmp(a.y.get_mpz_t(), b.y.get_mpz_t()) == 0) {
        A = Point_Doubling(a);
        return A;
    } else {
        mpz_sub(u.get_mpz_t(), b.y.get_mpz_t(), a.y.get_mpz_t());
        mpz_sub(v.get_mpz_t(), b.x.get_mpz_t(), a.x.get_mpz_t());
        mpz_invert(v.get_mpz_t(), v.get_mpz_t(), EC.p.get_mpz_t());
        mpz_mul(slope.get_mpz_t(), u.get_mpz_t(), v.get_mpz_t());
        mpz_mod(slope.get_mpz_t(), slope.get_mpz_t(), EC.p.get_mpz_t());
        mpz_mul(A.x.get_mpz_t(), slope.get_mpz_t(), slope.get_mpz_t());
        mpz_sub(A.x.get_mpz_t(), A.x.get_mpz_t(), A1Temp.x.get_mpz_t());
        mpz_sub(A.x.get_mpz_t(), A.x.get_mpz_t(), A2Temp.x.get_mpz_t());
        mpz_mod(A.x.get_mpz_t(), A.x.get_mpz_t(), EC.p.get_mpz_t());
        mpz_sub(temp.get_mpz_t(), A1Temp.x.get_mpz_t(), A.x.get_mpz_t());
        mpz_mul(A.y.get_mpz_t(), slope.get_mpz_t(), temp.get_mpz_t());
        mpz_sub(A.y.get_mpz_t(), A.y.get_mpz_t(), A1Temp.y.get_mpz_t());
        mpz_mod(A.y.get_mpz_t(), A.y.get_mpz_t(), EC.p.get_mpz_t());
        return A;
    }
}

Point Secp256k1::Scalar_Multiplication(mpz_class pk) {
    Point A;
    int no_of_bits, loop;
    no_of_bits = mpz_sizeinbase(pk.get_mpz_t(), 2);
    mpz_set(A.x.get_mpz_t(), G.x.get_mpz_t());
    mpz_set(A.y.get_mpz_t(), G.y.get_mpz_t());
    for(loop = no_of_bits - 2; loop >= 0 ; loop--) {
        A = Point_Doubling(A);
        if(mpz_tstbit(pk.get_mpz_t(), loop)) {
            A = Point_Addition(A, G);
        }
    }
    return A;
}

Point Secp256k1::Point_Multiplication(Point &a, mpz_class pk) {
    Point A, ATemp;
    mpz_set(ATemp.x.get_mpz_t(), a.x.get_mpz_t()); mpz_set(ATemp.y.get_mpz_t(), a.y.get_mpz_t());
    int no_of_bits, loop;
    no_of_bits = mpz_sizeinbase(pk.get_mpz_t(), 2);
    mpz_set(A.x.get_mpz_t(), a.x.get_mpz_t());
    mpz_set(A.y.get_mpz_t(), a.y.get_mpz_t());
    for(loop = no_of_bits - 2; loop >= 0 ; loop--) {
        A = Point_Doubling(A);
        if(mpz_tstbit(pk.get_mpz_t(), loop)) {
            A = Point_Addition(A, ATemp);
        }
    }
    return A;
}

Point Secp256k1::Point_Negation(Point &a) {
    Point A;
    mpz_set(A.x.get_mpz_t(), a.x.get_mpz_t());
    mpz_sub(A.y.get_mpz_t(), EC.p.get_mpz_t(), a.y.get_mpz_t());
    return A;
}

Point Secp256k1::Point_Subtraction(Point &a, Point &b) {
    Point A;
    if(mpz_cmp_ui(b.x.get_mpz_t(), 0) == 0 && mpz_cmp_ui(b.y.get_mpz_t(), 0) == 0) {
        mpz_set(A.x.get_mpz_t(), a.x.get_mpz_t());
        mpz_set(A.y.get_mpz_t(), a.y.get_mpz_t());
        return A;
    } else if (mpz_cmp(a.x.get_mpz_t(), b.x.get_mpz_t()) == 0 && mpz_cmp(a.y.get_mpz_t(), b.y.get_mpz_t()) == 0) {
        mpz_set_ui(A.x.get_mpz_t(), 0);
        mpz_set_ui(A.y.get_mpz_t(), 0);
        return A;
    } else {
        Point ATemp;
        mpz_set(ATemp.x.get_mpz_t(), b.x.get_mpz_t());
        mpz_set(ATemp.y.get_mpz_t(), b.y.get_mpz_t());
        ATemp = Point_Negation(ATemp);
        A = Point_Addition(a, ATemp);
        return A;
   }
}

Point Secp256k1::Point_Division(Point &a, mpz_class sc) {
    Point A;
    mpz_class div_s;
    mpz_invert(div_s.get_mpz_t(), sc.get_mpz_t(), EC.n.get_mpz_t());
    A = Point_Multiplication(a, div_s);
    return A;
}

bool Secp256k1::Point_On_Curve(Point &a) {
    mpz_class X, Y;
    mpz_pow_ui(X.get_mpz_t(), a.x.get_mpz_t(), 3);
    mpz_add(X.get_mpz_t(), X.get_mpz_t(), EC.b.get_mpz_t());
    mpz_mod(X.get_mpz_t(), X.get_mpz_t(), EC.p.get_mpz_t());
    mpz_pow_ui(Y.get_mpz_t(), a.y.get_mpz_t(), 2);
    mpz_mod(Y.get_mpz_t(), Y.get_mpz_t(), EC.p.get_mpz_t());
    if (mpz_cmp(X.get_mpz_t(), Y.get_mpz_t()) == 0) {
        return true;
    } else {
        return false;
    }
}

std::string Secp256k1::Point_To_Upub(Point &a) {
    std::string pub;
    gmp_snprintf(upub, 132, "04%0.64Zx%0.64Zx", a.x.get_mpz_t(), a.y.get_mpz_t());
    pub = upub;
    return pub;
}

std::string Secp256k1::Point_To_Cpub(Point &a) {
    std::string pub;
    if(mpz_tstbit(a.y.get_mpz_t(), 0) == 0) {
        gmp_snprintf(cpub, 67, "02%0.64Zx", a.x.get_mpz_t());
    } else {
        gmp_snprintf(cpub, 67, "03%0.64Zx", a.x.get_mpz_t());
    }
    pub = cpub;
    return cpub;
}

std::string Secp256k1::Private_Key_To_WIF(mpz_class pk, bool compressed) {
    size_t wif_size = 54;
    std::string wif_ret;
    bin_privatekey[0] = 0x80;
    gmp_snprintf(privatekey, 65, "%0.64Zx", pk.get_mpz_t());
    hexs2bin(privatekey, bin_privatekey+1);
    if (compressed) {
        bin_privatekey[33] = 0x01;
        sha256(bin_privatekey, 34, bin_sha256);
        sha256(bin_sha256, 32, bin_sha256);
        bin_privatekey[34] = bin_sha256[0];
        bin_privatekey[35] = bin_sha256[1];
        bin_privatekey[36] = bin_sha256[2];
        bin_privatekey[37] = bin_sha256[3];
        b58enc(wif, &wif_size, bin_privatekey, 38);
        wif_ret = wif;
        return wif_ret;
    }
    else {
        sha256(bin_privatekey, 33, bin_sha256);
        sha256(bin_sha256, 32, bin_sha256);
        bin_privatekey[33] = bin_sha256[0];
        bin_privatekey[34] = bin_sha256[1];
        bin_privatekey[35] = bin_sha256[2];
        bin_privatekey[36] = bin_sha256[3];
        b58enc(wif, &wif_size, bin_privatekey, 37);
        wif_ret = wif;
        return wif_ret;
    }
}

std::string Secp256k1::Point_To_Hash160(Point &a, bool compressed) {
    std::string ripemd160;
    if(compressed) {
        if(mpz_tstbit(a.y.get_mpz_t(), 0) == 0) {
            gmp_snprintf (cpub, 67, "02%0.64Zx", a.x.get_mpz_t());
        } else {
            gmp_snprintf(cpub, 67, "03%0.64Zx", a.x.get_mpz_t());
        }
        hexs2bin(cpub, bin_publickey);
        sha256(bin_publickey, 33, bin_sha256);
    } else {
        gmp_snprintf(upub, 132, "04%0.64Zx%0.64Zx", a.x.get_mpz_t(), a.y.get_mpz_t());
        hexs2bin(upub, bin_publickey);
        sha256(bin_publickey, 65, bin_sha256);
    }
    RMD160Data(bin_sha256, 32, bin_rmd160);
    tohex_dst(bin_rmd160, 20, hash160);
    ripemd160 = hash160;
    return ripemd160;
}

std::string Secp256k1::Point_To_Legacy_Address(Point &a, bool compressed) {
    size_t pubaddress_size = 50;
    std::string ret_address;
    if(compressed) {
        if(mpz_tstbit(a.y.get_mpz_t(), 0) == 0) {
            gmp_snprintf(cpub, 68, "02%0.64Zx", a.x.get_mpz_t());
        } else {
            gmp_snprintf(cpub, 68, "03%0.64Zx", a.x.get_mpz_t());
        }
        hexs2bin(cpub, bin_publickey);
        sha256(bin_publickey, 33, bin_sha256);
    } else {
        gmp_snprintf(upub, 132, "04%0.64Zx%0.64Zx", a.x.get_mpz_t(), a.y.get_mpz_t());
        hexs2bin(upub, bin_publickey);
        sha256(bin_publickey, 65, bin_sha256);
    }
    RMD160Data(bin_sha256, 32, bin_digest + 1);
    bin_digest[0] = 0;
    sha256(bin_digest, 21, bin_digest + 21);
    sha256(bin_digest + 21, 32, bin_digest + 21);
    b58enc(address, &pubaddress_size, bin_digest, 25);
    ret_address = address;
    return ret_address;
}

std::string Secp256k1::Point_To_P2SH_Address(Point &p) {
    size_t pubaddress_size = 50;
    std::string p2sh_address;
    if(mpz_tstbit(p.y.get_mpz_t(), 0) == 0) {
        gmp_snprintf(cpub, 68, "02%0.64Zx", p.x.get_mpz_t());
    }
    else {
        gmp_snprintf(cpub, 68, "03%0.64Zx", p.x.get_mpz_t());
    }
    hexs2bin(cpub, bin_publickey);
    sha256(bin_publickey, 33, bin_sha256);
    RMD160Data(bin_sha256, 32, bin_digest + 2);
    bin_digest[0] = 0x00; bin_digest[1] = 0x14;
    sha256(bin_digest, 22, bin_sha256);
    RMD160Data(bin_sha256, 32, bin_digest + 1);
    bin_digest[0] = 0x05;
    sha256(bin_digest, 21, bin_sha256);
    sha256(bin_sha256, 32, bin_sha256);
    bin_digest[21] = bin_sha256[0];
    bin_digest[22] = bin_sha256[1];
    bin_digest[23] = bin_sha256[2];
    bin_digest[24] = bin_sha256[3];
    b58enc(address, &pubaddress_size, bin_digest, 25);
    p2sh_address = address;
    return p2sh_address;
}

std::string Secp256k1::Point_To_Bech32_P2WPKH_Address(Point &p) {
    std::string p2wpkh_address;
    if(mpz_tstbit(p.y.get_mpz_t(), 0) == 0) {
        gmp_snprintf(cpub, 68, "02%0.64Zx", p.x.get_mpz_t());
    }
    else {
        gmp_snprintf(cpub, 68, "03%0.64Zx", p.x.get_mpz_t());
    }
    hexs2bin(cpub, bin_publickey);
    sha256(bin_publickey, 33, bin_sha256);
    RMD160Data(bin_sha256, 32, bin_digest);
    segwit_addr_encode(bech32_output, "bc", 0, bin_digest, 20);
    p2wpkh_address = bech32_output;
    return p2wpkh_address;
}

std::string Secp256k1::Point_To_Bech32_P2WSH_Address(Point &p) {
    std::string p2wsh_address;
    if(mpz_tstbit(p.y.get_mpz_t(), 0) == 0) {
        gmp_snprintf(cpub, 68, "02%0.64Zx", p.x.get_mpz_t());
    }
    else {
        gmp_snprintf(cpub, 68, "03%0.64Zx", p.x.get_mpz_t());
    }
    hexs2bin(cpub, bin_publickey);
    sha256(bin_publickey, 33, bin_sha256);
    segwit_addr_encode(bech32_output, "bc", 0, bin_sha256, 32);
    p2wsh_address = bech32_output;
    return p2wsh_address;
}

const char * Secp256k1::Tagged_Hash(mpz_class x) {
    gmp_snprintf(hex_mpz, 65, "%0.64Zx", x.get_mpz_t());
    hexs2bin(hex_mpz, pub_bin);
    sha256(tap_tweak, strlen(tap_tweak), taghash);
    memmove(taghash_final, taghash, sizeof(taghash));
    memmove(taghash_final + 32, taghash, sizeof(taghash));
    memmove(taghash_final + 64, pub_bin, sizeof(pub_bin));
    sha256(taghash_final, 96, bin_sha256);
    tohex_dst(bin_sha256, 32, bin_sha256_ret);
    return bin_sha256_ret;
}

std::string Secp256k1::Taproot_Tweaked_PrivKey(mpz_class k) {
    std::string tweaked_priv;
    Point AffinePoint;
    mpz_class tap_s, tap_t, seckey;
    AffinePoint = Scalar_Multiplication(k);
    if(mpz_tstbit(AffinePoint.y.get_mpz_t(), 0) == 0) {
        mpz_set(seckey.get_mpz_t(), k.get_mpz_t());
    }
    else {
        mpz_sub(tap_s.get_mpz_t(), EC.n.get_mpz_t(), k.get_mpz_t());
        mpz_set(seckey.get_mpz_t(), tap_s.get_mpz_t());
    }
    mpz_set_str(tap_t.get_mpz_t(), Tagged_Hash(AffinePoint.x), 16);
    mpz_add(seckey.get_mpz_t(), seckey.get_mpz_t(), tap_t.get_mpz_t());
    mpz_mod(seckey.get_mpz_t(), seckey.get_mpz_t(), EC.n.get_mpz_t());
    mpz_get_str(privatekey, 16, seckey.get_mpz_t());
    tweaked_priv = privatekey;
    return tweaked_priv;
}

std::string Secp256k1::Point_To_Taproot_Tweaked_Pubkey(Point &p) {
    Point TapPoint, AffinePoint;
    mpz_class tap_t;
    std::string tweaked_pub;
    mpz_set(TapPoint.x.get_mpz_t(), p.x.get_mpz_t());
    mpz_set(TapPoint.y.get_mpz_t(), p.y.get_mpz_t());
    if(mpz_tstbit(TapPoint.y.get_mpz_t(), 0) != 0) {
        TapPoint = Point_Negation(TapPoint);
    }
    mpz_set_str(tap_t.get_mpz_t(), Tagged_Hash(TapPoint.x), 16);
    AffinePoint = Scalar_Multiplication(tap_t);
    TapPoint = Point_Addition(AffinePoint, TapPoint);
    mpz_get_str(publickey, 16, TapPoint.x.get_mpz_t());
    tweaked_pub = publickey;
    return tweaked_pub;
}

std::string Secp256k1::Point_To_Bech32m_P2TR_Address(Point &p) {
    std::string p2tr_address;
    gmp_snprintf(cpub, 68, "%064s", Point_To_Taproot_Tweaked_Pubkey(p).c_str());
    hexs2bin(cpub, bin_publickey);
    segwit_addr_encode(bech32_output, "bc", 1, bin_publickey, 32);
    p2tr_address = bech32_output;
    return p2tr_address;
}

