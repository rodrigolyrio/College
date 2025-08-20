package banco;

public class Data {
    int dia, mes, ano;

    Data(int d, int m, int a) {
        this.dia = d;
        this.mes = m;
        this.ano = a;
    }

    void Imprimir() {
        System.out.println(this.dia + "/" + this.mes + "/" + this.ano);
    }
}

