public class DecimalToBinary {
    public static void main(String[] args) {
        String binary = findBinary(233, "");
    }

    public static String findBinary(int decimal, String result) {
        if (decimal == 0) {
            return result;
        }
        
        //concatenates division remainder to result
        result = decimal % 2 + result; 
        return findBinary(decimal/2, result);
    }
}
