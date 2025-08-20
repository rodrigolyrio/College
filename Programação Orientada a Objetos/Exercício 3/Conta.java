package banco;

public class Conta {
    String numero;
    Pessoa titular;
    double saldo, limite;

    Conta(String n, Pessoa t) {
        this.numero = n;
        this.titular = t;
        this.saldo = 0;
        this.limite = 200;
    }

    Conta(String n, Pessoa t, double l) {
        this(n, t);
        this.limite = l;
    }

    double disponivel() {
        return this.saldo + this.limite;
    }

    void Extrato() {
        System.out.println("\n" + "*** EXTRATO DA CONTA ***");
        System.out.println("Número: " + this.numero);
        System.out.println("Titular: " + this.titular.nome);
        System.out.println("Valor disponivel para saque: R$" + this.disponivel());
    }

    void depositar(double valor) {
        this.saldo = this.saldo + valor;
        System.out.println("Depósito realizado com Sucesso!");
        System.out.println("Novo saldo: R$" + this.saldo);
    }

    boolean sacar(double valor) {
        if (valor <= this.disponivel()) {
            this.saldo = this.saldo - valor;
            System.out.println("Saque na conta " + this.numero + " realizado com Sucesso!");
            return true;
        }

        else {
            System.out.println("ERRO! Saque na conta " + this.numero + " NÃO realizado!");
            return false;
        }
    }

    boolean transferir(double valor, Conta destino) {
        if (this.sacar(valor)) {
            destino.depositar(valor);
            System.out.println("Transferência de R$" + valor + " depositado na conta " + this.numero + " para a conta " + destino.numero + " realizado com SUCESSO!");
            return true;
        }

        else {
            System.out.println("ERRO! Não foi possível transferir o" + valor + " da conta " + this.numero + " para a conta " + destino.numero + ". Pois o valor disponível é de " + this.disponivel());
            return false;
        }
    }

    // METODO CHEQUE-ESPECIAL (EXERCICIO)
    void chequeEspecial(double juro) {
        if (this.saldo < 0) {
            this.saldo = this.saldo + (this.saldo * juro / 100); // Aplica juros apenas sobre o saldo negativo
        }
    }
}
