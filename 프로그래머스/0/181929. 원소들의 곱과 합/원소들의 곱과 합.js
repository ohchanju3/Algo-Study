function solution(num_list) {
    var product = 1; 
    var sum = 0; 
    
   
    for (var i = 0; i < num_list.length; i++) {
        product *= num_list[i]; 
        sum += num_list[i];
    }
    
    var squaredSum = sum * sum; 
    
    if (product < squaredSum) {
        return 1;
    } else {
        return 0;
    }
}