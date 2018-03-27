
import java.util.Scanner;


public class UpToCertainNumber {

    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        
        // Write your code here
        System.out.println("Up to what number?");
        int max_number = Integer.parseInt(reader.nextLine());
        
        int number = 1;
        
        while (number < max_number + 1){
            System.out.println(number);
            number++;
        }
        
    }
}
