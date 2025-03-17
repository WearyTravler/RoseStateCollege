package rectangle;

/**
 *
 * @author Jonah
 */
public class Rectangle {
    // Instance variables
    private double height;
    private double width;

    // Constructor to initialize the Rectangle object with height and width
    public Rectangle(double height, double width) {
        this.height = height;
        this.width = width;
    }

    // Getter for height
    public double getHeight() {
        return height;
    }

    // Setter for height
    public void setHeight(double height) {
        this.height = height;
    }

    // Getter for width
    public double getWidth() {
        return width;
    }

    // Setter for width
    public void setWidth(double width) {
        this.width = width;
    }

    // Method to calculate the area of the rectangle
    public double getArea() {
        return height * width;
    }

    // Method to calculate the perimeter of the rectangle
    public double getPerimeter() {
        return 2 * (height + width);
    }

    // Main method to test the Rectangle class
    public static void main(String[] args) {
        // Create a Rectangle object
        Rectangle rect = new Rectangle(10, 5);

        // Output the area and perimeter using getters and the methods
        System.out.println("Area of rectangle: " + rect.getArea());
        System.out.println("Perimeter of rectangle: " + rect.getPerimeter());

        
        rect.setHeight(20);
        rect.setWidth(10);

        // Output the new area and perimeter
        System.out.println("Updated Area of rectangle: " + rect.getArea());
        System.out.println("Updated Perimeter of rectangle: " + rect.getPerimeter());
    }
}
