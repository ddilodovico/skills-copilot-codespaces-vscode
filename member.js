function skillsMember() {
  const member = this;

  // Define a method that returns the skills of the member
  member.getSkills = function() {
    // Return the skills of the member
    return member.skills;
  };
}