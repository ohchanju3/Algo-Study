function solution(my_string, k) {
    let strArr = [];
    for(let i=0; i<k; i++){
        strArr.push(my_string);
    }
    var answer = strArr.join("");
    
    return answer;
}