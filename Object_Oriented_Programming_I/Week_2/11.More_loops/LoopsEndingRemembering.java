import java.util.Scanner;

public class LoopsEndingRemembering {
    public static void main(String[] args) {
        // program in this project exercises 36.1-36.5
        // actually this is just one program that is split in many parts
        
        Scanner reader = new Scanner(System.in);
        
        System.out.println("Type numbers:");
        
        int result = 0;
        int numbers = 0;
        int odd_numbers = 0;
        
        while (true){
            
            int number = Integer.parseInt(reader.nextLine());
            
            if (number == -1){
                System.out.println("Thank you and see you later!");
                System.out.println("The sum is " + result);
                System.out.println("How many numbers: " + numbers);
                
                float average = (float)result/numbers;
                
                System.out.println("Average: " + average);
                System.out.println("Even numbers" + (numbers-odd_numbers));
                System.out.println("Odd numbers: " +  odd_numbers);
                break;
                
            } else if (number%2 != 0){
            
                odd_numbers += 1;
                            
            }
                
            result += number;
            numbers += 1;
  
        }

    }
}
