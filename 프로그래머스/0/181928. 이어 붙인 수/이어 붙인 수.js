function solution(num_list) {
    var oddDigits = '';
    var evenDigits = '';
    
    for (var i = 0; i < num_list.length; i++) {
        if (num_list[i] % 2 === 0) {
            evenDigits += num_list[i];
        } else {
            oddDigits += num_list[i];
        }
    }
    
    var oddSum = parseInt(oddDigits);
    var evenSum = parseInt(evenDigits);
    
    return oddSum + evenSum;
}