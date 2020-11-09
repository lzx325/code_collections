#ifdef __cplusplus


extern "C"{
#endif

int fun1(int x); // This function is going to be implemented in C and called from C++.
int fun2(int x); // This function is going to be implemented in C++ source and called from C.

#ifdef __cplusplus
}
int fun2(); // This is a C++ overload

#endif

int fun3(int x); // This function is going to be implemented in C and called from C++.
int fun4(int x); // This function is going to be implemented in C++ and called from C.
