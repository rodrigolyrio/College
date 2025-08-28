package banco;

public class Conta {
    String numero;
    Pessoa titular;
    double saldo, limite;
    Data criacao;
    Gerente gerente;

    Conta(String n, Pessoa t, Data c, Gerente g) {
        this.numero = n;
        this.titular = t;
        this.saldo = 0;
        this.criacao = c;
        this.gerente = g;
    }

    void depositar(double valor) {
        this.saldo += valor;
        System.out.println("Depósito realizado com Sucesso!");
        System.out.println("Novo saldo: R$" + this.saldo);
    }
}