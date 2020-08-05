#!/usr/bin/env bash
warning_options="-pedantic -Wall -Wextra -Wconversion"
(
    set -e
    g++ -o test_interop_cpp.o -c test_interop_cpp.cpp $warning_options
    gcc -o test_interop_c.o -c test_interop_c.c $warning_options
    g++ -o test_interop_main_cpp.out test_interop_main.cpp test_interop_c.o $warning_options
    gcc -o test_interop_main_c.out test_interop_main.c test_interop_cpp.o $warning_options
)
