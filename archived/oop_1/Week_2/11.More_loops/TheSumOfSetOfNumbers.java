
import java.util.Scanner;

public class TheSumOfSetOfNumbers {

    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        
        System.out.println("Until what?");
        int max_number = Integer.parseInt(reader.nextLine());
        
        int result = 0;
        int number = 0;
        
        while(number < max_number + 1){
            result += number;
            number++;
        }

        System.out.println("Sum is " + result);
        
    }
}
