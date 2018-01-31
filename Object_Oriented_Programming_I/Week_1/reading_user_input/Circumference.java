
import java.util.Scanner;

public class Circumference {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);

        // Program your solution here
        System.out.print("Type the radius: ");
        float radius = Integer.parseInt(reader.nextLine());
        
        double resultToPrint = 2 * Math.PI * radius;
        
        System.out.print("Circumference of the circle: " + resultToPrint);
    }
}
