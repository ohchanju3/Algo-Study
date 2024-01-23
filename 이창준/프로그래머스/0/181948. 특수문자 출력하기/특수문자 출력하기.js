const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("close", function () {
  console.log("!@#$%^&*(\\'\"<>?:;");
});

/*
    백슬래시로 이스케이프 처리를해야 한다.
    "\"는 \\로, "'"는 \'로, """는 \"로 이스케이프 처리하여 출력할 수 있다.
*/
