
import java.util.Scanner;

public class EvenOrOdd {

    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);

        // Type your program here
        
        System.out.println("Type a number: ");
        int a = Integer.parseInt(reader.nextLine());
        
        boolean isEven = a%2 == 0;
        
        if (isEven) {
            System.out.println("Number " + a + " is even.");
        }
        else {
            System.out.println("Number " + a + " is odd.");
        }
    }
}
