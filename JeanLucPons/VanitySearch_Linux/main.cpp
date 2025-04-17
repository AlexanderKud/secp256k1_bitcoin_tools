#include <stdio.h>
#include <string.h>
#include <string>
#include <iostream>
#include <iomanip>
#include "secp256k1/SECP256k1.h"

using namespace std;

int main() {

    string addr { "1EHNa6Q4Jz2uvNExL497mE43ikXi239kyRH" };
    Secp256K1* secp256k1 = new Secp256K1();
    secp256k1->Init();
    Int privKey;
    privKey.SetBase16("0000000000000000000000000000000000000000000000000000000000000001");
    Point pub = secp256k1->ComputePublicKey(&privKey);
    cout << "Privkey: " << privKey.GetBase16() << endl;
    cout << "Privkey: " << setw(64) << setfill('0') << privKey.GetBase16() << endl;
    cout << "Pub_U: " << secp256k1->GetPublicKeyHex(false, pub) << endl;
    cout << "Pub_C: " << secp256k1->GetPublicKeyHex(true, pub) << endl;
    string p2pkh_U = secp256k1->GetAddress(0, false, pub);
    string p2pkh_C = secp256k1->GetAddress(0, true, pub);
    string p2sh = secp256k1->GetAddress(1, true, pub);
    string bech32 = secp256k1->GetAddress(2, true, pub);
    string wif_U = secp256k1->GetPrivAddress(false, privKey);
    string wif_C = secp256k1->GetPrivAddress(true, privKey);
    cout << p2pkh_U << endl;
    cout << p2pkh_C << endl;
    cout << p2sh << endl;
    cout << bech32 << endl;
    cout << wif_U << endl;
    cout << wif_C << endl;
    //printf("Addr : %s \n", calcAddress.c_str());
    /*
    if((addr.compare(calcAddress)) == 0)
        cout << addr << " is equal to " << calcAddress << endl;
    else
        cout << addr << " is not equal to " << calcAddress << endl;*/
        //Point pub1 = secp256k1->Double(pub);
        //pub1.Reduce();
        //printf("Pub : %s \n", secp256k1->GetPublicKeyHex(true, pub1));
        //printf("G.x: %s\n", secp256k1->G.x.GetBase16());
        //printf("G.y: %s\n", secp256k1->G.y.GetBase16());
        //printf("G.z: %s\n", secp256k1->G.z.GetBase16());
        //privKey.AddOne();
        //printf("Privkey: %s\n", privKey.GetBase10());
        //#Point S = (secp256k1->G);
        //Point Q;
    //Point P = (secp256k1->G);
    //Point P = secp256k1->ComputePublicKey(&privKey);
    //G2.Reduce();
    //printf("Pub : %s \n", secp256k1->GetPublicKeyHex(false, G2));
    //Point G3 = secp256k1->Add(G2, S);
    //G3.Reduce();
    //printf("Pub : %s \n", secp256k1->GetPublicKeyHex(true, G3));
    /*
    for (int i = 0; i < 1000000; i++) {
        //P.Reduce();
        //printf("Priv : %d \n", i);
        //printf("Pub : %s \n", secp256k1->GetPublicKeyHex(true, P));
        //P = secp256k1->Add(P, secp256k1->G); // a little slower than Add2
        P = secp256k1->Add2(P, secp256k1->G); // fastest point addition
        //P.Reduce();
        //P = secp256k1->AddDirect(P, secp256k1->G); // slowest
        //P = secp256k1->Add3(P, secp256k1->G);
    }
    */
    return 0;

}
