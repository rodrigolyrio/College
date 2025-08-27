package banco;

public class Banco {
    public static void main(String[] args) {
        Pessoa p1 = new Pessoa("Rodrigo", "123.456.789-00", new Data(5,8,1998), 'M');
        Pessoa p2 = new Pessoa("Gepeto", "098.876.234-55", new Data(20,12,1995), 'F');

        int IdadeP1 = p1.idade(new Data(20,8,2025));
        int IdadeP2 = p2.idade(new Data(20, 8,2025));

        System.out.println("A Idade de " + p1.nome + " é " + IdadeP1);
        System.out.println("A Idade de " + p2.nome + " é " + IdadeP2);

        Gerente g = new Gerente("Giraldeli", "123.456.877-00", new Data(30,3, 1971), 'M', "0001", "12345");
        ContaCorrente c1 = new ContaCorrente("1234-5", p1, new Data(12, 3,2019), g);
        ContaCorrente c2 = new ContaCorrente("2345-6", p2, new Data(13,3,2019), g);

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

        // TESTANDO O MÉTODO MAIOR

        System.out.println("\n### TESTANDO O MÉTODO MAIOR ###");
        Data data1 = new Data(27, 8, 2025);
        Data data2 = new Data(15, 10, 2024);

        System.out.print("\nA data " + data1.Imprimir() + " é maior que a data " + data2.Imprimir() + "?");
        System.out.println("\nResposta: " + data1.maior(data2));

        System.out.print("\nA data " + data2.Imprimir() + " é maior que a data " + data1.Imprimir() + "?");
        System.out.println("\nResposta: " + data2.maior(data1));

        // TESTANDO O MÉTODO RENDIMENTOS

        System.out.println("\n### TESTANDO O MÉTODO RENDIMENTOS ###");
        Pessoa p3 = new Pessoa("Tesla", "111.222.333-44", new Data(1, 1, 2000), 'M');
        Poupanca cp3 = new Poupanca("9876-5", p3, new Data(27, 8, 2025), g);

        System.out.println("Saldo inicial da poupança: " + cp3.saldo);

        cp3.rendimentos(1);

        System.out.println("\nDepositando R$1000 na poupança.");
        cp3.depositar(1000);

        System.out.println("\nAplicando rendimento de 0.5%.");
        cp3.rendimentos(0.5);

        System.out.println("Saldo final da poupança após rendimento: " + cp3.saldo);
    }
}
