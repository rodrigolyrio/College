public class TesteRetangulo {
    public static void main(String[] args) {
        Retangulo r1 = new Retangulo(10, 5);
        System.out.println("Área de r1: " + r1.calcularArea());
        System.out.println("Perímetro de r1 " + r1.calcularPerimetro());
        System.out.println("r1 é um quadrado? " + r1.ehQuadrado());

        System.out.println("======================");

        Retangulo r2 = new Retangulo(7, 7);
        System.out.println("Área de r2: " + r2.calcularArea());
        System.out.println("Perímetro de r2: " + r2.calcularPerimetro());
        System.out.println("r2 é um quadrado? " + r2.ehQuadrado());
    }
}
