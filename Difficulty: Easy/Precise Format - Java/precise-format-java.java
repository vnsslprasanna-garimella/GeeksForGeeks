import java.util.*;

class Solution {
    static ArrayList<Float> divisionWithPrecision(float a, float b) {

        ArrayList<Float> l = new ArrayList<>();

        l.add(a/b);

        l.add(Float.parseFloat(String.format("%.3f",(a/b))));

        return l;

        

    }
}
