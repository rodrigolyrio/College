package banco;

public class Banco {
    public static void main(String[] args) {
        Pessoa p1 = new Pessoa();
        p1.nome = "Rodrigo";
        p1.cpf = "123.456.789-00";
        p1.idade = 14;
        p1.sexo = 'M';

        Pessoa p2 = new Pessoa();
        p2.nome = "Gepeto";
        p2.cpf = "098.876.234-55";
        p2.idade = 999;
        p2.sexo = 'F';

        Conta c1 = new Conta();
        c1.numero = "1234-5";
        c1.titular = p1;
        c1.saldo = 0;
        c1.limite = 10000;

        Conta c2 = new Conta();
        c2.numero = "2345-6";
        c2.titular = p2;
        c2.saldo = 10;


        c1.Extrato();
        c2.Extrato();
    }
}
