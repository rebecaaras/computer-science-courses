package AtmAnalogy;
public class AtmAnalogy {

    public int getMyPositionInLine(Person person) {
        if (person.nextInLine == null){
            return 1;
        }

        return 1 + getMyPositionInLine(person.nextInLine); 
    }
}
