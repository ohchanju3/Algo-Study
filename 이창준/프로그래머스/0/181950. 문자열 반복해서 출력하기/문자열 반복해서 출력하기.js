const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", function (line) {
  input = line.split(" ");
}).on("close", function () {
  str = input[0];
  n = Number(input[1]);
  let result = "";
  for (let i = 0; i < n; i++) {
    result += str;
  }
  console.log(result);
});

/*
    console.log(str.repeat(n));로, 위에 for문 없이 바로 repeat해서 반복시킬 수도 있다.
    앞으로는 반복 문제 있으면, repeat사용하는 것이 더 좋아보인다.
*/
