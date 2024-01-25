const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    strArr = line.split("");
}).on('close',function(){
    for(let i=0; i<strArr.length; i++){
        console.log(strArr[i]);
    }
});