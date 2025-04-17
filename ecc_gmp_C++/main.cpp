#include <iostream>
#include <fstream>
#include <vector>
#include <time.h>
#include <gmpxx.h>
#include <gmp.h>
#include "secp256k1/secp256k1.h"
#include "bloom/bloom.h"
//#include "util/util.h"

using namespace std;

const char *bloomfile = "points_bloomfilter.blm";

int main(int argc, char *argv[])
{
    time_t seconds; struct tm *timeStruct;
    ifstream file("points.txt");
    Secp256k1 *secp256k1 = new Secp256k1(); 
    secp256k1->Context_Init();
    vector<string> pubkeys;
    size_t pubkeys_size = 1048576;
    pubkeys.reserve(pubkeys_size);
    string pub;
    seconds = time(NULL);
    timeStruct = localtime(&seconds);
    printf("[%02d:%02d:%02d] Loading pubkeys to vector...\n", timeStruct->tm_hour, timeStruct->tm_min, timeStruct->tm_sec);
    while (file >> pub) {
        pubkeys.push_back(pub);
    }
    seconds = time(NULL);
    timeStruct = localtime(&seconds);
    printf("[%02d:%02d:%02d] Done.Total %ld pubkeys.\n", timeStruct->tm_hour, timeStruct->tm_min, timeStruct->tm_sec, pubkeys.size());
    
    //string pubkeys[1048576];
    //Point Q = secp256k1->G;
    //Point P = secp256k1->Point_Division(Q, mpz_class("2", 10));
    //P.print_Point();
    //P = secp256k1->Point_Addition(P, secp256k1->G);
    //P.print_Point();
    /*
    Point Q = secp256k1->G;
    seconds = time(NULL);
    timeStruct = localtime(&seconds);
    printf("[%02d:%02d:%02d] Start\n", timeStruct->tm_hour, timeStruct->tm_min, timeStruct->tm_sec);
    for(int i = 0; i < 1000000; i++) {
        Q = secp256k1->Point_Addition(Q, secp256k1->G);
    }
    seconds = time(NULL);
    timeStruct = localtime(&seconds);
    printf("[%02d:%02d:%02d] Finish\n", timeStruct->tm_hour, timeStruct->tm_min, timeStruct->tm_sec);
    Q.print_Point();
    */
    //Point a = secp256k1->G;
    /*Point a {mpz_class("bf23c1542d16eab70b1051eaf832823cfc4c6f1dcdbafd81e37918e6f874ef8b", 16),
             mpz_class("a34c79903ccffc8c8526d75f45ac6d1b3add03ab7ee1d087b23c8100997cde90", 16)};
    a.print_Point();
    string pubkey = "03acd484e2f0c7f65309ad178a9f559abde09796974c57e714c35f110dfc27ccbe";//9G
    Point b = secp256k1->PubKey_To_Point(pubkey);
    b.print_Point();
    Point c = secp256k1->Point_Doubling(b);
    c.print_Point();
    Point d = secp256k1->Point_Addition(secp256k1->Infinity, a);
    d.print_Point();
    Point e = secp256k1->Scalar_Multiplication(mpz_class("57896044618658097711785492504343953926418782139537452191302581570759080747169", 10));
    e.print_Point();
    Point f = secp256k1->Point_Multiplication(b, mpz_class("7", 10));
    f.print_Point();
    Point g = secp256k1->Point_Negation(f);
    g.print_Point();
    Point h = secp256k1->Point_Subtraction(b, b);
    h.print_Point();
    Point i = secp256k1->Point_Division(b, mpz_class("3", 10));
    i.print_Point();
    cout << secp256k1->Point_On_Curve(i) << '\n';
    cout << secp256k1->Point_To_Upub(i) << '\n';
    cout << secp256k1->Point_To_Cpub(i) << '\n';
    */
    /*
    mpz_class pk;
    pk = 1;
    Point Q = secp256k1->G;
    for(int i = 0; i < 5; i++) {
        cout << secp256k1->Private_Key_To_WIF(pk, false) << '\n';
        cout << secp256k1->Private_Key_To_WIF(pk, true) << '\n';
        cout << secp256k1->Point_To_Hash160(Q, false) << '\n';
        cout << secp256k1->Point_To_Hash160(Q, true) << '\n';
        cout << secp256k1->Point_To_Legacy_Address(Q, false) << '\n';
        cout << secp256k1->Point_To_Legacy_Address(Q, true) << '\n';
        cout << secp256k1->Point_To_P2SH_Address(Q) << '\n';
        cout << secp256k1->Point_To_Bech32_P2WPKH_Address(Q) << '\n';
        cout << secp256k1->Point_To_Bech32_P2WSH_Address(Q) << '\n';
        cout << secp256k1->Point_To_Bech32m_P2TR_Address(Q) << '\n';
        cout << secp256k1->Point_To_Taproot_Tweaked_Pubkey(Q) << '\n';
        cout << secp256k1->Taproot_Tweaked_PrivKey(pk) << '\n';
        Q = secp256k1->Point_Addition(Q, secp256k1->G);
        mpz_add_ui(pk.get_mpz_t(), pk.get_mpz_t(), 1);
        cout << " " << '\n';
    }
    */
    cout << "Press <Enter> to exit ...\n";
    cin.get();
    return 0;
}
