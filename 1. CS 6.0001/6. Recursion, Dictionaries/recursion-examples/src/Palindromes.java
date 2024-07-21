public class Palindromes {
     public static boolean isPalindrome(String input){
        //Define base-case/ stopping condition
        if (input.length() == 0 || input.length() == 1){
            return true;
        }

        //So some work to shrinken the problem space
        if (input.charAt(0) == input.charAt(input.length() - 1)){
            return isPalindrome(input.substring(1, input.length() - 1));
        }

        //Additional base-case to handle non-palindromes
        return false;
     }
     public static void main(String[] args) {
        System.out.println(isPalindrome("hannah"));
     }
     
}
