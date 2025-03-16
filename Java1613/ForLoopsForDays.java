public class ForLoopsForDays {

    /**
     * @param args the command line arguments
     */
        public static void main(String[] args) {
        // While loop: 1 to 10
        int i = 1;
        while (i <= 10) {
            System.out.print(i + " ");
            i++;
        }
        System.out.println();

        // Do-while loop: 1 to 10
        int j = 1;
        do {
            System.out.print(j + " ");
            j++;
        } while (j <= 10);
        System.out.println();

        // For loop: 1 to 10
        for (int k = 1; k <= 10; k++) {
            System.out.print(k + " ");
        }
        System.out.println();

        // For loop: 10 to 1
        for (int l = 10; l >= 1; l--) {
            System.out.print(l + " ");
        }
        System.out.println();

        // For loop: 10 to 100 (step 10)
        for (int m = 10; m <= 100; m += 10) {
            System.out.print(m + " ");
        }
        System.out.println();
    }
}
