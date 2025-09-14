const sum = require('../sum')

test(' adds 2 + 3 equals to 5',()=>{
    expect(sum(2,3)).toBe(5)
}) 
test(' adds negative numbers',()=>{
    expect(sum(-2,-3)).toBe(-5)
}) 