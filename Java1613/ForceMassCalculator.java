package forcemasscalculator;
import java.util.Scanner;
import java.lang.Math;
/**
 *
 * @author Jonah
 */
public class ForceMassCalculator {

  
    public static void main(String[] args) {
        // double force;
        double M1; //kg
        double M2; //kg 
        double d; // meters
        double G;
        double F;
        
        G = 6.67E-11;
        
        // calculate force
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Calculating force...");
        System.out.print("M1's mass in kg: ");
        M1 = sc.nextDouble(); // Mass of M1
        System.out.print("M2's mass in kg: ");
        M2 = sc.nextDouble(); // Mass of M2
        System.out.print("What is the distance: ");
        d = sc.nextDouble(); // Distance between eachother
        System.out.println("Here's your force:");
        F = G*M1*M2/Math.pow(d,2);
        System.out.printf("The force between M1 and M2 is %e Newtons \n", F);
      
    }
    
}
