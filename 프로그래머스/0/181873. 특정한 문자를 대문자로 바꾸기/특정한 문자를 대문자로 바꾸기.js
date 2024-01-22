function solution(my_string, alp) {
    var regExp = new RegExp(alp, 'g');
    var answer = my_string.replace(regExp, alp.toUpperCase());
    return answer;
}