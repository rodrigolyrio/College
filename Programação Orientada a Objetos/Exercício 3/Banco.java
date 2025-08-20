package banco;

public class Banco {
    public static void main(String[] args) {
        Pessoa p1 = new Pessoa("Rodrigo", "123.456.789-00", new Data(5,8,1998), 'M');
        Pessoa p2 = new Pessoa("Gepeto", "098.876.234-55", new Data(20,12,1995), 'F');

        int IdadeP1 = p1.idade(new Data(20, 8, 2025));
        int IdadeP2 = p2.idade(new Data(20, 8, 2025));

        System.out.println("A Idade de " + p1.nome + " é " + IdadeP1);
        System.out.println("A Idade de " + p2.nome + " é " + IdadeP2);

        Conta c1 = new Conta("1234-5", p1);
        Conta c2 = new Conta("2345-6", p2);

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
