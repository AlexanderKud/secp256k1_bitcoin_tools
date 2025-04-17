#include <stdio.h>
#include <string.h>
#include <string>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <ctime>

#include "secp256k1/SECP256k1.h"
#include "secp256k1/Int.h"
#include "bloom/bloom.h"

using namespace std;

//const char *bloomfile = "address_bloomfilter.blm";

char* to_hex(unsigned char *ptr, int length) {
	if(ptr == NULL || length <= 0)
		return NULL;
	// Allocate memory for the hexadecimal string and initialize it to zero
	char *hex_string = (char *)calloc((2 * length) + 1, sizeof(char));
	if(hex_string == NULL)
		fprintf(stderr,"Erro calloc()\n");
	// Convert the input string to a hexadecimal string
	for (int i = 0; i < length; i++) {
		snprintf((char*)(hex_string + (2 * i)), 3, "%.2x",(uint8_t) ptr[i]);
	}
	return hex_string;
}

char *ltrim(char *str, const char *seps) {
	size_t totrim;
	if (seps == NULL) {
		seps = "\t\n\v\f\r ";
	}
	totrim = strspn(str, seps);
	if (totrim > 0) {
		size_t len = strlen(str);
		if (totrim == len) {
			str[0] = '\0';
		}
		else {
			memmove(str, str + totrim, len + 1 - totrim);
		}
	}
	return str;
}

char *rtrim(char *str, const char *seps) {
	int i;
	if (seps == NULL) {
		seps = "\t\n\v\f\r ";
	}
	i = strlen(str) - 1;
	while (i >= 0 && strchr(seps, str[i]) != NULL) {
		str[i] = '\0';
		i--;
	}
	return str;
}

char *trim(char *str, const char *seps)	{
	return ltrim(rtrim(str, seps), seps);
}

int main() {
    
    Secp256K1* secp256k1 = new Secp256K1(); secp256k1->Init();
    time_t seconds; struct tm *timeStruct;
    
    /*
    unsigned char h160u[20];
    unsigned char h160c[20];
    string addr { "1EHNa6Q4Jz2uvNExL497mE43ikXi239kyRH" };
    Secp256K1* secp256k1 = new Secp256K1();
    secp256k1->Init();
    Int privKey;
    privKey.SetBase16("0000000000000000000000000000000000000000000000000000000000000002");
    Point pub = secp256k1->ComputePublicKey(&privKey);
    cout << "Privkey: " << privKey.GetBase16() << endl;
    cout << "Privkey: " << setw(64) << setfill('0') << privKey.GetBase16() << endl;
    cout << "Pub_U: " << secp256k1->GetPublicKeyHex(false, pub) << endl;
    cout << "Pub_C: " << secp256k1->GetPublicKeyHex(true, pub) << endl;
    secp256k1->GetHash160(0, false, pub, h160u);
    secp256k1->GetHash160(0, true, pub, h160c);
    cout << "Ripemd160_U: " << to_hex(h160u, 20) << endl;
    cout << "Ripemd160_C: " << to_hex(h160c, 20) << endl;
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
    */
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
