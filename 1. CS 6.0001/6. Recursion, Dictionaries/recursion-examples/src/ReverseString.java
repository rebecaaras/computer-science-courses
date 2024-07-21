public class ReverseString {
    public static String reverseString (String input) {
        //What is your base case?
        if (input.equals("")) {
            return "";
        }
        
        //What is the smallest amount of work I can do in each iteration?
        return reverseString(input.substring(1))+ input.charAt(0);
    }

    public static void main(String[] args) {
        System.out.println(reverseString("hello"));
    }
}
