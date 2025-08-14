section .data
    hello db 'Olá, Mundo!', 0

section .text
    global _start

_start:
    ; Escrever a mensagem
    mov eax, 4             ; Código da syscall sys_write
    mov ebx, 1             ; Descritor de arquivo (stdout)
    mov ecx, hello         ; Endereço da mensagem
    mov edx, 13            ; Comprimento da mensagem
    int 0x80               ; Chamada do sistema

    ; Sair do programa
    mov eax, 1             ; Código da syscall sys_exit
    xor ebx, ebx           ; Código de retorno 0
    int 0x80               ; Chamada do sistema
