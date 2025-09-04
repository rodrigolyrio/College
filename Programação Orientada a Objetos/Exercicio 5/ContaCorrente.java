package banco;

public class ContaCorrente extends Conta{
    double limite;

    ContaCorrente(Gerente gerente) {
        super(gerente);
        this.limite = 200;
    }

    ContaCorrente(String numero, Pessoa titular, Data c, Gerente gerente) {
        super(numero, titular, c, gerente);
        this.limite = 200;
    }

    double disponivel() {
        return this.saldo + this.limite;
    }

    void extrato() {
        System.out.println("*** EXTRATO DA CONTA CORRENTE ***");
        super.extrato();
    }


    // METODO CHEQUE-ESPECIAL (EXERCICIO)
    void chequeEspecial(double juro) {
        if (this.saldo < 0) {
            this.saldo = this.saldo + (this.saldo * juro / 100); // Aplica juros apenas sobre o saldo negativo
        }
    }
}
