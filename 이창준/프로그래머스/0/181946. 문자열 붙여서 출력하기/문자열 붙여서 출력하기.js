const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", function (line) {
  input = line.split(" ");
}).on("close", function () {
  str1 = input[0];
  str2 = input[1];
  console.log(str1 + str2);
});

/*
    console.log(strArr.join(''))를 통해서 문자열을 붙일 수 있음.

    **공식문서 설명**
    Array 인스턴스의 Join() 메서드는 배열의 모든 요소를 쉼표나 지정된 구분 문자열로 구분하여 연결한 새 문자열을 만들어 반환합니다. 
    배열에 항목이 하나만 있는 경우, 해당 항목은 구분 기호를 사용하지 않고 반환됩니다.

    **정리**
    정리하자면, join()을 통해서 결합하면 strArr안에 있는 요소들이 콤마(,)를 기준으로 붙여진다.
    따라서 그냥 연결되게 만들고싶다면 공백문자('')를 써서 붙여야 한다.

 */
