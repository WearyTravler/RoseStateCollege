package molecularcalculator;
import java.util.Scanner;

public class MolecularCalculator {

    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // Homework: Modify this to use H2SO4 rather 
        // than CO2
        
        System.out.println("Welcome to the Moleculator!");
        System.out.println("Let's calculate the number of molecules.\n");
        
        
        String substance = "H2SO4 (sulfuric acid)";
        double molar_mass = 98.079; //m.mass of the substance
        
        final double avogadros = 6.022E23;
        
        double mass;
        double moles;
        double molecules;
        
        System.out.print("How many grams of " + substance + "?");
        mass = sc.nextDouble();
        
        moles = mass * avogadros;
        molecules = moles * molar_mass;
        
        System.out.printf("%f grams of %s contains %e molecules\n", mass, substance, molecules);
        
    }
}
