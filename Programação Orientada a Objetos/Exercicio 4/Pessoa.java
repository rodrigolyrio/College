package banco;

public class Pessoa {
    String nome, cpf;
    Data nascimento;
    char sexo;

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
