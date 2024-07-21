package AtmAnalogy;
public class Person {
    /***
     * Abstraction of a person who has another person next in line
     * to them.
     */
    public String name;
    public Person nextInLine;

    public Person(String name, Person nextInLine){
        if (nextInLine == null) {
            this.nextInLine = null;
        }

        this.name = name;
        this.nextInLine = nextInLine;
    }

    public static void main(String[] args) {
        mary = new Person("Mary", adam);
        adam = new Person("Adam", john);
        john = new Person("John", )
    }
}
