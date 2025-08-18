package main

import "fmt"

func main() {
    var nome string

    fmt.Print("Digite o nome: ")
    fmt.Scanln(&nome)

    fmt.Printf("Olá, %s\n", nome)
}
