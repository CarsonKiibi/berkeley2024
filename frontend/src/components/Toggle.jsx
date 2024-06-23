function Toggle() {
    return (
        <div className="flex flex-row">
            <span className="label-text">Interviewer</span> 
            <input type="checkbox" className="toggle mx-4"  />
            <span className="label-text">Interviewee</span> 
        </div>
    );
}

export default Toggle;