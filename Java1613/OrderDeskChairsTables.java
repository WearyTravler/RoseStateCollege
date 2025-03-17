package deskchairstables;
import java.util.*;

public class DeskChairsTables {

   
    public static void main(String[] args) {
        // Create a dictionary (HashMap) with item prices or values
        Map<String, Integer> items = new HashMap<>();
        items.put("Desks", 150);
        items.put("Chairs", 50);
        items.put("Tables", 75);

        // Store user input quantities
        Map<String, Integer> userQuantities = new HashMap<>();
        Scanner scanner = new Scanner(System.in);

        // First ask for each item's quantity
        for (String item : items.keySet()) {
            System.out.print("How many " + item + " do you wish to buy? ");
            int quantity = scanner.nextInt();
            userQuantities.put(item, quantity);  // Store user input
        }

        //System.out.println("\nOrder Summary:");
        int grandTotal = 0;
        // Now print out each total
        for (Map.Entry<String, Integer> entry : items.entrySet()) {
            String item = entry.getKey();
            int value = entry.getValue();
            int quantity = userQuantities.get(item);
            int total = quantity * value;
            grandTotal += total;

            System.out.println("Total price of " + item + " = " + "$" + total);
            
        }
        System.out.println("Total bill = $" + grandTotal);
        scanner.close(); // Close scanner
    }
    
}
