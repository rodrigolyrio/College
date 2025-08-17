#include <stdio.h>

int main() {
    char nome[100];  // Assume um nome de até 99 caracteres

    printf("Digite o nome: ");
    scanf("%s", nome);

    printf("Olá, %s\n", nome);

    return 0;
}
