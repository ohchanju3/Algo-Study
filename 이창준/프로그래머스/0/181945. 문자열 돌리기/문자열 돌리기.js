const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", function (line) {
  strArr = line.split("");
}).on("close", function () {
  for (let i = 0; i < strArr.length; i++) {
    console.log(strArr[i]);
  }
});

/*
    현재 내가 쓴 방법은  input에 안 받고 line에 적히는 문자를 바로 split해서 한 글자씩 나눈 방법임.
    line 배열에 먼저 담아 나누는 방법을 사용하려면

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    str = input[0];
    [...str].forEach(c => console.log(c))
});
    와 같은 방법을 사용할 수 있음. 여기 문제에서는 forEach 대신에 map을 사용해서 쭉 순회해도 됨. (forEach -> map 가능)

    
    그리고 for문 쓸 때 축약형으로 써도 나쁘지 않을 것 같다. 아래 코드가 보기 더 간결해보임.
for(let i of str){
    console.log(i)
}
*/
