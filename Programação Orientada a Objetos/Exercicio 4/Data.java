package banco;

public class Data {
    int dia, mes, ano;

    Data(int d, int m, int a) {
        this.dia = d;
        this.mes = m;
        this.ano = a;
    }

    /*
    void Imprimir() {
        System.out.println(this.dia + "/" + this.mes + "/" + this.ano);
     */

    String Imprimir() {
        return this.dia + "/" + this.mes + "/" + this.ano;
    }

    /*
    String Maior(Data d2) {
        String frase;
        if (this.ano > d2.ano) {
            frase = this.dia + "/" + this.mes + "/" + this.ano + "É maior que " + d2.dia + "/" + d2.mes + "/" + d2.ano;
        } else if (this.mes > d2.mes) {
            frase = this.dia + "/" + this.mes + "/" + this.ano + "É maior que " + d2.dia + "/" + d2.mes + "/" + d2.ano;
        } else if (this.dia > d2.dia) {
            frase = this.dia + "/" + this.mes + "/" + this.ano + "É maior que " + d2.dia + "/" + d2.mes + "/" + d2.ano;
        } else {
            frase = d2.dia  + "/" + d2.mes + "/" + d2.ano + "É maior que " + this.dia + "/" + this.mes + "/" + this.ano;
        }
        return frase;
    }
    */

    boolean maior(Data d2) {
        if (this.ano > d2.ano) {
            return true;
        } else if (this.ano == d2.ano) {
            if (this.mes > d2.mes) {
                return true;
            } else if (this.mes == d2.mes) {
                if (this.dia > d2.dia) {
                    return true;
                }
            }
        }
        return false;
    }
}