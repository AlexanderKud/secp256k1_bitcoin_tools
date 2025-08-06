#include <windows.h>
#include <cstdio>

//typedef INT (CALLBACK* LPFNDLLFUNC1)(INT, INT);
typedef INT (*AddFunc)(INT, INT);
typedef VOID (*PrintStrFunc)(PCHAR);

int main()
{
HINSTANCE hDLL;               // Handle to DLL
//LPFNDLLFUNC1 lpfnDllFunc1;    // Function pointer
//AddFunc lpfnDllFunc1;
PrintStrFunc lpfnDllFunc1;
//DWORD dwParam1;
INT  uReturnVal;

hDLL = LoadLibrary("adder");
//printf("%d", hDLL);

if (hDLL != NULL)
{
    printf("%s\n", "Success");
    
   //lpfnDllFunc1 = (LPFNDLLFUNC1)GetProcAddress(hDLL, "add_int");
   //lpfnDllFunc1 = (AddFunc)GetProcAddress(hDLL, "add_int");
   lpfnDllFunc1 = (PrintStrFunc)GetProcAddress(hDLL, "print_str");
   if (!lpfnDllFunc1)
   {
      // handle the error
      FreeLibrary(hDLL);
      //return SOME_ERROR_CODE;
   }
   else
   {
      // call the function
      //uReturnVal = lpfnDllFunc1(9, 88);
      //printf("%d", uReturnVal);
      char* str = "Fuck it";
      lpfnDllFunc1(str);
   }

}
else { printf("%s\n", "Failure"); }
return 0;
}
