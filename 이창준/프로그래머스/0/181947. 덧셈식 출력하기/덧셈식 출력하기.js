const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = line.split(' ');
}).on('close', function () {
    let num1 = parseInt(input[0], 10);
    let num2 = parseInt(input[1], 10);
    let result = num1+num2;
    console.log(`${num1} + ${num2} = ${result}`)
});