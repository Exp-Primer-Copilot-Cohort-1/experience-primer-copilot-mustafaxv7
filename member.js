function skillsMember(){
    return {
        name: 'John Doe',
        skills: ['JavaScript', 'TypeScript', 'React']
    };
}var member = skillsMember();
console.log(member.name + ' has the following skills: ' + member.skills.join(', '));