package banco;

public class Banco {
    public static void main(String[] args) {
        Pessoa p1 = new Pessoa();
        p1.nome = "Rodrigo";
        p1.cpf = "123.456.789-00";
        p1.idade = 18;
        p1.sexo = 'M';

        Pessoa p2 = new Pessoa();
        p2.nome = "Gepeto";
        p2.cpf = "098.876.234-55";
        p2.idade = 999;
        p2.sexo = 'F';

        Conta c1 = new Conta();
        c1.numero = "1234-5";
        c1.titular = p1;
        c1.saldo = 100;
        c1.limite = 200;

        Conta c2 = new Conta();
        c2.numero = "2345-6";
        c2.titular = p2;
        c2.saldo = 150;
        c2.limite = 200;

        c1.Extrato();
        c2.Extrato();

        c1.sacar(150);
        c1.transferir(100, c2);
        c1.sacar(100);
        c1.depositar(100);
        c1.transferir(200, c2);


        // TESTANDO CHEQUE-ESPECIAL
        for (int i = 1; i <= 120; i++) {
            c1.chequeEspecial(0.5);
            System.out.println("Saldo após " + i + " dias: " + c1.saldo);
        }
    }
}
