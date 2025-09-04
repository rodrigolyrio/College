package banco;

import java.util.Scanner;

public class Conta {
    String numero;
    Pessoa titular;
    double saldo;
    Data criacao;
    Gerente gerente;

    // Construtor interativo (não será usado na solução final, mas pode ser mantido)
    Conta(Gerente g) {
        Scanner s = new Scanner(System.in);

        System.out.println("Digite o número: ");
        this.numero = s.nextLine();

        System.out.println("Digite os dados do titular: ");
        this.titular = new Pessoa();

        this.saldo = 0;

        System.out.println("Digite a data de criação: ");
        this.criacao = new Data();

        this.gerente = g;
    }

    // Construtor com dados pré-definidos
    Conta(String n, Pessoa t, Data c, Gerente g) {
        this.numero = n;
        this.titular = t;
        this.saldo = 0;
        this.criacao = c;
        this.gerente = g;
    }

    double disponivel() {
        return this.saldo;
    }

    boolean sacar(double valor) {
        if (valor <= this.disponivel()) {
            this.saldo = this.saldo - valor;
            // ALTERAÇÃO: Mensagem de saque ajustada para incluir o novo saldo.
            System.out.println("Saque na conta " + this.numero + " realizado com sucesso. Novo saldo: R$" + this.saldo);
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
            // ALTERAÇÃO: Mensagem de transferência ajustada para o formato exato.
            // Usando String.format para garantir a casa decimal (ex: 30.0)
            System.out.println("Transferência de R$" + String.format("%.1f", valor) + " da conta " + this.numero + " para a conta " + destino.numero + " realizado com sucesso.");
            return true;
        }

        else {
            System.out.println("ERRO! Não foi possível transferir o" + valor + " da conta " + this.numero + " para a conta " + destino.numero + ". Pois o valor disponível é de " + this.disponivel());
            return false;
        }
    }

    void depositar(double valor) {
        this.saldo += valor;
        System.out.println("Depósito realizado com sucesso.");
        System.out.println("Novo saldo: R$" + this.saldo);
    }

    // CORREÇÃO: Lógica do extrato movida para o método com nome correto (minúsculo)
    void extrato() {
        System.out.println("Número: " + this.numero);
        System.out.println("Titular: " + this.titular.nome);
        System.out.println("Valor disponível para saque: R$" + this.disponivel());
    }
}