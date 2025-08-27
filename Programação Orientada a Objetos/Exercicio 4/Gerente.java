package banco;

public class Gerente extends Pessoa {
    String matricula, senha;

    Gerente(String nome, String cpf, Data d, char sexo, String matricula, String senha) {
        super(nome, cpf, d, sexo);
        this.matricula = matricula;
        this.senha = senha;
    }

    boolean validarAcesso(String senha) {
        return senha.equals(this.senha);
    }
}
