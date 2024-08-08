public class EssayRevision {
    function revise(essay){
        read(essay);
        get_feedback_on(essay);
        apply_changes_to(essay);
        revise(essay) unless essay.complete?;
    }    
}
