package banco;

import java.util.Scanner;


public class Pessoa {
    String nome, cpf;
    Data nascimento;
    char sexo;


    Pessoa() {
        Scanner s = new Scanner(System.in);

        System.out.println("Digite o nome: ");
        this.nome = s.nextLine();

        System.out.println("Digite o CPF: ");
        this.cpf = s.nextLine();

        System.out.println("Digite a data de nascimento: ");
        this.nascimento = new Data();

        System.out.println("Digite o sexo: ");
        this.sexo = s.nextLine().charAt(0);

    }

    Pessoa(String n, String c, Data nasc, char s) {
        this.nome = n;
        this.cpf = c;
        this.nascimento = nasc;
        this.sexo = s;
    }

    int idade(Data hoje) {
        int idade = hoje.ano - this.nascimento.ano;

        if (hoje.mes < this.nascimento.mes || (hoje.mes == this.nascimento.mes && hoje.dia < this.nascimento.dia)) {
            idade -= 1;
        }

        return idade;
    }
}