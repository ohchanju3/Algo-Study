function solution(a, b) {
    var ab = a.toString() + b.toString();
    var ba = b.toString() + a.toString();
    
    var numAB = parseInt(ab);
    var numBA = parseInt(ba);

    return Math.max(numAB, numBA);
}