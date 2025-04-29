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
#include "util/util.h"

using namespace std;
const char *bloomfile = "address_bloomfilter.blm";

int main() {
    Secp256K1* secp256k1 = new Secp256K1(); secp256k1->Init();
    time_t seconds; struct tm *timeStruct;
    Int max_value, min_value, divide, max_min_stride, between, walker, walker_stride, loop;
    Point max_point, min_point, max_min_stride_point, walker_point, walker_stride_point;
    string temp, bitAddr_U, bitAddr_C, addrBech32, wif_U, wif_C;
    int counter{0};
    
    ifstream inFile("settings.txt");
    getline(inFile, temp); max_value.SetBase10(trim(const_cast<char*>(temp.c_str()), NULL));
    getline(inFile, temp); min_value.SetBase10(trim(const_cast<char*>(temp.c_str()), NULL));
    getline(inFile, temp); divide.SetBase10(trim(const_cast<char*>(temp.c_str()), NULL));
    inFile.close();
    
    max_point = secp256k1->ComputePublicKey(&max_value);
    min_point = secp256k1->ComputePublicKey(&min_value);
    max_min_stride.SetBase10("1");
    max_min_stride_point = secp256k1->ComputePublicKey(&max_min_stride);
    between.Sub(&max_value, &min_value);

    seconds = time(NULL);
    timeStruct = localtime(&seconds);
    printf("[%02d:%02d:%02d] Loading Bloomfilter\n", timeStruct->tm_hour, timeStruct->tm_min, timeStruct->tm_sec);
    BloomFilter bfd;
    bloom_filter_import(&bfd, bloomfile);
    seconds = time(NULL);
    timeStruct = localtime(&seconds);
    printf("[%02d:%02d:%02d] Bloomfilter ready\n", timeStruct->tm_hour, timeStruct->tm_min, timeStruct->tm_sec);

    while(divide.IsLower(&between)) {
        seconds = time(NULL);
        timeStruct = localtime(&seconds);
        printf("[%02d:%02d:%02d] [%d] %s\n", timeStruct->tm_hour, timeStruct->tm_min, timeStruct->tm_sec, counter, divide.GetBase10().c_str());
        // max_point
        bitAddr_U = secp256k1->GetAddress(0, false, max_point);
        if (bloom_filter_check_string(&bfd, bitAddr_U.data()) == BLOOM_SUCCESS) {
            wif_U = secp256k1->GetPrivAddress(false, max_value);
            printf("[--------] Found address: %s %s \n", bitAddr_U.c_str(), wif_U.c_str());
            ofstream outFile;
            outFile.open("found.txt", ios::app);
            outFile << bitAddr_U << " " << wif_U << '\n';
            outFile.close();
            counter++;
        }
        bitAddr_C = secp256k1->GetAddress(0, true, max_point);
        if (bloom_filter_check_string(&bfd, bitAddr_C.data()) == BLOOM_SUCCESS) {
            wif_C = secp256k1->GetPrivAddress(true, max_value);
            printf("[--------] Found address: %s %s \n", bitAddr_C.c_str(), wif_C.c_str());
            ofstream outFile;
            outFile.open("found.txt", ios::app);
            outFile << bitAddr_C << " " << wif_C << '\n';
            outFile.close();
            counter++;
        }
        addrBech32 = secp256k1->GetAddress(2, true, max_point);
        if (bloom_filter_check_string(&bfd, addrBech32.data()) == BLOOM_SUCCESS) {
            wif_C = secp256k1->GetPrivAddress(true, max_value);
            printf("[--------] Found address: %s %s \n", addrBech32.c_str(), wif_C.c_str());
            ofstream outFile;
            outFile.open("found.txt", ios::app);
            outFile << addrBech32 << " " << wif_C << '\n';
            outFile.close();
            counter++;
        }
        // min_point
        bitAddr_U = secp256k1->GetAddress(0, false, min_point);
        if (bloom_filter_check_string(&bfd, bitAddr_U.data()) == BLOOM_SUCCESS) {
            wif_U = secp256k1->GetPrivAddress(false, min_value);
            printf("[--------] Found address: %s %s \n", bitAddr_U.c_str(), wif_U.c_str());
            ofstream outFile;
            outFile.open("found.txt", ios::app);
            outFile << bitAddr_U << " " << wif_U << '\n';
            outFile.close();
            counter++;
        }
        bitAddr_C = secp256k1->GetAddress(0, true, min_point);
        if (bloom_filter_check_string(&bfd, bitAddr_C.data()) == BLOOM_SUCCESS) {
            wif_C = secp256k1->GetPrivAddress(true, min_value);
            printf("[--------] Found address: %s %s \n", bitAddr_C.c_str(), wif_C.c_str());
            ofstream outFile;
            outFile.open("found.txt", ios::app);
            outFile << bitAddr_C << " " << wif_C << '\n';
            outFile.close();
            counter++;
        }
        addrBech32 = secp256k1->GetAddress(2, true, min_point);
        if (bloom_filter_check_string(&bfd, addrBech32.data()) == BLOOM_SUCCESS) {
            wif_C = secp256k1->GetPrivAddress(true, min_value);
            printf("[--------] Found address: %s %s \n", addrBech32.c_str(), wif_C.c_str());
            ofstream outFile;
            outFile.open("found.txt", ios::app);
            outFile << addrBech32 << " " << wif_C << '\n';
            outFile.close();
            counter++;
        }
        // walker_point
        between.Sub(&max_value, &min_value);
        walker.Set(&min_value);
        walker_stride.floor_Div(&between, &divide);
        walker_point = secp256k1->ComputePublicKey(&walker);
        walker_stride_point = secp256k1->ComputePublicKey(&walker_stride);
        for(loop.SetBase10("0"); loop.IsLower(&divide); loop.AddOne()) {
            walker_point = secp256k1->Add2(walker_point, walker_stride_point);
            walker_point.Reduce();
            walker.Add(&walker_stride);
            bitAddr_U = secp256k1->GetAddress(0, false, walker_point);
            if (bloom_filter_check_string(&bfd, bitAddr_U.data()) == BLOOM_SUCCESS) {
                wif_U = secp256k1->GetPrivAddress(false, walker);
                printf("[--------] Found address: %s %s \n", bitAddr_U.c_str(), wif_U.c_str());
                ofstream outFile;
                outFile.open("found.txt", ios::app);
                outFile << bitAddr_U << " " << wif_U << '\n';
                outFile.close();
                counter++;
            }
            bitAddr_C = secp256k1->GetAddress(0, true, walker_point);
            if (bloom_filter_check_string(&bfd, bitAddr_C.data()) == BLOOM_SUCCESS) {
                wif_C = secp256k1->GetPrivAddress(true, walker);
                printf("[--------] Found address: %s %s \n", bitAddr_C.c_str(), wif_C.c_str());
                ofstream outFile;
                outFile.open("found.txt", ios::app);
                outFile << bitAddr_C << " " << wif_C << '\n';
                outFile.close();
                counter++;
            }
            addrBech32 = secp256k1->GetAddress(2, true, walker_point);
            if (bloom_filter_check_string(&bfd, addrBech32.data()) == BLOOM_SUCCESS) {
                wif_C = secp256k1->GetPrivAddress(true, walker);
                printf("[--------] Found address: %s %s \n", addrBech32.c_str(), wif_C.c_str());
                ofstream outFile;
                outFile.open("found.txt", ios::app);
                outFile << addrBech32 << " " << wif_C << '\n';
                outFile.close();
                counter++;
            }
        }
        
        divide.AddOne();
        min_value.Add(&max_min_stride);
        max_value.Sub(&max_min_stride);
        min_point = secp256k1->Add2(min_point, max_min_stride_point);
        min_point.Reduce();
        max_point = secp256k1->Subtract(max_point, max_min_stride_point);
        max_point.Reduce();
        
        ofstream outFile("settings.txt");
        outFile << max_value.GetBase10() << '\n';
        outFile << min_value.GetBase10() << '\n';
        outFile << divide.GetBase10() << '\n';
        outFile.close();
    }
   
    seconds = time(NULL);
    timeStruct = localtime(&seconds);
    printf("[%02d:%02d:%02d] Finished...Found %d targets\n", timeStruct->tm_hour, timeStruct->tm_min, timeStruct->tm_sec, counter);
    cin.clear();
    cin.get();
    return 0;
}
