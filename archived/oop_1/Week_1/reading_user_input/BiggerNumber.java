
import java.util.Scanner;

public class BiggerNumber {

    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);

        // Implement your program here. Remember to ask the input from user
        System.out.print("Type a number: ");
        int a = Integer.parseInt(reader.nextLine());
        System.out.print("Type another number: ");
        int b = Integer.parseInt(reader.nextLine());
        
        int resultToPrint = Math.max(a, b);
        
        System.out.print("The bigger number of the two numbers given was: " + resultToPrint);
    }
}
