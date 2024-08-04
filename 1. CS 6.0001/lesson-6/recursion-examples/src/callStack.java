public class callStack {
    public static String A(){
        return "hello " + B();
    }

    public static String B(){
        return "my " + C();
    }

    public static String C() {
        return "friends.";
    }
    public static void main(String[] args) {
        System.out.println(A());
    } 
}
