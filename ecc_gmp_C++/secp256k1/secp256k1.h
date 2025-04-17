#ifndef SECP256K1_H
#define SECP256K1_H

class Point {
public:
    mpz_class x;
    mpz_class y;
    Point();
    Point(mpz_class x, mpz_class y);
    Point(const Point &p);
    void print_Point();
};

class Elliptic_Curve {
public:
    mpz_class a; 
    mpz_class b; 
    mpz_class p;
    mpz_class n;
    Elliptic_Curve(); 
};

class Secp256k1 {
public:
    Point G;
    Point Infinity;
    Elliptic_Curve EC;
    Secp256k1();
    Point PubKey_To_Point(std::string &pubkey);
    Point Point_Doubling(Point &p);
    Point Point_Addition(Point &a, Point &b);
    Point Scalar_Multiplication(mpz_class pk);
    Point Point_Multiplication(Point &a, mpz_class pk);
    Point Point_Negation(Point &p);
    Point Point_Subtraction(Point &a, Point &b);
    Point Point_Division(Point &a, mpz_class sc);
    bool Point_On_Curve(Point &p);
    std::string Point_To_Upub(Point &p);
    std::string Point_To_Cpub(Point &p);
    std::string Private_Key_To_WIF(mpz_class pk, bool compressed);
    std::string Point_To_Hash160(Point &a, bool compressed);
    std::string Point_To_Legacy_Address(Point &a, bool compressed);
    std::string Point_To_P2SH_Address(Point &p);
    std::string Point_To_Bech32_P2WPKH_Address(Point &p);
    std::string Point_To_Bech32_P2WSH_Address(Point &p);
    const char * Tagged_Hash(mpz_class x);
    std::string Taproot_Tweaked_PrivKey(mpz_class k);
    std::string Point_To_Taproot_Tweaked_Pubkey(Point &p);
    std::string Point_To_Bech32m_P2TR_Address(Point &p);
    void Context_Init();
};

#endif
