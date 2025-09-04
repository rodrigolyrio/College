package banco;

import java.util.Scanner;

public class Gerente extends Pessoa {
    String matricula, senha;

    Gerente() {
        super();
        Scanner s = new Scanner(System.in);

        System.out.println("Digite a matrícula: ");
        this.matricula = s.nextLine();

        System.out.println("Digite a senha: ");
        this.senha = s.nextLine();
    }

    Gerente(String nome, String cpf, Data d, char sexo, String matricula, String senha) {
        super(nome, cpf, d, sexo);
        this.matricula = matricula;
        this.senha = senha;
    }

    boolean validarAcesso(String senha) {
        return senha.equals(this.senha);
    }

    boolean validarAcesso() {
        Scanner s = new Scanner(System.in);

        System.out.println("Informe a senha: ");
        String senha = s.nextLine();
        return this.validarAcesso(senha);
    }
}
