import java.util.Scanner;

public class OlaFulano {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o nome: ");
        String nome = scanner.nextLine();

        System.out.println("Olá, " + nome);

        scanner.close();
    }
}
