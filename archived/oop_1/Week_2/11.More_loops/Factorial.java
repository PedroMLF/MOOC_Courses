import java.util.Scanner;

public class Factorial {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        
        System.out.println("Type a number:");
        int max = Integer.parseInt(reader.nextLine());
        
        int number = 1;
        int result = 1;
        
        while (number < max+1){
            
            result*=number;
            
            number++;
        }

        System.out.println("Factorial is " + result);
        
    }
}
