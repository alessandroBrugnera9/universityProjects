cmake_minimum_required(VERSION 3.15)
project(vendingMachine C)

set(CMAKE_C_STANDARD 99)

add_executable(vendingMachine main.c definicoes.h estoque.c estoque.h caixaDeDinheiro.c caixaDeDinheiro.h comunicador.c comunicador.h)
