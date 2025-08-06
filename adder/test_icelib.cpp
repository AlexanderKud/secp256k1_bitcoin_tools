#include <windows.h>
#include <iostream>
#include <vector>
#include <string.h>
#include <wchar.h>
#include <sstream>

typedef VOID (*Version)(VOID);
typedef VOID (*Scalar_Multiplication)(PCHAR,PCHAR);

int hexchr2bin(const char hex, char *out)	{
	if (out == NULL){
		return 0;
	}

	if (hex >= '0' && hex <= '9') {
		*out = hex - '0';
	} else if (hex >= 'A' && hex <= 'F') {
		*out = hex - 'A' + 10;
	} else if (hex >= 'a' && hex <= 'f') {
		*out = hex - 'a' + 10;
	} else {
		return 0;
	}

	return 1;
}

int hexs2bin(char *hex, char *out)	{
	int len;
	char b1;
	char b2;
	int i;
	if (hex == NULL || *hex == '\0' || out == NULL)
		return 0;

	len = strlen(hex);
	if (len % 2 != 0)
		return 0;
	len /= 2;
	memset(out, 0, len);
	for (i=0; i<len; i++) {
		if (!hexchr2bin(hex[i*2], &b1) || !hexchr2bin(hex[i*2+1], &b2)) {
			return 0;
		}
		out[i] = (b1 << 4) | b2;
	}
	return len;
}

char* tohex(char *ptr, int length) {
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

int main()
{
    char privkey_bin[33];
    char pub[65];
    char privkey[] = "0000000000000000000000000000000000000000000000000000000000000001";
    std::stringstream ss;
    for(int i=0; i<strlen(privkey); ++i) ss << std::hex << (int)privkey[i];
    std::string mystr = ss.str();
    //for(int i=0; i< strlen(privkey); ++i)
    //std::cout << std::hex << (int)privkey[i];
    //unsigned int *n = new unsigned int(64);
    hexs2bin(privkey_bin, const_cast<char*>(mystr.c_str()));
    //for(int i = 0; i < 64; i++) {
        //printf("%c", privkey_bin[i]);
    //}
    LPCSTR dll_file {"ice_secp256k1"};
    HINSTANCE hDLL;     // Handle to DLL LPCSTR and HINSTANCE->(Windows API Data Types)
    //Version version;    // Function pointer
    Scalar_Multiplication scalar_multiplication;
    hDLL = LoadLibrary(dll_file); // Loading DLL library ice_secp256k1.dll
    if (hDLL != NULL) { // Success
        std::cout << dll_file << " dll loaded" << '\n';
        //scalar_multiplication = (Version)GetProcAddress(hDLL, "version"); // getting address of function version()
        scalar_multiplication = (Scalar_Multiplication)GetProcAddress(hDLL, "scalar_multiplication"); // getting address of function version() 
        if (!scalar_multiplication) { // Failure getting address
            FreeLibrary(hDLL); // Clearing memory
        }
        else {
            //version(); // Executing function version() from secp256k1.dll
            //FreeLibrary(hDLL); // Clearing memory
            scalar_multiplication(privkey_bin, pub);
            std::cout << "Scalar_Multiplication Success" << '\n';
            printf("%s\n", tohex(pub, 65));
            for(int i = 0; i < 64; i++) {
                 printf("%d ", pub[i]);
            }
        }
        /*
        version = (Version)GetProcAddress(hDLL, "version"); // getting address of function version() 
        if (!version) { // Failure getting address
            FreeLibrary(hDLL); // Clearing memory
        }
        else {
            version(); // Executing function version() from secp256k1.dll
            FreeLibrary(hDLL); // Clearing memory
        }*/
    }
    else { //Failure loading dll
        std::cout << dll_file << " dll not loaded" << '\n';
    }
    return 0;
}
