section .data
    hello db 'Olá, ', 0
    max_name_length equ 50
    name db max_name_length, 0

section .bss
    input_len resb 1

section .text
    global _start

_start:
    ; Leia o nome do usuário
    mov eax, 3
    mov ebx, 0
    mov ecx, name
    mov edx, max_name_length
    int 0x80

    ; Remova a quebra de linha do nome
    mov esi, name
    mov edi, input_len
    dec edi
    mov al, 0
    repne scasb
    mov byte [esi - 1], 0

    ; Escreva a saudação "Olá, (input)"
    mov eax, 4
    mov ebx, 1
    mov ecx, hello
    int 0x80

    ; Saia do programa
    mov eax, 1
    int 0x80
