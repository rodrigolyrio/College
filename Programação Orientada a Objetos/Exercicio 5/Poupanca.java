package banco;

public class Poupanca extends Conta{
    Poupanca(String numero, Pessoa titular, Data c, Gerente gerente) {
        super(numero, titular, c, gerente);
    }

    Poupanca(Gerente gerente) {
        super(gerente);
    }

    void rendimentos(double juros) {
        if (this.saldo > 0) {
            this.saldo += this.saldo * (juros / 100);
            System.out.println("Operação Realizado! Rendimento adicionado ao saldo! Novo saldo: " + this.saldo);
        } else {
            System.out.println("Não há saldo positivo para aplicar rendimentos.");
        }
    }

    void extrato() {
        System.out.println("*** EXTRATO DA POUPANÇA ***");
        super.extrato();
    }
}
