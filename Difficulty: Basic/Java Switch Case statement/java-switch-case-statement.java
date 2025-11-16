class Solution {
    static double switchCase(int choice, List<Double> arr) {
        double area = 0;

        switch (choice) {
            case 1: // area of circle
                double r = arr.get(0);
                area = Math.PI * r * r;
                break;

            case 2: // area of rectangle
                double l = arr.get(0);
                double b = arr.get(1);
                area = l * b;
                break;
        }

        return area;
    }
}
