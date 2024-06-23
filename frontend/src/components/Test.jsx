function Test() {
    return (
        <div className="flex">
  <form id="submitForm" method="POST" action="https://localhost:3000">
    <label htmlFor="resume">Resume:</label>
    <input type="file" id="resume" name="resume" />

    <label htmlFor="bio">Bio:</label>
    <textarea id="bio" name="bio" rows="4" cols="50" placeholder="Enter your bio here"></textarea>

    <button type="submit">Submit</button>
  </form>
</div>
        );
    }
    
    export default Test;