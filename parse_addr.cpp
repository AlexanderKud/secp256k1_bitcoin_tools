#include <iostream>
#include <fstream>
#include <algorithm>
#include <string.h>
#include <ctime>

using namespace std;

const std::string WHITESPACE = " \n\r\f\v";
 
std::string ltrim(const std::string &s)
{
    size_t start = s.find_first_not_of(WHITESPACE);
    return (start == std::string::npos) ? "" : s.substr(start);
}
 
std::string rtrim(const std::string &s)
{
    size_t end = s.find_last_not_of(WHITESPACE);
    return (end == std::string::npos) ? "" : s.substr(0, end + 1);
}
 
std::string trim(const std::string &s) {
    return rtrim(ltrim(s));
}

bool startsWith(std::string mainStr, std::string toMatch)
{
    // std::string::find returns 0 if toMatch is found at starting
    if(mainStr.find(toMatch) == 0)
        return true;
    else
        return false;
}

int main() {
    time_t seconds; struct tm *timeStruct;
    string line;
    
    ifstream ReadFile("address.tsv");
    ofstream WriteFile("address_parsed.txt", std::ios_base::app);

    seconds = time(NULL);
    timeStruct = localtime(&seconds);
    printf("[%02d:%02d:%02d] Start parsing address file\n", timeStruct->tm_hour, timeStruct->tm_min, timeStruct->tm_sec);
    while (getline(ReadFile, line)) {
        line = trim(line);
        if(startsWith(line, "1")) {
            WriteFile << line << '\n';
        }
    }
    seconds = time(NULL);
    timeStruct = localtime(&seconds);
    printf("[%02d:%02d:%02d] Finish parsing address file\n", timeStruct->tm_hour, timeStruct->tm_min, timeStruct->tm_sec);
    
    ReadFile.close();
    WriteFile.close();
    return 0;
}
