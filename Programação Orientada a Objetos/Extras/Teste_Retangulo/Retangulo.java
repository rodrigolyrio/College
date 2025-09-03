public class Retangulo {
    double largura;
    double altura;

    Retangulo(double largura, double altura) {
        this.largura = largura;
        this.altura = altura;
    }

    double calcularArea() {
        double formula = largura * altura;
        return formula;
    }

    double calcularPerimetro() {
        double formula = 2 * (largura + altura);
        return formula;
    }

    boolean ehQuadrado() {
        if (largura == altura) {
            return true;
        } else {
            return false;
        }
    }
}
